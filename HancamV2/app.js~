var express = require('express'),
    app = express(),
    server = require('http').createServer(app),
    io = require('socket.io')(server),
    fs = require('fs');

var watcher = require('node-watch');
var db = require('./db.js');
var db2 = require('./dbV2.js');
var init = require('./initdb.js');
var url = require('url');
var exec = require('child_process').exec;
var child_p = require('child_process');
var bodyParser = require('body-parser');

var current ;
var r_var;
var t_var;
var current_fil;
var current_mat;

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

//Fonction utiles
function getListeStudent(fil, mat, res){
	var noms = [];
	var nb = []
	db2.retrieveStudentByFiliere(fil, function(err, result){
		for(var i=0; i<result.length; i++){
			noms.push(result[i].nom);
			db2.retrieveAbsence(result[i].id_e, mat, function(err, rets){
				console.log('NB_P : '+rets[0].nb_p);
				nb.push(rets[0].nb_p);
			});
		}
	});
	setTimeout(function(){
	   res.render('index', {names: noms, numbers: nb });
	}, 1000);
}

//Implementation du cote Serveur

app.get('/', function(req, res)
{
  //init.init();
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.render('login');
});

app.use(bodyParser());
app.post('/login', function(req, res)
{
	res.statusCode = 200;
   res.setHeader('Content-Type', 'text/html');
	var pseudo = req.body.pseudo;
	var mdp = req.body.pass;
	db2.retrieveProf(function(err, result){
		var find = false;
		var index = 0;
		for(index = 0; index < result.length; index++){
			if(result[index].pseudo == pseudo){
				if(result[index].mdp == mdp){
					find = true;
				   current = result[index];
				   console.log(result[index].nom);
					db2.retrieveFiliereByProfId(result[index].id_p, function(err, ret){
						res.render('home', {nom : current.nom, filieres: ret});
					});
				}else{
					res.render('errorp', {info: "Mot de passe incorrect!"});
				}
			}else if(result[index].mdp == mdp){
				if(!result[index].pseudo == pseudo){
					res.render('errorp', {info: "Pseudo incorrect!"});
				}
			}
		}
		
		if(!find){
			res.render('errorp', {info: "pseudo & mot de passe incorrect!"});
		}
	});
});

app.get('/liste', function(req, res){
	var fil = req.query.fil;
	var mat = req.query.mat;
	current_fil = fil;
	current_mat = mat;
	getListeStudent(fil, mat, res);
	
});

app.get('/plus', function(req, res){
	var nom = req.query.nom;
	update(nom, 1);
	getListeStudent(current_fil, current_mat, res);
});

app.get('/moins', function(req, res){
	var nom = req.query.nom;
	update(nom, -1);
	getListeStudent(current_fil, current_mat, res);
});

app.get('/addStudent', function(req, res){
	var ide = req.query.ide;
	var nom = req.query.nom;
	var fil = req.query.filiere;
	//console.log('I : '+ide+' N : '+nom+' F : '+fil);
	init.addStudentToGi4(ide, nom, fil);
	getListeStudent(current_fil, current_mat, res);
});


//Ressource Static
var fichier = 'ressources/liste.txt';
var jeton = 'ressources/jeton.txt';


//Fonction effectuant la mise à jour de la base à la reconnaissance
function update(nom_e, aj){
	//console.log('Current Matiere : '+current_mat);
	//console.log('Current Filiere : '+current_fil);
	db2.retrieveStudentByFiliere(current_fil, function(err, result){
		for(var i = 0; i<result.length; i++){
			if(result[i].nom.toLowerCase().indexOf(nom_e.toLowerCase()) > -1){
				db2.retrieveAbsence(result[i].id_e, current_mat, function(err, res){
					var p = parseInt(res[0].nb_p); p += aj;
					db2.updateAbsence(result[i].id_e, current_mat, p);
				});
				io.emit('data', {donne: result[i].nom});
				break;
			}
		}
	});
}

io.on('connection', function(socket){
	
	//Ecouteur du fichier Contenant la liste des etudiants
	watcher(fichier, function(filename){
		console.log('\u0007');
   	var data = fs.readFileSync(filename, "utf8");
   	var tmp = data.toString().split('\n')[0];
   	if(tmp !== ""){
   	  update(tmp, 1);
   	}
		
   });
   
   //Traitement du clique sur le CheckBox
   socket.on('checkbox', function(data){
   	if(data.checked == "on"){
   		//fs.writeFile(jeton, "on");
   		//executer('./launch.sh'); 
   		r_var = child_p.spawn('./launch.sh', {detached: true});
   		
   	}else if(data.checked == "off"){
   		//fs.writeFile(jeton, "off");
   		//executer('./stop.sh');
   		process.kill(-r_var.pid, 'SIGKILL');
   		
   	}else if(data.checked == "tp"){
   		//fs.writeFile(jeton, "off");
   		//executer('./tof.sh');
   		t_var = child_p.spawn('./tof.sh', {detached: true});
   		console.log('Emited : '+data.checked);
   		
   	}else if(data.checked == "stp"){
   		//fs.writeFile(jeton, "off");
   		//executer('./stoptp.sh');
   		process.kill(-t_var.pid, 'SIGKILL');
   		console.log('Emited : '+data.checked);
   	}
   });
   
   socket.on('ajout', function(data){
   	db.ajout(data.nom);
   	//console.log('Donnée à inserer : '+data.nom);
   });
	
});


server.listen(8000);

/*
	var queryData = url.parse(req.url, true).query;
	name=queryData.nom;
	plus = queryData.plus;
	moins = queryData.moins;
	if(name !== undefined){
		console.log('Parametre Name = '+name);
		if(plus !== undefined){
			update(name, 1);
		}
		else if(moins !== undefined){
			substractPresence(name);
		}
	}
*/






