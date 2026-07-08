import xbmcgui
import xbmcplugin
import sys

handle = int(sys.argv[1])

item = xbmcgui.ListItem(label="JoniSport")
item.setInfo("video", {"title": "JoniSport"})

xbmcplugin.addDirectoryItem(handle, "", item, False)
xbmcplugin.endOfDirectory(handle)
