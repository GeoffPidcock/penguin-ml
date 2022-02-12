# setup
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import pickle

rfc_pickle = open('random_forest_penguin.pickle', 'rb') 
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rfc_pickle) 
unique_penguin_mapping = pickle.load(map_pickle) 


st.markdown("""
# Penguin Species
Share some information about the penguin you saw...
We will guess it's specie
""")


# user input
with st.form('user_inputs'): 
  island = st.selectbox('Penguin Island', options=[
    'Biscoe', 'Dream', 'Torgerson']) 
  sex = st.selectbox('Sex', options=[
    'Female', 'Male']) 
  bill_length = st.number_input(
    'Bill Length (mm)', min_value=0) 
  bill_depth = st.number_input(
    'Bill Depth (mm)', min_value=0) 
  flipper_length = st.number_input(
    'Flipper Length (mm)', min_value=0) 
  body_mass = st.number_input(
    'Body Mass (g)', min_value=0) 
  st.form_submit_button() 

# process user input
island_biscoe, island_dream, island_torgerson = 0, 0, 0 
if island == 'Biscoe': 
  island_biscoe = 1 
elif island == 'Dream': 
  island_dream = 1 
elif island == 'Torgerson': 
  island_torgerson = 1 

sex_female, sex_male = 0, 0 

if sex == 'Female': 
  sex_female = 1 

elif sex == 'Male': 
  sex_male = 1 

new_prediction = rfc.predict(
    [[bill_length, bill_depth, flipper_length, 
  body_mass, island_biscoe, island_dream, 
  island_torgerson, sex_female, sex_male]]
)

prediction_species = unique_penguin_mapping[new_prediction][0]

st.write(f"Your species is probably {prediction_species}")