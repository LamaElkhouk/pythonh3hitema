# pythonh3hitema
api ensemble d'interface 
on lance un script seveur qui att les requetes client qui fonctionne sous forme de routes
=>Dockerfile = fichier de configuration,

=>contient des instructions qui construise (build) une image docker
FROM : d'ou on part, FROM image:version
MAINTEINER : instructions pas obligatoire, la personne qui prend en charge l'image
RUN : lancement de commandes ex apt
ENV : definir des variables d 'environnements
EXPOSE : expositions des ports
VOLUME : définition de volumes
COPY : copier des elements entre le host docker et le conteneur
ENTRYPOINT : definir le processus maitre du conteneur


=>but : faciliter le deployement , et pret a etre utiliser par le serveur client
=>Exemple de dockerfile

FROM ubuntu
MAINTAINER Lamia
RUN apt-get update\

!!!!! soit on utilise CMD soit ENTRYPOINT
ENTRYPOINT ["streamlit","run","app.py"] }
			  		 		            }=> streamlit run app.py
CMD ["streamlit","run","app.py"]		}

=>commande pour lancer l'image


sudo service docker start
sudo docker build -t imagestreamlit:1 .

=>commande pour build 
sudo docker run -itd --name streamlitcontaineur -p 8501:8501 imagestreamlit

docker images -q     => id de l'image créer 
sudo docker container ls -a  => liste des 

(niveau 0) IAAS infrastructure as a service => Azure / Oracle /vmware  (on configure nos serveurs, stockage computing et networking)
(niveau 1) PAAS platform as a service => Heroku  
(niveau 2) SAAS software as a service => store, service payant (on voit uniqueement notre consomation, googledrive 


deployer l'application (docker container) sur oracle ou heroku ou azure 