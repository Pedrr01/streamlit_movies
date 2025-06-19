import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

reviews = [
    {
        'id' : 1,
        'stars' : 5
    },
      {
        'id' : 2,
        'stars' : 3 
    },
      {
        'id' : 3,
        'stars' : 1
    },
]

def show_review():
    st.write('Lista de Avaliações')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )
