# Coordinate Picker

Este proyecto es una aplicación en Python que permite a los usuarios seleccionar manualmente una región de la pantalla y obtener las coordenadas de esa región. Es útil para capturar imágenes de áreas específicas de la pantalla.

## Estructura del Proyecto

- `src/main.py`: Punto de entrada de la aplicación. Contiene la lógica principal para interactuar con el usuario y obtener las coordenadas.
- `src/coordinate_picker.py`: Contiene la lógica para capturar las coordenadas de la región especificada.
- `src/utils/__init__.py`: Funciones auxiliares utilizadas en el proyecto, como la conversión de coordenadas o la validación de entradas.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.
- `.gitignore`: Archivos y carpetas que deben ser ignorados por Git.

## Requisitos

Asegúrate de tener Python instalado en tu sistema. Este proyecto requiere las siguientes bibliotecas:

- `pyautogui`

Puedes instalar las dependencias ejecutando:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

Sigue las instrucciones en pantalla para seleccionar la región de la que deseas obtener las coordenadas. Las coordenadas se mostrarán en la consola y se pueden utilizar para capturas de pantalla o cualquier otra aplicación que requiera estas coordenadas.