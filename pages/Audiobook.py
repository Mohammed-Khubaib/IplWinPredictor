import pyttsx3
import PyPDF2
import os
import streamlit as st
import tempfile

st.title('My AudioBook')
file = st.file_uploader("Pick a file",type="pdf")
if file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(file.read())
        book = open(tmp_file.name, 'rb')

    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.getNumPages()

    speaker = pyttsx3.init()
    s = st.number_input("Starting PageNo.")
    e = st.number_input("ending PageNo.")
    button = st.button('Press to start')
    if button:
        for num in range(s-1, e):
            page = pdfReader.pages[num]
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
