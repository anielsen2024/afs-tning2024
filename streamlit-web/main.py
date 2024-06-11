import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import base64

# Funktion til at udtrække en PDF-side som billede med høj opløsning
def get_pdf_page_as_image(pdf_path, page_num, zoom=2):
    pdf_document = fitz.open(pdf_path)
    page = pdf_document.load_page(page_num)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    image_bytes = pix.tobytes(output="png")
    image = Image.open(io.BytesIO(image_bytes))
    return image

# Funktion til at vise PDF-sider for en bestemt opgave
def display_pdf_for_task(pdf_path, start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        image = get_pdf_page_as_image(pdf_path, page_num)
        st.image(image, use_column_width=True)

# Funktion til at finde antal sider i PDF'en
def get_pdf_page_count(pdf_path):
    pdf_document = fitz.open(pdf_path)
    return pdf_document.page_count

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

# Angiv stien til dit baggrundsbillede
background_image_path = "C:/Users/andly/OneDrive/Desktop_Lenovo/Dokumentationsopgave/streamlit-web/bg.png"

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
