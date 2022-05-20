import streamlit as st
import pandas as pd
import os

def app():
     st.markdown("<h1 style='text-align: center; color: #a711b7;'>The E-Gift Store</h1><br>", unsafe_allow_html=True) 
     #Introductory Statements
     st.markdown("<center><h5> Want to get to know your customers better? <br> Well, let's analyze their purchasing behaviors. <br> Upload your dataset and let our Streamlit App introduce you to your e-gifters. </center></h5>", unsafe_allow_html=True)

     #Setting a place to upload the dataset
     uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"]) 
     #Setting the data to be global as to be used throughout the multiapp
     global data 

     #if the data is uploaded, read the uploaded file & store into another csv file within the folder
     if uploaded_file is not None:
          data = pd.read_csv(uploaded_file)
          data.to_csv(r'C:\Users\itm\Desktop\Multipage\apps\main_data.csv', index=False) #considering this is a multiapp, this was my go to method to carry the dataset to the other pages (by thus saving the file into a csv that is then saved in the folder)
     else:
          data = ""

     #If the file is available, show the first 5 columns for inspection purposes, else do not show anything  
     if uploaded_file is not None: 
          st.dataframe(data.head(n=5)) 
     else:
          st.write("")