import streamlit as st

st.title("📝 TODOアプリ")

task = st.text_import("タスクを入力")
add_button = st.button("追加")

if add_button:
    st.write(f"{task}")