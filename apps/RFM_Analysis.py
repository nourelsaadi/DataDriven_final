import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
        #Title of this App/page
        st.markdown("<h1 style='text-align: center; color: #a711b7;'>RFM Analysis</h1><br>", unsafe_allow_html=True)

        #Making this app read the agg file that has the cluster names and their fields
        df_agg = pd.read_csv(r'C:\Users\itm\Desktop\Multipage\apps\Cluster_data.csv')
        
        #Preparing the bar graph for the clusters' Monetary mean
        fig_mon = px.bar(df_agg, x="Cluster_name", y="MonetaryMean")
        fig_mon.update_xaxes(title_text="Monetary Mean Of Each Cluster")
        fig_mon.update_xaxes(showgrid=False)
        fig_mon.update_yaxes(showgrid=False)
        fig_mon.update_xaxes(showgrid=False, zeroline=False)
        fig_mon.update_yaxes(showgrid=False, zeroline=False)
        fig_mon.update_layout(xaxis={'categoryorder':'total descending'})

        #Preparing the bar graph for the clusters' Recency mean
        fig_rec = px.bar(df_agg, x="Cluster_name", y="RecencyMean")
        fig_rec.update_xaxes(title_text="Recency Mean Of Each Cluster")
        fig_rec.update_xaxes(showgrid=False)
        fig_rec.update_yaxes(showgrid=False)
        fig_rec.update_xaxes(showgrid=False, zeroline=False)
        fig_rec.update_yaxes(showgrid=False, zeroline=False)
        fig_rec.update_layout(xaxis={'categoryorder':'total descending'})

        #Preparing the bar graph for the clusters' Frequency mean
        fig_frq = px.bar(df_agg, x="Cluster_name", y="FrequencyMean") 
        fig_frq.update_xaxes(title_text="Frequency Mean Of Each Cluster")
        fig_frq.update_xaxes(showgrid=False)
        fig_frq.update_yaxes(showgrid=False)
        fig_frq.update_xaxes(showgrid=False, zeroline=False)
        fig_frq.update_yaxes(showgrid=False, zeroline=False)
        fig_frq.update_layout(xaxis={'categoryorder':'total descending'})

        #Splitting the page into 3 columns for the 3 different graphs & a quick analysis which could indeed have been not hardcoded, but I was short on time:) 
        col1,col2,col3=st.columns([0.3,0.3,0.3]) 
        with col1:
        #plotting the Frequency Mean Of Each Cluster
            st.plotly_chart(fig_frq, use_container_width=True) 
            st.write("The type of customers that take the longest to buy from our shop again are the Sleepers")
        #plotting the Recency Mean Of Each Cluster
        with col2:
            st.plotly_chart(fig_rec, use_container_width=True)
            st.write("The type of customers that has not bought from us in the longest are the ")
        with col3:
        #plotting the Monetary Mean Of Each Cluster
            st.plotly_chart(fig_mon, use_container_width=True) 
            st.write("The type of customers that spend the most are the Star E-Shoppers")