function(doc) {
 	if( doc.lat ){
		emit( doc.lat, doc );
	} 
}
