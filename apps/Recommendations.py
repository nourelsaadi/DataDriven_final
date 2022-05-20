import streamlit as st

def app():
    #Title of this App/page
    st.markdown("<h1 style='text-align: center; color: #a711b7;'>Recommendations For Tomorrow</h1><br>", unsafe_allow_html=True)

    #Writing an introductory statement to the content
    st.markdown("<h5 style='text-align: center'><br><br>There are a few ways through which we can segment our customers & build tailored marketing strategies:</h5><br>", unsafe_allow_html=True)
        
    #Splitting the page into 4 columns 
    col1,col2,col3,col4 = st.columns([0.25,0.25,0.25,0.25])
    with col1:
        st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/MBA.png"></center>', unsafe_allow_html = True)
        st.markdown("<center><h9 style='text-align: center'>Market Basket Analysis</h9></center>", unsafe_allow_html=True)
    with col2:
        st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Demographic.png"></center>', unsafe_allow_html = True)
        st.markdown("<center><h9 style='text-align: center'>Demographic Analysis</h9></center>", unsafe_allow_html=True)
    with col3:
        st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/RFM.png"></center>', unsafe_allow_html = True)
        st.markdown("<center><h9 style='text-align: center'>Recency, Frequency, Monetary Value Analysis</h9></center>", unsafe_allow_html=True)
    with col4:
        st.markdown('<center><img style="max-width:80%" src="https://raw.githubusercontent.com/nourelsaadi/nae51_dddm_streamlit/main/Geographic.png"></center>', unsafe_allow_html = True)
        st.markdown("<center><h9 style='text-align: center'>Geographic Analysis</h9></center>", unsafe_allow_html=True)

    #Writing the concluding statement
    st.markdown("<h5 style='text-align: center'><br><br>Ideally, we would combine all 4 of these methods to get to know our custoners better, therefore achieve more accurate clusters & better business recommendations.</h5><br>", unsafe_allow_html=True)#setting the title

    
