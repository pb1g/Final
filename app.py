# from pydub import AudioSegment
import model
import streamlit as st


st.title('New Post')

option = st.selectbox(
    'Select the Media type',
    ('Choose', 'Text', 'Sound File', 'Voice'))

if option == 'Text':
    pred = st.text_area('Text Area', height=70, max_chars=1000, help='Text area to enter the text',
                        placeholder='Enter the text')
    col1, col2 = st.columns(2)
    with col1:
        a = st.button("Detect", key='ab', help='Click to check', disabled=False)
    with col2:
        b = st.button("Post", key='bb', help='Click to Post')
    col3, col4 = st.columns(2)
    de = model.detect([pred])
    if a:
        st.markdown(de[0])
    if b:
        if de[0] == "Offensive Language Detected":
            st.write("Offensive Language Detected. Change the post and retry.")
        else:
            st.write("Posted Successfully.")

if option == 'Sound File':
    fileObject = st.file_uploader(label="Please upload your file")
    if fileObject:
        col5, col6, col7 = st.columns(3)
        with col5:
            d = st.button("Preview", help="Click to preview")
        with col6:
            e = st.button("Detect")
        with col7:
            f = st.button("Post")
        fg = model.detect([model.voice_file(fileObject.name)])
        if d:
            audio_file = open(fileObject.name, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
        if e:
            st.write(fg[0])

        if f:
            if fg[0] == "Offensive Language Detected":
                st.write("Offensive Language Detected. Change the post and retry.")
            else:
                st.write("Posted Successfully.")
