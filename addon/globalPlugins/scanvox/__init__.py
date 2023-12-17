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

addonHandler.initTranslation()

confspecs = {
	"nbWeek": "integer(default=60)",
	"autoUpdate": "boolean(default=True)",
	"updateEveryStart": "boolean(default=False)",
}

config.conf.spec["scanvox"] = confspecs

from . import update_scanvox as update

baseDir = os.path.dirname(__file__) 
exe = os.path.join(baseDir, "scanvox.exe")
document = getDocumentsPath()
txtFile = os.path.join(baseDir, "scanvox.txt")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.createMenu()
		gui.NVDASettingsDialog.categoryClasses.append(update.ScanvoxPanel)
	
	def createMenu(self):
		self.submenu_item = gui.mainFrame.sysTrayIcon.toolsMenu.Insert(8, wx.ID_ANY, "&Scanvox", "Scanvox")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.displayDialog, self.submenu_item)
	
	def displayDialog(self, evt):
		gui.mainFrame.popupSettingsDialog(Scanvox)
	
	@script(gesture="kb:nvda+alt+s",
		description=_("Open the Scanvox dialog"),
		category=_("Scanvox for NVDA")
	)
	def script_openScanvoxDialog(self, gesture):
		self.displayDialog(None)

	def terminate(self):
		gui.mainFrame.sysTrayIcon.toolsMenu.Remove(self.submenu_item)
		gui.NVDASettingsDialog.categoryClasses.remove(update.ScanvoxPanel) 
		super().terminate()
	
class Scanvox(wx.Dialog):
	def __init__(self, parent=None):
		subprocess.run([exe, "-c"])
		super().__init__(parent, title="Scanvox")
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		self.scan = sHelper.addItem(wx.Button(self, label=_("&Scan")))
		self.scan.Bind(wx.EVT_BUTTON, self.on_scan)
		self.save = sHelper.addItem(
			wx.Button(self, label=_("&Save the scanned pages"))
		)
		self.save.Bind(wx.EVT_BUTTON, self.on_save)
		self.save.Enable(False)
		self.open = sHelper.addItem(wx.Button(self, label=_("See the result in the &notepad")))
		self.open.Enable(False)
		self.open.Bind(wx.EVT_BUTTON, self.on_open)
		self.delete = sHelper.addItem(wx.Button(self, label=_("&Delete the scanned pages")))
		self.delete.Bind(wx.EVT_BUTTON, self.on_delete)
		self.delete.Enable(False)
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		self.closeBtn = bHelper.addButton(self, wx.ID_CLOSE)
		self.closeBtn.Bind(wx.EVT_BUTTON, self.on_close)
		self.SetEscapeId(wx.ID_CLOSE)
		self.SetDefaultItem(self.closeBtn)

		mainSizer.Add(sHelper.sizer, border=10, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
	
	def on_scan(self, evt):
		ui.message(_("Scanning in progress, please wait..."))
		threading.Thread(target=self.scanThread).start()
	
	def on_save(self, evt):
		saveDialog = wx.FileDialog(self, message=_("Select the location where you want to save the file"), wildcard=_("Text file: *.txt|*.txt"), name=_("Save the file"), defaultDir=document, style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
		saveDialog.SetFilename("Scanvox.txt")
		if saveDialog.ShowModal() == wx.ID_OK:
			path=saveDialog.GetPath()
			name = saveDialog.GetFilename()
			copy(txtFile, path)
			self.on_Enable_Button(None)
	
	def on_open(self, evt):
		open = subprocess.run([exe, "-n"])
		result = open.returncode
		if result == 1002:
			ui.message(_("No page is scanned"))
			self.on_Enable_Button(None)
	
	def on_delete(self, evt):
		threading.Thread(target=self.deleteThread).start()
	
	def on_close(self, evt):
		subprocess.run([exe, "-c"])
		self.Destroy()
	
	def on_Enable_Button(self, evt):
		if not self.open.IsEnabled():
			self.save.Enable(True)
			self.open.Enable(True)
			self.delete.Enable(True)

	def scanThread(self):
		scan = subprocess.run([exe, "-s"], capture_output=True)
		result = scan.returncode
		if result == 0:
			core.callLater(0, lambda: ui.message(_("Scan completed")))
			self.on_Enable_Button(None)
		elif result == 1003:
			core.callLater(0, ui.message(_("No OCR matching the language of your system is available")))
		elif result == 1005:
			core.callLater(0, lambda: ui.message(_("No compatible scanner detected")))

	def deleteThread(self):
		delete = subprocess.run([exe, "-c"], capture_output=True)
		result = delete.returncode
		if result == 0:
			core.callLater(0, ui.message(_("All the pages have been erased")))
			self.save.Enable(False)
			self.open.Enable(False)
			self.delete.Enable(False)
		else:
			core.callLater(0, ui.message(_("It's impossible to delete the scanned pages")))
	
