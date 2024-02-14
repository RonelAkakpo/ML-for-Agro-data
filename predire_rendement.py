import streamlit as st
import joblib
import numpy as np

def load_model():
    with open('saved_file_rendement.joblib', 'rb') as file:
       data = joblib.load(file)
    return data

data = load_model()

Rdf_loaded = data["model"]    
preprocesser = data["encoder"]

def show_predire_rendement():
    st.markdown("""
    <div style='color: green;'>
        <h1>Vous souhaitez prédire le rendement agricole ?</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("""### Nous avons besoins des informations suivantes :""")
    
    
    
    Region = (
          "DAKAR", 
          "SEDHIOU",
          "REGION DE SEDHIOU",        
          "REGION DE KOLDA",          
          "KOLDA",                    
          "REGION DE TAMBACOUNDA",    
          "GOUDOMP",                  
          "BOUNKILING",              
          "TAMBACOUNDA",              
          "VELINGARA",               
          "REGION DE KAOLACK",        
          "REGION DE SAINT-LOUIS",    
          "BIGNONA",                  
          "KAOLACK",                  
          "ZIGUINCHOR",               
          "REGION DE ZIGUINCHOR",     
          "REGION DE FATICK",         
          "KAFFRINE",                 
          "FOUNDIOUGNE",              
          "REGION DE KAFFRINE",      
          "MEDINA YORO FOULA",        
          "NIORO DU RIP",             
          "FATICK",                  
          "DAGANA",                   
          "REGION DE MATAM",          
          "KOUNGHEUL",                
          "MALEM HODDAR",             
          "REGION DE KEDOUGOU",       
          "BIRKILANE",                
          "SARAYA",                  
          "REGION DE DIOURBEL",       
          "KOUPENTOUM",               
          "MBACKE",                   
          "SAINT-LOUIS",             
          "BAMBEY",                   
          "DIOURBEL",                 
          "REGION DE LOUGA",          
          "GOSSAS",                   
          "KANEL",                    
          "PODOR",                    
          "GUINGUINEO",               
          "LINGUERE",                
          "OUSSOUYE",                 
          "REGION DE THIES",          
          "MBOUR",                   
          "THIES",                    
          "TIVAOUANE",               
          "RANEROU",                  
          "GOUDIRY",                  
          "KEDOUGOU",                 
          "SALEMATA",                 
          "BAKEL",                    
          "MATAM",                    
          "LOUGA",                    
          "KEBEMER",                  
          "RUFISQUE",                               
         )
    
    
    Culture = (
          "ARACHIDE",
          "MAIS",        
          "NIEBE",     
          "SORGHO",
          "MIL",         
          "MANIOC",      
          "RIZ",         
          "FONIO",
        )
    
    Region = st.selectbox("Veuillez choisir une région", Region)
    Culture = st.selectbox("Veuillez choisir la culture dont vous souhaitez prédire le rendement", Culture)
    
    Date = st.number_input("Veuillez renseigner l'année", min_value=2023, max_value=2027)
    
    Production = st.number_input("Production en tonne souhaitée", min_value=1, max_value=900000)
    
    Superficie = st.number_input("Superficie en ha prévue", min_value=2, max_value=230000)
    
    ok = st.button("J'obtiens la prédiction du rendement agricole")
    if ok:
        X = np.array([[Region, Culture, Date , Production , Superficie ]])
        X_essai_Rdf= preprocesser.transform(X)
        
        rendement = Rdf_loaded.predict(X_essai_Rdf)
        st.subheader(f"Le rendement de {Culture} sera de {rendement[0]:.2f}kg/ha d'après les critères que vous avez renseignés" )