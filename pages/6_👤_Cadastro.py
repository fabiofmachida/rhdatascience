import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import datetime
from datetime import datetime
import openpyxl
from PIL import Image

st.set_page_config(page_title="Rh Data Science", page_icon="🎲")
#=====================================================================================================================
# centraliza o texto na sidebar
#st.sidebar.markdown('# Rh Data Science')
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Cadastro</h1>", unsafe_allow_html=True)
    
#=====================================================================================================================  
# Carrega a imagem
#=====================================================================================================================
image = Image.open('logo2.png')
st.sidebar.image(image, width=250)

st.sidebar.markdown("""----""")

#=====================================================================================================================
# Lê o arquivo de texto em um DataFrame
#=====================================================================================================================
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"], disabled=True)

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')

#=====================================================================================================================
#funções
#=====================================================================================================================
#'/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/dataset/banco_dados.xlsx'
#função para criar um banco de dados
def criar_banco_dados(dados):
    try:
        df = pd.read_excel('dataset/banco_dados.xlsx')
        df = df.append(dados, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame(dados, columns=['CPF', 'PIS', 'COLABORADOR'])
    
    # Remover aspas e colchetes dos valores
    df = df.applymap(lambda x: x[0] if isinstance(x, list) else x)
    
    df.to_excel('dataset/banco_dados.xlsx', index=False)

#função para excluir colaborador
def excluir_colaborador(cpf_colaborador):
    try:
        df = pd.read_excel('dataset/banco_dados.xlsx')

        if cpf_colaborador not in df['CPF'].values:
            raise ValueError("CPF não encontrado no banco de dados!")

        df = df[df['CPF'] != cpf_colaborador]
        df.to_excel('dataset/banco_dados.xlsx', index=False)
        return True
    except FileNotFoundError:
        return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False

def main():
    st.title('Cadastro de Funcionário')

    # Criar caixas de texto para inserir os dados
    colaborador = st.text_input('COLABORADOR', key='colaborador_input', value='')
    cpf = st.number_input('CPF', step=1)
    pis = st.number_input('PIS', step=1)
    
    # Criar botão para salvar os dados no Excel
    if st.button('Salvar Cadastro'):
        if colaborador.strip() and cpf and pis:
            dados = {'COLABORADOR': [colaborador.strip()], 'CPF': [int(cpf)], 'PIS': [int(pis)]}
            criar_banco_dados(dados)
            st.success('Funcionário incluido com sucesso!')
        else:
            st.error('Por favor, preencha todos os campos antes de salvar.')
    
     # Criar caixa de texto para inserir o nome do colaborador a ser excluído
    cpf_para_excluir = st.number_input('CPF do Colaborador para Excluir', step=1)
    
    # Criar botão para excluir o colaborador
    if st.button('Excluir Colaborador'):
        if int(cpf_para_excluir):
            if excluir_colaborador(int(cpf_para_excluir)):
                st.success(f'CPF "{cpf_para_excluir}" excluído com sucesso!')
            else:
                st.error(f'Erro ao excluir o colaborador "{cpf_para_excluir}".')
    # Ler os dados do banco de dados de férias e exibir na tabela
    #/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/dataset/banco_dados_licenca.xlsx
    st.markdown("""----""")
    st.markdown("## Lista de Funcionários")
    try:
        df = pd.read_excel('dataset/banco_dados.xlsx')
        st.table(df.sort_values(['COLABORADOR', 'CPF', 'PIS']).reset_index())
    except FileNotFoundError:
        st.warning('Nenhum dado encontrado no banco de dados.')
        
if __name__ == '__main__':
    main()
   
