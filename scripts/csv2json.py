#!/usr/bin/python

#Imports a UTF-8 encoded CSV file and dump it into JSON
#Andi Gros http://andreasgros.net

import csv, json
import sys
import codecs

csvfile     = sys.argv[1] 
jsonoutfile = sys.argv[2]

def unicode_csv_reader( unicode_csv_data, dialect=csv.excel, **kwargs ):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader( utf_8_encoder( unicode_csv_data ),
                            dialect = dialect, **kwargs )
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [ unicode( cell, 'utf-8' ) for cell in row ]

def utf_8_encoder( unicode_csv_data ):
    for line in unicode_csv_data:
        yield line.encode( 'utf-8' )


csvreader = unicode_csv_reader( codecs.open( csvfile, 'rb', 'utf-8' ) )
data = []
for row in csvreader:
    r = []
    for field in row:
        if field == '': 
            field   = None
            t       = None
        else:
            try: 
                t = float( field )
            except ValueError:
                t = field
        r.append( t )
    data.append( r )

jrec = []
header = data[ 0 ]
hlen   = len( header )
for row in data[ 1: ]:
    d = {}
    for i in xrange( hlen ):
        d[ header[ i ] ] = row[ i ]
    jrec.append( d )
    
codecs.open( jsonoutfile, 'wb', 'utf-8' ).write(json.dumps(jrec, encoding="utf-8"))


