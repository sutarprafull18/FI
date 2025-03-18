import streamlit as st
import os

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

if st.sidebar.button("🛋️ Product 1"):
    st.session_state.page = 'product_1'

if st.sidebar.button("🛋️ Product 2"):
    st.session_state.page = 'product_2'

# Display the selected page
if st.session_state.get('page') == 'home':
    from app import home
    home.show_homepage()
elif st.session_state.get('page') == 'product_1':
    from app import product_1
    product_1.show_product_detail()
elif st.session_state.get('page') == 'product_2':
    from app import product_2
    product_2.show_product_detail()
else:
    from app import home
    home.show_homepage()
