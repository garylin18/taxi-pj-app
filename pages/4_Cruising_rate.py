import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Rebel with Rhythm", layout="wide")
#st.title("Weather data")
#st.markdown("This Streamlit app embeds the Tableau dashboard ")
# Embed Tableau dashboard using iframe

logo_url = "./image/project_logo.png"
st.sidebar.image(logo_url)
st.write("### Cruising rate:")
st.image("./image/cruisingrate.png",width=1200)
path_to_html= "./pages/Cruising_rate.html"

with open(path_to_html,'r') as f:
    html_data = f.read()
    components.html(html_data,width=1200, height=2000, scrolling=True)

#st.header("Data Source")
#st.components.v1.html(html_data)