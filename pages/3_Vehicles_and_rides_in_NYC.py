import streamlit as st
import streamlit.components.v1 as components

#st.title("")
#st.markdown("This Streamlit app embeds the Tableau dashboard ")
# Embed Tableau dashboard using iframe

st.set_page_config(
    page_title="NYC Taxi Analysis",
    page_icon="🚕",
    layout="wide"
)
with st.sidebar:
    st.image("./image/project_logo.png")

st.write("### Vehicle types in NYC:")
st.image("./image/vehicle_type.png",width=1200)

html_code = '''
<div style='background-color: teal; color: white; padding: 10px;'>
  Custom HTML in Streamlit
</div>
'''
#components.html(html_code, height=200)
path_to_html= "./pages/Vehicles_and_rides_in_NYC.html"

with open(path_to_html,'r') as f:
    html_data = f.read()
    components.html(html_data, width=1200, height=2000, scrolling=True)

#st.header("Data Source")
#st.components.v1.html(html_data)