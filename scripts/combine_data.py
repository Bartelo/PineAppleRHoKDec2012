


import pycurl
import cStringIO
import json


inlat =  -1.861764
inlon =   30.118369

cropdburl = 'http://andigros:aidA1941@localhost:5984/pineapple'
latuview = '_design/pinecouch/_view/latitudeupper'
latlview = '_design/pinecouch/_view/latitudelower'



c = pycurl.Curl()
buf = cStringIO.StringIO()
    
c.setopt(c.URL, str('%s/%s?startKey=%f&endKey=%f&limit=1' % (cropdburl, latuview, inlat, inlat) ))
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

cropsupper = json.loads( buf.getvalue() ) 

c.setopt(c.URL, str('%s/%s?startKey=%f&endKey=%f&limit=1' % (cropdburl, latlview, inlat, inlat) ))
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

cropslower = json.loads( buf.getvalue() ) 

    



