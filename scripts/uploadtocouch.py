#!/usr/bin/python

#Upload JSON data entries to pineapple couch
#Andi Gros http://andreasgros.net

import sys
import codecs
import json
import requests

infilename  = sys.argv[ 1 ]
couchurl    = sys.argv[ 2 ]
uName       = sys.argv[ 3 ]
pwd         = sys.argv[ 4 ]

infile      = codecs.open( infilename, 'rb', 'utf-8' )
jsonarr     = json.load( infile )

for row in jsonarr:
    t = requests.post(couchurl, data=json.dumps(row), headers={"Content-Type" : "application/json"}, auth = ( uName, pwd ))
    

