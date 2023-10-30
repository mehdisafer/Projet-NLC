import streamlit as st

st.title("Générateur de code :male-technologist:")

# Colonne à gauche
with st.sidebar:
    st.title(":trophy: Mode d'utilisation :trophy:")
    st.write("Ce générateur de code vous permet de générer du code dans différents langages.:medal:")
    st.write("Pour générer du code, sélectionnez un langage dans la liste déroulante, puis entrez la description du code que vous souhaitez générer dans la zone de texte.")
    st.write("Cliquez sur le bouton 'Générer' pour générer le code :cyclone:.")
    st.write("Pour exécuter le code, cliquez sur le bouton 'Exécuter':coffee:.")
    st.write("Vous pouvez également éditer le code généré ! :champagne:")

# Sélection
sélection = st.selectbox("Sélectionnez une langue", ["Python", "JavaScript", "PHP"])

# Zone de texte utilisateur et réponse API
description_code = st.text_area("Quelle Code souhaitez-vous généré", height=200)
Buton_1 = st.button('Générer')

generation_code = st.text_area("code généré par L'API OpenIA", height=200)
Buton_2= st.button("exécuter")

exécution_code = st.text_area("Exécution du code généré par L'API OpenIA", height=200)