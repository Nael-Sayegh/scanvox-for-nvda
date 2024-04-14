import os
import urllib.request
import datetime
import wx
import addonHandler
import config
import core
import ui
import languageHandler
import gui

addonHandler.initTranslation()

baseDir = os.path.dirname(__file__)
addon = os.path.join(baseDir, "..", "..")
addonInfos = addonHandler.Addon(addon).manifest

time = datetime.datetime.now()
week = int(time.strftime("%W"))


def updateAvailable():
	# Translators: title of a dialog box
	title = _("Update of %s version %s") % (addonInfos["summary"], oversion)
	# Translators: message to user to report a new version.
	msg = _(
		"%s version %s is available. Would you like to update now? You can view the changes by clicking on the What's New button and scrolling down to Changes."
	) % (addonInfos["summary"], oversion)
	updateDialog(title=title, msg=msg).ShowModal()


def installupdate():
	file = os.environ.get('TEMP') + "\\" + addonInfos["name"] + ".nvda-addon"
	url = f"https://module.nael-accessvision.com/addons/addons/{addonInfos['name']}/{addonInfos['name']}.nvda-addon"
	urllib.request.urlretrieve(url, file)
	curAddons = []
	for addon in addonHandler.getAvailableAddons():
		curAddons.append(addon)
	bundle = addonHandler.AddonBundle(file)
	prevAddon = None
	bundleName = bundle.manifest['name']
	for addon in curAddons:
		if not addon.isPendingRemove and bundleName == addon.manifest["name"]:
			prevAddon = addon
			break
	if prevAddon:
		prevAddon.requestRemove()
	addonHandler.installAddonBundle(bundle)
	os.remove(file)
	config.conf[addonInfos["name"]]["nbWeek"] = week
	core.restart()


def verifUpdate(gesture=False):
	global oversion
	version = addonInfos["version"]
	rversion = urllib.request.urlopen(
		"https://module.nael-accessvision.com/addons/addons/"
		+ addonInfos["name"]
		+ "/version.txt"
	)
	tversion = rversion.read().decode()
	oversion = tversion.replace("\n", "")
	if version != oversion:
		wx.CallAfter(updateAvailable)
	else:
		if gesture:
			ui.message(
				# Translators: message to user to report that no update is available.
				_("No update is available.")
			)


class updateDialog(wx.Dialog):
	def __init__(self, parent=None, title=None, msg=None):
		super().__init__(parent, title=title)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: message to user to report a new version.
		text = sHelper.addItem(wx.StaticText(self))
		text.SetLabel(msg)
		bHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: This is a label of a button appearing
		yes = bHelper.addButton(
			self,
			wx.ID_YES,
			# Translators: label of a button
			label=_("&Yes"),
		)
		yes.Bind(wx.EVT_BUTTON, lambda evt: installupdate())
		yes.SetFocus()
		# Translators: This is a label of a button appearing
		no = bHelper.addButton(
			self,
			wx.ID_NO,
			# Translators: label of a button
			label=_("&No"),
		)
		no.Bind(wx.EVT_BUTTON, self.onNo)
		releaseNotes = bHelper.addButton(
			self,
			# Translators: label of a button
			label=_("Wha&t's new"),
		)
		releaseNotes.Bind(wx.EVT_BUTTON, self.onReleaseNotes)
		sHelper.addDialogDismissButtons(bHelper)
		self.EscapeId = wx.ID_NO
		mainSizer.Add(
			sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL
		)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CentreOnScreen()

	def onNo(self, evt):
		config.conf[addonInfos["name"]]["nbWeek"] = week
		self.Destroy()

	def onReleaseNotes(self, evt):
		url = f"https://module.nael-accessvision.com/addons/addons/{addonInfos['name']}/doc/"
		remoteLanguage = os.listdir(os.path.join(addon, "locale"))
		localLanguage = languageHandler.getLanguage()
		localLanguage = localLanguage.split("_")[0]
		if localLanguage in remoteLanguage:
			os.startfile(url + localLanguage + "/readme.html")
		else:
			os.startfile(url + "en/readme.html")
