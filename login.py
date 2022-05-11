"""
Login MVP page 

- not secure 
- not the best way 
- it works
"""

import streamlit as st
from pages import aluno, professor

st.set_page_config(layout="wide")

login = {'livia':"123","Mariana":"456"} # future: get from DB


def validate(user,password): 
    if user not in login.keys(): return 0 
    elif login[user] != password: return 0
    else: return 1 


if ('user' not in st.session_state) and ('password' not in st.session_state) :
    st.session_state.user, st.session_state.password  = "",""

if not validate(st.session_state.user,st.session_state.password):
    
    header = st.header("Gênesis - Redação 2022")
    subheader = st.subheader("Faça seu login")

    pwd_placeholder, user_placehold,erro = st.empty(), st.empty(), st.empty()

    user = user_placehold.text_input("User:", value="")
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
        
    st.session_state.user = user
    st.session_state.password = pwd
    
    if validate(st.session_state.user,st.session_state.password):
        user_placehold.empty()
        pwd_placeholder.empty()
        header.empty()
        subheader.empty()
        erro.empty()
        aluno.app()
    
    elif st.session_state.user != "" and st.session_state.password != "":
        erro = st.error("Login ou senha incorreto")

else:
    aluno.app()
 

   