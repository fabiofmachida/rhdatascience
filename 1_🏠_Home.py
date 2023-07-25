# Libraries
import streamlit as st
import datetime
from datetime import datetime
import openpyxl

# bibliotecas necessarias
import pandas as pd
from PIL import Image
from streamlit_folium import folium_static

#======================================================================================================================
# Side Bar Streamlit
#======================================================================================================================
#st.sidebar.markdown('# Rh Data Science')
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Home</h1>", unsafe_allow_html=True)

#image_path = '/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/logo.png'
image = Image.open('/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/logo2.png')
st.sidebar.image(image, width=250)

st.sidebar.markdown("""----""")

# Lê o arquivo de texto em um DataFrame
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"])

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')

# Excluir após 15 dias
st.info('Novidade!! Cadastro de Funcionário. 👤', icon="⭐️")
st.info('Novidade!! Cadastro de Férias. ☀️', icon="⭐️")
st.info('Novidade!! Cadastro de Licença Maternidade. 🍼', icon="⭐️")

st.title('Rh Data Science')

st.markdown(
""" 
    Esse Dashboard foi construido para acompanhar a presença e ausência dos Colaboradores.
    ### Como utilizar esse Rh Data?
    - **Importação dos dados:** 
        - Abra o aplicativo do relógio de ponto e faça o download do arquivo no formato "txt".
        - Ao extrair os dados do aplicativo do relógio de ponto, extrair sempre, hora desejada até a hora atual.
        - Faça o "Upload" do arquivo para análise dos dados.
    ### Cadastros
    - **Guia Cadastro:**
        - Sempre cadastre um novo colaborador utilizando letras MAIÚSCULAS.
        - Utilize APENAS números, sem pontos, traços ou caracteres especiais.
        - CUIDADO:
            - Os erros de cadastro resultará em problemas na análise dos dados.
        - **Excluir Colaborador:**
            - Digite apenas o CPF do colaborador, utilizando SOMENTE números.
    - **Guia Férias:**
        - Sempre cadastrar os colaboradores com letras MAIÚSCULAS.
        - **Excluir Colaborador:**
            - Digite o nome do colaborador exatamente igual ao cadastrado.
    - **Guia Licença Maternidade:**
        - Sempre cadastrar as colaboradoras com letras MAIÚSCULAS.
        - **Excluir Colaborador:**
            - Digite o nome da colaboradora exatamente igual ao cadastrado.

    ### Suporte
    - Consultar a Administração:
        - @LeonardoDelVechio
        - @IvoneSantos
    
""")

st.markdown("""----""") 
st.markdown("""Atualizado 19/07/2023""") 
st.markdown("""Build 2.0""")
