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
    var ets = [{nom: "Seydou Berthe", ab: "0"},
    				{nom: "Bouh Oualid", ab: "0"},
    				{nom: "Ayachi Mohamed", ab: "0"},
    				{nom: "Messaoudi Oussama", ab: "0"},
    				{nom: "Kotb Rahbi", ab: "0"},
    				{nom: "Ouali Yassir", ab: "0"},
    				{nom: "Malek Yassir", ab: "0"},
    				{nom: "Rhorbal Zakaria", ab: "0"},
    				{nom: "Fadellah Abdelilah", ab: "0"},
    				{nom: "Alraj Zouhair", ab: "0"},
    				{nom: "Soufian Chalouh", ab: "0"}
    			  ];
   

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

ajout : function(n){
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
    var ets = [{nom: n, ab: "0"}];
   

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

}

}
