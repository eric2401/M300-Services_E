# Modul-300

Um diese "Dokumentation" zu schreiben habe ich die Website https://stackedit.io benutzt.


## Git Commands:
```
cd Pfad/zu/meinem/Repository    # Zum lokalen GitHub-Repository wechseln

git pull                        #Synchronisiert das repository mit der aktuellen online version

git status                      # Geänderte Datei(en) werden rot aufgelistet
git add -A                      # Fügt alle Dateien zum "Upload" hinzu
git status                      # Der Status ist nun grün > Dateien sind Upload-bereit (Optional) 
git commit -m "Mein Kommentar"  # Upload wird "commited" > Kommentar zu Dokumentationszwecken ist dafür notwendig
git status                      # Dateien werden nun als "zum Pushen bereit" angezeigt
git push                        #Upload bzw. Push wird durchgeführt

```

Unter **[Cloud Computing](https://de.wikipedia.org/wiki/Cloud_Computing)** (deutsch Rechnerwolke) versteht man die Ausführung von Programmen, die nicht auf dem lokalen Rechner installiert sind, sondern auf einem anderen Rechner, der aus der Ferne aufgerufen wird (bspw. über das Internet).

Eine **dynamische Infrastruktur-Plattform** ist ein System, das Rechen-Ressourcen bereitstellt (Virtualisiert), insbesondere Server (compute), Speicher (storage) und Netzwerke (networks), und diese Programmgesteuert zuweist und verwaltet, sogenannte **Virtuelle Maschinen** (VM).
Damit "Infrastructure as Code" auf "Dynamic Infrastructure Platforms" genutzt werden können, müssen sie die folgenden Anforderungen erfüllen:
*	**Programmierbar** - Ein Userinterface ist zwar angenehm und viele Cloud Anbieter haben eines, aber für "Infrastructure as Code" muss die Plattform via Programmierschnittstelle ([API](https://de.wikipedia.org/wiki/Programmierschnittstelle)) ansprechbar sein.
*	**On-demand** - Ressourcen (Server, Speicher, Netzwerke) schnell erstellen und vernichtet.
*	**Self-Service** - Ressourcen anpassen und auf eigene Bedürfnisse zuschneiden.
*	**Portabel** - Anbieter von Ressourcen müssen austauschbar sein. Sicherheit, Zertifizierungen (z.B. [ISO 27001](https://de.wikipedia.org/wiki/ISO/IEC_27001)), ...

## Vagrant einrichten
Befehle für das einrichten von Vagrant

```
vagrant init ubuntu/xenial64        #Vagrantfile erzeugen
vagrant up --provider virtualbox    #Virtuelle Maschine erstellen & starten
```
Die VM ist jetzt erfolgreich gestartet. Jetzt kann mit SSH verbindet werden
```
vagrant ssh
```

Befehle um die VM zu löschen und Updaten
```
vagrant destroy                   #löscht die VM
vagrant upgrade                   #updated die VM
```

## sed
sed (von stream editor) ist ein nicht-interaktiver Texteditor für die Verwendung auf der Kommandozeile oder in Skripten. sed zählt zu den "Urgesteinen" in der Unix- / Linux-Welt und ist quasi in jeder Linux-Installation (auch Minimalinstallationen) enthalten.

## SSH Tunnel
Befehle für SSH Tunnel.
```
vagrant ssh
sudo -s
```
Admin user erstellen
```
adduser admin01
#Password: luki2001
usermod -aG sudo admin01
sudo su - admin01
```
SSH Key erstellen
```
ssh-keygen -t rsa -b 4096
```
Public Key kopieren
```
ssh-copy-id -i ~/.ssh/id_rsa.pub admin01@db01
#Wenn dieser Befehlt nicht funktioniert dann:
cat id_rsa.pub | ssh db01 'cat>> ~/.ssh/authorized_keys'
```

## UFW Firewall
Befehle für das aufsetzen der UFW Firewall

Zuerst müssen wir natürlich UFW überhaupt installieren, falls dies nicht schon erledigt ist.
```
sudo apt-get install ufw
```

Folgender Befehl gibt die Offenen Ports aus
```
netstatt -tulpen
```
Um den TCP Port 80 zu öffnen also den Standard Port für den Apache dienst (http). Muss folgender Befehl eingegeben werden:
```
sudo ufw allow 80/tcp
```
Wichtig bevor die Firewall aktiviert wird noch den SSH Port freigeben, ansonsten wird der Zugriff von SSH abgeblockt. Falls die IP des Host Computers nicht immer gleich bleibt am besten einfach allen Geräten auf den Port 22 Zugriff lassen.
```
sudo ufw allow 22
```
Falls die IP des Host PC bleibt kann diese spezifische IP auch genannt werden.
```
sudo ufw allow from [Host PC IP] to any port 22
```
Jetzt kann die Firewall aktiviert werden
```
sudo ufw enable
```
Den Status kann man folgendermassen aufrufen.
```
sudo ufw status
```

Um den Zugriff zu testen verwende
```
curl -f [IP]:80
curl -f [IP]:22
```

## Webserver einrichten 
Um einen Webserver direkt mittels eines Vagrant Files zu installieren und konfigurieren müssen folgende Lines der Shell Config im Vagrant File hinzugefügt werden:
```
# Shell Code:	
  config.vm.provision "shell", inline: <<-SHELL
  # Set Hostname for Identification
  sudo hostnamectl set-hostname webserver1
  sudo sed -i s/ubuntu-xenial/webserver1/g /etc/hosts
  # Apache2 Setup 
  sudo apt-get update
  sudo apt-get install -y apache2
```
Um die Installation abzuschliessen empfiehlt sich den Apache Service neuzustarten
```
 #sudo a2ensite 001-mysite.conf
  sudo service apache2 restart
```
Der Webserver Pfad kann lokal mit folgender Einstellung lokal synchronisiert werden
```
# Für einen snyced ordner mit VM Host
  config.vm.synced_folder "src/", "/var/www/html" 
```
## Reverseproxy Netzwerkübersicht
![enter image description here](data:image/png;base64,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)
 







## Proxy einrichten 
Um einen Proxy Server direkt mir dem Vagrant File zu installieren müssen folgende Befehle in der Vagrant File Shell Config hinzugefügt werden
```
# Shell Code:
  config.vm.provision "shell", inline: <<-SHELL
  # Apache2 Setup for Reverse Proxy
  sudo a2enmod proxy
  sudo a2enmod proxy_http
  sudo a2enmod proxy_ajp
  sudo a2enmod rewrite
  sudo a2enmod deflate
  sudo a2enmod headers
  sudo a2enmod proxy_balancer
  sudo a2enmod proxy_connect
  sudo a2enmod proxy_html
  sudo sed -i '$aServerName localhost' /etc/apache2/apache2.conf
```
## Statische IP-Adresse & Port konfigurieren
Dies wird ebenfalls im in der Shell Section dees Vagrant Files configuriert.
```
# NOTE: This will enable public access to the opened port
  config.vm.network "private_network", ip: "172.28.128.12"
  config.vm.network "forwarded_port", guest: 80, host: 9090
```
##Wie funktionieren Docker Container
![enter image description here](https://blog.gbs.com/wp-content/uploads/2016/10/windows-server-2016-grafik.jpg?x99775)
## Docker
Installiere Docker auf der Offiziellen Webseite und führe das Programm als Administrator aus.

Erstelle ein Dockerfile womit dann ein Image geladen werden kann. Dieses könnte folgendes beinhalten:
```
FROM php:7.0-apache
COPY src /var/www/html
EXPOSE 80
```
Dies ist ein einfach Apache image mit php. Dafür wird aber noch ein PHP file benötigt. Wie  zum Beispiel ein einfach Hello World:
```
<?php

echo "Hello, World";
```

Um diese dann zu laden, muss in Powershell als Admin zuerst in den richtigen Ordner navigiert werden, wo das Dockerfile abgespeichert ist.
Danach folgenden Befehlt ausführen.
```
docker build -t [Name des Images] .
```
Jetzt kann der Container gestartet werden mit
```
docker run -p [port][vergebener name des Images]
#Zum beispiel
docker run -p 80:80 hello-world .
```
Jetzt kann in unserem Fall localhost aufgerufen werden.
Bei einer Änderung des PHP files, wird die Webseite nicht aktualisiert.
Dafür müsste man den Container jedes mal wieder neu starten. Um dies einfach zu gestallten kann man ein Directory für Docker mounten. Mit folgendem command:
```
docker run -p 80:80 -v [directory pfad]:[pfad auf dem container] hello-world
#In unserem Beispiel
docker run -p 80:80 -v 'C:\Users\ELH9\OneDrive - HAWORTH INC\Schule\Modul 300\Github-local-Repository\Modul-300\Docker\src\':/var/www/html/ hello-world
```
Jetzt kann das PHP file im src Ordner abgeändert werden und Docker aktualisiertdoc die Webseite automatisch.
![Falls es nicht funktionieren sollte, wird es daran liegen, dass Docker keine zugriff auf den Pfad hat. Dies kann angepasst werden, indem man in den Settings Docker zugriff auf den Datenträger gibt.](https://github.com/Lukas-Hunziker/Modul-300/blob/master/Docker_Shared-Drives_Error.png)

Falls es dann immer noch nicht funktionieren sollte wird es daran liegen, dass die Firewall den Zugriff blockt. Also in meinem Beispiel ist es unmöglich dies zu ändern, da es von der Domäne verwaltet wird und somit immer alles von Docker abgeblockt wird.

## Mehrere Docker Services zusammen benutzen

Um mehrere Services miteinander zu benutzen kann kein ein Docker-compose file erstellt werden. So muss nicht jeder Service mühsam einzeln mit 
```
docker run -p [port][vergebener name des Images]
```
gestartet werden.

In unserem Fall sieht das docker-compose.yml file folgendermassen aus:
```
version: '3'

services:
    product-service:
        build: ./product
        volumes:
         - ./prodcut:/usr/src/app
        ports:
          - 5001:80
    
    website:
      image: php:apache
      volumes:
        - ./website:/var/www/html
      ports:
        - 5000:80
      depends_on:
        - product-service
```

Wenn dieses File erstellt ist, können die definierten Services ganz einfach mit
```
docker-compose up
```
gestartet werden.

Bei dem website service wurde sogar auf das Dockerfile verzichtet, indem einfach ein image geladen wird und dann der Ordner website dem Service geshared wird.

Beim product service wurde ein Dockerfile erstellt wasa folgendermassen aussieht:
```
FROM php:7.0-apache
COPY src/ /var/www/html
EXPOSE 80
``` 
Um die Products aufzulisten wurde ein Python File erstellt, was folgenden Code beinhaltet:
```
# Product service

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(self):
		return{
				'products': ['Bannane',
							'Schokolade',
							'Donut']
			  }

api.add_resource(Product, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
```
Damit dieses Python file vom Docker ausgeführt wird, benötigt man noch ein requirements.txt file was folgendermassen aussieht:
```
Flask==0.12
flask-restful==0.3.5
```
Für die Webseite wurde ein einfach PHP file erstellt, was folgendermassen aussieht:
```
<html>
	<head>
		<title>My Webshop</title>
	</head>
	
	<body>
		<h1>Welcome to my Webshop</h1>
		<ul>
			<?php
				$json = file_get_contents('http://product-service');
				$obj = json_decode($json);
				
				$products = $obj->products;
				foreach ($products as $product) {
					echo "<li>$product</li>";
				}				
	</body>
</html>
```
