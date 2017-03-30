## 1. Sistemas Raid:  

|   Tipos  | Num. Discos | Num. Fallados | Capacidad |    Read   |   Write   |
| -------- | ----------- | ------------- | --------- | --------- | --------- |
|  Raid 0  |      2      |       0       |    100%   | Excelente | Excelente |
|  Raid 1  |    2(MAX)   |       1       |     50%   | Very good |    Good   |
|  Raid 5  |      3      |       1       | 67% - 94% | Very good |    Good   |
|  Raid 6  |      4      |       2       | 50% - 88% |    Good   |    Good   |
|  Raid 10 |      4      |   1/mirror    |     50%   | Very good | Very good |
|  Raid 50 |      6      |   1/Raid 5    | 67% - 94% | Excelente | Very good |
|  Raid 60 |      8      |   2/Raid 6    | 50% - 88% | Very good |    Good   |  

## 2. Como crear raids en Virt-Manager ?  

* Para poder hacer un raid en la maquina virtual lo primero que tenemos de hacer es crear los discos duros que necesitaremos para las mismas, dependiendo de que raid queramos crea seran mas o menos. Creamos los dicos en la pertaña de añadir mas hardware y los hacemos tipo Virtio.  

## 3. Comando para crear una raid 1:  

**mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/(*nombre primer disco*) /dev/(*nombre segundo disco*)**  

## 4. Comando para crear una raid 5:  

**mdadm --create /dev/md1 --level=5 --raid-devices=3 /dev/(nombre primer disco) /dev/(nombre segundo disco) /dev/(nombre tercer disco)**  

## 5. Comando para crear una raid 6:  

**mdadm --create /dev/md1 --level=6 --raid-devices=4 /dev/(nombre primer disco) /dev/(nombre segundo disco) /dev/(nombre tercer disco) /dev/(nombre cuarto disco)**   

## 6. Comando para crear una raid 10:  

**mdadm --create /dev/md1 --level=10 --raid-devices=4 /dev/(nombre primer disco) /dev/(nombre segundo disco) /dev/(nombre tercer disco) /dev/(nombre cuarto disco)**   

