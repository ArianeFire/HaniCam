var mongodb = require('mongodb');

//We need to work with "MongoClient" interface in order to connect to a mongodb server.
var MongoClient = mongodb.MongoClient;

// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/datas';

module.exports = {


insert : function(){
// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // Get the documents collection
    var collection = db.collection('student');

    //Create some users
    var ets = [{nom: "Seydou Berthe", ab: "0"}]
   

    // Insert some users
    collection.insert(ets, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }
      //Close connection
      db.close();
    });
  }
});

},

retrieve : function(retour){
   var resp = [];
	MongoClient.connect(url, function (err, db) {
   if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
   } else {
    	//HURRAY!! We are connected. :)
    	console.log('Connection established to', url);

    	// Get the documents collection
    	var collection = db.collection('student');

    	// Insert some users
    	   collection.find().toArray(function (err, result) {
      	if (err) {
        		console.log(err);
        		retour(err, null);
      	} else if (result.length) {
        		console.log('Found:', result.length);
        		retour(null, result);
      	} else {
       		 console.log('No document(s) found with defined "find" criteria!');
     	   }
          //Close connection
        db.close();
        });
      }
    });

},

update : function(n, num){

	MongoClient.connect(url, function (err, db) {
  		if (err) {
    		console.log('Unable to connect to the mongoDB server. Error:', err);
  		} else {
    		//HURRAY!! We are connected. :)
    		console.log('Connection established to', url);
			var collection = db.collection('student');
			
			// Insert some users
			collection.update({nom: n}, {$set: {ab: num}}, function (err, numUpdated) {
  				if (err) {
    				console.log(err);
 			 	} else if (numUpdated) {
   			 	console.log('Updated '+n+'to '+num+' Successfully %d document(s).', numUpdated);
  			 	} else {
    				console.log('No document found with defined "find" criteria!');
 		   	}
  				//Close connection
  				db.close();
			});
		}
	});
},

nothing : function(){
	MongoClient.connect(url, function (err, db) {
  		if (err) {
    		console.log('Unable to connect to the mongoDB server. Error:', err);
  		} else {
  			db.close();
		}
	});
},

//=======================================================VERSION 2 DE LA BASE DE DONNEES=======================//


ajoutProf : function(id_p_, nom_, pseudo_, mdp_){
// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // Get the documents collection
    var collection = db.collection('professor');

    //Create some users
    var ets = [{id_p: id_p_, nom: nom_, pseudo: pseudo_, mdp: mdp_}];

    // Insert some users
    collection.insert(ets, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }
      //Close connection
      db.close();
    });
  }
});

},

ajoutClasse : function(id_c_, filiere_,mat_, id_p_){
// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // Get the documents collection
    var collection = db.collection('classe');

    //Create some users
    var ets = [{id_c: id_c_, filiere: filiere_, matiere:mat_, id_p: id_p_}];

    // Insert some users
    collection.insert(ets, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }
      //Close connection
      db.close();
    });
  }
});

},

ajoutEtudiant : function(id_e_, nom_, filiere_){
// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // Get the documents collection
    var collection = db.collection('eleve');

    //Create some users
    var ets = [{id_e: id_e_, nom: nom_, filiere: filiere_}];

    // Insert some users
    collection.insert(ets, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }
      //Close connection
      db.close();
    });
  }
});

},

ajoutAbsence : function(id_e_, matiere_, nb_p_){
// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // Get the documents collection
    var collection = db.collection('absence');

    //Create some users
    var ets = [{id_e: id_e_, matiere: matiere_, nb_p: nb_p_}];

    // Insert some users
    collection.insert(ets, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }
      //Close connection
      db.close();
    });
  }
});

},

retrieveProf : function(retour){
	MongoClient.connect(url, function (err, db) {
   if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
   } else {
    	//HURRAY!! We are connected. :)
    	console.log('Connection established to', url);

    	// Get the documents collection
    	var collection = db.collection('professor');

    	// Insert some users
    	   collection.find().toArray(function (err, result) {
      	if (err) {
        		console.log(err);
        		retour(err, null);
      	} else if (result.length) {
        		console.log('Found:', result.length);
        		retour(null, result);
      	} else {
       		 console.log('No document(s) found with defined "find" criteria!');
     	   }
          //Close connection
        db.close();
        });
      }
    });
},

retrieveFiliereByProfId : function(idp, retour){
	MongoClient.connect(url, function (err, db) {
   if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
   } else {
    	//HURRAY!! We are connected. :)
    	console.log('Connection established to', url);

    	// Get the documents collection
    	var collection = db.collection('classe');

    	// Insert some users
    	   collection.find({"id_p": idp}).toArray(function (err, result) {
      	if (err) {
        		console.log(err);
        		retour(err, null);
      	} else if (result.length) {
        		console.log('Found:', result.length);
        		retour(null, result);
      	} else {
       		 console.log('No document(s) found with defined "find" criteria!');
     	   }
          //Close connection
        db.close();
        });
      }
    });
},

retrieveStudentByFiliere : function(filiere, retour){
	MongoClient.connect(url, function (err, db) {
   if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
   } else {
    	//HURRAY!! We are connected. :)
    	console.log('Connection established to', url);

    	// Get the documents collection
    	var collection = db.collection('eleve');

    	// Insert some users
    	   collection.find({"filiere": filiere}).toArray(function (err, result) {
      	if (err) {
        		console.log(err);
        		retour(err, null);
      	} else if (result.length) {
        		console.log('Found:', result.length);
        		retour(null, result);
      	} else {
       		 console.log('No document(s) found with defined "find" criteria!');
     	   }
          //Close connection
        db.close();
        });
      }
    });
},

retrieveAbsence : function(ide, mat, retour){
	MongoClient.connect(url, function (err, db) {
   if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
   } else {
    	//HURRAY!! We are connected. :)
    	console.log('Connection established to', url);

    	// Get the documents collection
    	var collection = db.collection('absence');

    	// Insert some users
    	   collection.find({"id_e": ide, "matiere": mat}).toArray(function (err, result) {
      	if (err) {
        		console.log(err);
        		retour(err, null);
      	} else if (result.length) {
        		console.log('Found:', result.length);
        		retour(null, result);
      	} else {
       		 console.log('No document(s) found with defined "find" criteria!');
     	   }
          //Close connection
        db.close();
        });
      }
    });
},

updateAbsence : function(ide, mat, num){

	MongoClient.connect(url, function (err, db) {
  		if (err) {
    		console.log('Unable to connect to the mongoDB server. Error:', err);
  		} else {
    		//HURRAY!! We are connected. :)
    		console.log('Connection established to', url);
			var collection = db.collection('absence');
			
			// Insert some users
			collection.update({id_e: ide, matiere: mat}, {$set: {nb_p: num}}, function (err, numUpdated) {
  				if (err) {
    				console.log(err);
 			 	} else if (numUpdated) {
   			 	console.log('Updated '+ide+'to '+num+' Successfully %d document(s).', numUpdated);
  			 	} else {
    				console.log('No document found with defined "find" criteria!');
 		   	}
  				//Close connection
  				db.close();
			});
		}
	});
}

}
