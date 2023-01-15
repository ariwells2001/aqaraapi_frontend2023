import streamlit as st
def dummyFunc():

    if 'count' not in st.session_state:
        st.session_state.count = 0
    #st.session_state.last_updated = datetime.time(0,0)

    def update_counter(status):
        st.session_state.count += 1
        if status=="onState":
            st.write("Power is on")
        elif status=="offState":
            st.write("Powre is off")

    placeholder = st.sidebar.empty()
    with placeholder.container():
        status = st.radio("Choose on or off",("onState","offState"))
        
    print(status)
    if status=="onState":
        st.write("Power is on")
    elif status=="offState":
        st.write("Powre is off")
        # placeholder1 = st.empty()
        # with placeholder1.form("Dummy"):
        #     test=st.selectbox("aha",{"please","test3","test4"})
        #     dummyButton = st.form_submit_button("Dummy")
        # if dummyButton:
        #     st.write("Success!!!!!")
        # if test=="test3":
        #     st.write("aha")
        # elif test=="test4":
        #     st.write("alas")