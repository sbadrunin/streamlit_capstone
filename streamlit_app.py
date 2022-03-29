import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

## SELECT course
course = ['Starter', 'Main', 'Dessert']
recipe = st.selectbox("Choose a course preference:", course)

## SELECT skill
skill = ['Beginner', 'Intermediate', 'Advanced']
recipe = st.selectbox("Choose your skill preference:", skill)

## SELECT DIET
diet = ['Vegetarian', 'Vegan']
recipe = st.selectbox("Choose your diet preference:", diet)
