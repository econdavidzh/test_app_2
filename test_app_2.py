import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la App:
st.set_page_config(page_title="Mi App en Python", page_icon="📊")

# Barra lateral:
st.sidebar.markdown('__Conceptos y Aplicaciones Estadísticas__')
st.sidebar.image("Images//bioadviser.png", use_column_width=True)
st.sidebar.markdown('Introducción')
st.sidebar.markdown('Origen e historia de la estadística')
st.sidebar.markdown('Conceptos Estadísticos:')
st.sidebar.markdown(' * Población y Muestra')
st.sidebar.markdown(' * Tipos de Variables')
st.sidebar.markdown('Medidas de tendencia central')
st.sidebar.markdown('Medidas de dispersión')
st.sidebar.markdown('Medidas de posición')
st.sidebar.markdown('Visualización de datos')
st.sidebar.markdown('Aplicación elaborada para los estudiantes de Fundamentos de Python de [David Zambrano](https://www.linkedin.com/in/david-enrique-zambrano-a753a764/)')

# Estructura:
## Título de la Aplicación:
st.image('Images//CCBIO.png')
st.title('Conceptos y Aplicaciones de la Estadística')
st.subheader('Introducción')

## Imagen introducción:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//estadis.jpg",  width=500)
    
## Texto Introducción:
st.markdown('__¿Qué es la estadística?__ La estadística es una disciplina científica que se ocupa de la obtención, orden y análisis de un conjunto de datos con el fin de obtener explicaciones y predicciones sobre fenómenos observados. Los tipos de estadística se puede subdividir en dos grandes ramas: descriptiva e inferencial.')
st.markdown('_-_ __Estadística descriptiva:__ Se refiere a los métodos de recolección, organización, resumen y presentación de un conjunto de datos. Se trata principalmente de describir las características fundamentales de los datos y para ellos se suelen utilizar indicadores, gráficos y tablas.')
st.markdown('_-_ __Estadística inferencial:__ Se trata de un paso más allá de la mera descripción. Se refiere a los métodos utilizados para poder hacer predicciones, generalizaciones y obtener conclusiones a partir de los datos analizados teniendo en cuenta el grado de incertidumbre existente.')

## Origen e historia:
st.subheader('Origen e historia de la estadística')
st.markdown('La historia de la estadística data desde antes del 3.000 antes de Cristo. Nace con el objetivo de recolectar información que necesitaba el Estado, por ejemplo, sobre la agricultura y el comercio.')

## Imagen origen e historia de la estadística:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//agricultura.jpeg",  width=500)
    
## estadística y modernidad:
st.markdown('En la antigua Asiria y en Egipto se tiene evidencia de la recolección de datos estadísticos. Asimismo, en Roma se recogían datos demográficos de los habitantes del imperio, como aquellos de natalidad y mortalidad. Esto, con el propósito de tomar mejores decisiones desde el gobierno.')
st.markdown('Posteriormente, durante la Edad Media, la estadística no tuvo grandes avances. Sin embargo, en la Edad Moderna se elaboraría el primer censo estadístico moderno. Luego, hacia el siglo XX, se comenzaron a incorporar herramientas matemáticas provenientes de la teoría de la probabilidad a la estadística.')
st.markdown('La estadística continúa desarrollándose y cada vez más deprisa. Junto con la computación y los programas informáticos, ha sido posible almacenar grandes cantidades datos, y realizar cálculos en fracciones de segundo que hace unos años eran inimaginables. Como resultado de estos avances, la __estadística__ es la piedra angular para el desarrollo de lo que hoy conocemos como __Inteligencia Artificial__.')

## Imagen inteligencia artificial:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//ai.jpeg",  width=500)

## Conceptos estadísticos:
st.subheader('__Conceptos estadísticos__')
st.markdown(' - __Población:__ Es el conjunto de individuos que reúnen una característica que desea ser estudiada.')
st.markdown(' - __Muestra:__ Es un subgrupo de individuos extraídos de una población que debe representar adecuadamente la totalidad del grupo.')

## Imagen población y muestra:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//muestra.jpeg",  width=500)
    
## Introducción a la base de datos:    
st.markdown('La siguiente base de datos contiene la información de __5806 series y películas__ que se encuentran en __Netflix__. Vamos a tomar una muestra de estas para estudiar varios conceptos estadísticos. La descripción de las variables es la siguiente:')
st.text("""
    id: The title ID on JustWatch.
    title: The name of the title.
    type: TV show or movie.
    description: A brief description.
    release_year: The release year.
    age_certification: The age certification.
    runtime: The length of the episode (SHOW) or movie.
    genres: A list of genres.
    production_countries: A list of countries that produced the title.
    seasons: Number of seasons if it's a SHOW.
    imdb_id: The title ID on IMDB.
    imdb_score: Score on IMDB.
    imdb_votes: Votes on IMDB.
    tmdb_popularity: Popularity on TMDB.
    tmdb_score: Score on TMDB.
""")

## organización de variables:
cualitativas = ['selecciona una variable', 'type', 'release_year', 'age_certification', 'genres', 'first_genre', 'production_countries', 'first_country']
cuantitativas = ['selecciona una variable', 'release_year', 'runtime', 'seasons', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']
lista_variables = ['type', 'release_year', 'age_certification', 'genres', 'production_countries', 'runtime', 'seasons', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']

## acceso a base de datos:
netflix = pd.read_csv('Data//titles.csv')
netflix    

## determinar tamaño de la muestra:
st.subheader('Ahora vamos a determinar el __tamaño__ de nuestra muestra:')
st.markdown('El __tamaño de la muestra__ se le conoce como aquel número determinado de sujetos, o cosas, que componen la muestra extraída de una población, necesarios para que los datos obtenidos sean __representativos de la población.__')

## definición de la muestra:
sample_size = st.slider('Tamaño de la muestra', 0, 1000)
st.markdown('Así se ha generado nuestra muestra con el tamaño indicado:')

@st.cache
def sample_function(sample_size):
    sample = netflix.sample(sample_size).reset_index(drop = True)
    sample['genres'] = sample['genres'].replace("[]", "['no_genre']'")
    sample['first_genre'] = sample['genres'].apply(lambda x: x.split("'")[1])
    sample['production_countries'] = sample['production_countries'].replace("[]", "['undefined']")
    sample['first_country'] = sample['production_countries'].apply(lambda x: x.split("'")[1])
    return sample

sample = sample_function(sample_size)
sample

## tipos de variables:
st.subheader('Ahora recordemos los tipos de variables:')
st.markdown('__Variable:__ La característica o cualidad de una muestra o población a la cual se le puede asignar un valor.')
st.markdown('__Variables cuantitativas:__ Son variables que se expresan numéricamente:')
st.markdown(' - __Variable continua:__ Toman un valor infinito de valores entre un intervalo de datos. Por ejemplo, el tiempo que tarda un corredor en completar una carrera de 100 metros.')
st.markdown(' - __Variable discreta:__ Toman un valor finito de valores entre un intervalo de datos. Por ejemplo, el número de helados vendidos.')
st.markdown('__Variables cualitativas (categóricas):__ Son variables que se expresan, por norma general, en palabras. Esta se puede diferenciar entre:')
st.markdown(' - __Variable ordinal:__ Expresa diferentes niveles y orden.')
st.markdown(' - __Variable nominal:__ Expresa un nombre claramente diferenciado. Por ejemplo el color de ojos puede ser azul, negro, castaño, verde, etc.')

## momentos estadísticos:
st.subheader('Momentos Estadísticos')
st.markdown('Son medidas que ofrecen información sobre el centro de un conjunto de datos (__medidas de tendencia central__), otras sobre la dispersión o variabilidad (__medidas de dispersión__), y otras sobre la __posición__ de un valor como los percentiles.')
st.markdown('__Medidas de tendencia central:__')
st.markdown('__Mediana:__ es el número que ocupa el lugar central una vez estos han sido ordenados de menor a mayor.')
st.markdown('__Moda:__ es el valor más frecuente en una distribución de datos, es decir, el que más veces aparece.')
st.markdown('__Media:__ también conocida como __promedio__, es el resultado de la suma de todos los valores de una distribución dividida entre el número de valores sumados.')

## imagen media, moda, mediana
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//media.jpeg",  width=500)
    
## histograma medidas de tendencia central:
st.subheader('Observemos estos parámetros de tendencia central:')
st.markdown('Vamos a crear unos histogramas para visualizar la distribución de los datos así como sus correspondientes media, moda y mediana:')

@st.cache
def histograma(variable):
    mediana = np.round(sample[variable].median(), 2)
    moda = sample[variable].mode()[0]
    media = np.round(sample[variable].mean(), 2)   
    fig = px.histogram(sample, x=variable, text_auto=True)
    fig.add_vline(x=mediana, line_dash = 'dot', line_color = 'red')
    fig.add_vline(x=moda, line_dash = 'dash', line_color = 'yellow')
    fig.add_vline(x=media, line_dash = 'dashdot', line_color = 'blue')
    fig.update_traces(marker_line_width = 1.5, opacity = 0.7)
    return fig, mediana, moda, media

variable = str(st.selectbox('Selecciona una variable:', cuantitativas))

try:
    st.plotly_chart(histograma(variable)[0], use_container_width = True)
    st.write("mediana =", histograma(variable)[1], "(roja)")
    st.write("moda =", histograma(variable)[2], "(amarilla)")
    st.write("media =", histograma(variable)[3], "(azul).")
except:
    st.write('Selecciona una variable para graficar')
    
## gráfica de barras para variables cuantitativas:    
st.markdown('Para las variables cualitativas podemos construir unas gráficas similares para observar las frecuencias absolutas: las gráficas de barras.')

@st.cache
def grafica_de_barras(variable):
    conteo = sample.groupby(variable).count()["id"].sort_values(ascending=False)
    filtro = conteo > 1
    fig = px.bar(conteo[filtro], text_auto=True)
    fig.update_traces(marker_line_width = 1.5, opacity = 0.7)
    return fig

variable_cuali = str(st.selectbox('Selecciona una variable:', cualitativas))

try:
    st.plotly_chart(grafica_de_barras(variable_cuali), use_container_width = True)  
except:
    st.write('Selecciona una variable para graficar')    
    
## medidas de dispersión:
st.subheader('Medidas de dispersión:')
st.markdown('Son números que indican si una variable se mueve mucho, poco, más o menos que otra. La razón de ser de este tipo de medidas es conocer de manera resumida una característica de la variable estudiada.')
st.markdown(' - __Rango:__ es un valor numérico que indica la diferencia entre el valor máximo y el mínimo de una población o muestra estadística.')
st.markdown(' - __Desviación media:__ es la media de los valores absolutos (esto es, sin tener en cuenta si son positivos o negativos) de las desviaciones de una serie de observaciones con respecto a su media.')
st.markdown(' - __Varianza:__ es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.')
st.markdown(' - __Desviación Estándar:__ ofrece información de la dispersión respecto a la media. Su cálculo es exactamente el mismo que la varianza, pero realizando la raíz cuadrada de su resultado.')    
    
## imagen medidas de dispersión:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//desv.jpeg",  width=500)
    
## medidas de posición de valor:    
st.subheader('Medidas de posición de un valor:')
st.markdown('__Percentiles:__ El percentil es una medida estadística la cual divide una serie de datos ordenados de menor a mayor en cien partes iguales. Se trata de un indicador que busca mostrar la proporción de la serie de datos que queda por debajo de su valor.')
st.markdown(' - __Los percentiles__ dividen a la distribución en cien partes. Por lo tanto, dan los valores correspondientes al 1%, al 2% ... y al 99% de los datos.')
st.markdown('__Los cuantiles__ suelen usarse por grupos que dividen la distribución de los datos en partes iguales; entendidas estas como intervalos que comprenden la misma proporción de valores. Los más usados son:')
st.markdown(' - __Los cuartiles,__ que dividen a la distribución en cuatro partes (corresponden a los cuantiles 0.25, 0.50, 0.75 y 1).')
st.markdown(' - __Los quintiles,__ que dividen a la distribución en cinco partes (corresponden a los cuantiles 0.20, 0.40, 0.60, 0.80 y 1).')
st.markdown(' - __Los deciles,__ que dividen a la distribución en diez partes (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 y 1).')

## imagen medidas de posición de valor:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//perc.png",  width=500)
    
## visualización de datos:    
st.subheader('Visualizaciones de datos:')
st.markdown('Cuando piensas en la __visualización de datos__, tu primer pensamiento probablemente se dirija de inmediato a __gráficos de barras__ o __gráficos de pastel.__ Si bien esto puede ser una parte integral de la visualización de datos y una línea base común para muchos gráficos de datos, la visualización correcta debe emparejarse con el conjunto correcto de información. Los gráficos simples son solo la punta del iceberg. Hay toda una selección de métodos de visualización para presentar datos de manera eficaz e interesante.')
st.markdown('La visualización correcta nos ayuda a responder preguntas sobre nuestros datos, plantear hipótesis sobre estos, y nos ayuda a transmitirla adecuadamente a los demás.')
st.markdown(' - __Gráfica de pastel:__ Tiene la forma de un disco dividido en sectores, cuyas áreas son proporcionales a los porcentajes de los distintos componentes de la población estadística.')

## gráfica de pastel:
@st.cache
def grafica_pastel(variable, threshold):
    temp = sample[variable].value_counts()[sample[variable].value_counts() > threshold]
    fig = px.pie(temp, values = temp.values, names = temp.index)
    return fig

variable = str(st.selectbox('Selecciona una variable para la gráfica de pie:', cualitativas))
threshold = st.slider('Límite inferior de frecuencia de la categoría', 0, 50)

try:
    st.plotly_chart(grafica_pastel(variable, threshold), use_container_width = True)  
except:
    st.write('Selecciona una variable para graficar')

## gráfica de cajas y bigotes:
@st.cache
def cajas_bigotes(var_cuali, var_cuanti, color):
    fig = px.box(sample, x = var_cuali, y = var_cuanti, color = color)
    return fig

var_cuali = str(st.selectbox('Selecciona una variable cualitativa para la gráfica de cajas y bigotes:', cualitativas))
var_cuanti = str(st.selectbox('Selecciona una variable cuantitativa para la gráfica de cajas y bigotes:', cuantitativas))
color = str(st.selectbox('Selecciona una variable para diferenciar por colores:', cualitativas))

try:
    st.plotly_chart(cajas_bigotes(var_cuali, var_cuanti, color), use_container_width = True)  
except:
    st.write('Selecciona una variable para graficar')
    
## gráfica de dispersión de puntos:    
st.markdown(' - __Gráfica de dispersión:__ se utiliza cuando hay muchos puntos de datos diferentes y se desea destacar las relaciones entre estos datos. Esto es útil cuando se buscan valores atípicos o para entender la distribución de los datos.')

@st.cache
def grafica_dispersion(var1, var2, color):
    fig = px.scatter(sample, x = var1, y = var2, color = color)
    return fig

var1 = str(st.selectbox('Selecciona una variable para el eje X:', cuantitativas))
var2 = str(st.selectbox('Selecciona una variable para el eje Y:', cuantitativas))
color = str(st.selectbox('Selecciona una variable para diferenciar por color:', cualitativas))

try:
    st.plotly_chart(grafica_dispersion(var1, var2, color), use_container_width = True)  
except:
    st.write('Selecciona las variable para graficar')
    
st.markdown('Para conocer muchos más tipos de gráficos para visualizar los datos puedes ingresar al siguiente link:')
st.write('https://seaborn.pydata.org/examples/index.html')    
    
st.subheader('Referencias:')

st.write('https://economipedia.com/definiciones/estadistica.html')
st.write('https://economipedia.com/historia/historia-de-la-estadistica.html')
st.write('https://economipedia.com/definiciones/variable-estadistica.html')
st.write('https://economipedia.com/definiciones/medidas-de-dispersion.html')
st.write('https://www.dicenlen.eu/es/diccionario/entradas/desviacion-media')
st.write('https://curiosoando.com/que-son-los-percentiles')
st.write('https://www.tableau.com/es-mx/learn/articles/data-visualization')
st.write('https://tudashboard.com/grafica-de-pastel/')
st.write('https://tudashboard.com/diagrama-de-caja-bigote/')
st.write('https://tudashboard.com/grafica-de-dispersion/')
    
