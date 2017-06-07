### Comandos para instalar el servidor web:
+ dnf install nginx
### Comandos para activar el servidor web y ver que esta activo:
+ Para activarlo: systemctl start nginx.service
+ Para ver que esta activo: systemctl status nginx.service
### Comandos para activar el cortafuegos firewalld y ver que esta activo:
+ Para activarlo: systemctl start firewalld.service
+ Para ver que esta activo: systemctl status firewalld.service
### Comandos para dar acceso remoto a el servido web:
+ firewall-cmd --zone=FedoraWorkstation --add-port=80/tcp --permanent
+ firewall-cmd --zone=FedoraWorkstation --add-port=80/udp --permanent
+ Para que se apliquen los cambios sin tener se apagar el servicio: firewall-cmd --reload
