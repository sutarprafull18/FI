import streamlit as st
import os

def show_product_detail():
    st.title("S1_71 Details")
    st.write("Description of S1_71.")

    # Path to the images folder for S1_71
    image_folder = "images/S1_71"

    # List all images in the folder
    image_files = sorted(os.listdir(image_folder))

    # Display each image
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        st.image(image_path, caption=image_file, use_column_width=True)
