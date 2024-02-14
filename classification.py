import streamlit as st
import joblib
import numpy as np

def load_model():
    with open('saved_file_recommandation.joblib', 'rb') as file:
       data = joblib.load(file)
    return data

data = load_model()

rdfc_loaded = data["model"]    
preprocesser4 = data["encoder"]

def show_classification():
    st.markdown("""
    <div style='color: green;'>
        <h1>Laissez vous guider par nos recommandations agricoles</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""### Ce sytème de recommandation s'appuie sur des modèles robustes de classification afin de fournir des réponses précises""")


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
    
    
    Region = st.selectbox("Veuillez choisir une région", Region)
    
    Production = st.number_input("Production en tonne envisagée", min_value=1, max_value=900000)
    
    Superficie = st.number_input("Superficie en ha", min_value=2, max_value=230000)

    Rendement = st.number_input("Rendement en kg/ha", min_value=2, max_value=30000)
    
    ok = st.button("J'obtiens ma recommandation")
    if ok:
       X = np.array([[Region, Production, Superficie, Rendement]])
       X_rdfc = preprocesser4.transform(X)
    
       y_rdfc = rdfc_loaded.predict(X_rdfc)
    
       df_dict = {1: "ARACHIDE", 2: "MAIS", 3: "NIEBE", 4: "SORGHO", 5: "MIL", 6: "MANIOC", 7: "RIZ", 8: "FONIO"}

       if y_rdfc[0] in df_dict:
          culture_recommandee = df_dict[y_rdfc[0]]
          st.subheader(f"Le {culture_recommandee} est la meilleure culture qui pourrait être cultivée selon les critères renseignés")
       else:
          st.write("Désolé, nous ne sommes pas en mesure de recommander une culture adaptée pour cette région")