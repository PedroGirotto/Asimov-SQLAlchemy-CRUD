import streamlit as st
from time import sleep

from src.Usuario import ler_todos_usuarios, ler_usuario_id


def web_app():
    with st.container(border=True):
        st.markdown("# Bem-vindo ao WebApp")


def login(engine):
    with st.container(border=True):
        st.markdown("Bem-vindo a tela de login")

        usuarios = ler_todos_usuarios(engine)
        usuarios = {usuario.nome: usuario for usuario in usuarios}

        nome_usuarios = st.selectbox(
            "Selecione o usuário",
            list(usuarios.keys())
        )
        senha = st.text_input(
            "Digite sua senha",
            type="password"
        )

        if st.button("Logar"):
            usuario = usuarios[nome_usuarios]
            if usuario.verificar_senha(senha):
                st.success("Login efetuado com sucesso")
                st.session_state["usuario"] = usuario
                st.session_state["logado"] = True
                sleep(0.5)
                st.rerun()
            else:
                st.error("Senha incorreta")


def start_front(engine):
    if not "logado" in st.session_state:
        st.session_state["logado"] = False
        
    if not st.session_state["logado"]:
        login(engine)
    else:
        web_app()