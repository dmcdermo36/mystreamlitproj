import time
import numpy as np
import pandas as pd
import streamlit as st


# streamlit run my_streamlit_app.py --server.runOnSave true
st.title("Title goes here!")

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""
import streamlit as st
# Or use "with" notation:



st.sidebar.write("This is a sidebar")
st.sidebar.radio("Select one:", [1, 2, 3, 4, 5])

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
tab2.radio("Select one:", [1, 2, 3, 4, 5, 6 , 7])


col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F", help="Mean temperature")
col2.metric("Wind", "9 mph", "-8%")
col4.metric("Humidity", "86%", "4%")
button_reference = st.button("st button")
# print('butt ref: ', button_reference)
# st.download_button("Download", "hello", "Click here")
# st.page_layout("wide")
# st.page_link("some Page link")
st.checkbox("check box")
a_toggle = st.toggle("Enable")
print('a_toggle: ', a_toggle)
st.radio("RADIO", ["a", "b", "c"])
st.selectbox("SELECT", ["a", "b", "c"])
st.multiselect("MULTI", ["a", "b", "c"])
st.slider("SLIDER", 0, 100, 50)
st.select_slider("SELECT SLIDER", ["a", "b", "c"])
st.text_input("TEXT INPUT")
st.number_input("NUMBER INPUT")
st.text_area("TEXT AREA")
st.date_input("DATE INPUT")
st.time_input("TIME INPUT")
st.file_uploader("FILE UPLOADER")


code = '''def testfunc():
    print("testing Streamlit!")'''
st.code(code, language="python")

st.latex(r"e^{i\pi} + 1 = 0")


# Embed custom JavaScript to run in the browser
st.components.v1.html(
    """
    <script>
    document.getElementById('myButton').onclick = function() {
        alert('This is running on the client side!');
    };
    </script>
    <button id="myButton">Click Meeee</button>
    """,
    height=100,
)


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)