import streamlit as st
from factorial import fac
import os

def load_users():
    try:
        if os.path.exists("user.txt"):
            with open("user.txt","r",encoding="utf-8") as f:
                users=[line.strip() for line in f.readlines() if line.strip()]
                return users
        else:
            st.error("File users.txt does not exist")
            return []
    except Exception as e:
        st.error(f"Error while reading file uses.txt:{e}")
        return []
            
def login_page():
    st.title("Login")

    username=st.text_input("Input username")

    if st.button("Login"):
        if username:
            users=load_users()
            if username in users:
                st.session_state.logged_in=True
                st.session_state.username=username
                st.rerun()
            else:
                st.session_state.show_greeting=True
                st.session_state.username=username
                st.rerun()
    else:
        st.warning("Please enter input user name")
        
def factorial():
    st.title("Factorial calculator")

    st.write(f"Hello, {st.session_state.username}")
    #Log out button
    if st.button("Log out"):
        st.session_state.logged_in=False
        st.session_state.username=""
        st.rerun()
    st.divider()

    n=st.number_input("Enter a number",min_value=0,max_value=999)
    if st.button("Calculate"):
        st.write(f'The factorial of {n} is {fac(n)}')

def greeting_page():
    st.title("Hello!")
    st.write(f"Hello, {st.session_state.username}")
    st.write("You do not have right to access factorial calculation function")

    if st.button("Back to Log in"):
        st.session_state.username=""
        st.session_state.show_greeting=False
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in=False
    if 'username' not in st.session_state:
        st.session_state.username=""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting=False

    if st.session_state.logged_in:
        factorial()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()
        
if __name__=="__main__":
    main()