import streamlit as st
from multiapp import MultiApp
from apps import Home, EDA, RFM_Analysis, Clustering_Customers, Customer_Breakdown, Recommendations # import your app modules here
import os
import base64
st.set_page_config(layout="wide")
app = MultiApp()

#Putting the dashboard's navbar and inserting direct links to the hypothetical e-store, in this case a subset of amazon, as well as a link to my linkedin profile and my email address
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #a711b7;">
  <a class="navbar-brand" href="https://www.amazon.co.uk/s?i=merchant-items&me=A245H4QRR5QR3Y" target="_blank">The E-Gift Store</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/nourelsaadi/" target="_blank">LinkedIn</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="mailto:nae51@mail.aub.edu" target="_blank">Email</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# Adding all my applications here
app.add_app("Home", Home.app)
app.add_app("Explore Your Data", EDA.app)
app.add_app("Clustering Customers", Clustering_Customers.app)
app.add_app("RFM Analysis", RFM_Analysis.app)
app.add_app("Customer Breakdown", Customer_Breakdown.app)
app.add_app("Recommendations", Recommendations.app)

# The main app
app.run() 