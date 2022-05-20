import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
        #Title of this App/page
        st.markdown("<h1 style='text-align: center; color: #a711b7;'>Customer Breakdown</h1><br>", unsafe_allow_html=True)
        #To carry the data to this app, the file that has the cluster names and the corresponding values are read from the Cluster_data csv file in the folder
        df_agg = pd.read_csv(r'C:\Users\itm\Desktop\Multipage\apps\Cluster_data.csv')
        #putting the cluster names in a list 
        customer_list = [i for i in df_agg["Cluster_name"]]
        #splitting the page
        col1,col2,col3 = st.columns([0.3,0.3,0.3])
        #Creating a dropdown menu to select the customer/cluster that we want to focus on 
        with col1:
             customer = st.selectbox("Choose the Customer:", customer_list)
         #when selected, the sleepers' cluster's brief description & a business recommendation tailored for that customer type appear 
        if customer == "Sleepers":
            with col1:
                st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Sleeper.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Meet the Sleepers</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br> Our poorest performers. They have not bought from us in a while and they generally barely buy from us. They might even be loyal to our competitors, yet they make up most of our clientele.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Recommendations </span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br> Considering they make up over 90% of our clients, we must not let them go. We recommend establishing direct contact by sending MailChimp marketing emails. The latter would share limited offers to draw their attention back to our website.</span></center>", unsafe_allow_html= True)
         #same goes for the loyal shoppers' cluster
        elif customer == "Loyal Shoppers":
            with col1:
                st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Loyals.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 150%;color: #a711b7'> Meet our Loyal Shoppers</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br> Our loyal shoppers are those who spend a lot, and they do that frequently.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Recommendations</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br> Since this cluster of customers is ready to pay large amounts, we recommend to up-sell items with a higher price. We could even ask them for referrals, and we should definitely send them gifts. They must have access to premium customer service.</span></center>", unsafe_allow_html= True)
         #same goes for the star e-shoppers' cluster
        elif customer == "Star E-Shoppers":
            with col1:
                st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/StarShopper.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Meet our Star E-Shoppers</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br>They are the customers who spend the largest amount of money in our e-store, and they do so frequently. They form a minority of our clientele, and they might even be larger organizations. </span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Recommendations</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'> <br><br><br>Reward them with Loyalty Card, Points, Gifts, Special offers, Quicker Delivery & Premium Customer Service.</span></center>", unsafe_allow_html= True)
         #same goes for the regular e-shoppers' cluster
        elif customer == "Regular E-Shoppers":
            with col1:
                st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Regulars.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Meet our Regular E-Shoppers</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'><br><br><br> These are our regular customers who spend, but could ideally spend more.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Recommendations</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'><br><br><br> If we want them to spend more, progressively, we must opt for cross-selling items to keep them in the loop of our e-gift store. Sending further gifts would be beneficial to encourage them to buy from us! One must also note that they might quickly join the Sleepers if not maintained, therefore, direct contact by our agents must be made as any of their orders are canceled as to understand the reasons and perhaps tailor better offers. </span></center>", unsafe_allow_html= True)
         #same goes for the newest e-shoppers' cluster
        elif customer == "Newest E-Shoppers":
            with col1:
                st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/NewCustomers.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Meet our Newest E-Shoppers</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'><br><br><br> A recent shopper who is still to grow into a regular customer.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 150%; color: #a711b7'> Recommendations</span></center>", unsafe_allow_html= True)
                st.markdown("<center><span style='text-align: center; font-size: 150%'><br><br><br> We should offer Sam loyalty programs and cross sell items to make him progressively buy more</span></center>", unsafe_allow_html= True)
         #When cluster/customer type is not selected, nothing appears 
        else:
            with col1:
                st.write("")
            with col2:
                st.write("")
            with col3:
                st.write("")