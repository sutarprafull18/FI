import streamlit as st
import os

def show_product_detail():
    st.title("side_table Details")
    st.write("Description of side_table.")

    # Path to the images folder for Bed
    image_folder = "images/side_table"

    # List all images in the folder
    if os.path.exists(image_folder):
        image_files = sorted(os.listdir(image_folder))

        # Display each image
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            st.image(image_path, caption=image_file, use_column_width=True)
    else:
        st.write("No images found for side_table.")
