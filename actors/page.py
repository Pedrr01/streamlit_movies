import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

actors = [
    {
        'id' : 1,
        'name' : 'Leonardo Di Caprio' 
    },
      {
        'id' : 2,
        'name' : 'Chris Brown' 
    },
      {
        'id' : 3,
        'name' : 'Jóse' 
    },
]

def show_actor():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid'
    )

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz:')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')