import streamlit as st
import os
from PIL import Image
import base64
import streamlit.components.v1 as components
import pandas as pd

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

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
    "--Segmentering og målgruppevalg": ["1.jpg", "11.jpg"],
    "--Marketingmix": ["2.jpg"],
    "--Udbud - Konkurrence": ["3.jpg"],
    "--Service og kundebetjening": ["4.jpg"],
    "--Forretningsforståelse": ["5.jpg"],
    "--Behov og købemotiv": ["6.jpg"],
}

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
    .sources-table {{
        margin: 20px auto;
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }}
    .sources-table th, .sources-table td {{
        color: white;
        padding: 10px;
        border: 1px solid white;
    }}
    .sources-table th {{
        text-align: center;
    }}
    .sources-table td {{
        text-align: center;
    }}
    .expander {{
        background: rgba(0, 0, 0, 0.6);
        color: white;
        margin: 20px 0;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid white;
    }}
    .expander > div[role="button"] {{
        text-align: center;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit sidebar til navigation
st.sidebar.title("Navigér til opgave")
selected_task = st.sidebar.selectbox("", ["Forside"] + list(tasks.keys()) + ["Virtuel Butik", "Download Word"])
for i in range(40):
    st.sidebar.write("\n")
st.sidebar.write("© Andreas Lykke Nielsen | Afsætning 2024")

# Svar til spørgsmål for hver opgave
task_answers = {
    "--Segmentering og målgruppevalg": {
        "Spørgsmål 1": "Beskriv segmenteringsprocessen og dens betydning.",
        "Svar til spørgsmål 1": """
        Segmenteringsprocessen indebærer at opdele markedet i mindre, ensartede grupper, der har fælles karakteristika og behov. 
        Dette er afgørende for at målrette markedsføringen effektivt. Processen omfatter følgende trin:
        1. Identifikation af segmenteringsvariabler (demografiske, geografiske, psykologiske, adfærdsmæssige).
        2. Udvikling af segmenteringsprofiler.
        3. Evaluering af segmenternes attraktivitet.
        4. Valg af målgruppe.
        5. Udvikling af markedsføringsprogrammer for hver målgruppe.
        """,
        "Spørgsmål 2": "Hvordan vælger man den rette målgruppe?",
        "Svar til spørgsmål 2": """
        Valget af den rette målgruppe sker gennem evaluering af de identificerede segmenter baseret på størrelse, vækstpotentiale, konkurrenceintensitet og profitabilitet.
        Det er vigtigt at vælge segmenter, hvor virksomheden har konkurrencemæssige fordele og kan tilbyde en unik værdi.
        """
    },
    "--Marketingmix": {
        "Spørgsmål 1": "Hvad er marketingmix, og hvorfor er det vigtigt?",
        "Svar til spørgsmål 1": """
        Marketingmix består af de 4 P'er: Produkt, Pris, Place (distribution) og Promotion. 
        Det er vigtigt, fordi det giver en ramme for at udvikle effektive marketingstrategier, der kan tiltrække og fastholde kunder.
        """,
        "Spørgsmål 2": "Hvordan kan man bruge de 4 P'er til at skabe en succesfuld marketingstrategi?",
        "Svar til spørgsmål 2": """
        Ved at balancere de 4 P'er kan man skabe en sammenhængende marketingstrategi:
        - Produkt: Sikre høj kvalitet og opfylde kundernes behov.
        - Pris: Fastlægge konkurrencedygtige priser.
        - Place: Vælge de rigtige distributionskanaler for at nå målgruppen.
        - Promotion: Anvende effektive kommunikationsmetoder for at skabe opmærksomhed og interesse.
        """
    },
    "--Udbud - Konkurrence": {
        "Spørgsmål 1": "Hvordan analyserer man konkurrencesituationen på markedet?",
        "Svar til spørgsmål 1": """
        For at analysere konkurrencesituationen kan man anvende Porters Five Forces-model, som vurderer konkurrenceintensiteten baseret på følgende faktorer:
        1. Truslen fra nye indtrængere.
        2. Truslen fra substituerende produkter.
        3. Kundernes forhandlingsstyrke.
        4. Leverandørernes forhandlingsstyrke.
        5. Rivaliseringen blandt eksisterende konkurrenter.
        """,
        "Spørgsmål 2": "Hvad er forskellen mellem direkte og indirekte konkurrenter?",
        "Svar til spørgsmål 2": """
        Direkte konkurrenter tilbyder produkter eller tjenester, der ligner virksomhedens egne og henvender sig til samme målgruppe. 
        Indirekte konkurrenter tilbyder forskellige produkter eller tjenester, der kan opfylde de samme kundebehov på alternative måder.
        """
    },
    "--Service og kundebetjening": {
        "Spørgsmål 1": "Hvad kendetegner god kundeservice?",
        "Svar til spørgsmål 1": """
        God kundeservice kendetegnes ved:
        - Hurtig og effektiv respons på kundernes forespørgsler.
        - Venlig og imødekommende behandling.
        - Personlig tilpasning af service til kundernes behov.
        - Løsning af problemer og håndtering af klager professionelt.
        """,
        "Spørgsmål 2": "Hvordan kan man måle kundetilfredshed?",
        "Svar til spørgsmål 2": """
        Kundetilfredshed kan måles ved hjælp af forskellige metoder som:
        - Spørgeskemaer og feedback-undersøgelser.
        - Net Promoter Score (NPS), der måler kundernes villighed til at anbefale virksomheden.
        - Analyse af kundeklager og deres løsning.
        """
    },
    "--Forretningsforståelse": {
        "Spørgsmål 1": "Hvad er en forretningsmodel, og hvorfor er den vigtig?",
        "Svar til spørgsmål 1": """
        En forretningsmodel beskriver, hvordan en virksomhed skaber, leverer og indfanger værdi. Den er vigtig, fordi den giver en struktureret tilgang til at forstå og udvikle virksomhedens strategi og operationer.
        """,
        "Spørgsmål 2": "Hvad er de vigtigste elementer i en forretningsmodel?",
        "Svar til spørgsmål 2": """
        De vigtigste elementer i en forretningsmodel inkluderer:
        - Værdiforslag: Hvilken værdi tilbyder virksomheden til kunderne.
        - Målgrupper: Hvem er virksomhedens kunder.
        - Kanaler: Hvordan leverer virksomheden værdien til kunderne.
        - Kunderelationer: Hvordan interagerer virksomheden med kunderne.
        - Indtægtsstrømme: Hvordan tjener virksomheden penge.
        - Nøgleaktiviteter: Hvad skal virksomheden gøre for at levere værdien.
        - Nøgleressourcer: Hvilke ressourcer er nødvendige.
        - Nøglepartnere: Hvem hjælper virksomheden.
        - Omkostningsstruktur: Hvad koster det at drive virksomheden.
        """
    },
    "--Behov og købemotiv": {
        "Spørgsmål 1": "Hvad er Maslows behovspyramide, og hvordan relaterer den til forbrugeradfærd?",
        "Svar til spørgsmål 1": """
        Maslows behovspyramide er en teori, der kategoriserer menneskelige behov i en hierarkisk struktur, fra de mest grundlæggende fysiologiske behov til selvrealisering. I marketing er det vigtigt at forstå, hvor på pyramiden virksomhedens produkter eller tjenester adresserer kundernes behov.
        """,
        "Spørgsmål 2": "Hvordan påvirker købemotiver forbrugerens beslutningsproces?",
        "Svar til spørgsmål 2": """
        Købemotiver, såsom behov for sikkerhed, social accept eller selvrealisering, påvirker forbrugerens beslutningsproces ved at bestemme, hvilke produkter eller tjenester der opfylder disse behov bedst. Markedsførere skal identificere og målrette disse motiver for at påvirke købsadfærden.
        """
    },
}

# Visning baseret på valgt opgave
if selected_task == "Forside":
    st.markdown("<div class='header'>Eksamensopgave i Afsætning</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Denne applikation præsenterer opgaverne fra Word-filen og giver mulighed for at gennemse dem enkeltvis.</div>", unsafe_allow_html=True)
elif selected_task == "Virtuel Butik":
    st.markdown("<div class='subheader'>Virtuel Butik</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>Interaktiv visning af den virtuelle butik</div>", unsafe_allow_html=True)
    components.iframe("https://my.matterport.com/show/?m=vq47Jte1ucv", height=600)
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
else:
    task_images = tasks[selected_task]
    st.markdown(f"<div class='task-header'>{selected_task.strip('--')}</div>", unsafe_allow_html=True)
    display_images_for_task(image_folder, task_images)
    
    # Ekspandere for spørgsmål og svar
    task_answer = task_answers[selected_task]
    for i, (question, answer) in enumerate(task_answer.items(), 1):
        if i % 2 != 0:
            with st.expander(f"Spørgsmål {i//2 + 1} til {selected_task.strip('--')}"):
                st.markdown(question)
        else:
            with st.expander(f"Svar til spørgsmål {i//2}"):
                st.markdown(answer)
    
    # Kilder sektion per opgave
    sources = {
        "Segmentering og målgruppevalg": [
            {"kilde": "Afsætning C, Systime, kapitel 7, side 273", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 7, side 274", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 7, side 275", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 7, side 276", "link": "https://afs-fc-eudeux.systime.dk/"}
        ],
        "Marketingmix": [
            {"kilde": "Afsætning C, Systime, kapitel 10, side 226", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 10, side 228", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Meny's hjemmeside", "link": "https://meny.dk"}
        ],
        "Udbud - Konkurrence": [
            {"kilde": "Afsætning C, Systime, kapitel 9, side 251", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 8, side 238", "link": "https://afs-fc-eudeux.systime.dk/"}
        ],
        "Service og kundebetjening": [
            {"kilde": "Afsætning C, Systime, kapitel 14, side 170", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 14, side 172", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 14, side 148", "link": "https://afs-fc-eudeux.systime.dk/"}
        ],
        "Forretningsforståelse": [
            {"kilde": "Afsætning C, Systime, kapitel 1, side 133", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 2, side 260", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 3, side 268", "link": "https://afs-fc-eudeux.systime.dk/"}
        ],
        "Behov og købemotiv": [
            {"kilde": "Afsætning C, Systime, kapitel 8, side 243", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 8, side 245", "link": "https://afs-fc-eudeux.systime.dk/"},
            {"kilde": "Afsætning C, Systime, kapitel 8, side 246", "link": "https://afs-fc-eudeux.systime.dk/"}
        ],
    }

    if selected_task.strip('--') in sources:
        with st.expander(f":notebook: Kilder til {selected_task.strip('--')} :notebook:", expanded=False):
            sources_for_task = sources[selected_task.strip('--')]
            df_sources = pd.DataFrame(sources_for_task)
            # Create a markdown table with clickable links
            table_markdown = "| Kilde | Link |\n|:------|:-----|\n"
            for _, row in df_sources.iterrows():
                table_markdown += f"| {row['kilde']} | [Læs mere]({row['link']}) |\n"
            st.markdown(table_markdown)

    # Vis Word-dokumentet
    with st.expander(f"Vis Word-dokumentet"):
        word_path = "streamlit-web/Opgave.docx"
        with open(word_path, "rb") as file:
            st.download_button(
                label="Download Word",
                data=file,
                file_name="Opgave.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
