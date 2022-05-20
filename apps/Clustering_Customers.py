import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta
import plotly.express as px
import matplotlib as plt
import seaborn as sns
import os

def app():
   #Title of this App/page
    st.markdown("<h1 style='text-align: center; color: #a711b7;'>Clustering Customers with RFM analysis</h1><br>", unsafe_allow_html=True)
    #Reading the data (it is a multiapp, this was the only known method for the time being (that actually worked). Loaded the data from the main_data csv file that was generated and added to the folder
    df = pd.read_csv(r'C:\Users\itm\Desktop\Multipage\apps\main_data.csv')
    
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    # Group data by customerID
    # Create snapshot date
    snapshot_date = df['InvoiceDate'].max() + timedelta(days=1)
    print(snapshot_date)
    #Grouping by CustomerID
    data_process = df.groupby(['CustomerID']).agg({
      'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
      'InvoiceNo': 'count',
      'Sales': 'sum'})
    #Rename the columns 
    data_process.rename(columns={'InvoiceDate': 'Recency',
                              'InvoiceNo': 'Frequency',
                              'Sales': 'MonetaryValue'}, inplace=True)
     
    #unsupervised ml
    from sklearn.cluster import KMeans
    sse ={}
    for k in range(1,20):
      kmeans = KMeans(n_clusters =k, random_state = 42)
      kmeans.fit(data_process)
      sse[k] = kmeans.inertia_
   
    #Assessing the optimal number of clusters with the Elbow Method
    #CODE WAS THEN COMMENTED BECAUSE IT WAS USED FOR SETTING K 

    #plt.title("The Elbow Method")
    #plt.xlabel('k')
    #plt.ylabel('SSE')
    #sns.pointplot(x=list(sse.keys()), y = list(sse.values()))
    #plt.show()

    #we then set the number of clusters we want according to the optimal number we saw through the Elbow methow
    k = 5
    #instantiating the model
    ml = KMeans(n_clusters=k, random_state = 42)
    #fit the cleaned data into the machine learning model
    ml.fit(data_process)
    #creating a cluster column according to the resulted labels after the model was fit
    data_process["Cluster"] = ml.labels_
    #creating a cluster name column using the cluster number!
    data_process["Cluster_name"] = 'Cluster' + data_process["Cluster"].astype('str')
    #RFM values extraction: calculating average values for each Cluster, and returning a size of each segment
    df_agg = data_process.groupby("Cluster_name").agg({"Recency": 'mean', 'Frequency': 'mean', 'MonetaryValue':['mean', 'count']}).round(0)
    df_agg.columns = df_agg.columns.droplevel()
    df_agg.columns = ["RecencyMean", "FrequencyMean", "MonetaryMean","Count"]
    df_agg["Percent"] = round((df_agg['Count']/df_agg.Count.sum())*100,2)
    #resetting index
    df_agg = df_agg.reset_index()
    #Renaming the Clusters
    labels_dict = {'Cluster0': "Sleepers", "Cluster1": 'Loyal Shoppers', "Cluster2": "Star E-Shoppers", "Cluster3": "Regular E-Shoppers", "Cluster4": "Newest E-Shoppers"}
    df_agg["Cluster_name"] = df_agg['Cluster_name'].map(labels_dict)
    data_process['Cluster_name'] = data_process['Cluster_name'].map(labels_dict)
    
    #to carry the resulting aggregated data into the other apps, a file was created into the folder
    df_agg.to_csv(r'C:\Users\itm\Desktop\Multipage\apps\Cluster_data.csv', index=False)
   
    #preparing the scatter plot that shows the distribution of customers based on recency & monetary value
    fig_clust = px.scatter(df_agg, x="RecencyMean", y="MonetaryMean", size = "FrequencyMean", color = "Cluster_name", hover_name ="Cluster_name", size_max = 100)
    fig_clust.update_xaxes(title_text="Distribution of Customers based on their Recency and Monetary means")
    fig_clust.update_xaxes(showgrid=False)
    fig_clust.update_yaxes(showgrid=False)
    fig_clust.update_xaxes(showgrid=False, zeroline=False)
    fig_clust.update_yaxes(showgrid=False, zeroline=False)
    
    #preparing the bar plot that shows the distribution of customers within clusters
    fig_clust_perc = px.bar(df_agg, x="Cluster_name", y="Percent")
    fig_clust_perc.update_xaxes(title_text="Distribution of Customers within Clusters")
    fig_clust_perc.update_xaxes(showgrid=False)
    fig_clust_perc.update_yaxes(showgrid=False)
    fig_clust_perc.update_xaxes(showgrid=False, zeroline=False)
    fig_clust_perc.update_yaxes(showgrid=False, zeroline=False)
    fig_clust_perc.update_layout(xaxis={'categoryorder':'total descending'})

    #splitting the page & plotting the graphs with quick hardcoded analysis 
    col1,col2 = st.columns([0.5,0.5])
    with col1:
       st.plotly_chart(fig_clust, use_container_width=True)
       st.write("From the RFM analysis coupled with an unsupervised machine learning method, customers can be clustered into 5 different clusters, meaning we can distinguish 5 different types of customers.")
    with col2:
       st.plotly_chart(fig_clust_perc, use_container_width=True)
       st.write("Around 95% of our customers fall under the Sleepers' Cluster.")

      