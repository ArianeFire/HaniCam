var mongoose = require('mongoose');

// On se connecte à la base de données
// N'oubliez pas de lancer ~/mongodb/bin/mongod dans un terminal !
mongoose.connect('mongodb://localhost/etudiants', function(err) {
  if (err) { throw err; }
});
 
// Création du schéma
var etudiantSchema = new mongoose.Schema({
  nom : String,
  absence : String
});
 
// Création du Model
var EtudiantModel = mongoose.model('etudiants', etudiantSchema);
 
module.exports = {

	insererEtudiant : function(name, ab){
		// On crée une instance du Model	
		var etudiant = new EtudiantModel();
		etudiant.nom = name;
		etudiant.absence = ab;
 
		// On le sauvegarde dans MongoDB !
		etudiant.save(function (err) {
  			if (err) { throw err; }
  			console.log('Etudiant ajouté avec succès !');
  			// On se déconnecte de MongoDB maintenant
  			mongoose.connection.close();
		});
	},
	
	
	recupererEtudiant : function(name){
		var query = EtudiantModel.find(null);
		query.where('nom', name);
		query.exec(function (err, comms) {
  			if (err) { throw err; }
  		
  			return comms;
		});
	}
	

}

