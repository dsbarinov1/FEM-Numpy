import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import math
from datetime import time
import plotly.express as px
import datetime
from st_pages import Page, show_pages, add_page_title
st.sidebar.title("NumPy")

from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers


#add_page_title ("Введение")

show_pages(
    [
        Page("main.py", "Введение", "🏠"),
        Page("1.py", "Общая характеристика ПО", ":books:"),
        # Page("2.py", "Создание массивов", ":books:"),
        # Page("3.py", "Работа с массивами", ":books:"),
        # Page("4.py", "Линейная алгебра", ":books:"),
        # Page("5.py", "Работа с полиномами", ":books:"),
    ]
)



st.title("NumPy - универсальная библиотека для научных вычислений на Python")

for i in range(0, 20):
    st.write("\n")

st.write("Работу выполнили студенты МГУ Саров из группы ВМ-123:\n")
st.write("Бабенко Михаил, Баринов Даниил, Гайсин Роберт, Кислер Роман")