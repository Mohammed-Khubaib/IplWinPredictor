import pyttsx3
import PyPDF2
import os
import streamlit as st
st.title('My AudioBook')
file = st.file_uploader("Pick a file",type="pdf")
book = open(file, 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()
s = st.number_input("Starting PageNo.")
e = st.number_input("ending PageNo.")
button = st.button('Press to start')
if button:
    for num in range(s, e):
        page = pdfReader.pages[num]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()