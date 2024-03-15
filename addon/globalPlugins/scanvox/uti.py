# coding:utf-8

def getDocumentsPath() :
	import ctypes.wintypes
	CSIDL_PERSONAL = 5       # My Documents
	SHGFP_TYPE_CURRENT = 0   # Get current, not default value

	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
	#message(buf.value)
	return str(buf.value)
