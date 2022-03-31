import streamlit as st
from pearson import get_recommendation

st.title('Sistema de Recomendação de Vinhos')
st.subheader("Sistema de recomendação que utiliza o Streamlit para renderização de interfaces no front-end, no back-end, utiliza Python, e o Algoritmo de recomendação Pearson.")


form = st.form("my_form")
username = form.text_input(
      'Insira o nome de usuário para verificar as recomendações de vinhos',
      value = '',
      max_chars = 30
)

# Every form must have a submit button.
submitted = form.form_submit_button("Submit")
if submitted:
      print(username)
      
      for i in range(5):
            st.write(get_recommendation(username))