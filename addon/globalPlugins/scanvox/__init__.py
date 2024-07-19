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
from speech import speakMessage

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
	"chanel": "integer(default=0)",
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
		log.info(
			"Scanvox for NVDA version %s initialized" % update.addonInfos["version"]
		)

	def createMenu(self):
		self.submenu_item = gui.mainFrame.sysTrayIcon.menu.Insert(
			2, wx.ID_ANY, "&Scanvox", "Scanvox"
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
		gui.mainFrame.sysTrayIcon.menu.Remove(self.submenu_item)
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
		self.deletePage = sHelper.addItem(
			wx.Button(
				self,
				# Translators: this is the label for a button that deletes the last page scanned
				label=_("Delete the last page scanned"),
			)
		)
		self.deletePage.Bind(wx.EVT_BUTTON, self.on_deletePage)
		self.deletePage.Enable(False)
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
		self.addShortcuts()

	def on_scan(self, evt):
		ui.message(
			# Translators: a message that is spoken when the scanning process starts
			_("Scanning in progress, please wait...")
		)
		Thread(function='scan', ScanvoxClass=self, textInstance=self.manageText).start()

	def on_deletePage(self, evt):
		self.manageText.deletePage()

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
				sections = text.split(f"\n{separator}")
				saveDocx = Document()
				for section in sections:
					saveDocx.add_paragraph(section)
					saveDocx.add_page_break()
				saveDocx.save(path)
			else:
				copy(txtFile, path)
			self.on_Enable_Button(None)

	def on_delete(self, evt):
		Thread(
			function='delete', ScanvoxClass=self, textInstance=self.manageText
		).start()

	def on_close(self, evt):
		subprocess.run([exe, "-c"])
		self.Destroy()

	def on_Enable_Button(self, evt):
		if not self.save.IsEnabled():
			self.deletePage.Enable(True)
			self.save.Enable(True)
			self.delete.Enable(True)

	def addEntry(self, accelEntries, modifiers, key, func):
		id = wx.Window.NewControlId()
		self.Bind(wx.EVT_MENU, func, id=id)
		accelEntries.append((modifiers, key, id))

	def addShortcuts(self):
		accelEntries = []
		self.addEntry(
			accelEntries,
			wx.ACCEL_CTRL + wx.ACCEL_SHIFT,
			wx.WXK_UP,
			self.manageText.previousPage,
		)
		self.addEntry(
			accelEntries,
			wx.ACCEL_CTRL + wx.ACCEL_SHIFT,
			wx.WXK_DOWN,
			self.manageText.nextPage,
		)
		self.addEntry(
			accelEntries,
			wx.ACCEL_NORMAL,
			wx.WXK_PAGEUP,
			self.manageText.previousPageWithUp,
		)
		self.addEntry(
			accelEntries,
			wx.ACCEL_NORMAL,
			wx.WXK_PAGEDOWN,
			self.manageText.nextPageWithDown,
		)
		accelTable = wx.AcceleratorTable(accelEntries)
		self.contentText.SetAcceleratorTable(accelTable)


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
				writeFile.write(separator)
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
			self.ScanvoxClass.deletePage.Enable(False)
			self.ScanvoxClass.save.Enable(False)
			self.ScanvoxClass.delete.Enable(False)
			self.textInstance.page = 1
			self.textInstance.start = 0
			self.textInstance.end = 0
		else:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the scanned pages cannot be deleted
					_("It's impossible to delete the scanned pages")
				),
			)


class Text:
	start = []
	end = 0
	page = 1

	def __init__(self, control, text=None):
		self.control = control
		self.text = text

	def setText(self, text):
		self.text = text

	def addText(self):
		if self.text is None:
			return
		self.control.SetInsertionPointEnd()
		self.start.append(self.control.GetInsertionPoint())
		self.control.AppendText(
			# Translators: this is the text that is added to the scanned text
			_("Page ") + str(self.page) + "\n" + self.text + separator
		)
		self.end = self.control.GetInsertionPoint()
		self.getText()
		self.page += 1

	def getText(self):
		if not self.start:
			self.control.SetInsertionPoint(0)
		else:
			self.control.SetInsertionPoint(self.start[-1])

	def deletePage(self):
		if self.start:
			self.control.Remove(self.start[-1], self.end)
			with open(txtFile, 'r', encoding="utf-8") as file:
				lines = file.readlines()
				linesSeparator = [
					index
					for index, line in enumerate(lines)
					if line.strip() == separator.strip()
				]
				if linesSeparator:
					if len(linesSeparator) == 1:
						new_lines = ''
					else:
						new_lines = lines[: linesSeparator[-2] + 1]
					with open(txtFile, 'w', encoding="utf-8") as file:
						file.writelines(new_lines)
			self.start.remove(self.start[-1])
			self.page -= 1
			ui.message(
				# Translators: a message that is spoken when the last page is deleted
				_("The last page has been deleted")
			)
		else:
			ui.message(
				# Translators: a message that is spoken when there are no pages to delete
				_("There are no pages to delete")
			)

	def nextPage(self, evt):
		pos = self.control.GetInsertionPoint()
		moved = False
		for page in self.start:
			if pos < page:
				self.control.SetInsertionPoint(page)
				core.callLater(
					0, lambda: speakMessage(self.control.GetRange(page, page + 6))
				)
				moved = True
				break
		if not moved:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the last page is reached
					_("End")
				),
			)

	def nextPageWithDown(self, evt):
		pos = self.control.GetInsertionPoint()
		moved = False
		for page in self.start:
			if pos < page:
				self.control.SetInsertionPoint(page)
				moved = True
				break
		if not moved:
			core.callLater(
				0,
				lambda: ui.message(
					# Translators: a message that is spoken when the last page is reached
					_("End")
				),
			)

	def previousPage(self, evt):
		pos = self.control.GetInsertionPoint()
		for page in reversed(self.start):
			if pos > page:
				self.control.SetInsertionPoint(page)
				core.callLater(
					0, lambda: speakMessage(self.control.GetRange(page, page + 6))
				)
				break

	def previousPageWithUp(self, evt):
		pos = self.control.GetInsertionPoint()
		for page in reversed(self.start):
			if pos > page:
				self.control.SetInsertionPoint(page)
				break
