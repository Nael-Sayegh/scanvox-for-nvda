import addonHandler
import gui
import wx
from logHandler import log
import config
import ui

try:
	from gui.settingsDialogs import SettingsPanel
except ImportError:
	from gui import SettingsPanel
from . import update
from .update import addonInfos

addonHandler.initTranslation()


class ScanvoxPanel(SettingsPanel):
	# Translators: title of the settings panel
	title = _("Scanvox for NVDA")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: A group of settings in the settings panel
		generalGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=_("General"))
		generalGroupBox = generalGroupSizer.GetStaticBox()
		generalGroup = gui.guiHelper.BoxSizerHelper(self, sizer=generalGroupSizer)
		sHelper.addItem(generalGroup)

		self.automaticalyReadText = generalGroup.addItem(
			wx.CheckBox(
				generalGroupBox,
				# Translators: Checkbox label in parameter panel
				label=_("&Automatically read the text when the scan is completed"),
			)
		)
		self.automaticalyReadText.SetValue(
			config.conf[addonInfos['name']]["automaticalyReadText"]
		)

		# Translators: A group of settings in the settings panel
		updateGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=_("Update"))
		updateGroupBox = updateGroupSizer.GetStaticBox()
		updateGroup = gui.guiHelper.BoxSizerHelper(self, sizer=updateGroupSizer)
		sHelper.addItem(updateGroup)
		self.autoUpdate = updateGroup.addItem(
			wx.CheckBox(
				updateGroupBox,
				# Translators: A checkbox label in the settings interface
				label=_("Automatically search for updates"),
			)
		)
		self.autoUpdate.SetValue(config.conf[addonInfos['name']]["autoUpdate"])

		self.searchUpdate = updateGroup.addItem(
			wx.Button(
				updateGroupBox,
				# Translators: A button label in the settings panel
				label=_("Search for an update now"),
			)
		)
		self.searchUpdate.Bind(wx.EVT_BUTTON, self.on_searchUpdate)

	def on_searchUpdate(self, evt):
		update.verifUpdate(True)

	def onSave(self):
		config.conf[addonInfos['name']]["autoUpdate"] = self.autoUpdate.GetValue()
		config.conf[addonInfos['name']]["automaticalyReadText"] = (
			self.automaticalyReadText.GetValue()
		)
