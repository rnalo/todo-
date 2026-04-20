import streamlit as st

st.title("📝 TODOアプリ")

tasks = []

task = st.text_import("タスクを入力")
if st.button("追加"):
   tasks.append(task)
   st.write(f"{task}")


st.write(task)
