import streamlit as st

import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

st.title('This is the Streamlit Quest')

# Créer une liste de pays uniques
pays_uniques = df['continent'].unique().tolist()

# Ajouter une option pour afficher tous les pays
pays_uniques.insert(0, 'Tous')

# Ajouter un widget selectbox pour sélectionner un pays
pays_selectionne = st.selectbox('Sélectionnez un pays', pays_uniques)

# Filtrer les données en fonction du pays sélectionné
if pays_selectionne != 'Tous':
    df = df[df['continent'] == pays_selectionne]

# Afficher les données filtrées
st.write(df)

import seaborn as sns
viz_correlation = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("Spectral_r", as_cmap=True), annot = True
								)

st.pyplot(viz_correlation.figure)


import plotly.express as px

fig = px.scatter(df, x = 'cylinders', y = 'cubicinches')
st.plotly_chart(fig)

st.write('On remarque une forte corrélation positive entre les cylindres et la quantité du réservoir')
