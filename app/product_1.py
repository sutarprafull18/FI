import streamlit as st
import os

def show_product_detail():
    st.title("Product 1 Details")
    st.write("Description of Product 1.")

    # Path to the images folder for Product 1
    image_folder = "images/product_1"

    # List all images in the folder
    image_files = sorted(os.listdir(image_folder))

    # Display each image
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        st.image(image_path, caption=image_file, use_column_width=True)
