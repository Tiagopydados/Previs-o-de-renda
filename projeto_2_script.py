import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

sns.set(context='talk', style='ticks')

renda = pd.read_csv(
    r"C:\Users\lifem\Desktop\Soberano\PROGRAMAÇÃO\T.i\Cientista de Dados\AULA 17 - Métodos de análise\ATIVIDADES\EXERCÍCIO 1\input\previsao_de_renda.csv"
)

st.set_page_config(
    page_title="Previsão de renda",
    page_icon="https://static.vecteezy.com/ti/vetor-gratis/t1/8084989-dinheiro-saco-e-pilha-de-moeda-de-ouro-vetor.jpg",  # Ícone da página
    layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda['data_ref'] = pd.to_datetime(renda['data_ref'], format='%Y-%m-%d')

min_data = renda.data_ref.min()
max_data = renda.data_ref.max()

data_inicial = st.sidebar.date_input('Data inicial',
                                     value=min_data,
                                     min_value=min_data,
                                     max_value=max_data)

data_final = st.sidebar.date_input('Data Final',
                                   value=max_data,
                                   min_value=min_data,
                                   max_value=max_data)

st.write('Data inicial ', data_inicial)
st.write('Data final ', data_final)

renda = renda[(renda['data_ref'] >= pd.to_datetime(data_inicial))
              & (renda['data_ref'] <= pd.to_datetime(data_final))]

with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader('Escolaridade')
        plt.figure(figsize=(0.5, 0.5))
        fig = px.pie(renda, names='educacao',
                     color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig)

    with col2:
        st.subheader('Quantidade de pessoas por sexo')
        plt.figure(figsize=(1, 2))
        fig = px.histogram(renda, x='sexo', color='sexo', color_discrete_map={
                           'F': '#FFA07A', 'M': '#4682B4'})
        st.plotly_chart(fig)

    with col3:
        st.subheader('Quantidade de pessoas que vivem em uma mesma residência')
        plt.figure(figsize=(1, 2))
        fig = px.histogram(renda, x='qt_pessoas_residencia',
                           color_discrete_sequence=['#8A2BE2'])
        st.plotly_chart(fig)


with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader('Tipo de renda')
        plt.figure(figsize=(1, 2))
        fig = px.histogram(renda, x='tipo_renda', color='tipo_renda',
                           color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig)

    with col2:
        st.subheader('Média de Renda por Idade')

        media_renda_por_idade = renda.groupby(
            'idade')['renda'].mean().reset_index()
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=media_renda_por_idade['idade'],
            y=media_renda_por_idade['renda'],
            marker_color='#2E8B57'
        ))

        fig.update_layout(
            xaxis_title='Idade',
            yaxis_title='Média de Renda',
            xaxis=dict(tickmode='array'),
            template='plotly_white'
        )

        st.plotly_chart(fig)
