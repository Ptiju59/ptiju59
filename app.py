import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt




st.title("Bienvenue dans les Dataset du Module SEABORN")
#Choix du Dataset
data = sns.get_dataset_names() 
selection = st.selectbox("Choisissez votre dataset :", data)
dataset = sns.load_dataset(selection)
st.write(f"Affichage des premières lignes du dataset {selection}:")
st.write(dataset.head())

numerical_columns = dataset.select_dtypes("number").columns
x = st.selectbox("Sélectionner la colonne X", numerical_columns)
y = st.selectbox("Sélectionner la colonne Y", numerical_columns)
graph = st.selectbox("Choisissez votre dataset :", ["scatter_chart", "line_chart","bar_chart"])
st.subheader(f'Affichage du graphique : {graph}')

if graph == 'scatter_chart':
    fig = px.scatter(dataset, x=x, y=y, title=f'Scatter Plot de {x} vs {y}')
    st.plotly_chart(fig)
elif graph == 'bar_chart':
    fig = px.bar(dataset, x=x, y=y, title=f'Bar Chart de {x} vs {y}')
    st.plotly_chart(fig)

elif graph == 'line_chart':
    fig = px.line(dataset, x=x, y=y, title=f'Line Chart de {x} vs {y}')
    st.plotly_chart(fig)

st.subheader('Matrice de Corrélation')
show_corr = st.checkbox('Afficher la matrice de corrélation')
if show_corr:
    numerical_data = dataset.select_dtypes("number")
    corr_matrix = numerical_data.corr()
    st.write('Matrice de corrélation des données numériques :')

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    st.pyplot(fig)
