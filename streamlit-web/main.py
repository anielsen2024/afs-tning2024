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
    "Segmentering og målgruppevalg": ["1.jpg", "11.jpg"],
    "Marketingmix": ["2.jpg"],
    "Udbud - Konkurrence": ["3.jpg"],
    "Service og kundebetjening": ["4.jpg"],
    "Forretningsforståelse": ["5.jpg"],
    "Behov og købemotiv": ["6.jpg"],
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
selected_task = st.sidebar.selectbox("", ["Forside"] + list(tasks.keys()) + ["Virtuel Butik"])

for i in range(40):
    st.sidebar.write("\n")
st.sidebar.write("© Andreas Lykke Nielsen | Afsætning 2024")

# Visning baseret på valgt opgave
if selected_task == "Forside":
    st.markdown("<div class='header'>Eksamensopgave i Afsætning</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Denne applikation præsenterer opgaverne fra Word-filen og giver mulighed for at gennemse dem enkeltvis.</div>", unsafe_allow_html=True)
elif selected_task == "Virtuel Butik":
    st.markdown("<div class='subheader'>Virtuel Butik</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description2'>Interaktiv visning af den virtuelle butik</div>", unsafe_allow_html=True)
    components.iframe("https://my.matterport.com/show/?m=vq47Jte1ucv", height=600)
else:
    task_images = tasks[selected_task]
    st.markdown(f"<div class='task-header'>{selected_task}</div>", unsafe_allow_html=True)
    display_images_for_task(image_folder, task_images)
    
    # Ekspandere for spørgsmål og svar
    if selected_task == "Segmentering og målgruppevalg":
        with st.expander("Spørgsmål 1: Segmenteringsprocessen"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Redegør for segmenteringsprocessens 4 trin og hvorfor det er vigtigt at segmentere markedet.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Segmenteringsprocessen"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Segmenteringsprocessen indebærer at opdele markedet i mindre, ensartede grupper, der har fælles karakteristika og behov. Dette er afgørende for at målrette markedsføringen effektivt. Processen omfatter følgende trin:</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>1. Identifikation af segmenteringsvariabler (demografiske, geografiske, psykologiske, adfærdsmæssige).</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>2. Udvikling af segmenteringsprofiler.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>3. Evaluering af segmenternes attraktivitet.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>4. Valg af målgruppe.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>5. Udvikling af markedsføringsprogrammer for hver målgruppe.</div>", unsafe_allow_html=True)
        with st.expander("Spørgsmål 2: Valg af målgruppe"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Vurder også hvilke segmenteringskriterier der vil være relevante for Meny, at segmentere efter, og begrund hvorfor.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 2: Valg af målgruppe"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Valget af den rette målgruppe sker gennem evaluering af de identificerede segmenter baseret på størrelse, vækstpotentiale, konkurrenceintensitet og profitabilitet. Det er vigtigt at vælge segmenter, hvor virksomheden har konkurrencemæssige fordele og kan tilbyde en unik værdi.</div>", unsafe_allow_html=True)
    
    elif selected_task == "Marketingmix":
        with st.expander("Spørgsmål 1: Marketingmix"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Beskriv de 4 P’er i marketingmixet for Meny.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Marketingmix"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Marketingmixet består af 4 P'er: Produkt, Pris, Place (Distribution) og Promotion.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>1. Produkt: Meny tilbyder et bredt sortiment af dagligvarer.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>2. Pris: Meny anvender en konkurrencedygtig prissætning.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>3. Place: Meny er strategisk placeret i byer og større samfund.</div>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>4. Promotion: Meny bruger forskellige promotionsaktiviteter, herunder reklamer og tilbudsaviser.</div>", unsafe_allow_html=True)
    
    elif selected_task == "Udbud - Konkurrence":
        with st.expander("Spørgsmål 1: Konkurrence"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Analyser konkurrencen på dagligvaremarkedet og Menys position i markedet.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Konkurrence"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Konkurrencen på dagligvaremarkedet er intens med flere store aktører som Coop, Salling Group og Lidl. Meny positionerer sig som en kvalitetsbutik med et bredt udvalg af varer og god kundeservice.</div>", unsafe_allow_html=True)
    
    elif selected_task == "Service og kundebetjening":
        with st.expander("Spørgsmål 1: Kundeservice"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Beskriv Menys kundeservice og hvordan den kan forbedres.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Kundeservice"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Meny tilbyder en høj grad af kundeservice gennem veluddannede medarbejdere, personligt engagement og fokus på kundetilfredshed. Forbedringer kan omfatte udvidede åbningstider, flere selvbetjeningskasser og en forbedret online kundeservice.</div>", unsafe_allow_html=True)
    
    elif selected_task == "Forretningsforståelse":
        with st.expander("Spørgsmål 1: Forretningsmodel"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Redegør for Menys forretningsmodel.</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Forretningsmodel"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Menys forretningsmodel bygger på at levere kvalitetsdagligvarer gennem et bredt sortiment, konkurrencedygtige priser og høj kundeservice. De fokuserer på at skabe en god indkøbsoplevelse og opbygge langvarige kunderelationer.</div>", unsafe_allow_html=True)
    
    elif selected_task == "Behov og købemotiv":
        with st.expander("Spørgsmål 1: Købemotiver"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Hvad motiverer forbrugerne til at handle hos Meny?</div>", unsafe_allow_html=True)
        with st.expander("Svar til spørgsmål 1: Købemotiver"):
            st.markdown("<div style='background-color: black; color: white; padding: 10px;'>Forbrugerne motiveres til at handle hos Meny på grund af den høje kvalitet af produkter, et bredt sortiment, konkurrencedygtige priser og en god kundeservice. Meny's fokus på at skabe en behagelig indkøbsoplevelse og deres lokale tilstedeværelse spiller også en væsentlig rolle.</div>", unsafe_allow_html=True)

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

    if selected_task in sources:
        with st.expander(f":notebook: Kilder til {selected_task} :notebook:", expanded=False):
            sources_for_task = sources[selected_task]
            df_sources = pd.DataFrame(sources_for_task)
            # Create a markdown table with clickable links
            table_markdown = "| Kilde | Link |\n|:------|:-----|\n"
            for _, row in df_sources.iterrows():
                table_markdown += f"| {row['kilde']} | [Læs mere]({row['link']}) |\n"
            st.markdown(table_markdown)

    # Vis Word-dokumentet i en expander
    word_path = "streamlit-web/Opgave.docx"
    with st.expander("Vis Word-dokumentet"):
        with open(word_path, "rb") as file:
            st.download_button(
                label="Download Word",
                data=file,
                file_name="Opgave.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
