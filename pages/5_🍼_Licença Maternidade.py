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
    st.markdown("<h1 style='text-align: center;'>Licença Maternidade</h1>", unsafe_allow_html=True)

#image_path = '/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/logo.png'
image = Image.open('logo2.png')
st.sidebar.image(image, width=250)

st.sidebar.markdown("""----""")

# Lê o arquivo de texto em um DataFrame
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"], disabled=True)

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')

##======================================================================================================================
## Criar uma lista vazia
##======================================================================================================================
#@st.cache_resource
#def get_lista():
#    # Crie uma lista vazia para armazenar os itens
#    lista = []
#    return lista
#
## Obtenha a lista do cache ou gere uma nova lista
#lista = get_lista()
#
##======================================================================================================================
## Adicione um campo de entrada de texto e um botão "Adicionar" para adicionar itens à lista
##======================================================================================================================
#item = st.text_input("Digite um item para adicionar à lista:")
#if st.button("Adicionar"):
#    if item:
#        lista.append(item)
#        st.write("Item adicionado à lista.")
#
##======================================================================================================================
## Adicione um campo de entrada de texto e um botão "Remover" para remover itens da lista
##======================================================================================================================
#remover = st.text_input("Digite um item para remover da lista:")
#if st.button("Remover"):
#    if remover in lista:
#        lista.remove(remover)
#        st.write("Item removido da lista.")
#
##======================================================================================================================
## Salve a lista no cache
##======================================================================================================================
#st.cache()
#get_lista()
#
#data = pd.DataFrame(lista)
#data = data.rename(columns={0: 'COLABORADORAS'})
#
##======================================================================================================================
## Exiba a lista atualizada
##======================================================================================================================
#st.markdown('## Colaboradoras em Licença Maternidade')
#st.write(data)
#=======================================================================================================================================================================
#função para criar um banco de dados ferias
def criar_banco_dados_ferias(dados):
    try:
        df = pd.read_excel('dataset/banco_dados_licenca.xlsx')
        df = df.append(dados, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame(dados, columns=['COLABORADOR'])
    
    # Remover aspas e colchetes dos valores
    df = df.applymap(lambda x: x[0] if isinstance(x, list) else x)
    
    df.to_excel('dataset/banco_dados_licenca.xlsx', index=False)

#função para excluir colaborador
def excluir_colaborador(colaborador):
    try:
        df = pd.read_excel('dataset/banco_dados_licenca.xlsx')

        if colaborador not in df['COLABORADOR'].values:
            raise ValueError("COLABORADOR não encontrado no banco de dados!")

        df = df[df['COLABORADOR'] != colaborador]
        df.to_excel('dataset/banco_dados_licenca.xlsx', index=False)
        return True
    except FileNotFoundError:
        return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False

def main():
    st.title('Cadastro de Funcionária de Licença Maternidade')

    # Criar caixas de texto para inserir os dados
    colaborador = st.text_input('COLABORADOR', key='colaborador_input', value='')
    
    # Criar botão para salvar os dados no Excel
    if st.button('Salvar Cadastro'):
        if colaborador.strip():
            dados = {'COLABORADOR': [colaborador.strip()]}
            criar_banco_dados_ferias(dados)
            st.success('Funcionário incluido com sucesso!')
        else:
            st.error('Por favor, preencha todos os campos antes de salvar.')
    
    
     # Criar caixa de texto para inserir o nome do colaborador a ser excluído
    colaborador_para_excluir = st.text_input('COLABORADOR do Colaborador para Excluir')
    
    # Criar botão para excluir o colaborador
    if st.button('Excluir Colaborador'):
        if (colaborador_para_excluir):
            if excluir_colaborador(colaborador_para_excluir):
                st.success(f'COLABORADOR "{colaborador_para_excluir}" excluído com sucesso!')
            else:
                st.error(f'Erro ao excluir o colaborador "{colaborador_para_excluir}".')
    
    # Ler os dados do banco de dados de férias e exibir na tabela
    st.markdown("""----""")
    st.markdown("## Lista de Licença Maternidade")
    try:
        df = pd.read_excel('dataset/banco_dados_licenca.xlsx')
        st.table(df)
    except FileNotFoundError:
        st.warning('Nenhum dado encontrado no banco de dados de férias.')
                
if __name__ == '__main__':
    main()