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
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Sidebar Navigation
st.sidebar.title("Furn Italia")
st.sidebar.markdown("---")

# Navigation buttons
if st.sidebar.button("Home"):
    st.session_state.page = 'home'
    st.session_state.selected_category = None

st.sidebar.markdown("### Product Categories")

# Categorized product pages
categories = {
    "Fabric Sofa": [
         "Sahara", "Durban", "Casa", 
       "Stallion",  "Linus",  "Niwasa", "Prada",
     "Steel_Land", "Straight_Line", "Violino",
     
    ],
    "Leather Sofa": ["S1_71","FI_3306_Rec","BIG_BOX","Z006", "E091", "FI_5713", "FI_5855", "FI_6429", "FM252", "Jupiter","ZM896", "ZM899", "WA355", "ZA63",],
    "Other": ["Chester","Single_Chair_bed","Longer","wooden","Boat",],
    "Bedroom": ["bed","side_table"],
    "Outdoor": [],
    "Dining": [],
    "Office": []
}

# Category selection
for category in categories.keys():
    if st.sidebar.button(category, key=f"cat_{category}"):
        st.session_state.selected_category = category

# Show products only if a category is selected
if st.session_state.selected_category:
    st.sidebar.markdown(f"#### {st.session_state.selected_category}")
    products = categories[st.session_state.selected_category]
    search_query = st.sidebar.text_input("Search Product:")
    filtered_products = [p for p in products if search_query.lower() in p.lower()]
    
    for product in filtered_products:
        if st.sidebar.button(product, key=f"prod_{product}"):
            st.session_state.page = product

# Try to load the selected page
try:
    if st.session_state.page == 'home':
        from app import home
        home.show_homepage()

    elif st.session_state.page in sum(categories.values(), []):
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
