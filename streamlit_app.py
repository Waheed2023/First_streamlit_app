import streamlit

streamlit.title( 'My Parents Healthy Dinner')
streamlit.header( 'Breakfast Menu')
streamlit.text(' 🥣 Oats meal')
streamlit.text('  🥑 🍞 Apple,banana, garpes, Avacado')
streamlit.text(' 🐔 hard boiled free range eggs')
streamlit.text(' 🥗 pure veg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

