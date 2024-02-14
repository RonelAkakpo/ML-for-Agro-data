import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv("RENDEMENT.csv", sep=';')
    df = df[["region","culture","Date","Production en tonne","Superficie en ha","Rendement kg/ha"]]
    df = df.rename({"region":"Region"}, axis=1)
    df = df.rename({"culture":"Culture"}, axis=1)
    df = df[df["Rendement kg/ha"].notnull()]
    df = df.rename({"Rendement kg/ha":"Rendement"}, axis=1)
    df = df.rename({"Superficie en ha":"Superficie"}, axis=1)
    df = df.rename({"Production en tonne":"Production"}, axis=1)
        
    return df

df = load_data()


def show_explorer_rendement():
    st.title("BIENVENUE SUR AGRO DATA METRICS")
        
    st.write(
            """
        ### Explorer les données agricoles par région au Sénégal
        """   
        )
        
        
    st.write(
            """
        ### Les données proviennent de l'ANSD et ont été collectées à partir de l'Enquete Agricole Annuelle de 2017 à 2022
        """   
        )
        

        
        
    st.write("""
            #### Superficie moyenne par culture
        """)
        
    data = df.groupby(["Culture"])["Superficie"].mean()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(data.index, data, color='green')
    ax.set_ylabel('Superficie moyenne')
    ax.set_title(f'Superficie moyenne par culture')
    st.pyplot(fig)
        
        
        
    st.write(
            """
        #### Rendement moyen par culture
        """
        )

    data = df.groupby(["Culture"])["Rendement"].mean().sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    data.plot(kind='line', color='green', ax=ax)
    ax.set_ylabel('Rendement moyen')
    ax.set_title('Rendement moyen par culture')
    st.pyplot(fig)


        
        
        
    st.write(
            """
        #### Rendement moyen des cultures par région
        """
        )
    data = df.groupby(["Region", "Culture"])["Rendement"].mean().unstack()
        
    selected_region = st.selectbox("Veuillez sélectionnez une région", data.index)

    selected_data = data.loc[selected_region]

    fig, ax = plt.subplots()
    selected_data.plot(kind='bar', ax=ax, color='green')
    ax.set_ylabel('Rendement moyen')
    ax.set_title(f'Rendement des cultures pour la région de {selected_region}')
    st.pyplot(fig)




    st.write(
            """
        #### Top 4 des villes avec le meilleur rendement par culture
        """
        )
        
    selected_culture = st.selectbox("Veuillez sélectionnez une culture", data.columns)
        
    filtered_data = data[selected_culture].sort_values(ascending=False)
        
    top_cities = filtered_data.head(4)
        
    st.write(f"Les quatres villes avec le meilleur rendement pour la culture de {selected_culture}:")
        
    table_data = pd.DataFrame({'Ville': top_cities.index, 'Rendement moyen': top_cities.values}, index=range(1, 5))
        
    st.table(table_data.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white')]},
        {'selector': 'td', 'props': [('text-align', 'center')]}
    ]))

