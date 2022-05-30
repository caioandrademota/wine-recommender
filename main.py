import streamlit as st
from similarity import get_recommendations

st.title('Sistema de Recomendação de Filmes - Só Filme TOP')
st.subheader("Sistema de recomendação que utiliza o Streamlit para renderização de interfaces no front-end, no back-end, utiliza Python.")


form = st.form("my_form")
movie = form.text_input(
      'Insira o nome do filme para verificar as recomendações de filmes semelhantes',
      value = '',
      max_chars = 30
)

# Every form must have a submit button.
submitted = form.form_submit_button("Submit")
if submitted:
      print(movie)
      listRecommend  = get_recommendations(movie)
      st.subheader("Se você gostou de " + movie + "...")
      st.subheader("...você vai gostar de: ")
      st.write(listRecommend)