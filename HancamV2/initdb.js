var db2 = require('./dbV2.js');


//Fonction initialisant la BD

list_matiere_gi4 = ["UL", "APR", "APR1", "ANG", "UL1", "FR", "MF", "MFOMP", "IR"];

module.exports = {
init : function(){
	//Ajout des Professeurs
	db2.ajoutProf("P1", "Toumi Bouchentouf", "tbouchentouf@gmail.com", "toumi");
	db2.ajoutProf("P2", "Belkasmi Gaouth", "gbelkasmi@gmail.com", "belkasmi");
	db2.ajoutProf("P3", "Jamal Berrich", "jberrich@gmail.com", "jberrich");
	db2.ajoutProf("P4", "Ayad", "ayad@gmail.com", "ayad");
	db2.ajoutProf("P5", "Ettifouri", "ettifouri@gmail.com", "ettifouri");
	db2.ajoutProf("P6", "Saida Bellouali", "saida@gmail.com", "saida");
	db2.ajoutProf("P7", "Setta", "setta@gmail.com", "setta");
	db2.ajoutProf("P8", "Moquadem", "moquadem@gmail.com", "moquadem");
	db2.ajoutProf("P9", "Mohamed Saber", "saber@gmail.com", "saber");
	
	//Ajout de classe aux professeurs
	db2.ajoutClasse("DR2", "GI4", "UL", "P1");
	db2.ajoutClasse("DR2", "GI4", "APR", "P2");
	db2.ajoutClasse("DR2", "GI4", "APR1", "P3");
	db2.ajoutClasse("DR2", "GI4", "ANG", "P4");
	db2.ajoutClasse("DR2", "GI4", "UL1", "P5");
	db2.ajoutClasse("DR2", "GI4", "FR", "P6");
	db2.ajoutClasse("DR2", "GI4", "MF", "P7");
	db2.ajoutClasse("DR2", "GI4", "MFOMP", "P8");
	db2.ajoutClasse("DR2", "GI4", "IR", "P9");
	
	//Ajout des Etuduants & les Tables d'absences associés
	db2.ajoutEtudiant("E1", "Seydou Berthe", "GI4");
	db2.ajoutAbsence("E1", "UL", "0");
	db2.ajoutAbsence("E1", "APR", "0");
	db2.ajoutAbsence("E1", "APR1", "0");
	db2.ajoutAbsence("E1", "ANG", "0");
	db2.ajoutAbsence("E1", "UL1", "0");
	db2.ajoutAbsence("E1", "FR", "0");
	db2.ajoutAbsence("E1", "MF", "0");
	db2.ajoutAbsence("E1", "MFOMP", "0");
	db2.ajoutAbsence("E1", "IR", "0");
	
	db2.ajoutEtudiant("E2", "Bouh Oualid", "GI4");
	db2.ajoutAbsence("E2", "UL", "0");
	db2.ajoutAbsence("E2", "APR", "0");
	db2.ajoutAbsence("E2", "APR1", "0");
	db2.ajoutAbsence("E2", "ANG", "0");
	db2.ajoutAbsence("E2", "UL1", "0");
	db2.ajoutAbsence("E2", "FR", "0");
	db2.ajoutAbsence("E2", "MF", "0");
	db2.ajoutAbsence("E2", "MFOMP", "0");
	db2.ajoutAbsence("E2", "IR", "0");
	
	db2.ajoutEtudiant("E3", "Ayachi Mohamed", "GI4");
	db2.ajoutAbsence("E3", "UL", "0");
	db2.ajoutAbsence("E3", "APR", "0");
	db2.ajoutAbsence("E3", "APR1", "0");
	db2.ajoutAbsence("E3", "ANG", "0");
	db2.ajoutAbsence("E3", "UL1", "0");
	db2.ajoutAbsence("E3", "FR", "0");
	db2.ajoutAbsence("E3", "MF", "0");
	db2.ajoutAbsence("E3", "MFOMP", "0");
	db2.ajoutAbsence("E3", "IR", "0");
	
	db2.ajoutEtudiant("E4", "Fadellah Abdelilah", "GI4");
	db2.ajoutAbsence("E4", "UL", "0");
	db2.ajoutAbsence("E4", "APR", "0");
	db2.ajoutAbsence("E4", "APR1", "0");
	db2.ajoutAbsence("E4", "ANG", "0");
	db2.ajoutAbsence("E4", "UL1", "0");
	db2.ajoutAbsence("E4", "FR", "0");
	db2.ajoutAbsence("E4", "MF", "0");
	db2.ajoutAbsence("E4", "MFOMP", "0");
	db2.ajoutAbsence("E4", "IR", "0");
	
	db2.ajoutEtudiant("E5", "Messaoudi Oussama", "GI4");
	db2.ajoutAbsence("E5", "UL", "0");
	db2.ajoutAbsence("E5", "APR", "0");
	db2.ajoutAbsence("E5", "APR1", "0");
	db2.ajoutAbsence("E5", "ANG", "0");
	db2.ajoutAbsence("E5", "UL1", "0");
	db2.ajoutAbsence("E5", "FR", "0");
	db2.ajoutAbsence("E5", "MF", "0");
	db2.ajoutAbsence("E5", "MFOMP", "0");
	db2.ajoutAbsence("E5", "IR", "0");
	
	db2.ajoutEtudiant("E6", "Kotb Rabhi", "GI4");
	db2.ajoutAbsence("E6", "UL", "0");
	db2.ajoutAbsence("E6", "APR", "0");
	db2.ajoutAbsence("E6", "APR1", "0");
	db2.ajoutAbsence("E6", "ANG", "0");
	db2.ajoutAbsence("E6", "UL1", "0");
	db2.ajoutAbsence("E6", "FR", "0");
	db2.ajoutAbsence("E6", "MF", "0");
	db2.ajoutAbsence("E6", "MFOMP", "0");
	db2.ajoutAbsence("E6", "IR", "0");
	
	db2.ajoutEtudiant("E7", "Ouali Yassir", "GI4");
	db2.ajoutAbsence("E7", "UL", "0");
	db2.ajoutAbsence("E7", "APR", "0");
	db2.ajoutAbsence("E7", "APR1", "0");
	db2.ajoutAbsence("E7", "ANG", "0");
	db2.ajoutAbsence("E7", "UL1", "0");
	db2.ajoutAbsence("E7", "FR", "0");
	db2.ajoutAbsence("E7", "MF", "0");
	db2.ajoutAbsence("E7", "MFOMP", "0");
	db2.ajoutAbsence("E7", "IR", "0");
	
	db2.ajoutEtudiant("E8", "Malek Yasser", "GI4");
	db2.ajoutAbsence("E8", "UL", "0");
	db2.ajoutAbsence("E8", "APR", "0");
	db2.ajoutAbsence("E8", "APR1", "0");
	db2.ajoutAbsence("E8", "ANG", "0");
	db2.ajoutAbsence("E8", "UL1", "0");
	db2.ajoutAbsence("E8", "FR", "0");
	db2.ajoutAbsence("E8", "MF", "0");
	db2.ajoutAbsence("E8", "MFOMP", "0");
	db2.ajoutAbsence("E8", "IR", "0");
	
	db2.ajoutEtudiant("E9", "Rhorbal Zakaria", "GI4");
	db2.ajoutAbsence("E9", "UL", "0");
	db2.ajoutAbsence("E9", "APR", "0");
	db2.ajoutAbsence("E9", "APR1", "0");
	db2.ajoutAbsence("E9", "ANG", "0");
	db2.ajoutAbsence("E9", "UL1", "0");
	db2.ajoutAbsence("E9", "FR", "0");
	db2.ajoutAbsence("E9", "MF", "0");
	db2.ajoutAbsence("E9", "MFOMP", "0");
	db2.ajoutAbsence("E9", "IR", "0");
	
	db2.ajoutEtudiant("E10", "Alraj Zouhair", "GI4");
	db2.ajoutAbsence("E10", "UL", "0");
	db2.ajoutAbsence("E10", "APR", "0");
	db2.ajoutAbsence("E10", "APR1", "0");
	db2.ajoutAbsence("E10", "ANG", "0");
	db2.ajoutAbsence("E10", "UL1", "0");
	db2.ajoutAbsence("E10", "FR", "0");
	db2.ajoutAbsence("E10", "MF", "0");
	db2.ajoutAbsence("E10", "MFOMP", "0");
	db2.ajoutAbsence("E10", "IR", "0");
	
	db2.ajoutEtudiant("E11", "Soufiane Chalouh", "GI4");
	db2.ajoutAbsence("E11", "UL", "0");
	db2.ajoutAbsence("E11", "APR", "0");
	db2.ajoutAbsence("E11", "APR1", "0");
	db2.ajoutAbsence("E11", "ANG", "0");
	db2.ajoutAbsence("E11", "UL1", "0");
	db2.ajoutAbsence("E11", "FR", "0");
	db2.ajoutAbsence("E11", "MF", "0");
	db2.ajoutAbsence("E11", "MFOMP", "0");
	db2.ajoutAbsence("E11", "IR", "0");
	
	db2.ajoutEtudiant("E12", "Imane Echenafi", "GI4");
	db2.ajoutAbsence("E12", "UL", "0");
	db2.ajoutAbsence("E12", "APR", "0");
	db2.ajoutAbsence("E12", "APR1", "0");
	db2.ajoutAbsence("E12", "ANG", "0");
	db2.ajoutAbsence("E12", "UL1", "0");
	db2.ajoutAbsence("E12", "FR", "0");
	db2.ajoutAbsence("E12", "MF", "0");
	db2.ajoutAbsence("E12", "MFOMP", "0");
	db2.ajoutAbsence("E12", "IR", "0");
	
	db2.ajoutEtudiant("E13", "Moussi Meryem", "GI4");
	db2.ajoutAbsence("E13", "UL", "0");
	db2.ajoutAbsence("E13", "APR", "0");
	db2.ajoutAbsence("E13", "APR1", "0");
	db2.ajoutAbsence("E13", "ANG", "0");
	db2.ajoutAbsence("E13", "UL1", "0");
	db2.ajoutAbsence("E13", "FR", "0");
	db2.ajoutAbsence("E13", "MF", "0");
	db2.ajoutAbsence("E13", "MFOMP", "0");
	db2.ajoutAbsence("E13", "IR", "0");
	
	db2.ajoutEtudiant("E14", "Abir Dahmani", "GI4");
	db2.ajoutAbsence("E14", "UL", "0");
	db2.ajoutAbsence("E14", "APR", "0");
	db2.ajoutAbsence("E14", "APR1", "0");
	db2.ajoutAbsence("E14", "ANG", "0");
	db2.ajoutAbsence("E14", "UL1", "0");
	db2.ajoutAbsence("E14", "FR", "0");
	db2.ajoutAbsence("E14", "MF", "0");
	db2.ajoutAbsence("E14", "MFOMP", "0");
	db2.ajoutAbsence("E14", "IR", "0");
	
	db2.ajoutEtudiant("E15", "Assia Chigeur", "GI4");
	db2.ajoutAbsence("E15", "UL", "0");
	db2.ajoutAbsence("E15", "APR", "0");
	db2.ajoutAbsence("E15", "APR1", "0");
	db2.ajoutAbsence("E15", "ANG", "0");
	db2.ajoutAbsence("E15", "UL1", "0");
	db2.ajoutAbsence("E15", "FR", "0");
	db2.ajoutAbsence("E15", "MF", "0");
	db2.ajoutAbsence("E15", "MFOMP", "0");
	db2.ajoutAbsence("E15", "IR", "0");
	
	db2.ajoutEtudiant("E16", "Houda Kessou", "GI4");
	db2.ajoutAbsence("E16", "UL", "0");
	db2.ajoutAbsence("E16", "APR", "0");
	db2.ajoutAbsence("E16", "APR1", "0");
	db2.ajoutAbsence("E16", "ANG", "0");
	db2.ajoutAbsence("E16", "UL1", "0");
	db2.ajoutAbsence("E16", "FR", "0");
	db2.ajoutAbsence("E16", "MF", "0");
	db2.ajoutAbsence("E16", "MFOMP", "0");
	db2.ajoutAbsence("E16", "IR", "0");
	
	db2.ajoutEtudiant("E17", "Houmada Fatima Zahra", "GI4");
	db2.ajoutAbsence("E17", "UL", "0");
	db2.ajoutAbsence("E17", "APR", "0");
	db2.ajoutAbsence("E17", "APR1", "0");
	db2.ajoutAbsence("E17", "ANG", "0");
	db2.ajoutAbsence("E17", "UL1", "0");
	db2.ajoutAbsence("E17", "FR", "0");
	db2.ajoutAbsence("E17", "MF", "0");
	db2.ajoutAbsence("E17", "MFOMP", "0");
	db2.ajoutAbsence("E17", "IR", "0");
	
	db2.ajoutEtudiant("E18", "Fatima Zahra", "GI4");
	db2.ajoutAbsence("E18", "UL", "0");
	db2.ajoutAbsence("E18", "APR", "0");
	db2.ajoutAbsence("E18", "APR1", "0");
	db2.ajoutAbsence("E18", "ANG", "0");
	db2.ajoutAbsence("E18", "UL1", "0");
	db2.ajoutAbsence("E18", "FR", "0");
	db2.ajoutAbsence("E18", "MF", "0");
	db2.ajoutAbsence("E18", "MFOMP", "0");
	db2.ajoutAbsence("E18", "IR", "0");
	
	db2.ajoutEtudiant("E19", "Kouna Safah", "GI4");
	db2.ajoutAbsence("E19", "UL", "0");
	db2.ajoutAbsence("E19", "APR", "0");
	db2.ajoutAbsence("E19", "APR1", "0");
	db2.ajoutAbsence("E19", "ANG", "0");
	db2.ajoutAbsence("E19", "UL1", "0");
	db2.ajoutAbsence("E19", "FR", "0");
	db2.ajoutAbsence("E19", "MF", "0");
	db2.ajoutAbsence("E19", "MFOMP", "0");
	db2.ajoutAbsence("E19", "IR", "0");
	
	db2.ajoutEtudiant("E20", "Ilham Mouzouri", "GI4");
	db2.ajoutAbsence("E20", "UL", "0");
	db2.ajoutAbsence("E20", "APR", "0");
	db2.ajoutAbsence("E20", "APR1", "0");
	db2.ajoutAbsence("E20", "ANG", "0");
	db2.ajoutAbsence("E20", "UL1", "0");
	db2.ajoutAbsence("E20", "FR", "0");
	db2.ajoutAbsence("E20", "MF", "0");
	db2.ajoutAbsence("E20", "MFOMP", "0");
	db2.ajoutAbsence("E20", "IR", "0");
	
	db2.ajoutEtudiant("E21", "Lagmiri Najim", "GI4");
	db2.ajoutAbsence("E21", "UL", "0");
	db2.ajoutAbsence("E21", "APR", "0");
	db2.ajoutAbsence("E21", "APR1", "0");
	db2.ajoutAbsence("E21", "ANG", "0");
	db2.ajoutAbsence("E21", "UL1", "0");
	db2.ajoutAbsence("E21", "FR", "0");
	db2.ajoutAbsence("E21", "MF", "0");
	db2.ajoutAbsence("E21", "MFOMP", "0");
	db2.ajoutAbsence("E21", "IR", "0");
	
},

addStudentToGi4 : function(ide, nome, file){
	db2.ajoutEtudiant(ide, nome, file);
	for(var i = 0; i < list_matiere_gi4.length; i++){
		db2.ajoutAbsence(ide, list_matiere_gi4[i], "0");
	}
}

}


