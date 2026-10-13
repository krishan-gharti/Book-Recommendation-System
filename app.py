from regex import P
import streamlit as st
import pickle
import joblib
st.title("Book Recommendation System")

with open ("books.pickle","rb")as file:
  books=pickle.load(file)

book_names=books["title"].values

name_book=st.selectbox("Enter the book name :",book_names)

similarities=joblib.load("similarities.joblib")

def recommend(name_book):
  book_index = books[books["title"] == name_book].index[0]
  recommendations = similarities[book_index]
  book_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
  recommended_books = []
  for i in book_list:
    recommended_books.append(books.iloc[i[0]].title)
  return recommended_books


if st.button("Recommend"):
  r=recommend(name_book)
  st.write("The recommended movies are : ")

  for i in r:
    st.write(i)


