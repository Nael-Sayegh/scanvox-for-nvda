# -*- coding	: UTF-8 -*-
# This file is covered by the GNU General Public License.

import addonHandler
import os
# from logHandler import log
from tones import beep
addonHandler.initTranslation()

def onInstall():
	installPath = os.path.dirname(__file__)
	addonName, addonNewVersion = getNewAddonInfo(installPath)
	addonOldVersion = getOldVersion(addonName, installPath)

	if addonOldVersion != addonNewVersion:
		update(addonName, addonOldVersion, addonNewVersion) 
	
def getNewAddonInfo(installPth) :
	if  ".pendingInstall" not in installPth :
		installPth = installPth + ".pendingInstall"
	newManifest = installPth + "\\manifest.ini"
	if  not os.path.exists(newManifest) :
		return "none", "0.0.0"
	try :
		with open(newManifest, 'r', encoding="utf-8", errors="surrogateescape") as f:
			lines = f.readlines()
			f.close()
	except OSError :
		return "none", "0.0.0"
	
	n = v = "none"
	for l in lines:
		if l.startswith("name") :
			n = l.split("=")[1]
			n = n.strip()
		if l.startswith("version") :
			v = l.split("=")[1]
			return n, v.strip()

	return  "none", "20aa.mm.dd"
def getOldVersion(addName, installPth) :
	# tests if a version is already installed or not
	if  installPth.endswith(".pendingInstall") :
		installPth = installPth.replace(".pendingInstall", "")

	if  not os.path.exists(installPth + "\\manifest.ini") :
		return "0.0.0"
	# retrive version of installed addon
	try :
		for a in addonHandler.getAvailableAddons():
			if a.name == addName :
				return a.version
	except : pass

	return "2099.01.01"

try: 	from urllib import urlopen
except Exception: from urllib.request import urlopen
try: 	from urllib import Request
except Exception: from urllib.request import Request
try: from urllib import parse
except Exception: from urllib.request import parse


def update(name, oldVer, newVer) :
	lg = getWinLang()
	kl = getKL()
	# appeler ici page PHP en transmettant name, OldVersion
	url = "https://module.nael-accessvision.com/instTasks.php?addon={}&ov={}&nv={}&lg={}&kl={}&u={}".format(name, oldVer, newVer, lg, kl, parse.quote(os.getenv('username') .encode('latin-1')))
	# if  isDebug : return
	try :
		with urlopen  (url) as data :
			data = data.read()
	except :
		pass

import ctypes, winUser
from ctypes import windll
import languageHandler

def getWinLang():
	"""
	Fetches the locale name of the user's configured language in Windows.
	"""
	windowsLCID = windll.kernel32.GetUserDefaultUILanguage()
	localeName = languageHandler.windowsLCIDToLocaleName(windowsLCID)
	if not localeName:
		localeName = "en_0"
	return localeName

def getKL() :
	hkl = ctypes.c_ulong(windll.User32.GetKeyboardLayout(0)).value
	lastLanguageID=winUser.LOWORD(hkl)
	KL_NAMELENGTH=9
	buf = ctypes.create_unicode_buffer(KL_NAMELENGTH)
	res = windll.User32.GetKeyboardLayoutNameW(buf)
	if res:
		val = buf.value
		return val[4:]
	return "0000"
