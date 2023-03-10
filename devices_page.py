import streamlit as st
import json,requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tokenonly import dummy


##### Backend URL Endpoints ######
signup_point = 'sighup/'
login_point = 'login/'
hubm2_point = 'hubm2/'
smartplug_point = 'smartplug/'
rollershade_point = 'rollershade/'
curtain_point = 'curtain/'
relay_point = 'relay/'
motion_point = 'motion/'
door_point = 'door/'
weather_point = 'weather/'
illuminance_point = 'illuminance/'
cube_point = 'cube/'
miniswitch_point = 'miniswitch/'
wallswitch1_point = 'wallswitch1/'
wallswitch2_point = 'wallswitch2/'
wirelessswitch1_point = 'wirelessswitch1/'
wirelessswitch2_point = 'wirelessswitch2/'

endpoints1 = [hubm2_point,smartplug_point,relay_point,motion_point,
            door_point,illuminance_point,cube_point,miniswitch_point,wallswitch1_point,wirelessswitch1_point
             ]
endpoints2 = [rollershade_point,curtain_point,wallswitch2_point,wirelessswitch2_point]

location="http://localhost:8000/backend/"
username="iotuser"
password="iot12345"



def devices(location,username,password,rows,tableRows):
    print(location,username,password,rows,tableRows)
    # st.write(location,username,password)
    if 'count' not in st.session_state:
        st.session_state.count = 0
        st.session_state.name = 'test'
    #st.session_state.last_updated = datetime.time(0,0)
    placeholder1=st.sidebar.empty()

    def update_counter(page):
        
        st.session_state.name = page
        st.session_state.count += 1
        st.write(st.session_state.count)
        st.write("first:",st.session_state.name,";;;",st.session_state.count)
        # with placeholder1.form("Detail"):
        #     page = st.selectbox("Test",full_list)
        #     testButton = st.form_submit_button("Detail",on_click=update_counter, args=[page,full_list])

        # if testButton:
        #     st.write("Success")
        
    data = {
            'username': username,
            'password': password
            }

    data = json.dumps(data)
    # placeholder1.empty()
    # placeholder2.empty()
    # placeholder3.empty()
    
    response = requests.post(url=(location + login_point),data=data)
    data = json.loads(response.text)
    TOKEN = data['token']
    status = response

    dataLogs1 =[]
    dataLogs2 =[]
    full_list = []
    DN = rows
    #st.subheader("Information on all devices installed")
    #st.write("Logged as {}".format(username))
    
    # DN=st.number_input(label="Retrieved Data",value=10)
    headers = {
        'Authorization': 'Token {}'.format(TOKEN),
        'Content-Type': 'application/json;charset=UTF-8',
        'DN':str(DN),
        'ORDERING':'-id'
    }

    response = requests.get(url= (location + weather_point),headers=headers)
    data = json.loads(response.text)
    status = response

    #print('data is {} and status is {}'.format(data[0]['modelName'],status))
    if data !=[]:
        #print(data[0])
        df = pd.DataFrame.from_dict(data)
        df[['temperature']] = df[['temperature']]/100
        df[['humidity']] = df[['humidity']]/100
        df[['airpressure']] = df[['airpressure']]/100
        st.write(location+weather_point)
        #st.write(df[['temperature','humidity','airpressure','datetime']].head(tableRows))
        st.dataframe(df.head(tableRows))
        full_list.append((weather_point)[0:-1])
    
    # st.write("""### Pair Grid Chart for Correlation""")
    # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
    # g.map_diag(sns.histplot)
    # g.map_offdiag(sns.scatterplot)
    # g.add_legend()
    # g.savefig("output.png")
    # st.pyplot(g)
        fig_col1,fig_col2,fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("##### Temperature Chart")
            fig = plt.figure(figsize=(5,2))
            sns.lineplot(data=df[['datetime','temperature']])
            st.pyplot(fig)
            
        with fig_col2:
            st.markdown("##### Humidity Chart")
            fig = plt.figure(figsize=(5,2))
            sns.lineplot(data=df[['datetime','humidity']])
            st.pyplot(fig)
        #fig = plt.figure(figsize=(10,4))
        
        with fig_col3:
            st.markdown("##### Ambient Chart")
            fig = plt.figure(figsize=(5,2))
            sns.lineplot(data=df[['datetime','airpressure']])
            st.pyplot(fig)

    i = 0
    for endpoint1 in endpoints1:
        response = requests.get(url=(location + endpoint1),headers=headers)
        dataLogs1.append(json.loads(response.text))
        status = response

        #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
        print(dataLogs1[i])
        df = pd.DataFrame.from_dict(dataLogs1[i])
        if dataLogs1[i]!=[]:
            st.write(location+endpoint1)
            #st.write(df[(["modelName","deviceId","value","datetime"]].head(tableRows))
            st.dataframe(df.head(tableRows))
            full_list.append((endpoint1)[0:-1])
            st.markdown("##### {} chart".format(endpoint1[0:-1]))
            fig = plt.figure(figsize=(40,10))
            sns.lineplot(data=df[['datetime','value']])
            st.pyplot(fig)
        i=i+1
    
    j = 0
    for endpoint2 in endpoints2:
        response = requests.get(url=(location + endpoint2),headers=headers)
        dataLogs2.append(json.loads(response.text))
        status = response

        #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
        print(dataLogs2[j])
        df = pd.DataFrame.from_dict(dataLogs2[j])
    
        if dataLogs2[j]!=[]:
            st.write(location+endpoint2)
            #st.write(df[["modeName","deviceId","value1","value2","datetime"]].head(1))
            st.dataframe(df.head(tableRows))
            full_list.append((endpoint2)[0:-1])
            st.markdown("##### {} chart".format(endpoint1[0:-1]))
            fig = plt.figure(figsize=(40,10))
            sns.lineplot(data=df[['datetime','value1']])
            sns.lineplot(data=df[['datetime','value2']])
            st.pyplot(fig)
        j=j+1
        # df[['temperature']] = df[['temperature']]/100
        # df[['humidity']] = df[['humidity']]/100
        # df[['airpressure']] = df[['airpressure']]/100
        # st.write(df[['temperature','humidity','airpressure','datetime']])
        # st.sidebar.button("Test")
        # st.write("""### Pair Grid Chart for Correlation""")
        # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
        # g.map_diag(sns.histplot)
        # g.map_offdiag(sns.scatterplot)
        # g.add_legend()
        # g.savefig("output.png")
        # st.pyplot(g)

        # fig = plt.figure(figsize=(10,4))
        # sns.lineplot(data=df[['datetime','temperature']])
        # st.pyplot(fig)


    print("FUll List is {}".format(full_list))
    # logoff = st.sidebar.button("Logoff")
    st.write("Devices List",full_list)
    # placeholder1 = st.sidebar.empty()
    # with placeholder1.form("Details"):
    #     page = st.selectbox("Test",full_list)
    #     testButton = st.form_submit_button("Detail")
    
    # if testButton:
    #      st.write("Success")
    #      st.write(page)

    # if page =="weather":
    #     st.write("Hahahha")
    # elif page=="smartplug":
    #     st.write("Mama")

    # if page=="weather":
    #     dummy()
    # if logoff:
    #     dummy()

    #devices(location,username,password)
    return 0



if __name__ == '__main__':
    devices(location,username,password)
