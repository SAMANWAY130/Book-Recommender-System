import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def recomend(txt):
    ans = []

    if txt in book_pivot.index:

        ind = book_pivot.index.get_loc(txt)
        sim = similarity[ind]
        sim = enumerate(sim)
        sim = sorted(sim, key=lambda x: x[1], reverse=True)
        sim = sim[1:6]
        y = []
        for i in sim:
            y.append(i[0])

        for i in y:
            ans.append(book_pivot.index[i])
        return ans


    else:
        return []


similarity = pickle.load(open('similarity.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))

st.title("Book Recommendation System")
inp = st.selectbox("Select a book", book_pivot.index.tolist())
books = recomend(inp)
i=1
st.subheader("Recommended Books are .....")


for book in books:

    st.write(f"{i} no -  {book}")
    i += 1

