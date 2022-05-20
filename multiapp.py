from asyncio.windows_events import NULL
from pickle import NONE
import streamlit as st
import pandas as pd
import os

#Setting the multiapp, code from the dataprofessor's repository on Github
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def run(self):
         #Displaying the Logo of the E-gift Store in the sidebar 
        with st.sidebar:
            st.markdown('<center><img style="max-width:50%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Logo.png"></center>', unsafe_allow_html = True)
         #Dropdown menu to move around the apps in our multiapp streamlit
        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])
       
        app['function']()
