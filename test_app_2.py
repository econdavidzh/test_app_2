import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuraci贸n de la App:
st.set_page_config(page_title="Mi App en Python", page_icon="馃搳")

# Barra lateral:
st.sidebar.markdown('__Conceptos y Aplicaciones Estad铆sticas__')
st.sidebar.image("Images//bioadviser.png", use_column_width=True)
st.sidebar.markdown('Introducci贸n')
st.sidebar.markdown('Origen e historia de la estad铆stica')
st.sidebar.markdown('Conceptos Estad铆sticos:')
st.sidebar.markdown(' * Poblaci贸n y Muestra')
st.sidebar.markdown(' * Tipos de Variables')
st.sidebar.markdown('Medidas de tendencia central')
st.sidebar.markdown('Medidas de dispersi贸n')
st.sidebar.markdown('Medidas de posici贸n')
st.sidebar.markdown('Visualizaci贸n de datos')
st.sidebar.markdown('Aplicaci贸n elaborada para los estudiantes de Fundamentos de Python de [David Zambrano](https://www.linkedin.com/in/david-enrique-zambrano-a753a764/)')

# Estructura:
## T铆tulo de la Aplicaci贸n:
st.image('Images//CCBIO.png')
st.title('Conceptos y Aplicaciones de la Estad铆stica')
st.subheader('Introducci贸n')

## Imagen introducci贸n:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//estadis.jpg",  width=500)
    
## Texto Introducci贸n:
st.markdown('__驴Qu茅 es la estad铆stica?__ La estad铆stica es una disciplina cient铆fica que se ocupa de la obtenci贸n, orden y an谩lisis de un conjunto de datos con el fin de obtener explicaciones y predicciones sobre fen贸menos observados. Los tipos de estad铆stica se puede subdividir en dos grandes ramas: descriptiva e inferencial.')
st.markdown('_-_ __Estad铆stica descriptiva:__ Se refiere a los m茅todos de recolecci贸n, organizaci贸n, resumen y presentaci贸n de un conjunto de datos. Se trata principalmente de describir las caracter铆sticas fundamentales de los datos y para ellos se suelen utilizar indicadores, gr谩ficos y tablas.')
st.markdown('_-_ __Estad铆stica inferencial:__ Se trata de un paso m谩s all谩 de la mera descripci贸n. Se refiere a los m茅todos utilizados para poder hacer predicciones, generalizaciones y obtener conclusiones a partir de los datos analizados teniendo en cuenta el grado de incertidumbre existente.')

## Origen e historia:
st.subheader('Origen e historia de la estad铆stica')
st.markdown('La historia de la estad铆stica data desde antes del 3.000 antes de Cristo. Nace con el objetivo de recolectar informaci贸n que necesitaba el Estado, por ejemplo, sobre la agricultura y el comercio.')

## Imagen origen e historia de la estad铆stica:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//agricultura.jpeg",  width=500)
    
## estad铆stica y modernidad:
st.markdown('En la antigua Asiria y en Egipto se tiene evidencia de la recolecci贸n de datos estad铆sticos. Asimismo, en Roma se recog铆an datos demogr谩ficos de los habitantes del imperio, como aquellos de natalidad y mortalidad. Esto, con el prop贸sito de tomar mejores decisiones desde el gobierno.')
st.markdown('Posteriormente, durante la Edad Media, la estad铆stica no tuvo grandes avances. Sin embargo, en la Edad Moderna se elaborar铆a el primer censo estad铆stico moderno. Luego, hacia el siglo XX, se comenzaron a incorporar herramientas matem谩ticas provenientes de la teor铆a de la probabilidad a la estad铆stica.')
st.markdown('La estad铆stica contin煤a desarroll谩ndose y cada vez m谩s deprisa. Junto con la computaci贸n y los programas inform谩ticos, ha sido posible almacenar grandes cantidades datos, y realizar c谩lculos en fracciones de segundo que hace unos a帽os eran inimaginables. Como resultado de estos avances, la __estad铆stica__ es la piedra angular para el desarrollo de lo que hoy conocemos como __Inteligencia Artificial__.')

## Imagen inteligencia artificial:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//ai.jpeg",  width=500)

## Conceptos estad铆sticos:
st.subheader('__Conceptos estad铆sticos__')
st.markdown(' - __Poblaci贸n:__ Es el conjunto de individuos que re煤nen una caracter铆stica que desea ser estudiada.')
st.markdown(' - __Muestra:__ Es un subgrupo de individuos extra铆dos de una poblaci贸n que debe representar adecuadamente la totalidad del grupo.')

## Imagen poblaci贸n y muestra:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//muestra.jpeg",  width=500)
    
## Introducci贸n a la base de datos:    
st.markdown('La siguiente base de datos contiene la informaci贸n de __5806 series y pel铆culas__ que se encuentran en __Netflix__. Vamos a tomar una muestra de estas para estudiar varios conceptos estad铆sticos. La descripci贸n de las variables es la siguiente:')
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

## organizaci贸n de variables:
cualitativas = ['selecciona una variable', 'type', 'release_year', 'age_certification', 'genres', 'first_genre', 'production_countries', 'first_country']
cuantitativas = ['selecciona una variable', 'release_year', 'runtime', 'seasons', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']
lista_variables = ['type', 'release_year', 'age_certification', 'genres', 'production_countries', 'runtime', 'seasons', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']

## acceso a base de datos:
netflix = pd.read_csv('Data//titles.csv')
netflix    

## determinar tama帽o de la muestra:
st.subheader('Ahora vamos a determinar el __tama帽o__ de nuestra muestra:')
st.markdown('El __tama帽o de la muestra__ se le conoce como aquel n煤mero determinado de sujetos, o cosas, que componen la muestra extra铆da de una poblaci贸n, necesarios para que los datos obtenidos sean __representativos de la poblaci贸n.__')

## definici贸n de la muestra:
sample_size = st.slider('Tama帽o de la muestra', 0, 1000)
st.markdown('As铆 se ha generado nuestra muestra con el tama帽o indicado:')

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
st.markdown('__Variable:__ La caracter铆stica o cualidad de una muestra o poblaci贸n a la cual se le puede asignar un valor.')
st.markdown('__Variables cuantitativas:__ Son variables que se expresan num茅ricamente:')
st.markdown(' - __Variable continua:__ Toman un valor infinito de valores entre un intervalo de datos. Por ejemplo, el tiempo que tarda un corredor en completar una carrera de 100 metros.')
st.markdown(' - __Variable discreta:__ Toman un valor finito de valores entre un intervalo de datos. Por ejemplo, el n煤mero de helados vendidos.')
st.markdown('__Variables cualitativas (categ贸ricas):__ Son variables que se expresan, por norma general, en palabras. Esta se puede diferenciar entre:')
st.markdown(' - __Variable ordinal:__ Expresa diferentes niveles y orden.')
st.markdown(' - __Variable nominal:__ Expresa un nombre claramente diferenciado. Por ejemplo el color de ojos puede ser azul, negro, casta帽o, verde, etc.')

## momentos estad铆sticos:
st.subheader('Momentos Estad铆sticos')
st.markdown('Son medidas que ofrecen informaci贸n sobre el centro de un conjunto de datos (__medidas de tendencia central__), otras sobre la dispersi贸n o variabilidad (__medidas de dispersi贸n__), y otras sobre la __posici贸n__ de un valor como los percentiles.')
st.markdown('__Medidas de tendencia central:__')
st.markdown('__Mediana:__ es el n煤mero que ocupa el lugar central una vez estos han sido ordenados de menor a mayor.')
st.markdown('__Moda:__ es el valor m谩s frecuente en una distribuci贸n de datos, es decir, el que m谩s veces aparece.')
st.markdown('__Media:__ tambi茅n conocida como __promedio__, es el resultado de la suma de todos los valores de una distribuci贸n dividida entre el n煤mero de valores sumados.')

## imagen media, moda, mediana
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//media.jpeg",  width=500)
    
## histograma medidas de tendencia central:
st.subheader('Observemos estos par谩metros de tendencia central:')
st.markdown('Vamos a crear unos histogramas para visualizar la distribuci贸n de los datos as铆 como sus correspondientes media, moda y mediana:')

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
    
## gr谩fica de barras para variables cuantitativas:    
st.markdown('Para las variables cualitativas podemos construir unas gr谩ficas similares para observar las frecuencias absolutas: las gr谩ficas de barras.')

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
    
## medidas de dispersi贸n:
st.subheader('Medidas de dispersi贸n:')
st.markdown('Son n煤meros que indican si una variable se mueve mucho, poco, m谩s o menos que otra. La raz贸n de ser de este tipo de medidas es conocer de manera resumida una caracter铆stica de la variable estudiada.')
st.markdown(' - __Rango:__ es un valor num茅rico que indica la diferencia entre el valor m谩ximo y el m铆nimo de una poblaci贸n o muestra estad铆stica.')
st.markdown(' - __Desviaci贸n media:__ es la media de los valores absolutos (esto es, sin tener en cuenta si son positivos o negativos) de las desviaciones de una serie de observaciones con respecto a su media.')
st.markdown(' - __Varianza:__ es una medida de dispersi贸n que representa la variabilidad de una serie de datos respecto a su media. Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.')
st.markdown(' - __Desviaci贸n Est谩ndar:__ ofrece informaci贸n de la dispersi贸n respecto a la media. Su c谩lculo es exactamente el mismo que la varianza, pero realizando la ra铆z cuadrada de su resultado.')    
    
## imagen medidas de dispersi贸n:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//desv.jpeg",  width=500)
    
## medidas de posici贸n de valor:    
st.subheader('Medidas de posici贸n de un valor:')
st.markdown('__Percentiles:__ El percentil es una medida estad铆stica la cual divide una serie de datos ordenados de menor a mayor en cien partes iguales. Se trata de un indicador que busca mostrar la proporci贸n de la serie de datos que queda por debajo de su valor.')
st.markdown(' - __Los percentiles__ dividen a la distribuci贸n en cien partes. Por lo tanto, dan los valores correspondientes al 1%, al 2% ... y al 99% de los datos.')
st.markdown('__Los cuantiles__ suelen usarse por grupos que dividen la distribuci贸n de los datos en partes iguales; entendidas estas como intervalos que comprenden la misma proporci贸n de valores. Los m谩s usados son:')
st.markdown(' - __Los cuartiles,__ que dividen a la distribuci贸n en cuatro partes (corresponden a los cuantiles 0.25, 0.50, 0.75 y 1).')
st.markdown(' - __Los quintiles,__ que dividen a la distribuci贸n en cinco partes (corresponden a los cuantiles 0.20, 0.40, 0.60, 0.80 y 1).')
st.markdown(' - __Los deciles,__ que dividen a la distribuci贸n en diez partes (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 y 1).')

## imagen medidas de posici贸n de valor:
col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("Images//perc.png",  width=500)
    
## visualizaci贸n de datos:    
st.subheader('Visualizaciones de datos:')
st.markdown('Cuando piensas en la __visualizaci贸n de datos__, tu primer pensamiento probablemente se dirija de inmediato a __gr谩ficos de barras__ o __gr谩ficos de pastel.__ Si bien esto puede ser una parte integral de la visualizaci贸n de datos y una l铆nea base com煤n para muchos gr谩ficos de datos, la visualizaci贸n correcta debe emparejarse con el conjunto correcto de informaci贸n. Los gr谩ficos simples son solo la punta del iceberg. Hay toda una selecci贸n de m茅todos de visualizaci贸n para presentar datos de manera eficaz e interesante.')
st.markdown('La visualizaci贸n correcta nos ayuda a responder preguntas sobre nuestros datos, plantear hip贸tesis sobre estos, y nos ayuda a transmitirla adecuadamente a los dem谩s.')
st.markdown(' - __Gr谩fica de pastel:__ Tiene la forma de un disco dividido en sectores, cuyas 谩reas son proporcionales a los porcentajes de los distintos componentes de la poblaci贸n estad铆stica.')

## gr谩fica de pastel:
@st.cache
def grafica_pastel(variable, threshold):
    temp = sample[variable].value_counts()[sample[variable].value_counts() > threshold]
    fig = px.pie(temp, values = temp.values, names = temp.index)
    return fig

variable = str(st.selectbox('Selecciona una variable para la gr谩fica de pie:', cualitativas))
threshold = st.slider('L铆mite inferior de frecuencia de la categor铆a', 0, 50)

try:
    st.plotly_chart(grafica_pastel(variable, threshold), use_container_width = True)  
except:
    st.write('Selecciona una variable para graficar')

## gr谩fica de cajas y bigotes:
@st.cache
def cajas_bigotes(var_cuali, var_cuanti, color):
    fig = px.box(sample, x = var_cuali, y = var_cuanti, color = color)
    return fig

var_cuali = str(st.selectbox('Selecciona una variable cualitativa para la gr谩fica de cajas y bigotes:', cualitativas))
var_cuanti = str(st.selectbox('Selecciona una variable cuantitativa para la gr谩fica de cajas y bigotes:', cuantitativas))
color = str(st.selectbox('Selecciona una variable para diferenciar por colores:', cualitativas))

try:
    st.plotly_chart(cajas_bigotes(var_cuali, var_cuanti, color), use_container_width = True)  
except:
    st.write('Selecciona una variable para graficar')
    
## gr谩fica de dispersi贸n de puntos:    
st.markdown(' - __Gr谩fica de dispersi贸n:__ se utiliza cuando hay muchos puntos de datos diferentes y se desea destacar las relaciones entre estos datos. Esto es 煤til cuando se buscan valores at铆picos o para entender la distribuci贸n de los datos.')

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
    
st.markdown('Para conocer muchos m谩s tipos de gr谩ficos para visualizar los datos puedes ingresar al siguiente link:')
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
    
