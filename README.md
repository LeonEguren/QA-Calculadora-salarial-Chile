# Calculadora Salarial Chile

Este proyecto automatiza las pruebas para una aplicación de **calculadora salarial** en Chile, utilizando **Python** y la librería **Playwright**.

## Descripción

El objetivo de este proyecto es realizar pruebas automatizadas sobre una calculadora salarial, asegurando que funcione correctamente en todos los casos de uso esperados. Para ello, se utilizan pruebas automatizadas con **Playwright** en el lenguaje de programación **Python**.

## Requisitos

Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- Node.js
- Playwright para Python

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/calculadora-salarial-chile.git
   cd calculadora-salarial-chile
2. Crea un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias necesarias:
pip install -r requirements.txt

4. Instala Playwright
pip install playwright



## La estructura de carpetas del proyecto es la siguiente:
/calculadora-salarial-chile
    /tests              # Carpeta con los archivos de prueba
    /database           # Scripts para la gestión de base de datos (si es necesario)
    .gitignore          # Archivos o carpetas a ignorar por Git
    requirements.txt    # Archivo con las dependencias del proyecto
    README.md           # Este archivo


## Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama para tu característica (git checkout -b feature-nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva característica').
Haz push a la rama (git push origin feature-nueva-caracteristica).
Crea un Pull Request.

## Correr casos de prueba con reporte
pytest --html=report.html 

## Correr casos de prueba desde  la Extensión de Testing de Playwright
- En el panel lateral de Test Explorer, verás una lista de las pruebas disponibles.
- Puedes hacer clic en cualquier prueba para ejecutarla.
- Si quieres ejecutar un archivo completo, haz clic en el archivo o una carpeta de pruebas.
- Ver Resultados:

Los resultados de las pruebas se mostrarán en la parte inferior de la ventana de VSCode, donde podrás ver si pasaron o fallaron, así como detalles adicionales si las pruebas fallaron.

Este método te permite correr y gestionar las pruebas de manera visual directamente desde VSCode, sin tener que usar la terminal.

