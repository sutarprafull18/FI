import streamlit as st
import sys
import os

# Add the app directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Set page configuration
st.set_page_config(
    page_title="Furn Italia - Premium Furniture",
    page_icon="🪑",
    layout="wide"
)

# Side panel for navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("---")

# Navigation buttons
if st.sidebar.button("🏠 Home"):
    st.session_state.page = 'home'

if st.sidebar.button("🛋️ S1_71"):
    st.session_state.page = 'S1_71'

if st.sidebar.button("🛋️ Sahara"):
    st.session_state.page = 'Sahara'

# Display the selected page
if st.session_state.get('page') == 'home':
    from app import home
    home.show_homepage()
elif st.session_state.get('page') == 'S1_71':
    from app import S1_71
    S1_71.show_product_detail()
elif st.session_state.get('page') == 'Sahara':
    from app import Sahara
    Sahara.show_product_detail()
else:
    from app import home
    home.show_homepage()
