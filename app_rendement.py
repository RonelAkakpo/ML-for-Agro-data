import streamlit as st
from explorer_rendement import show_explorer_rendement
from predire_rendement import show_predire_rendement
from classification import show_classification


page = st.sidebar.selectbox("Faites un choix parmis les options suivantes", ("Explorer les données","Predire le rendement","Obtenir une recommandation de Culture"))

if page == "Explorer les données":
   show_explorer_rendement()
elif page == "Predire le rendement":
    show_predire_rendement()
else:
    show_classification()
   


