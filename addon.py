# -*- coding: utf-8 -*-

import urllib, urllib2, re, sys
import xbmcplugin, xbmcgui

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
                            
    return param
	
def addLink(title, url):
    item = xbmcgui.ListItem(title.decode('windows-1251').encode('utf-8'), iconImage='DefaultAudio.png', thumbnailImage='')
    item.setInfo( type='Audio', infoLabels={'Title': title.decode('windows-1251').encode('utf-8')} )

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=item)

	
def Categories():
	addLink('Radio Record', 		'http://air.radiorecord.ru:8101/rr_320')
	addLink('Pirate Station',		'http://air.radiorecord.ru:8102/ps_320')
	addLink('Rock Radio',			'http://air.radiorecord.ru:8102/rock_320')
	addLink('Супердискотека 90-х',	'http://air.radiorecord.ru:8102/sd90_320')
	addLink('Trancemission', 		'http://air.radiorecord.ru:8102/tm_320')
	addLink('Russian Mix',			'http://air.radiorecord.ru:8102/rus_320')
	addLink('Медляк FM',			'http://air.radiorecord.ru:8102/mdl_320')
	addLink('Record Chill-Out',		'http://air.radiorecord.ru:8102/chil_320')
	addLink('Record Club',			'http://air.radiorecord.ru:8102/club_320')
	addLink('Гоп FM',				'http://air.radiorecord.ru:8102/gop_320')
	
params = get_params()
url    = None
title  = None
mode   = None

try:    title = urllib.unquote_plus(params['title'])
except: pass

try:    url = urllib.unquote_plus(params['url'])
except: pass

try:    mode = int(params['mode'])
except: pass

if mode == None:
    Categories()

xbmcplugin.endOfDirectory(int(sys.argv[1]))