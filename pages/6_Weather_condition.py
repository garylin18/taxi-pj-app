import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="NYC Taxi Analysis",
    page_icon="🚕",
    layout="wide"
)
with st.sidebar:
    st.image("./image/project_logo.png")
#st.write("# Weather condition vs. Trip amount:")
#st.image("./image/coco_amount.png", width=1200)

#st.write(" ")
st.write("### Weather condition:")
path_to_html= "./pages/weather.html"

with open(path_to_html,'r') as f:
    html_data = f.read()
    components.html(html_data, height=2000, scrolling=True)
    
