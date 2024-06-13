import streamlit as st
import os
from PIL import Image
import base64
import streamlit.components.v1 as components

# Angiv stien til billederne
image_folder = "streamlit-web/png"

# Funktion til at vise billeder for en bestemt opgave
def display_images_for_task(image_folder, task_images):
    for image_file in task_images:
        image_path = os.path.join(image_folder, image_file)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
        else:
            st.error(f"Billedet {image_file} blev ikke fundet.")

# Definer opgaverne og deres billeder
tasks = {
    "Forside": [],
    "Opgave 1: Segmentering og målgruppevalg": ["1.jpg", "11.jpg"],
    "Opgave 2: Marketingmix": ["2.jpg"],
    "Opgave 3: Udbud - Konkurrence": ["3.jpg"],
    "Opgave 4: Service og kundebetjening": ["4.jpg"],
    "Opgave 5: Forretningsforståelse": ["5.jpg"],
    "Opgave 6: Behov og købemotiv": ["6.jpg"],
}

# Tilføj en separat download-sektion
tasks["Download Word"] = None

# Tilføj "Virtuel Butik" til navigationen
tasks["Virtuel Butik"] = None

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
        text-align: center;
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
        text-align: left;
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
        color: white;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .sources-table {{
        align: center;
        margin-top: 20px;
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
    }}
    .sources-table th, .sources-table td {{
        color: white;
        padding: 10px;
        border: 1px solid white;
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
    st.markdown("<div class='header'>Eksamensopgave i Afsætning</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Denne applikation præsenterer opgaverne fra Word-filen og giver mulighed for at gennemse dem enkeltvis.</div>", unsafe_allow_html=True)
elif selected_task == "Download Word":
    st.markdown(f"<div class='subheader'>Vil du læse opgaven?</div>", unsafe_allow_html=True)
    word_path = "streamlit-web/Opgave.docx"
    with open(word_path, "rb") as file:
        st.download_button(
            label="Download Word",
            data=file,
            file_name="Opgave.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
elif selected_task == "Virtuel Butik":
    st.markdown("<div class='subheader'>Virtuel Butik</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>Interaktiv visning af den virtuelle butik</div>", unsafe_allow_html=True)
    components.iframe("https://my.matterport.com/show/?m=vq47Jte1ucv", height=600)
else:
    task_images = tasks[selected_task]
    st.markdown(f"<div class='task-header'>{selected_task}</div>", unsafe_allow_html=True)
    display_images_for_task(image_folder, task_images)

# Kilder sektion
st.markdown("<div class='description'>Kilder</div>", unsafe_allow_html=True)
st.markdown(
    """
    <table class="sources-table">
        <tr>
            <th>Kilde</th>
            <th>Link</th>
        </tr>
        <tr>
            <td>Afsætning C, Systime</td>
            <td><a href="https://www.systime.dk/da/afs%C3%A6tning-c-9788757140123" style="color: white;">Læs mere</a></td>
        </tr>
        <tr>
            <td>Meny's hjemmeside</td>
            <td><a href="https://meny.dk" style="color: white;">Besøg siden</a></td>
        </tr>
        <tr>
            <td>Virtuel Butik</td>
            <td><a href="https://my.matterport.com/show/?m=vq47Jte1ucv" style="color: white;">Se butikken</a></td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)
