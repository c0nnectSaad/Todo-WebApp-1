import streamlit as st
import functions as f

todos=f.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    print(todo)
    todos.append(todo)
    f.write_todo(todos)

todos = f.get_todo()

st.title("My To-Do WebApp")
st.subheader("This is my new todo app")
st.write("This is my first todo app")

for index, todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todo(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter new todo", placeholder="Enter todo here...",
              on_change=add_todo, key="new_todo")


