import streamlit as st
import os

st.set_page_config(page_title="Hoofdmenu", page_icon="📚")

# ======================
# LOGO BOVENAAN
# ======================
logo_path = "logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=400)  # pas breedte aan indien gewenst
else:
    st.warning(f"Logo '{logo_path}' niet gevonden.")

# ======================
# TITEL
# ======================
st.title("📚 Centrale Streamlit Hub")
st.write("Kies een toepassing uit het menu links:")

# ======================
# MENU STRUCTUUR
# ======================
st.sidebar.title("Menu")

apps = {
    "Dashboard leerlingen": "https://mijn-app-1.streamlit.app",
    "Sensor data": "https://mijn-app-2.streamlit.app",
    "AI demo": "https://mijn-app-3.streamlit.app",
}

keuze = st.sidebar.radio("Kies een toepassing:", list(apps.keys()))

st.write(f"### Gekozen: {keuze}")

url = apps[keuze]

st.write("Klik hieronder om naar de app te gaan:")
st.link_button("Open deze app", url)
