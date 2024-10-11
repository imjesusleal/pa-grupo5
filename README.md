# Proyecto de python para programacion aplicada.

## Instalacion del proyecto (para el grupo de desarrollo)

Copiate el repo haciendo un

    git clone https://url-del-proyecto.com .

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
