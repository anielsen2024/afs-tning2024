import streamlit as st
from docx import Document
from PIL import Image
import io
import base64
import os
import streamlit.components.v1 as components

# Funktion til at læse og vise indholdet fra en Word-fil
def display_word_content(word_path, start_para, end_para):
    doc = Document(word_path)
    for para_num in range(start_para, end_para + 1):
        if para_num < len(doc.paragraphs):
            st.write(doc.paragraphs[para_num].text)

# Funktion til at finde antal paragraffer i Word-filen
def get_word_para_count(word_path):
    doc = Document(word_path)
    return len(doc.paragraphs)

# Angiv Word-filens sti
word_path = "streamlit-web/opgave.docx"

# Hent antallet af paragraffer i Word-filen
para_count = get_word_para_count(word_path)

# Definer opgaverne og deres paragraffer
tasks = {
    "Forside": (0, 0),  # Forside
    "Opgave 1": (1, 10),  # Opgave 1: paragraf 1 til 10
}

# Tilføj opgaver dynamisk for de resterende paragraffer
for i in range(10, para_count, 10):  # Tilføj opgaver dynamisk for hver 10 paragraffer
    task_name = f"Opgave {i // 10 + 1}"
    tasks[task_name] = (i, min(i + 9, para_count - 1))

# Tilføj en separat download-sektion
tasks["Download Word"] = (None, None)  # Ingen paragraffer at vise for download

# Tilføj "Virtuel Butik" til navigationen
tasks["Virtuel Butik"] = (None, None)

# Angiv stien til dit baggrundsbillede
background_image_path = "streamlit-web/bg.png"

# Læs baggrundsbilledet og konverter det til base64
with open(background_image_path, "rb") as image_file:
    background_image_bytes = image_file.read()
    background_image_base64 = base64.b64encode(background_image_bytes).decode()

# CSS til at style forsiden med baggrundsbillede og forbedret tekstlæselighed
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url('data:image/jpg;base64,{background_image_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .header {{
        text-align: center;
        color: white;
        font-size: 50px;
        font-weight: bold;
        margin-top: 20%;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
    }}
    .subheader {{
        text-align: left;
        color: white;
        font-size: 30px;
        font-weight: bold;
        margin-top: 10%;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
    }}
    .description {{
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: normal;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-radius: 10px;
    }}
    .description2 {{
        text-align: left;
        color: white;
        font-size: 18px;
        font-weight: normal;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.8);
        padding: 15px;
        border-radius: 0px;
    }}
    .description3 {{
        text-align: center;
        color: white;
        font-size: 18px;
        font-weight: normal;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.7);
        padding: 5px;
        border-radius: 0px;
    }}
    .blurred {{
        filter: blur(5px);
    }}
    .task-header {{
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit sidebar til navigation
st.sidebar.title("Navigér til opgave")
selected_task = st.sidebar.selectbox("", list(tasks.keys()))
for i in range(40):
    st.sidebar.write("\n")
st.sidebar.write("© Andreas Lykke Nielsen | Afsætning 2024")

# Visning baseret på valgt opgave
if selected_task == "Forside":
    st.markdown("<div class='header'>Dokumentationsopgave i Afsætning</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Denne applikation præsenterer opgaverne fra Word-filen og giver mulighed for at gennemse dem enkeltvis.</div>", unsafe_allow_html=True)
elif selected_task == "Download Word":
    st.markdown(f"<div class='subheader'>Vil du læse opgaven?</div>", unsafe_allow_html=True)
    with open(word_path, "rb") as file:
        st.download_button(
            label="Download Word",
            data=file,
            file_name="Dokumentationsopgave.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
elif selected_task == "Virtuel Butik":
    st.markdown("<div class='subheader'>Virtuel Butik</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>Interaktiv visning af den virtuelle butik</div>", unsafe_allow_html=True)
    components.iframe("https://my.matterport.com/show/?m=vq47Jte1ucv", height=600)
else:
    start_para, end_para = tasks[selected_task]
    st.markdown(f"<div class='subheader'>{selected_task}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>Word-indhold</div>", unsafe_allow_html=True)
    display_word_content(word_path, start_para, end_para)

    # Prototype til upload af billeder relateret til opgaven (kun på opgavesider)
    st.markdown(f"<div class='description3'>Vælg et billede til visning</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        image_path = f"streamlit-web/uploads/{uploaded_file.name}"
        image.save(image_path)
        st.image(image, caption="Relevant billede")

        # Gem filstien til det uploadede billede
        if "uploaded_images" not in st.session_state:
            st.session_state["uploaded_images"] = []
        st.session_state["uploaded_images"].append(image_path)

    # Vis tidligere uploadede billeder
    if "uploaded_images" in st.session_state:
        for image_path in st.session_state["uploaded_images"]:
            image = Image.open(image_path)
            st.image(image, caption="Tidligere uploadet billede")

