
import streamlit as st

from chatbot import (
    DEPARTMENTS,
    MENU_OPTIONS,
    get_response,
    get_menu_response
)

# Page settings
st.set_page_config(
    page_title="SJCIT AI College Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10142b, #20204a);
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stChatMessage {
    background-color: #292d50;
    border-radius: 15px;
}

.stButton button {
    border-radius: 12px;
    background-color: #6956e8;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #8170ff;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Website heading
st.title("🎓 SJCIT AI College Chatbot")
st.write("Your smart college information assistant.")

st.markdown("---")

# Department selection
department_names = list(DEPARTMENTS.values())

if "department" not in st.session_state:
    st.session_state.department = department_names[0]

if "messages" not in st.session_state:
    st.session_state.messages = []

selected_department = st.selectbox(
    "Select your department",
    department_names,
    index=department_names.index(st.session_state.department)
)

if selected_department != st.session_state.department:
    st.session_state.department = selected_department
    st.session_state.messages = []
    st.rerun()

st.success(f"Selected Department: {selected_department}")

# Quick information menu
st.subheader("Explore College Information")

menu_labels = list(MENU_OPTIONS.values())

selected_option = st.selectbox(
    "Choose an information topic",
    menu_labels
)

if st.button("Show Information"):
    choice = list(MENU_OPTIONS.keys())[
        menu_labels.index(selected_option)
    ]

    if choice == "7":
        st.info("You can ask your question in the chat box below.")
    else:
        answer = get_menu_response(choice, selected_department)
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

# Display chat history
st.markdown("---")
st.subheader("💬 Chat with the College Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask about fees, exams, courses, placements...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = get_response(question, selected_department)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "[Visit Official SJCIT Website](https://sjcit.ac.in/)"
)
st.caption("SJCIT AI College Chatbot | Student Project")
