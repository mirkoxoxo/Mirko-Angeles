# -*- coding: utf-8 -*-
"""cerkitaweb_st

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iIo2jYmybNbwCAgMrNeyDTUf2UvEGonE
"""

import pandas as pd
import streamlit as st
import geopandas as gpd
import folium as fl
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F6FFC9;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100px; /* Tamaño */
    }
    .footer {
        bottom: 10px;
        width: 50%;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

data = {"nombre": ["Señor Bigotes 🍔", "Emolientando 🍶" ,"Canchitas por Samuel 🍿", "Camilon 🌭", "Morocho 🫐", "Yuquitas Doña Florinda 🧁"],
        "latitud": [-12.06861017065710, -12.068331914262530, -12.068928297764060, -12.069472609783920, -12.069817505441520, -12.070277921402420],
        "longitud": [-77.07747967098570, -77.07762186092730, -77.07765117725230, -77.07767675582580, -77.07770690533130, -77.07776229079620],
        "direccion": ["Av. Universitaria 123", "Jr. Libertad 456", "Calle San Martín 789", "Av. Universitaria 123", "Jr. Libertad 456", "Calle San Martín 789"],
        "tipo_comida": ["Hamburguesas", "Emoliente", "Canchita", "Salchipapas", "Mazamorra", "Yuquitas fritas"],
        "horarios": ["Lunes a Viernes: 12:00 - 22:00", "Lunes a Sábado: 11:00 - 20:00", "Lunes a Domingos: 15:00 - 22:00", "Lunes a Viernes: 12:00 - 22:00", "Lunes a Sábado: 11:00 - 20:00", "Lunes a Domingos: 11:00 - 22:00"]
        }

df = pd.DataFrame(data)
df.to_csv('vendedores.csv', index=False)

st.title("¡Bienvenido a *Cerkita Web*! 😃")
st.write("Descubre los mejores sabores locales cerca de la **PUCP** sin complicaciones. Disfruta de auténtica comida callejera en un ambiente acogedor y lleno de energía. Nuestro sitio web te ayudará a encontrar rápidamente puestos de comida ambulante, ahorrándote tiempo y ofreciendo opciones para todos los bolsillos. Cada bocado cuenta una historia de tradición y pasión culinaria. ¡Sumérgete en esta experiencia única!")

st.write("### ✅ Suscríbete a nuestro Newsletter")
st.write("¡Mantente al tanto de nuestras promociones y novedades! Suscríbete a nuestro boletín y descubre las delicias callejeras cerca de la PUCP. ¡No te lo pierdas!")

nombre = st.text_input("Ingresa tu nombre:")
email = st.text_input("Ingresa tu correo electrónico:")

if st.button("Suscribirse"):
    if email:
        try:
            df_correos = pd.read_csv('correos.csv')
            st.write("Archivo leído correctamente.")
        except FileNotFoundError:
            df_correos = pd.DataFrame(columns=['correo'])
            st.write("Archivo no encontrado, creando nuevo DataFrame.")

        if email not in df_correos['correo'].values:
            nuevo_registro = pd.DataFrame([[email]], columns=['correo'])
            df_correos = pd.concat([df_correos, nuevo_registro], ignore_index=True)
            df_correos.to_csv('correos.csv', index=False)
            st.success("¡Te has suscrito exitosamente! 🤗")
        else:
            st.warning("Ya estás suscrito 👍🏽")
    else:
        st.error("Por favor, ingresa un correo electrónico válido 😔")

st.write("### CerkitaMap")
st.write("Ubica tus puestos de comida ambulantes favoritos de una manera fácil")

user_location = [-12.069444444444, -77.079444444444]

df = pd.read_csv('vendedores.csv')

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitud, df.latitud))

m = fl.Map(location=[-12.069444444444, -77.079444444444], width="70%", height="70%", zoom_start=17)

fl.CircleMarker(user_location, radius=10, color='red', fill=True, fill_color='red').add_to(m)

marker_cluster = MarkerCluster().add_to(m)

for idx, row in df.iterrows():
    popup_text = f"<b>{row['nombre']}</b><br>{row['direccion']}<br>Comida: {row['tipo_comida']}<br>Horarios: {row['horarios']}"
    fl.Marker([row['latitud'], row['longitud']], popup=popup_text).add_to(marker_cluster)

st_folium(m)

promociones = [
    {"titulo": "Señor Bigotes 🍔", "descripcion": "**OFERTA EXCLUSIVA**: Mostrando la página de *Cerkita Web* obtendrás un 50% de descuento en toda nuestra carta de hamburguesas. Además, si comprás más de dos hamburguesas, obtendras una botella de refrescante chicha morada totalmente **GRATIS**. ¡No dejes pasar esta oportunidad de disfrutar 😋 y ahorrar al máximo 🤑 !", "imagen": "https://raw.githubusercontent.com/mirkoxoxo/Mirko-Angeles/main/señor_bigotes_final.png", "fecha": "03/07/2024"},
    {"titulo": "Canchitas por Samuel 🍿", "descripcion": "**OFERTA EXCLUSIVA**: Mostrando la página de *Cerkita Web* disfrutarás de un 30% de descuento en todas nuestras deliciosas canchitas, tanto dulces como saladas. ¡Aprovecha esta oportunidad 😉 para saborear tus favoritas a un precio de locura!", "imagen": "https://raw.githubusercontent.com/mirkoxoxo/Mirko-Angeles/main/canchitas_final.png", "fecha": "03/07/2024"},
    {"titulo": "Camilón 🌭", "descripcion": "**OFERTA EXCLUSIVA**: Mostrando la página de *Cerkita Web* accederás a un 20% de descuento en toda nuestra carta, la cual incluye hamburguesas jugosas, salchipapas crujientes, pollo broaster irresistible y mucho más. 😱 ¡Disfruta de tu antojo favorito a un precio increíble! 😎", "imagen": "https://raw.githubusercontent.com/mirkoxoxo/Mirko-Angeles/main/camilón_final.png", "fecha": "03/07/2024"}
]

df_promociones = pd.DataFrame(promociones)

st.write("### Promociones ¡🤑!")

for index, promocion in df_promociones.iterrows():
    st.image(promocion['imagen'], width=500)
    st.write(f"**{promocion['titulo']}**")
    st.write(promocion['descripcion'])
    st.write(f"*Fecha: {promocion['fecha']}*")
    st.write("---")

st.image("https://raw.githubusercontent.com/mirkoxoxo/Mirko-Angeles/main/cerkitaweb_logo.png", width=100)

st.markdown(
    """
    <div class="footer">
        <img src="data:image/png;base64,{}" class="logo">
    </div>
    """.format(st.image("https://raw.githubusercontent.com/mirkoxoxo/Mirko-Angeles/main/cerkitaweb_logo.png", use_column_width=True)),
    unsafe_allow_html=True
)
