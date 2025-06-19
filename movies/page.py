import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

movies = [
    {
        'id' : 1,
        'name' : 'Titanic' 
    },
      {
        'id' : 2,
        'name' : 'Efeito Borboleta' 
    },
      {
        'id' : 3,
        'name' : 'Star Wars' 
    },
]
def show_movie():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )

    