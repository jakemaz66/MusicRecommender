"""This file is is responsible for deploying the recommender system to Streamlit"""

import streamlit as st
from PIL import Image


def run():
    """
    This function runs the streamlit server
    """
    # Create a sidebar menu
    menu = st.sidebar.radio('Navigation', ['Home', 'Docs'])

    if menu == 'Home':

        #Defining title of the website
        st.title("Music Recommender")

        #Allowing user to upload an image of their fruit or vegetable
        img_file = st.file_uploader("Upload your Ingredients!", type=["jpg", "png"])

        if img_file is not None:
            #Reading in the image
            img = Image.open(img_file).resize((250, 250))

            #Displaying the image in streamlit app
            st.image(img, use_column_width=False)

           

            


if __name__ == '__main__':
    run()