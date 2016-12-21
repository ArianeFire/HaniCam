var http = require('http');
var connect = require('connect');
var fs = require('fs');
var watcher = require('node-watch');
var io = require('socket.io');
var db = require('./db.js');
var url = require('url');
var exec = require('child_process').exec;
var child_p = require('child_process');

var r_var;
var t_var;
var app = connect();
server = http.createServer(app);
server.listen(8000);
io = io(server);

//Implementation du cote Serveur

//Fonction d'ajout du nombre d'absence
function update(tmp, p){
	if(tmp !== ''){
   	
   		db.retrieve(function(err, ret){
   			var index = 0;
   			for(index = 0 ; index < ret.length; index++){
   				if(ret[index].nom.toLowerCase().indexOf(tmp.toLowerCase()) > -1){
   					var nb_abs = parseInt(ret[index].ab); nb_abs += p;
   					db.update(ret[index].nom, nb_abs);
   					io.emit('data', {donne : ret[index].nom});
   					break;
   				}
   			}
   		});
   		
		}
}

//Fonction de sustraction du nombre d'absence
function substractPresence(tmp){
	update(tmp, -1);
}


function racine(req, resp){
	//db.insert();
	resp.writeHead(200, {"Content-Type":"text/html"});
	fs.createReadStream('index.html').pipe(resp);

};

//Fonction effectuant traitant toutes les requetes avant la redirection
function router(req, resp, next){
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
	
	next();
}

app.use(router);
app.use('/', racine);



//Ressource Static
var fichier = 'ressources/liste.txt';
var jeton = 'ressources/jeton.txt';

//Fonction envoyant les données recuperer de mongodb
function calling(err, r){
  //console.log(r);
  io.emit('ets', r);
}

//Fonction Executat des Command Script
function executer(cmd){
	exec(cmd , function (error, stdout, stderr) {
    					console.log('stdout: ' + stdout);
   					console.log('stderr: ' + stderr);
    					if (error !== null) {
      					console.log('exec error: ' + error);
    					}
			});
}

io.on('connection', function(socket){
	
	//Ecouteur du fichier Contenant la liste des etudiants
	watcher(fichier, function(filename){
		console.log('\u0007');
   	var data = fs.readFileSync(filename, "utf8");
   	var tmp = data.toString().split('\n')[0];
   	update(tmp, 1);
		
   });
   
   //Traitement lorqu'un Client se Connecte
   socket.on('log', function(data){
      db.retrieve(calling);
   	console.log('Client Connecter and he said : '+data);
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






