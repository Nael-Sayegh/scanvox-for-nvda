# coding:utf-8

def getIA2Attr (obj,attribute_value=False,attribute_name ="id"):
	r= hasattr (obj,"IA2Attributes") and attribute_name in obj.IA2Attributes.keys ()
	if not r :return False
	r =obj.IA2Attributes[attribute_name]
	return r if not attribute_value  else r ==attribute_value

def getDocumentsPath() :
	import ctypes.wintypes
	CSIDL_PERSONAL = 5       # My Documents
	SHGFP_TYPE_CURRENT = 0   # Get current, not default value

	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
	#message(buf.value)
	return str(buf.value)
