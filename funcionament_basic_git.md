# Funcionamiento básico git  

### 1. Como clonar un repositorio git?

  * Para clonar un ***repositorio git*** tenemos que ir al directorio donde queramos depositarlo y una vez dentro, ejecutar el comando **git clone "la url dela pagina del *repositorio git*"** y ya estara clonado en el directorio indicado.  

### 2. Como editar o crear nuevos ficheros y subirlos al repositorio git?

  * Para editar un archivo ya creado ejecutamos el comando **vi "el nombre del archivo"**, entonces se abrira y le tendremos de dar a la tecla **i** para comenzar a editar, si el archivo no esta creado el comando **vi "el nobre que quieras"** te creara un archivo nuevo. Una vez acabada la edicion le damos a la tecla **Esc** y introducimos el comando **:wq** para volver a la terminal.  
  * Una vez hecho el paso anterior para subirlo debemos ejecutar el comando __git add *__, despues ejecutar el comando **git commit -am "el nombre del archivo"** y para terminar hacemos un **git push**, una vez hecho eso nos pediran el usuario y contraseña de **GitHub**, una vez lo pongamos todo lo que este dentro de nuestro directorio se habra subido a nuestro *repositorio git*.  

### 3. Como recuperar los ficheros del repositorio remoto?

 * Para recuperar los ficheros del **repositorio remoto** ejecutamos el comando **git pull** dentro del directorio para los archivos del git en el ordenador.  
  
