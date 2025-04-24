#import streamlit.components.v1 as components
import streamlit as st


st.set_page_config(
    page_title="NYC Taxi Analysis",
    page_icon="🚕",
    layout="wide"
)
with st.sidebar:
    st.image("./image/project_logo.png")  # Use a local image
#st.set_page_config(layout="wide")
#your page content, filters etc

#st.sidebar.image("/image/project_logo.png", use_container_width=True)
#st.set_page_config(layout="wide")
#st.set_page_config(
#    page_title="Hello",
#    page_icon="👋",
#)

st.write("# NYC Taxi - Congestion and Weather Conditions")
st.markdown(" ")
st.markdown("### Andrea Cano,  Elhassan Abouyousouf,  Pooneh Nezamabadi,  Shih-Chieh Lin")
#"## Team members: Andrea Cano,Elhassan Abouyousouf,Pooneh Neyam, Shih-Chieh Lin")

#st.sidebar.success("Team members: Andrea Cano,Elhassan Abouyousouf,Pooneh Neyam, Shih-Chieh Lin")
st.markdown(" ")
st.markdown(" ")
st.markdown(
    """
    ## Why This Project?

### As of 2024, New York City led the world in urban automobile traffic congestion, despite having a 24/7 rapid transit system.
### Together, the iconic Yellow Taxi and other app-based for-hire vehicles(FHV) such as Uber and Lyft, make up 53% of traffic in high-density areas within Manhattan.
### In recent years, New York City introduced congestion surcharges and tolls to tackle traffic.
### At the same time, weather remains a constant challenge for both drivers and passengers — slippery roads, reduced visibility, and fluctuating demand.
 """
    )

#We wanted to find out.

#But the big question is:
#Are these policies and natural conditions really influencing taxi operations and commuter behaviour?

#Are congestion fees actually reducing traffic or just shifting the cost to riders?
#Are these extra charges affecting ride numbers equally to both traditional yellow taxis and other app-based for-hire vehicles?
#Do factors such as tips influence the demand of rides within congestion zones despite the extra costs?
#And does bad weather genuinely impact how many people take taxis despite increased costs?
#This project dives into the data to answer those questions — helping city planners, taxi operators, and the public make smarter, data-driven decisions.