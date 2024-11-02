# Proyecto de python para programacion aplicada.

## Instalacion del proyecto (para el grupo de desarrollo)

Haz un fork del repositorio haciendo click en Fork.

Copiate el repo haciendo un

    git clone https://url-del-fork-del-proyecto.com .

En la carpeta donde clonaste el proyecto, genera un ambiente virtual para manejar las dependencias de desarrollo.

    python -m venv .venv

Asegurate de llamarlo ".venv" para que los formateadores puedan ignorar la carpeta correctamente.

Activa el ambiente virtual

    .venv\Scripts\activate

Para desactivarlo, solo utiliza el comando deactivate

    deactivate

Una vez activado, descarga las dependencias principales del proyecto haciendo.

    pip install -r requirements.txt

## Correr el proyecto
Una vez instaladas las dependencias del proyecto, puedes hacer un simple:

    python -m build

Esto te creara todos los links para poder ejecutar de manera mas sencilla el proyecto. Solo te falta instalar el proyecto:

    pip install -e .

Con esto podrás ejecutar el siguiente comando:

    tpo5

Y el resultado actual debería ser la impresion de una cadena diciendo lo siguiente:

    "Configuracion inicial para el proyecto"

## Hacer cambios al proyecto.

Trabajaremos sobre main para simplicidad, pero al momento de desarrollar una nueva funcionabilidad, seguiremos los
siguientes pasos:

    git checkout -b nueva-funcionabilidad

Al terminar el desarrollo de la nueva funcionabilidad, agregar los cambios al stage de git:

    git add * (cambia el * por los archivos que desees stagear)

Luego de eso haz el commit. Sobre esto queda decir que el commit tiene que ser claro y sencillo.
Utiliza prefijos como add, update o fix para especificar sobre qué se basa tu commit. Al final quedara algo como esto:

    git commit -m "add: nueva funcionabilidad para el proyecto"

Luego de eso, dirigete a tu fork del repo y cliquea "Make a pull request"
Luego de eso coloca un mensaje descriptivo para la solicitud del cambio y espera su aprobación!
