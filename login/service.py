import streamlit as st
from api.service import Auth

def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response.get('error'):
        st.error(f'Falha ao realizar login: {response.get('error')}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()