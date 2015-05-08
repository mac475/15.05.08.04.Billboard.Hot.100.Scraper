# -*- coding: utf-8-*-
import urllib2
from bs4 import BeautifulSoup

def hotProcess():
	hot100_url = 'http://www.billboard.com/charts/hot-100'
	hot100_html = urllib2.urlopen( hot100_url )
	hot100_soup = BeautifulSoup( hot100_html, 'lxml' )

	date_time = hot100_soup.find( 'time' ).get( 'datetime' )
	print date_time
	songs = hot100_soup.find_all( 'div', class_ = 'row-title' )
	idx = 1
	for song in songs :
		song_title = song.find( 'h2' ).text.lstrip().rstrip()
		artist = song.find( 'h3' ).text.lstrip().rstrip()
		if idx < 10 :
			idxStr =  '0' + str( idx )
		else :
			idxStr = str( idx )

		print idxStr, '.', artist, ' - ', song_title
		if idx == 50 : break
		idx += 1

hotProcess()