# Libraries
import streamlit as st
import datetime
from datetime import datetime
import openpyxl

# bibliotecas necessarias
import pandas as pd
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title="Rh Data Science", page_icon="🎲")
#======================================================================================================================
# Side Bar Streamlit
#======================================================================================================================
#st.sidebar.markdown('# Rh Data Science')
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Ausentes</h1>", unsafe_allow_html=True)

#image_path = '/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/logo.png'
image = Image.open('logo2.png')
st.sidebar.image(image, width=250)

st.sidebar.markdown("""----""")

st.title('Funcionários ausentes')

#======================================================================================================================
# IMPORTANDO O PRIMEIRO DATASET
#======================================================================================================================
# Lê o arquivo de texto em um DataFrame
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"], disabled=True)

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')
    
#======================================================================================================================
# Transformation 1
#======================================================================================================================  
    #mudar o nome da coluna
    df1 = df.rename(columns={df.columns[0]: 'log'})
    
    #criar um dataframe com os dados desagrupados
    data = []
    dados = df1['log'].unique()
    
    for i in dados:
        id = i[:10]
        data_ = i[10:18]
        hora = i[18:22]
        pis = i[23:34]
        cod = i[34:]
        data.append([id, data_, hora, pis, cod])
    df2 = pd.DataFrame(data, columns=['ID', 'Data', 'Hora', 'PIS', 'Cod'])

    #excluir os itens da coluna 'Cod' que tenha mais do que 4 caracteres
    df2 = df2[df2['Cod'].str.len() <= 4]
    
    # formatar a coluna data
    df2['Data'] = pd.to_datetime(df2['Data'], format='%d%m%Y')

    # formatar a coluna hora
    df2['Hora'] = pd.to_datetime(df2['Hora'], format='%H%M')
    
    # transformando a coluna em inteiro
    df2['PIS'] = pd.to_numeric(df2['PIS'])
    
#======================================================================================================================
# IMPORTANDO O SEGUNDO DATASET
#======================================================================================================================
    # Importando o dataset "banco_dados" '/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/dataset/banco_dados.xlsx'
    df3 = pd.read_excel('dataset/banco_dados.xlsx')
    
#======================================================================================================================
# Transformation 2
#======================================================================================================================   
    # unindo e comparando as tabelas atraves da coluna PIS
    df4 = pd.merge(df2, df3, left_on='PIS', right_on='PIS', how='right')[['Data', 'Hora', 'PIS', 'COLABORADOR']]
        
    # seleciona as linhas com valores nulos em pelo menos uma das três colunas
    df_aux = df4[['Data', 'Hora', 'PIS', 'COLABORADOR']].isnull().any(axis=1)
    
    # cria um novo dataframe com as linhas selecionadas
    faltas = df4[df_aux].reset_index()
    
#======================================================================================================================
    #st.markdown('### Funcionários ausentes')
    with st.container():
        faltas = faltas[['COLABORADOR']]
        st.table(faltas)
        
       
        
   
    
    

        


