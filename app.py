import streamlit as st
from factorial import fac

def main():
    st.title("Factorial calculator")
    n=st.number_input("Enter a number",min_value=0,max_value=999)
    if st.button("Calculate"):
        st.write(f'The factorial of {n} is {fac(n)}')

if __name__=="__main__":
    main()