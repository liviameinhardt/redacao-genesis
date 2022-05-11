"""
Main MVP Page

- gets data from csv (not DB yet)
"""
import streamlit as st
import pandas as pd 
import plotly.graph_objects as go 
import os
st.set_page_config(layout="wide")

from PIL import Image 

def app():
    user = str(st.session_state.user)
    st.title(f"Olá, {user.title()}!")

    # Novas tarefas 

    tarefas = pd.read_csv(f"data/tarefas.csv")

    num_tarefas = len(tarefas[tarefas["Entregue"]=="N"])
    aguardando_tarefas = len(tarefas[tarefas["Entregue"]=="S"])

    st.subheader(f"Você possui {num_tarefas} tarefas para entregar:")

    for index, row in tarefas.iterrows():

        titulo = f"Tarefa {row['Tarefa']} (Prazo: {row['Prazo']})"
        tema = f"Tema: {row['Tema']}"
        professor = f"Professor: {row['Professor']}"
        apoio = f"Textos de Apoio: {row['Textos de apoio']}"


        if row["Entregue"] ==  "N":

            expander = st.expander(titulo)
            expander.write(tema)
            expander.write(professor)
            expander.write(apoio)
            file = expander.file_uploader("Entrega",type=["png"],key=row['Tarefa'])
            
            if file is not None: 
                img = Image.open(file) 
                file_name = f"uploads/{user}_tarefa{row['Tarefa']}.png"  
                img.save(file_name)
                tarefas.loc[index,"Entregue"] = "S"


        else:

            st.write("---")
            st.subheader(f"Existem {aguardando_tarefas} tarefas envidas.")

            st.write(titulo)

        
        # Tarefas Enviadas (aguardando correção)


    # Histórico

    st.write("---")

    hist = pd.read_csv(f"data/livia.csv")
    col1, col2 = st.columns(2)

    with col1:

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hist["Tarefa"],y=hist["Nota"]))

        fig.update_layout(
            title=dict(
                text='<b>Histórico de Notas</b>',
                font=dict(size=24)),
            xaxis_title="Tarefa",
            yaxis_title='Nota Geral',
            font=dict(size=12)
        )

        st.plotly_chart(fig)

    with col2:

        st.subheader("Detalhes por Tarefa")
        for index, row in hist.iterrows():

            titulo = f"Tarefa {row['Tarefa']}"
            tema = f"Tema: {row['Tema']}"
            nota = f"Nota Geral: {row['Nota']}"
            comentarios = f"Comentários: {row['Comentários']}"

            expander = st.expander(titulo)
            expander.write(tema)
            expander.write(nota)
            expander.write(comentarios)

    


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                