import pandas as pd
import streamlit as st


## SELECT course
course = ['Starter', 'Main', 'Dessert']
recipe = st.selectbox("Choose a course preference:", course)

## SELECT skill
skill = ['Beginner', 'Intermediate', 'Advanced']
recipe = st.selectbox("Choose your skill preference:", skill)

## SELECT DIET
diet = ['Vegetarian', 'Vegan']
recipe = st.selectbox("Choose your diet preference:", diet)
