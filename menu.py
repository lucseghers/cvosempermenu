import streamlit as st
import os

st.set_page_config(page_title="Hoofdmenu", page_icon="📚")

# ======================
# LOGO
# ======================
logo_path = "logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=400)
else:
    st.warning(f"Logo '{logo_path}' niet gevonden.")

st.title("📚 Centrale H5P Hub")
st.write("Kies links een toepassing en lees rechts wat deze precies doet.")

# ======================
# MENU DATA
# ======================
APPS = {
    "Memory": {
        "url": "https://h5p-memory-generator-jyxcvbcxcag7cmbzoxqqym.streamlit.app/",
        "beschrijving": """
Deze maakt een H5P memory spel op basis van woorden. Dus steeds 2 bij elkaar horende woorden.
denk heirbij aan vb slot ; sleutel maar kan evengoed hond ; dog zijn.

Je geeft zelf volgende info:
- per lijn 2 woorden die bij elkaar horen
- De twee woorden moeten gescheiden zijn door een puntkomma (;)
- bij voorkeur niet meer dan 10 woordparen (bij meer past het sepl neit meer op eht scherm)  

Ideaal om snel een memory te maken.
"""
    },
    "Sensor data": {
        "url": "https://mijn-app-2.streamlit.app",
        "beschrijving": """
Deze toepassing toont live sensorgegevens van IoT-toestellen.

Functies:
- real-time temperatuur- en vochtigheidsmetingen  
- grafieken per dag/week  
- waarschuwingen bij grenswaarden  

Geschikt voor demo's rond IoT en datavisualisatie.
"""
    },
    "AI demo": {
        "url": "https://mijn-app-3.streamlit.app",
        "beschrijving": """
Interactieve AI demonstratie voor cursisten.

Hier kunnen gebruikers:
- AI-prompts uittesten  
- beeldgeneratie proberen  
- voorbeelden bekijken van AI in de praktijk  

Ideaal voor bewustmaking en praktijkoefeningen.
"""
    }
}

# ======================
# SIDEBAR MENU
# ======================
st.sidebar.title("Menu")
keuze = st.sidebar.radio("Kies een toepassing:", APPS.keys())

gekozen_app = APPS[keuze]

# ======================
# RECHTERKANT: UITLEG
# ======================
st.subheader(f"ℹ️ Over: {keuze}")
st.write(gekozen_app["beschrijving"])

st.divider()

st.link_button("🚀 Open deze toepassing", gekozen_app["url"])
