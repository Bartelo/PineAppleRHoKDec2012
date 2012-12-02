
#Import PH data from the FAO into couchdb
#Author Andreas Gros http://andreasgros.net
#python2.6 import_ph_data.py ../data/ph/ph_t http://localhost:5984/pineappleph uName pwd
import sys
import re
import json
import requests
import random
import time

num_re = re.compile( '([\d.-]+)' )


def fetch_num( line ):
    return num_re.findall( line )[ 0 ]


def postdata( data ):
    t = requests.post(couchurl, data=json.dumps( data ), headers={"Content-Type" : "application/json"}, auth = ( uName, pwd ))
    #print str(t)


#pH classes as they are used in this ph_t dataset
phclasses = {
    1 : [0, 4.5],
    2 : [4.5, 5.5],
    3 : [5.5, 7.2],
    4 : [7.2, 8.5],
    5 : [8.5, 15]   
}


infilename  = sys.argv[ 1 ]
couchurl    = sys.argv[ 2 ]
uName       = sys.argv[ 3 ]
pwd         = sys.argv[ 4 ]

infile      = open( infilename, 'rb' )

line = infile.readline()
lonnum  = int( fetch_num( line ) )
line = infile.readline()
latnum  = int( fetch_num( line ) )
line = infile.readline()
lonmin = float( fetch_num( line ) )
line = infile.readline()
latmin = float( fetch_num( line ) )
line = infile.readline()
delta = float( fetch_num( line ) )
line = infile.readline()
nodata = fetch_num( line )

arr = []
for row in infile:
    larr = num_re.findall( row )
    arr.append( larr )

infile.close()

idcnt = 0
latmax = latmin + latnum * delta
for ilat in xrange( latnum ):
    print ilat
    lat = latmax - delta * ilat
    latstore = []
    for ilon in xrange( lonnum ):
        lon = lonmin + delta * ilon
        val = int( arr[ ilat ][ ilon ] )
        if val >= 0 and val < 90:
            val = val / 10
            lower = phclasses[ val ][ 0 ]
            upper = phclasses[ val ][ 1 ]
            d = { "_id" : str( idcnt ) , "lat" : lat, "lon" : lon, "phlow" : lower, "phhigh" : upper }
            postdata( d )
            idcnt += 1




#curl http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{ "source": "pineappleph", "target": "https://uName:pwd@yourcouchserver.com/pineappleph" }'


