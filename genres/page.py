import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

genres = [
    {
        'id' : 1,
        'name' : 'Terror' 
    },
      {
        'id' : 2,
        'name' : 'Romance' 
    },
      {
        'id' : 3,
        'name' : 'Suspense' 
    },
]

def show_genre():
    st.write('Lista de Gêneros')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
    )

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero:')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')