#!/usr/bin/env python
import requests, sys, webbrowser, bs4

if len(sys.argv)<2:
	print "usage: Enter the search as a command line \n eg: gsearch India"
else:
	print "Googling...for ...."+sys.argv[1]
	# display text while downloading the Google page
	res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
	res.raise_for_status()
	#webbrowser.open('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
	soup = bs4.BeautifulSoup(res.text)
	# Open a browser tab for each result.
	linkElems = soup.select('.r a')
	numOpen = min(5, len(linkElems))
	for i in range(numOpen):
    		webbrowser.open('https://google.com' + linkElems[i].get('href'))
