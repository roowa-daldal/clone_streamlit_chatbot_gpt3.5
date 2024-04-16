import streamlit as st
import time
st.title("G-Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("무엇이든 물어보세요!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"AI 서칭 결과: [{prompt}](https://www.google.com/search?q={prompt})"
    # Display assistant response in chat message container

    with st.status("Wait for response...", expanded=True) as status:

        st.write("1. Ask AI & RAG engine...")
        time.sleep(1)
        st.write("2. Get response...")
        time.sleep(1)
        st.write("3. Now make a response for you!")
        time.sleep(1)
        status.update(label="Response!", state="complete", expanded=False)
    st.success('Done!')
    with st.chat_message("assistant"):
        st.markdown(response)
        st.toast('Hooray!', icon='🎉')
        st.balloons()
    time.sleep(2)
    st.snow()
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
