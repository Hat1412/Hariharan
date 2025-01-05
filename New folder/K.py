import streamlit as st
from datetime import datetime
from time import sleep


now = datetime.now()
st.set_page_config(page_title="Timer App", page_icon="⌚")

hero = st.container()
hero.markdown("# Timer App")

txt = hero.empty()
img = st.image("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif")


while 1:    
    txt.markdown(f" <h1 text-align: center> {now.strftime('%d %A %I : %M : %S')} </p>", unsafe_allow_html=True)
