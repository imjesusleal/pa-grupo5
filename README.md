# Proyecto de python para programacion aplicada.

## Instalacion de la aplicacion

```
pip install -i https://test.pypi.org/simple/ improc
```

## Usage

```
improc -h
````

Les desplegará el menu de opciones de ayuda. Es necesario indicar el directorio donde se encuentran las imagenes y el directorio de salida.  Este ultimo se creará de no ser encontrado.

```
improc . .\output --operation grayscale --mode comparar -c 4
```

Para la mayoria de los casos, este debería ser la forma ideal de utilizar la herramienta.
El primer punto ('.') seguido del nombre de la herramienta hace referencia al directorio donde estas parado, seguido del directorio de salida, seguido de la operacion a realizar (por ahora, resize y grayscale), el modo en el que quieres procesarlas (threads o procesos, para concurrencia o paralelismo) y por ultima -c que es la cantidad de hilos o procesos que quieres manejar.
