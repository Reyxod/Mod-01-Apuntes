## Gestión de Volúmenes Lógicos

***

* **Que són:** 

La gestión de volúmenes lógicos o ***logical volum manager (LVM)*** , es una implementación de un administrador de volúmenes lógicos para el kernel Linux. 

***

* **Tipologias de gestión volúmenes lógicos:**  

**PV:** Las siglas significan ***Physical volume.*** Es lo que llamariamos la identificación de los discos. A la hora de crear un volumen físico puedes hacerlo tanto con discos normales como con raids.  
**Como crear un PV:** `pvcreate/dev/sda`  

**VG:** Las siglas significan ***Volume group.*** Serian unos discos virtuales. Cuando creas un grupo de volúmenes este coje todas los gigabytes de los dicos que tenga y los utiliza todos no como algunos raids. Se le pueden añadir o quitar discos en caliente y esta creado de uno o varios LV.  
**Como crear un VG:** `vgcreate "nombre que le queramos dar" "Pv: los que queramos añadir"`

**LV:**
