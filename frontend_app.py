
import streamlit as st
from devices_page import devices
from all_page import all
from registration_page import registration
from signup_page import signup
from PIL import Image
import datetime

st.set_page_config(layout="wide")
image = Image.open("aqaralogo.png")
st.sidebar.title ("Test App for Backend API")

st.sidebar.image(image,width = 200)
server = st.sidebar.selectbox("Server",("Localhost","Aqara Korea","Ariwells","Other"))
if server == "Other":
    server = st.sidebar.text_input("Please write down IP")
placeholder1= st.sidebar.empty()
placeholder2 = st.sidebar.empty()
placeholder3 = st.sidebar.empty()
placeholder4 = st.sidebar.empty()
placeholder5 = st.sidebar.empty()


if 'count' not in st.session_state:
    st.session_state.count = 0
    #st.session_state.last_updated = datetime.time(0,0)

def update_counter(username,password,numberOfDataRetrieved,numberOfRowsInTable):
    st.session_state.count += 1
    if page=="Login":
    
        placeholder1.empty()
        placeholder2.empty()
        placeholder3.empty()
        placeholder4.empty()
        placeholder5.empty()
        

        if server == "Localhost":
            serverIP = "localhost"
        elif server == "Aqara Korea":
            serverIP = "aqarakorea.kr"
        elif server == "Ariwells":
            serverIP = "ariwells.kr"
        else: 
            serverIP = server
        


        if httpsOK == False:
            headValue = "http://"
        else:
            headValue = "https://"

        if eight000 == True:
            portValue=":8000/backend/"
        else:
            portValue="/backend/"

        location = headValue + serverIP + portValue
        devices(location,username,password,numberOfDataRetrieved,numberOfRowsInTable)

    elif page=="Aqara Account Registration":
        
        placeholder1.empty()
        placeholder2.empty()
        placeholder3.empty()
        placeholder4.empty()
        #placeholder5.empty()
        

        if server == "Localhost":
            serverIP = "localhost"
        elif server == "Aqara Korea":
            serverIP = "aqarakorea.kr"
        elif server == "Ariwells":
            serverIP = "ariwells.kr"
        else: 
            serverIP = server


        if httpsOK == False:
            headValue = "http://"
        else:
            headValue = "https://"

        if eight000 == True:
            portValue=":8000/backend/"
        else:
            portValue="/backend/"

        location = headValue + serverIP + portValue

        registration(location)

    elif page=="Signup":
        
        placeholder1.empty()
        placeholder2.empty()
        placeholder3.empty()
        placeholder4.empty()
        #placeholder5.empty()
        

        if server == "Localhost":
            serverIP = "localhost"
        elif server == "Aqara Korea":
            serverIP = "aqarakorea.kr"
        elif server == "Ariwells":
            serverIP = "ariwells.kr"
        else: 
            serverIP = server


        if httpsOK == False:
            headValue = "http://"
        else:
            headValue = "https://"

        if eight000 == True:
            portValue=":8000/backend/"
        else:
            portValue="/backend/"

        location = headValue + serverIP + portValue

        signup(location)

with placeholder1.form("Basic Settings"):


    httpsOK = st.checkbox("HTTPS",value=False)
    eight000 = st.checkbox("Port 8000",value=True)
    page = st.selectbox("Login/out-Signup",("Please select a menu","Aqara Account Registration","Login","Signup"))
    messageOnly = placeholder5.write("If you are a new user, please register an Aqara Account and sign up first")
    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")

    numberOfDataRetrieved = st.slider("Number of Data To Be Retrieved",min_value=1,max_value=100,value=50,step=10)
    numberOfRowsInTable = st.slider("Number of Rows in a Table",min_value=1,max_value=20,value=5,step=1)
    settingButton = st.form_submit_button("Submit")


if page=="Login":
    
        placeholder1.empty()
        placeholder2.empty()
        placeholder3.empty()
        placeholder4.empty()
        placeholder5.empty()
        

        if server == "Localhost":
            serverIP = "localhost"
        elif server == "Aqara Korea":
            serverIP = "aqarakorea.kr"
        elif server == "Ariwells":
            serverIP = "ariwells.kr"
        else: 
            serverIP = server


        if httpsOK == False:
            headValue = "http://"
        else:
            headValue = "https://"

        if eight000 == True:
            portValue=":8000/backend/"
        else:
            portValue="/backend/"

        location = headValue + serverIP + portValue
        all(location,username,password,numberOfDataRetrieved,numberOfRowsInTable)

elif page=="Aqara Account Registration":
    
    placeholder1.empty()
    placeholder2.empty()
    placeholder3.empty()
    placeholder4.empty()
    #placeholder5.empty()
    

    if server == "Localhost":
        serverIP = "localhost"
    elif server == "Aqara Korea":
        serverIP = "aqarakorea.kr"
    elif server == "Ariwells":
        serverIP = "ariwells.kr"
    else: 
        serverIP = server


    if httpsOK == False:
        headValue = "http://"
    else:
        headValue = "https://"

    if eight000 == True:
        portValue=":8000/backend/"
    else:
        portValue="/backend/"

    location = headValue + serverIP + portValue

    registration(location)

elif page=="Signup":
    
    placeholder1.empty()
    placeholder2.empty()
    placeholder3.empty()
    placeholder4.empty()
    #placeholder5.empty()
    

    if server == "Localhost":
        serverIP = "localhost"
    elif server == "Aqara Korea":
        serverIP = "aqarakorea.kr"
    elif server == "Ariwells":
        serverIP = "ariwells.kr"
    else: 
        serverIP = server

    if httpsOK == False:
        headValue = "http://"
    else:
        headValue = "https://"

    if eight000 == True:
        portValue=":8000/backend/"
    else:
        portValue="/backend/"

    location = headValue + serverIP + portValue

    signup(location)
# with st.form("Basic Settings"):

# server = placeholder1.selectbox("Server",("Localhost","Aqara Korea","Ariwells"))
# httpsOK = placeholder2.checkbox("HTTPS",value=False)
# eight000 = placeholder3.checkbox("Port 8000",value=True)
# page = placeholder4.selectbox("Login/out-Signup",("Please select a menu","Login","Aqara Account Registration","Signup"))
# messageOnly = placeholder5.write("If you are a new user, please register an Aqara Account and sign up first")
    # settingButton = st.form_submit_button("Submit")
#settingButton = placeholder5.button("Submit")

