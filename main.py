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

# Initialize session state for page navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Side panel for navigation
st.sidebar.title("Furn Italia")
st.sidebar.markdown("---")

# Navigation buttons
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = 'home'

with col2:
    if st.button("📞 Contact"):
        st.session_state.page = 'contact'

st.sidebar.markdown("Product Categories")

# Product buttons in required order
product_pages = [
    "S1_71", "Sahara", "Durban", "Casa", "FI_3306_Rec",
    "Z006", "E091", "BIG_BOX", "Chester", "Stallion", "FI_5713", "FI_5855", "FI_6429", "Boat", "FM252", "Jupiter", "Linus", "Longer", "Niwasa", "Prada",
    "Single_bed", "Steel_Land", "Straight_Line", "Violino", "WA355", "ZA63",
    "ZM896", "ZM899", "wooden"
]

for product in product_pages:
    if st.sidebar.button(f"🛋️ {product}"):
        st.session_state.page = product


# Display the selected page
try:
    if st.session_state.page == 'home':
        from app import home
        home.show_homepage()
    elif st.session_state.page in product_pages:
        exec(f"from app import {st.session_state.page}\n{st.session_state.page}.show_product_detail()")
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
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Please check the page module or contact support.")
