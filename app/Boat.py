import streamlit as st
import os

def show_product_detail():
    st.title("Boat Details")
    st.write("Description of Boat.")

    # Path to the images folder for Boat
    image_folder = "images/Boat"

    # List all images in the folder
    if os.path.exists(image_folder):
        image_files = sorted(os.listdir(image_folder))

        # Display each image
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            st.image(image_path, caption=image_file, use_column_width=True)
    else:
        st.write("No images found for Boat.")
