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
