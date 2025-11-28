import streamlit as st

st.set_page_config(page_title="Hoofdmenu", page_icon="📚")

st.sidebar.title("Menu")

# Hier definieer je je verschillende Streamlit apps
apps = {
    "Dashboard leerlingen": "https://mijn-app-1.streamlit.app",
    "Sensor data": "https://mijn-app-2.streamlit.app",
    "AI demo": "https://mijn-app-3.streamlit.app",
}

# Sidebar-selectie
keuze = st.sidebar.radio("Kies een toepassing:", list(apps.keys()))

st.write(f"### Gekozen: {keuze}")

url = apps[keuze]

st.write("Klik hieronder om naar de app te gaan:")
st.link_button("Open deze app", url)
# Of:
# st.markdown(f"[Open deze app]({url})")
