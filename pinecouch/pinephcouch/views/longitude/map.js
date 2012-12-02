function(doc) {
 	if( doc.lon ){
		emit( doc.lon, doc );
	} 
}
