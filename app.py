import streamlit as st
from auth import register_user, login_user

# Manejador de sesión básica con Streamlit
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""


def login_screen():
    st.subheader("Iniciar Sesión")
    email = st.text_input("Correo electrónico")
    passwd = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        user = login_user(email, passwd)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_name = user.username
            st.success("Ingreso exitoso")
        else:
            st.error("Correo o contraseña incorrectos")


def register_screen():
    st.subheader("Crear Cuenta")
    user = st.text_input("Nombre de usuario")
    email = st.text_input("Correo electrónico")
    passwd = st.text_input("Contraseña", type="password")
    passwd2 = st.text_input("Repetir contraseña", type="password")

    if st.button("Registrar"):
        if passwd != passwd2:
            st.warning("Las contraseñas no coinciden")
        elif len(passwd) < 6:
            st.warning("La contraseña debe tener al menos 6 caracteres")
        else:
            try:
                register_user(user, passwd, email)
                st.success("Usuario registrado correctamente")
            except:
                st.error(
                    "Error al registrar. Verifica que el correo o usuario no estén en uso."
                )


def dashboard():
    st.title("Bienvenido al Dashboard PETI")
    st.write(f"Hola, **{st.session_state.user_name}** 👋")
    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""


# --- Pantalla Principal ---

st.title("Aplicación PETI")

if st.session_state.logged_in:
    dashboard()
else:
    menu = ["Login", "Registro"]
    choice = st.sidebar.radio("Menú", menu)

    if choice == "Login":
        login_screen()
    else:
        register_screen()
