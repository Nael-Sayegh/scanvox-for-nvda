import core
import threading
import os
import globalPluginHandler
import subprocess
import addonHandler
from scriptHandler import script
import ui
import gui
import wx
import config
from .uti import getDocumentsPath
from shutil import copy
from logHandler import log
from .settings import ScanvoxPanel
from . import update
import globalVars
import sys

if sys.version_info.major == 3 and sys.version_info.minor == 7:
	lib = os.path.join(os.path.dirname(__file__), "lib", "3.7")
elif sys.version_info.major == 3 and sys.version_info.minor == 11:
	lib = os.path.join(os.path.dirname(__file__), "lib", "3.11")
else:
	log.error("Unsupported python version")

sys.path.insert(0, lib)
from docx import Document

sys.path.remove(lib)

addonHandler.initTranslation()

confspecs = {
	"nbWeek": "integer(default=60)",
	"autoUpdate": "boolean(default=True)",
	"updateEveryStart": "boolean(default=False)",
	"automaticalyReadText": "boolean(default=True)",
}

config.conf.spec["scanvox"] = confspecs


baseDir = os.path.dirname(__file__)
exe = os.path.join(baseDir, "scanvox.exe")
document = getDocumentsPath()
txtFile = os.path.join(baseDir, "scanvox.txt")
separator = "********************\n"

if (
	not globalVars.appArgs.secure
	and config.conf[update.addonInfos["name"]]["autoUpdate"]
	and (
		config.conf[update.addonInfos["name"]]["nbWeek"] != update.week
		or config.conf[update.addonInfos["name"]]["updateEveryStart"]
	)
):
	update.verifUpdate()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.createMenu()
		gui.NVDASettingsDialog.categoryClasses.append(ScanvoxPanel)

	def createMenu(self):
		self.submenu_item = gui.mainFrame.sysTrayIcon.toolsMenu.Insert(
			8, wx.ID_ANY, "&Scanvox", "Scanvox"
		)
		gui.mainFrame.sysTrayIcon.Bind(
			wx.EVT_MENU, self.displayDialog, self.submenu_item
		)

	def displayDialog(self, evt):
		gui.mainFrame.popupSettingsDialog(Scanvox)

	@script(
		gesture="kb:nvda+alt+s",
		# Translators: this is the description of a command that opens the Scanvox dialog
		description=_("Open the Scanvox dialog"),
		# Translators: this is the category for the Scanvox dialog command in the input gestures dialog
		category=_("Scanvox for NVDA"),
	)
	def script_openScanvoxDialog(self, gesture):
		self.displayDialog(None)

	def terminate(self):
		gui.mainFrame.sysTrayIcon.toolsMenu.Remove(self.submenu_item)
		gui.NVDASettingsDialog.categoryClasses.remove(ScanvoxPanel)
		super().terminate()


class Scanvox(wx.Dialog):
	def __init__(self, parent=None):
		subprocess.run([exe, "-c"])
		super().__init__(parent, title="Scanvox")
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		self.contentText = sHelper.addLabeledControl(
			# Translators: this is a label for a text control that displays the scanned text
			_("Text:"),
			wxCtrlClass=wx.TextCtrl,
			style=wx.TE_MULTILINE | wx.TE_READONLY,
		)
		self.contentText.SetMinSize((300, 200))
		self.manageText = Text(self.contentText)
		self.scan = sHelper.addItem(
			wx.Button(
				self,
				# Translators: this is the label for a button that starts the scanning process
				label=_("&Scan"),
			)
		)
		self.scan.SetFocus()
		self.scan.Bind(wx.EVT_BUTTON, self.on_scan)
		self.save = sHelper.addItem(
			wx.Button(
				self,
				# Translators: this is the label for a button that saves the scanned text
				label=_("&Save the scanned pages"),
			)
		)
		self.save.Bind(wx.EVT_BUTTON, self.on_save)
		self.save.Enable(False)
		self.delete = sHelper.addItem(
			wx.Button(
				self,
				# Translators: label for a button
				label=_("&Delete the scanned pages"),
			)
		)
		self.delete.Bind(wx.EVT_BUTTON, self.on_delete)
		self.delete.Enable(False)
		bHelper = sHelper.addDialogDismissButtons(
			gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		)
		self.closeBtn = bHelper.addButton(self, wx.ID_CLOSE)
		self.closeBtn.Bind(wx.EVT_BUTTON, self.on_close)
		self.SetEscapeId(wx.ID_CLOSE)
		self.SetDefaultItem(self.closeBtn)

		mainSizer.Add(sHelper.sizer, border=10, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)

	def on_scan(self, evt):
		ui.message(
			# Translators: a message that is spoken when the scanning process starts
			_("Scanning in progress, please wait...")
		)
		Thread(function='scan', ScanvoxClass=self, textInstance=self.manageText).start()

	def on_save(self, evt):
		saveDialog = wx.FileDialog(
			self,
			# Translators: title of a file dialog
			message=_("Select the location where you want to save the file"),
			# Translators: filter for a file dialog
			wildcard=_("Text file: *.txt|*.txt|Word document: *.docx|*.docx"),
			# Translators: label for a file dialog
			name=_("Save the file"),
			defaultDir=document,
			style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
		)
		saveDialog.SetFilename("Scanvox.txt")
		if saveDialog.ShowModal() == wx.ID_OK:
			path = saveDialog.GetPath()
			name = saveDialog.GetFilename()
			if '.docx' in name:
				with open(txtFile, 'r', encoding='utf-8') as file:
					text = file.read()
				saveDocx = Document()
				saveDocx.add_paragraph(text)
				saveDocx.save(path)
			else:
				copy(txtFile, path)
			self.on_Enable_Button(None)

	def on_delete(self, evt):
		Thread(function='delete', ScanvoxClass=self).start()

	def on_close(self, evt):
		subprocess.run([exe, "-c"])
		self.Destroy()

	def on_Enable_Button(self, evt):
		if not self.save.IsEnabled():
			self.save.Enable(True)
			self.delete.Enable(True)


class Thread(threading.Thread):
	def __init__(self, function, ScanvoxClass, textInstance=None):
		super(Thread, self).__init__()
		self.ScanvoxClass = ScanvoxClass
		self.function = getattr(self, function)
		self.textInstance = textInstance

	def run(self):
		self.function()

	def scan(self):
		scan = subprocess.run([exe, "-s"], capture_output=True)
		result = scan.returncode
		if result == 0:
			if not config.conf["scanvox"]["automaticalyReadText"]:
				core.callLater(
					0,
					lambda: ui.message(
						# Translators: a message that the scan is complete
						_("Scan complete")
					),
				)
			with open(txtFile, 'a', encoding="utf-8") as writeFile:
				writeFile.write("\n" + separator)
			with open(txtFile, 'r', encoding="utf-8") as file:
				lines = file.readlines()
			numberPages = 0
			indexes = []
			for index, line in enumerate(reversed(lines)):
				if line == separator:
					numberPages += 1
					if numberPages == 2:
						indexes.append(len(lines) - index)
						break
			if numberPages == 1:
				text = ''.join(lines[0:-2])
			elif indexes:
				lastIndex = indexes[-1]
				text = ''.join(lines[lastIndex:-2])
			if config.conf["scanvox"]["automaticalyReadText"]:
				core.callLater(0, lambda: ui.message(text.replace("\n", "")))
			self.textInstance.setText(text)
			self.textInstance.addText()
			self.ScanvoxClass.on_Enable_Button(None)
		elif result == 1003:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the OCR is not available
					_("No OCR matching the language of your system is available")
				),
			)
		elif result == 1005:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when no scanner is detected
					_("No compatible scanner detected")
				),
			)
		elif result == 1006:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the page is empty
					_("The page seems empty")
				),
			)

	def delete(self):
		delete = subprocess.run([exe, "-c"], capture_output=True)
		result = delete.returncode
		if result == 0:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the scanned pages are deleted
					_("All the pages have been erased")
				),
			)
			self.ScanvoxClass.contentText.Clear()
			self.ScanvoxClass.save.Enable(False)
			self.ScanvoxClass.delete.Enable(False)
		else:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the scanned pages cannot be deleted
					_("It's impossible to delete the scanned pages")
				),
			)


class Text:
	start = 0
	end = 0

	def __init__(self, control, text=None):
		self.control = control
		self.text = text

	def setText(self, text):
		self.text = text

	def addText(self):
		if self.text is None:
			return
		self.control.SetInsertionPointEnd()
		self.start = self.control.GetInsertionPoint()
		self.control.AppendText(self.text + separator)
		self.end = self.control.GetInsertionPoint()
		self.getText()

	def getText(self):
		if self.start == 0:
			self.control.SetInsertionPoint(0)
		else:
			self.control.SetInsertionPoint(self.start)
