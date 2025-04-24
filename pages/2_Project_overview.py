#import streamlit.components.v1 as components
import streamlit as st



st.set_page_config(
    page_title="NYC Taxi Analysis",
    page_icon="🚕",
    layout="wide"
)
with st.sidebar:
    st.image("./image/project_logo.png")

#your page content, filters etc

#st.sidebar.image("/image/project_logo.png", use_container_width=True)
#st.set_page_config(layout="wide")
#st.set_page_config(
#    page_title="Hello",
#    page_icon="👋",
#)



st.markdown( 
  """  
    ### Project Overview
    - The project is about analysing the NYC taxi data and evaluating the 2 main congestion pricing programs implemented and aims to identify any patterns or trends that can be used to improve taxi services and traffic in NYC.
    - Moreover, we wanted to assess its correlation with weather conditions to understand how weather conditions affect taxi demand and supply in NYC.
    
    ### What are our Hypothesis?
    - Have the congestion fees impacted the volume of rides?
    - Can the optimization of patterns in cruising time and utilization rate be used to improve taxi services and traffic in NYC?
    - Are tips and weather determining factors for high demand in congestion zones?
    
    ### Data source
    - Data source: Meteostat, New York City TLC (https://www.nyc.gov/site/tlc/passengers/your-ride.page)
    - Period of data: 
      - Impact of congestion pricing: 01.01.2019- 31.01.2025
      - Assessment of cruising rate, tips and weather: 01.01.2024 - 31-12-2024
    - Sampling rate: 5%
    """
)

st.markdown("###  Tools used")


logos1 = {
    "Python": "https://www.python.org/static/community_logos/python-logo.png",
    "Pandas": "https://pandas.pydata.org/static/img/pandas_mark.svg",
    "Streamlit": "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg",
    "Tableau": "https://www.tableau.com/sites/default/files/pages/tableaulogo_highres.png",
    "Postgresql": "https://www.os4x.com/wp-content/uploads/2021/01/postgresql-logo.png"
}
# Display each logo in a column with caption
cols = st.columns(len(logos1))
for col, (tech, url) in zip(cols, logos1.items()):
    col.image(url, caption=tech, use_container_width=True)