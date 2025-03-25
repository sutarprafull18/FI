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
if st.sidebar.button("🛋️ S1_71"):
    st.session_state.page = 'S1_71'
if st.sidebar.button("🛋️ Sahara"):
    st.session_state.page = 'Sahara'
if st.sidebar.button("🪑 Custom Furniture"):
    st.session_state.page = 'custom'

# Display the selected page
try:
    if st.session_state.page == 'home':
        from app import home
        home.show_homepage()
    elif st.session_state.page == 'S1_71':
        from app import S1_71
        S1_71.show_product_detail()
    elif st.session_state.page == 'Sahara':
        from app import Sahara
        Sahara.show_product_detail()
    elif st.session_state.page == 'contact':
        # If you don't have a contact page, you can create a simple one
        st.title("Contact Furn Italia")
        st.write("Get in touch with us:")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.success("Thank you for your message! We'll get back to you soon.")
    elif st.session_state.page == 'custom':
        # Placeholder for custom furniture page
        st.title("Custom Furniture Design")
        st.write("Design your dream furniture with Furn Italia")
        
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Please check the page module or contact support.")
