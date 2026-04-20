import streamlit as st

st.title("📝 TODOアプリ")

tasks = []

if "tasks" not in st.session_state:
   st.session_state.tasks = []

task = st.text_imput("タスクを入力")
if st.button("追加"):
   st.session_state.tasks.append(task)


st.write("### タスク一覧")
st.write(st.session_state.tasks)
