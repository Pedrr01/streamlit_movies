import streamlit as st
from genres.page import show_genre

def main():
    st.markdown(
        """
        <style>
        * {
            user-select: none;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Inicio', 'Gêneros', 'Filmes', 'Atores/Atrizes', 'Avaliações',]
    )

    if menu_option == 'Início':
        st.write('Início')
    
    if menu_option == 'Gêneros':
        show_genre()

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')
    
    if menu_option == 'Atores/Atrizes':
        st.write('Lista de Atores/Atrizes')
    
    if menu_option == 'Avaliações':
        st.write('Lista de Avaliações')

if __name__ == '__main__':
    main()