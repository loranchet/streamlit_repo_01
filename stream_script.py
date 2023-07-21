import streamlit as st

st.title("Philippe Loranchet et lilian")
st.title("troisieme essai")

# Header styles
st.header("Header")
st.subheader("Subheader")
st.write("Regular text")

# Text styles
st.markdown("# Markdown Heading")
st.markdown("**Bold** text")
st.markdown("*Italic* text")
st.markdown("***Bold and italic*** text")

# Colors and backgrounds
st.success("Success message")
st.info("Info message")
st.warning("Warning message")
st.error("Error message")
st.info("Customized color")

# Fonts and sizes
st.title("Large title")
st.header("Medium header")
st.subheader("Small subheader")
st.write("Default text size")
st.write("<span style='font-size:20px'>Custom font size</span>", unsafe_allow_html=True)

# Code blocks
st.code("print('Hello, World!')", language="python")
st.code("SELECT * FROM table", language="sql")

# Bullets and numbered lists
st.markdown("- Bullet 1\n- Bullet 2\n- Bullet 3")
st.markdown("1. Item 1\n2. Item 2\n3. Item 3")

