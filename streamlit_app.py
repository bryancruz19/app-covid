import streamlit as st

st.balloons()

st.title("🎈")

import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


####################
## ajustar el layout
#################### 

st.set_page_config(layout="wide")


##################
## tamaño del plot
################## 

fig, ax = plt.subplots()


#########
## titulo
######### 

#imagenes

col1, col2, col3 = st.columns(3)


col1.image("https://github.com/elioramospr/hola_streamlit_mj/blob/main/covid.png?raw=true", width=150)

col2.title("Datos de COVID - Variante Onicrón")

col3.image("https://github.com/elioramospr/hola_streamlit_mj/blob/main/logouprh.png?raw=true", width=150)


##############################################
## esto es para que salga una linea horizontal
############################################## 

st.divider()

#################
## datos de covid 
################# 

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])


nombres = list(df_covid.columns)[1:]

columns = st.sidebar.selectbox("Columna de interes:", nombres)


suavizado = st.sidebar.checkbox ("Suavizado")

tabla = st.sidebar.checkbox("Mostrar datos")

                   

df_covid.plot(x="date", y= columns, ax = ax,
              xlabel="fecha", 
              ylabel=columns)

col1, col2 = st.columns(2)

if suavizado: 
    ventana = st.sidebar.slider("Ventana de suavizado [dias]",
                                1,15,7)
    df_rolling = df_covid[columns].rolling(ventana, center = True).mean()
    df_covid[columns + "_rolling"] = df_rolling
    df_covid.plot(x = "date", y = columns +"_rolling", ax=ax)
    st.sidebar.divider()

col1.pyplot(fig)
 
if tabla: 
        df_covid["date"] = df_covid["date"].dt.strftime("%d - %b - %Y")
        df_filtrado = df_covid[["date", columns]]
        col2.write(df_filtrado)
        
st.sidebar.markdown("""Aplicacion desarrollada por: Bryan Cruz <br>
                    Comp3005 <br> Universidad de Puerto Rico en Humacao""",
                   unsafe_allow_html = True)
        


#st.image("https://online.upr.edu/mod/resource/view.php?id=4169768)"
