import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import io
import base64

# Funktion til at udtrække en PDF-side som billede med høj opløsning
def get_pdf_page_as_image(pdf_path, page_num, dpi=300):
    images = convert_from_path(pdf_path, first_page=page_num, last_page=page_num, dpi=dpi)
    return images[0]

# Funktion til at vise PDF-sider for en bestemt opgave
def display_pdf_for_task(pdf_path, start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        image = get_pdf_page_as_image(pdf_path, page_num)
        st.image(image, use_column_width=True)

# Funktion til at finde antal sider i PDF'en
def get_pdf_page_count(pdf_path):
    images = convert_from_path(pdf_path)
    return len(images)

# Angiv PDF-stien
pdf_path = "C:/Users/andly/OneDrive/Desktop_Lenovo/Dokumentationsopgave/Dokumentationsopgave.pdf"

# Hent antallet af sider i PDF'en
page_count = get_pdf_page_count(pdf_path)

# Definer opgaverne og deres sidetal
tasks = {
    "Forside": (None, None),  # Forside
    "Opgave 1": (0, 1),  # Opgave 1: side 0 til 1
}

# Tilføj opgaver dynamisk for de resterende sider
for i in range(1, page_count - 1):  # Start fra side 2 og fortsæt
    task_name = f"Opgave {i + 1}"
    tasks[task_name] = (i + 1, i + 1)  # Hver opgave efter opgave 1 har én side

# Tilføj en separat download-sektion
tasks["Download PDF"] = (None, None)  # Ingen sider at vise for download

# CSS og sidebar
st.sidebar.title("Navigér til opgave")
selected_task = st.sidebar.selectbox("", list(tasks.keys()))
for i in range(40):
    st.sidebar.write("\n")
st.sidebar.write("© Andreas Lykke Nielsen | Afsætning 2024")

# Visning baseret på valgt opgave
if selected_task == "Forside":
    st.markdown("<div class='header'>Dokumentaionsopgave Afsætning</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Denne applikation præsenterer opgaverne fra PDF'en og giver mulighed for at gennemse dem enkeltvis.</div>", unsafe_allow_html=True)
elif selected_task == "Download PDF":
    st.markdown(f"<div class='subheader'>Vil du læse opgaven?</div>", unsafe_allow_html=True)
    with open(pdf_path, "rb") as file:
        st.download_button(
            label="Download PDF",
            data=file,
            file_name="Dokumentationsopgave.pdf",
            mime="application/pdf"
        )
else:
    start_page, end_page = tasks[selected_task]
    st.markdown(f"<div class='subheader'>{selected_task}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>PDF-visning</div>", unsafe_allow_html=True)
    display_pdf_for_task(pdf_path, start_page, end_page)

    # Prototype til upload af billeder relateret til opgaven (kun på opgavesider)
    st.markdown(f"<div class='description3'>Vælg et billede til visning</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Relevante billede")
