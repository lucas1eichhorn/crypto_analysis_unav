## PYTHON PARA ANALISIS DE DATOS

## MASTER BIG DATA SCIENCE

**UNAV 21-22**

# Análisis de Criptomonedas

Alumno: Lucas Eichhorn


## Repositorio:

Como software de control de versiones para la realizacion del proyecto se utilizó la tecnología GIT y un
repositorio de GitHub, que permiten la eficiencia, confiabilidad y compatibilidad del mantenimiento de
versiones de la aplicación al tener un gran número de archivos de código fuente.


## Framework de desarrollo: Streamlit

Para el desarrollo del presente proyecto se decidió aprender y utilizar el framework open-source Streamlit,
el cuando permite crear aplicaciones web para Machine Learning y Ciencia de datos en simples pasos. En
este caso permitió desarrollar rápidamente la aplicacion web e implementarla fácilmente usando el
framework para visualizar las cotizaciones de los pares de criptomonedas.

Streamlit ofrece acceso a su repositorio en la nube Streamlit Cloud para que los equipos implementen,
administren y colaboren fácilmente en sus aplicaciones Streamlit.

Este proyecto hace uso del plan gratuito de Streamlit Cloud, que como PasS permitió realizar el deploy del
proyecto y distribuirlo por internet para su presentación:

Pueden acceder al mismo mediante el siguiente [enlace](https://share.streamlit.io/lucas1eichhorn/crypto_analysis_unav/project_crypto_reader/app.py)

## Estructura del proyecto:

**POETRY**

La estructura inicial del proyecto fue creada con Poetry, la cual es es una herramienta para la gestión de
dependencias y el empaquetado en Python. Permite declarar las bibliotecas de las que depende el
proyecto y administrar la instalación o actualización al momento de compartir el proyecto.

Inicialmente se inició un nuevo proyecto ejecutando el comando:

```
poetry new project-critpo-reader
```
De esta manera se crea el proyecto con un template base de estructura
de archivos que nos permite desarrollar la aplicación a partir de aqui.


Poetry utiliza un archivo pyproject.toml que se ubica en el raíz de proyecto y donde podemos declarar las
dependencias de Python que se utilizaran para la ejecución del mismo.

Al utilizar el comando _poetry add [nombre_dependencia]_ , este se encargará de agregar por nosotros la
dependencias utilizadas en el archiv .toml

Para el despliegue de la aplicación en Streamlit se hace uso de un archivo **_requirements.txt_** donde se han
copiado los librerías requeridas. Dicho archivo es leído en la instancia remota de Streamlit para la
instalación de paquetes de forma automatizada.

**DIRECTORIOS:**

En la estructura del proyecto se pueden diferenciar diferentes directorios:

- Directorio raiz (/)

Encontramos los archivos de configuración de los diferentes entornos de ejecución y herramientas
utilizadas como soporte para el proyecto:

_.gitignore_ – archivos excluidos del versionado

_requirements.txt_ – dependencias a instalar en Streamlit Cloud

_pyproject.toml_ – dependencias a instalar con Poetry

___init__.py -_ utilizado para marcar directorios como directorios de paquetes de Python.

- mocks/


Aquí se encuentran los archivos estáticos con “mocks” que representan una copia de las llamadas a la API
para ejecutar los test. En este caso se considera beneficios en la utilización de mocks para poder prevenir
innecesarias llamadas a la API durante el testeo.

Muchas veces en los entornos con CI/CD de DevOps las aplicaciones no se tiene permiso de acceso a
internet para realizar las API por lo que su utilización resulta conveniente o se suele evitar llamarlas para
sobrecargar innecesariamente los servicios.

- test/

Contiene los casos de prueba del código con _unit testing e integration testing_. Para la realización de
pruebas se ha utilizado la librería **_pytest_** el cual se abordara con mas detalle próximamente.

- project_cripto_reader/

En este directorio encontramos los archivos y clases principales de la aplicación:

**CLASES:**

Si bien la ejecución de las tareas podría considerarse sencilla para hacer en un simple script en Python, a
fin de cubrir el requerimiento de utilización de POO para el proyecto se decidió crear algunas clases que
albergues los datos de las criptomonedas y parámetros de conexión a la API de Kraken.

_-CotizacionCripto_ : contiene la estructura de una cotización de un par de criptomonedas con los datos
necesarios para graficas las velas japonesas

_-KrakenApiConnector_ : utilizando el patrón de diseño _singleton_ se crea una clase cuya instancia única
provee la conexión a la API de Kraken para obtener las cotizaciones solicitadas.

**LIBRERÍAS DESTACADAS:**

Para la obtención y procesamiento de los datos de las cotizaciones desde la web de kraken ademas de las
librerías regulares para este tipo de proyectos como pueden ser Pandas o Numpy, se quiere destacar el uso
de las siguientes librerías de Python:


- **Krakenex** : Este paquete es lo más sencillo posible y solo proporciona una interfaz mínima para el
    intercambio de criptomonedas en Kraken.
- **Pykrakenapi** : librería que implementa los métodos de la API de Kraken utilizando el paquete de
    python krakenex a bajo nivel. Provee una capa de abstracción de los métodos de la API de
    Kraken en métodos simples Python y con las respuestas JSON convertidas ya en dataframes de
    Pandas.
- **ta :(technical analysis):** para el calculo del vwap se decidió utilizar una librería conocida por
    dedicarse al análisis técnico y que nos provee distintos indicadores, entre ellos el solicitado de
    VWAP.

```
Esta librería de análisis técnico es útil para realizar cálculos a partir de datos de series de tiempo
financieras (Apertura, Cierre, Alto, Bajo, Volumen). Está construido sobre Pandas y Numpy
```
**MANEJO DE ERRORES:**

En el presente proyecto se ha considerado la captura de los posibles errores lanzados por la API de Kraken,
de esta forma podremos tener una salida controlada de la aplicación e informar al usuario mediante la
interfaz web de lo ocurrido:


## Ejecución de la app en local mediante pycharm

Luego de clonar proyecto desde el repositorio de GitHub en su ordenador se puede abrir el mismo desde
PyCharm, el cual tiene incorporada la herramienta de _virtualenv_ la cual permite trabajar con un entrono
virtual para el proyecto.

Seleccionando el archivo de dependencias **_requiriments.txt_** (también utilizado en Streamlit Cloud)
PyCharm se encargará de instalar en su ordenador las librerías utilizadas en el para la ejecución del la
aplicación.

Para ejecutar la aplicación en local se deberá dirigir al directorio project_crypto_reader y lanzar la
aplicación. Dichas tareas han de realizarse con los siguientes comandos por la terminal:

```
cd project_crypto_reader
streamlit run app.py
```
## Guía de usuario:

La interfaz web desarrollada con Streamlit presenta al usuario un menú de opciones para elegir los
parámetros por los que desea filtrar la cotizaciones de la criptomonedas:

**Fecha** : en primer lugar el usuario selecciona, mediante un input de tipo Datepicker, la fecha desde el cual
desea obtener la cotización seleccionada. La API de Kraken solo nos devuelve 720 registros a partir de la
fecha solicitada para el intervalo de velas seleccionado


**Criptomonedas** : Disponemos de un dropdown completado mediante un request a la API de Kraken, de la
cual obtiene los pares de criptomonedas que tienen cotización disponible en el exchange, mostrando al
usuario las opciones para visualizar el par deseado.

**Intervalo velas:** mediante este componente de tipo dropdown el usuario puede seleccionar con que
periodo desea que se generen las velas japonesas que muestran la evolución de precio en el grafico.

**Intervalo de VWAP:** Este input permite al usuario elegir el intervalo con el que desea que se calcule el
indiciador de precio ponderado por volumen, conocido como VWAP.

## Testing con Pytest:

Se ha utilizado la librería Pytest para realizar las pruebas en el proyecto. El directorio **_test_** contiene los
casos de prueba del código con _unit testing e integration testing_. Tambien han sido incluidos los archivos
estáticos con “mocks” que representan una copia de las llamadas a la API para ejecutar los test. En este
caso se considera beneficios en la utilización de mocks para poder prevenir innecesarias llamadas a la API
durante el testeo.

Para ejecutar las pruebas se debe estar posicionado en el directorio raíz de proyecto desde una terminal, y
utilizar el comando:

python -m pytest tests


### NOTA:

Un error que no se ha llegado a solucionar, requerien que previamente a
correr los tests de cambié la importación del modulo de la API de Kraken
especificando el directorio en que se encuentra, ya que sino fallan los
test porque no se encuenta el modulo especificado.

## Linter: Pylint con PEP8

Es inevitable tener errores en el código cuando desarrollamos una aplicación. estos errores a veces son
malos y causan problemas en la interfaz que generan incomodidad en los usuarios, otros comprometen la
seguridad del sistema.

En este proyecto se ha utilizado la herramienta de código abierto Pylint enfocada en el proceso de "lintig"
para python que pude ser integrada a PyCharm.

Pylint es la herramienta predominante para la tarea de "limpiar" código python de acuerdo al estándar
PEP8, encargándose de tareas como: comprobar la longitud del código de línea, comprobar si los nombres
de las variables están bien formados de acuerdo con su estándar de codificación, comprobar si se utilizan
módulos importados, etc.



