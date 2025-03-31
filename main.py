import streamlit as st
import importlib
import os
import re

# Set page configuration
st.set_page_config(
    page_title="Furn Italia - Premium Furniture",
    page_icon="Furn Italia",
    layout="wide"
)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigation
st.sidebar.title("Furn Italia")
st.sidebar.markdown("---")

# Navigation buttons
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("Home"):
        st.session_state.page = 'home'
        st.rerun()

with col2:
    if st.button("Contact"):
        st.session_state.page = 'contact'
        st.rerun()

st.sidebar.markdown("### Product Categories")

# Product pages (numbers replaced with FI_xxxx format)
product_pages = [
    "S1_FI_71", "Sahara", "Durban", "Casa", "Rec_FI_3306",
    "Z_FI_006", "E_FI_091", "BIG_BOX", "Chester", "Stallion", "FI_5713", "FI_5855", "FI_6429", "Boat", "FM_FI_252", "Jupiter", "Linus", "Longer", "Niwasa", "Prada",
    "Single_Chair_bed", "Steel_Land", "Straight_Line", "Violino", "WA_FI_355", "ZA_FI_63",
    "ZM_FI_896", "ZM_FI_899", "wooden"
]

# Search box for filtering products
search_query = st.sidebar.text_input("Search Product:")
filtered_products = [p for p in product_pages if search_query.lower() in p.lower()]

# Dropdown menu for product selection
selected_product = st.sidebar.selectbox("Select a Product:", ["None"] + filtered_products)

if selected_product != "None":
    st.session_state.page = selected_product
    st.rerun()

# Try to load the selected page
try:
    if st.session_state.page == 'home':
        from app import home
        home.show_homepage()

    elif st.session_state.page == 'contact':
        st.title("Contact Furn Italia")
        st.write("Get in touch with us:")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.success("Thank you for your message! We'll get back to you soon.")

    elif st.session_state.page in product_pages:
        module_name = f"app.{st.session_state.page}"
        try:
            module = importlib.import_module(module_name)
            module.show_product_detail()
        except ModuleNotFoundError:
            st.error(f"Module for {st.session_state.page} not found.")
        except AttributeError:
            st.error(f"Function `show_product_detail()` not found in {st.session_state.page}.")

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Please check the page module or contact support.")
