# -*- coding	: UTF-8 -*-
# This file is covered by the GNU General Public License.

import addonHandler
import os

# from logHandler import log
from tones import beep
from languageHandler import getLanguage

addonHandler.initTranslation()


def onInstall():
	installPath = os.path.dirname(__file__)
	addonName, addonNewVersion = getNewAddonInfo(installPath)
	addonOldVersion = getOldVersion(addonName, installPath)

	if addonOldVersion != addonNewVersion:
		update(addonName, addonOldVersion, addonNewVersion)


def getNewAddonInfo(installPth):
	if ".pendingInstall" not in installPth:
		installPth = installPth + ".pendingInstall"
	newManifest = installPth + "\\manifest.ini"
	if not os.path.exists(newManifest):
		return "none", "0.0.0"
	try:
		with open(newManifest, 'r', encoding="utf-8", errors="surrogateescape") as f:
			lines = f.readlines()
			f.close()
	except OSError:
		return "none", "0.0.0"

	n = v = "none"
	for l in lines:
		if l.startswith("name"):
			n = l.split("=")[1]
			n = n.strip()
		if l.startswith("version"):
			v = l.split("=")[1]
			return n, v.strip()

	return "none", "20aa.mm.dd"


def getOldVersion(addName, installPth):
	# tests if a version is already installed or not
	if installPth.endswith(".pendingInstall"):
		installPth = installPth.replace(".pendingInstall", "")

	if not os.path.exists(installPth + "\\manifest.ini"):
		return "0.0.0"
	# retrive version of installed addon
	try:
		for a in addonHandler.getAvailableAddons():
			if a.name == addName:
				return a.version
	except:
		pass

	return "2099.01.01"


try:
	from urllib import urlopen
except Exception:
	from urllib.request import urlopen
try:
	from urllib import Request
except Exception:
	from urllib.request import Request
try:
	from urllib import parse
except Exception:
	from urllib.request import parse


def update(name, oldVer, newVer):
	lg = getLanguage() + "%20" + getEnglishLocaleInfo()
	# appeler ici page PHP en transmettant name, OldVersion
	url = "https://module.nael-accessvision.com/instTasksNew.php?addon={}&ov={}&nv={}&lg={}&u={}".format(
		name, oldVer, newVer, lg, parse.quote(os.getenv('username').encode('latin-1'))
	)
	# if  isDebug : return
	try:
		with urlopen(url) as data:
			data = data.read()
	except:
		pass


import ctypes, winUser
from ctypes import windll
import languageHandler


def getEnglishLocaleInfo(separ="%20"):  # iType 1 = country 2=language
	import winUser
	import scriptHandler
	import ctypes
	import languageHandler

	# Getting the handle of the foreground window.
	curWindow = winUser.getForegroundWindow()
	# Getting the threadID.
	threadID = winUser.getWindowThreadProcessID(curWindow)[1]
	# Getting the keyboard layout iD.
	klID = winUser.getKeyboardLayout(threadID)
	# Extract language ID from klID.
	lID = klID & (2**16 - 1)
	# Getting the current keyboard language AND COUNTRY IN eNGLISH  from ctypes.windll.kernel32.GetLocaleInfoW.
	# Some language IDs are not available in the local.windows_locale dictionary,
	# It is best to search their description directly in Windows itself
	# language
	lcType = (
		languageHandler.LOCALE_SENGLISHLANGUAGENAME
		if hasattr(languageHandler, "LOCALE_SENGLISHLANGUAGENAME")
		else languageHandler.LOCALE.SENGLISHLANGUAGENAME
	)
	buf = ctypes.create_unicode_buffer(1024)
	ctypes.windll.kernel32.GetLocaleInfoW(lID, lcType, buf, 1024)
	lang = buf.value
	# COUNTRY
	lcType = (
		languageHandler.LOCALE_SENGLISHCOUNTRYNAME
		if hasattr(languageHandler, "LOCALE_SENGLISHCOUNTRYNAME")
		else languageHandler.LOCALE.SENGLISHCOUNTRYNAME
	)
	ctypes.windll.kernel32.GetLocaleInfoW(lID, lcType, buf, 1024)
	country = buf.value
	return country + separ + lang
