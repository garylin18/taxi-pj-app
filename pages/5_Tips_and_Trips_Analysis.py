import streamlit.components.v1 as components
import streamlit as st


st.set_page_config(
    page_title="NYC Taxi Analysis",
    page_icon="🚕",
    layout="wide"
)
with st.sidebar:
    st.image("./image/project_logo.png")

#getting data,prepping data
path_to_html= "./pages/tipandtrip.html"
st.write("### Tips and Trips Analysis:")
with open(path_to_html,'r') as f:
    html_data = f.read()
    components.html(html_data, width=1300, height=2000, scrolling=True)
