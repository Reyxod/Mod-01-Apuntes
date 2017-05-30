# Tallafocs
### 1. Què es un sistema tallafocs? Quina és la seva finalitat?  
  + Un firewall o cortafuegos es un sistema de seguridad de red que monitoriza y controla el trafico de red que entra y sale en una red basado en unas reglas predeterminadas.  
  + Su finalidad puede ser tanto bloquear nuestro acceso a la red como el proteger nuestra red bloqueando el acceso que otros tiene a esta segun lo que le especifiquemos.  
### 2. Quines generacions de tallafocs hi ha hagut i què millorava cadascun?
  + Primera generacion: Filtraje de paquetes
  
Permetia analizar cada paquete y los comparaba para decidir si bloquearlos o aceptarlos.
  
  + Segunda generación: Filtros de estado

Esta segunda generación ademas tiene en cuenta la colocación de cada paquete individual dentro de una serie de paquetes, esta tecnología és capaz de determinar si un paquete inidica el inicio de la conexión, de si es parte de una conexión existente o un paquete erroneo.

  + Tercera generación: Capa de aplicacion

Actúa sobre la capa de aplicación OSI, puede entender diferentes protocolos y aplicaciones y permite detectar si algún protocolo no deseado se ha colado a través de un puerto no estándar o si estan utilizando algún protocolo para saltarse el firewall.  
### 3. Quines capes té el model OSI?
+ Capas del modelo OSI:

7- Aplicación  
6- Presentación  
5- Sesión  
4- Transporte  
3- Red  
2- Enlace de datos  
1- Física  
### 4. Quines capes té el model TCP/IP? En aquest cas feu una breu descripció de les funcionalitats de cada capa.
  + Aplicación: incorpora aplicaciones de red estándar.
  + Transporte: brinda los datos de enrutamiento, junto con los mecanismos que permiten conocer el estado de la transmisión.
  + Red: responsable de proporcionar el paquete de datos. 
  + Física: especifica la forma en la que los datos deben enrutarse, sea cual sea el tipo de red utilizada.
### 5. A quina capa/capes sol treballar tradicionalment un tallafocs?  
Un cortafuegos o firewall trabaja desde la capa 3 (Transporte) hasta la capa 4 (Aplicación) del modelo TCP / IP
# Tallafocs Linux
### 1. Busqueu quins són els tradicionals sistemes de tallafocs incorporats en linux i anomeneu-los
  + Son el firewalld y el iptables.
### 2. Quins dels anteriors tallafocs estan instal.lats al fedora de classe? Com ho comproveu?  
Los dos vienen por defecto instalados en Linux asi que estan en el de clase.
  + Comprobamos que el firewalld está, ejecutando: systemctl status firewalld.service 
  + Comprobamos que el iptables está, ejecutando: systemctl status iptables 
### 3. Algun dels anteriors tallafocs es troba activat?  
  + Los dos se encuentran inactivos.
### 4. Instal.leu el servidor web httpd o nginx i activeu-ne el servei (dnf installl ...  ; systemctl ....). Indiqueu les comandes i comproveu que des d'una altra màquina podeu accedir via web a la vostra IP (digueu-li a un company). Hauria de sortir la plana per defecte.
  + Para instalarlo: dnf install nginx 
  + Para activar el servicio: systemctl start nginx.service
### 5. Activeu el servei firewalld. Indiqueu com ho feu.
  + Lo activamos ejecutando: systemctl start firewalld.service
### 6. Comproveu si ara es pot seguir accedint.
Ya no se puede acceder.
# Win7
### 1. Porta aquest SO algun tallafocs incorporat?  
El Windows trae por defecto un cortafuegos llamado Firewall de Windows.  
### 2. Arrenqueu una màquina win7 a isard.escoladeltreball.org
### 3. Indiqueu com arribar al tallafocs (passos i pantalles)
1- Abrimos el menú de Inicio  
2- Abrimos el Panel de Control  
3- Hacemos click sobre Sistema y Seguridad  
4- Hacemos click sobre Firewall de Windows  
### 4. Es troba activat en aquest windows?
Si, está activado por defecto.  
