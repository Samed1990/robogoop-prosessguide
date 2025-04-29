import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Godkjenning - Prosessguide for RoboGOOP",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for improved styling
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #5E8BFF;  /* Lighter blue */
        --secondary-color: #F5F7FF;
        --accent-color: #FF8B8B;  /* Lighter red */
        --text-color: #333333;
        --light-gray: #f0f2f6;
        --dark-gray: #565656;
        --success-color: #4CAF50;
    }
    
    /* General styling */
    body {
        color: var(--text-color);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-header {
        color: var(--primary-color);
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--primary-color);
    }
    
    .sub-header {
        color: var(--dark-gray);
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    /* Process header styling */
    .process-header {
        background-color: var(--secondary-color);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid var(--primary-color);
        margin: 1.5rem 0;
        font-weight: 600;
        font-size: 1.3rem;
        color: var(--primary-color);
    }
    
    /* Button styling */
    div.stButton > button {
        font-size: 1.1rem;
        font-weight: 600;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        border: none;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .button-primary {
        background-color: var(--primary-color);
    }
    
    .button-primary:hover {
        background-color: #2a5cd8;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    
    .button-secondary {
        background-color: var(--accent-color);
    }
    
    .button-secondary:hover {
        background-color: #ff5252;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: var(--secondary-color) !important;
        border-radius: 10px !important;
        padding: 1rem 1.2rem !important;
        font-weight: 600 !important;
        color: var(--primary-color) !important;
        border: 2px solid var(--primary-color) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        font-size: 18px !important;
    }

    
    .streamlit-expanderHeader:hover {
        background-color: #e8ecff;
    }
    
    .streamlit-expanderContent {
        border: 1px solid #e0e0e0;
        border-top: none;
        border-radius: 0 0 8px 8px;
        padding: 1.5rem !important;
        background-color: white;
    }
    
    /* List items styling */
    .content-text ul li {
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .content-text {
        font-size: 1.05rem;
        line-height: 1.6;
    }
    
    /* Warning and info boxes */
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #e7f3ff;
        border-left: 5px solid #0d6efd;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e0e0e0;
        text-align: center;
        color: var(--dark-gray);
        font-size: 0.9rem;
    }
    
    /* Image captions */
    .caption {
        text-align: center;
        font-style: italic;
        color: var(--dark-gray);
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Response to hover over expandable sections */
    .st-emotion-cache-ztfqz8:hover {
        transform: translateY(-2px);
        transition: all 0.2s ease;
    }
    </style>
""", unsafe_allow_html=True)

# App Header with custom logo
col_logo, col_title = st.columns([1, 5])
with col_logo:
    # Using the RoboGOOP.png image instead of the emoji
    try:
        from PIL import Image
        import os
        
        # Check if the image exists
        if os.path.exists("RoboGOOP.png"):
            st.image("RoboGOOP.png", width=80)
        else:
            # Fallback to styled div if image doesn't exist
            st.markdown("""
                <div style="text-align: center; padding: 10px;">
                    <div style="background-color: #5E8BFF; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; 
                                justify-content: center; font-size: 24px; margin: 0 auto;">
                        🤖
                    </div>
                </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
            <div style="text-align: center; padding: 10px;">
                <div style="background-color: #5E8BFF; color: white; width: 60px; height: 60px; 
                            border-radius: 50%; display: flex; align-items: center; 
                            justify-content: center; font-size: 24px; margin: 0 auto;">
                    🤖
                </div>
            </div>
        """, unsafe_allow_html=True)

with col_title:
    st.markdown('<h1 class="main-header">Godkjenning - Prosessguide for RoboGOOP</h1>', unsafe_allow_html=True)

# Progress tracker - visual element to show where user is in process
# Making the process circles clickable
# Just header with adjusted container styling
st.markdown("""
    <div style="background-color: #F5F7FF; padding: 15px 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="margin: 0; color: #333;">Velg en prosess nedenfor:</h3>
    </div>
""", unsafe_allow_html=True)


# Process selection buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button {
            background-color: #5E8BFF;  /* Lighter blue */
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button:hover {
            background-color: #4A78F0;
        }
        </style>
    """, unsafe_allow_html=True)
    prosess1 = st.button("📜 Prosess 1: Ekspedering av vedtak ✉️", use_container_width=True)
    
with col2:
    st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button {
            background-color: #FF8B8B;  /* Lighter red */
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button:hover {
            background-color: #FF7575;
        }
        </style>
    """, unsafe_allow_html=True)
    prosess2 = st.button("🔎 Prosess 2: Historikksjekk", use_container_width=True)

# Initialize session state
if "valg" not in st.session_state:
    st.session_state.valg = "1"  # Default

# Update based on user button clicks
if prosess1:
    st.session_state.valg = "1"
if prosess2:
    st.session_state.valg = "2"

valg = st.session_state.valg

# Horizontal line for visual separation
st.markdown("<hr style='margin: 30px 0; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)

if valg == "1":
    st.markdown('<div class="process-header" style="color: #5E8BFF;">📜 Prosess 1: Ekspedering av vedtak ✉️</div>', unsafe_allow_html=True)
    
    # Short description
    st.markdown("""
        <div class="info-box">
            <strong>Om denne prosessen:</strong> Her finner du informasjon om hvordan RoboGOOP håndterer ekspedering av vedtak
            og hvilke begrensninger og utfordringer som kan oppstå.
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Gjenåpnede saker (klager eller retting av tidligere vedtak) og saker som har mer enn et vedtak (feks. utligningstiltak)"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Anbefaling:</strong> Saksbehandlere bør håndtere disse manuelt.</li>
        <li><strong>Hvorfor?</strong> Robot oppdager ikke nyskrevet vedtak hvis det allerede finnes et vedtak i saken fra før.</li>
        <li><strong>Hvordan fungerer det?</strong> Roboten sjekker om "Forhåndsvis vedtak"-knappen eksisterer i eSam. Hvis ja, betyr det at vedtak allerede er generert, og roboten hopper over saken for å unngå dobbeltvedtak.</li>
        <li><strong>Best practice:</strong> Siden gjenåpnede saker utgjør en marginal andel av sakene, er det ryddigst at saksbehandlerne håndterer dem manuelt.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Saker med oppgaver i eSam"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Viktig:</strong> Oppgaver må settes som "fullført" før en sak teknisk sett kan avsluttes i eSam i Steg 4. Robot skal ikke røre de sakene som har åpne oppgaver.</li>
        <li><strong>Anbefaling:</strong> Fordi innholdet og typen oppgaver varierer fra sak til sak, anbefales det at saksbehandler selv markerer oppgaven som fullført.</li>
        <li><strong>Kan roboten gjøre dette?</strong> Ja, den kan trykke på knappen for alle – men den vurderer ikke innholdet. Å avslutte oppgaver uten å kontrollere dem bryter med god saksbehandlingsskikk og vårt forvaltningsansvar.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Dokumenter som ikke ekspederes av roboten"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Dokumenter uten filer i P360:</strong> Robot finner fortsatt saker der det ligger dokumenter uten tilknyttede filer i P360. Disse sakene rapporteres automatisk til superbrukere via "RoboGOOP-nødkontakt" 😊 (gruppechat med superbrukere).</li>
        <li><strong>Ekspedering av e-postdokumenter i P360:</strong> Enkelte dokumenter i P360 må ekspederes manuelt av saksbehandlere fordi de er adressert til bestemte personer eller organisasjoner som sendes via e-post. Typiske eksempler er verifiseringsforespørsler eller annen korrespondanse som er sendt ut fra oss.</li>
        <li><strong>Begrensning:</strong> Siden roboten kun er programmert til å ekspedere dokumenter til Digipost og eSam-portalen, skal den ikke håndtere ekspedering til e-post.</li>
        <li><strong>Løsning:</strong> I slike tilfeller vil roboten rapportere URL-en til dokumentet til superbrukerne, slik at de kan videreformidle informasjonen til riktig saksbehandler for manuell ekspedering.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Typiske problemer med ekspedering og løsninger"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>F-nummer endringer:</strong> Noen søkere får norsk fødselsnummer (F-nummer) mens de venter på at søknaden deres behandles. Robot kan feile ved ekspedering til Digipost hvis oppdatert nummer ikke er registrert.
            <div class="info-box">
            <strong>Løsning:</strong> Ta kontakt med arkivet.
            </div>
        </li>
        <li><strong>Status endres ikke:</strong> Vedtak er "sendt til Sikker post", men status endres ikke til "levert" eller "ekspedert". Det blir stående som "ferdig fra ansvarlig" (altså ferdig fra vår side).
            <div class="info-box">
            <strong>Løsning:</strong> Roboten skal manuelt oppdatere status til "ekspedert". Dette er avklart med arkivet.
            </div>
        </li>
        <li><strong>Feilet ved sending til Sikker post:</strong> I slike situasjoner ekspederes det til eSam-portalen.</li>
        <li><strong>Feilet levert til eSam-portalen:</strong> Dette gjelder noen få saker.
            <div class="info-box">
            <strong>Løsning:</strong> Ta kontakt med nærmeste superbruker og få hjelp fra arkivet.
            </div>
        </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif valg == "2":
    st.markdown('<div class="process-header" style="color: #FF8B8B;">🔎 Prosess 2: Historikksjekk</div>', unsafe_allow_html=True)
    
    # Short description
    st.markdown("""
        <div class="info-box">
            <strong>Om denne prosessen:</strong> Denne seksjonen forklarer hvordan RoboGOOP utfører historikksjekk, 
            erfaringer og justeringer som er gjort basert på tilbakemeldinger fra brukere.
        </div>
    """, unsafe_allow_html=True)

    with st.expander("RoboGOOP sjekker historiske fagsystemer og arkivet"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Systemer som sjekkes:</strong> Robot sjekker historisk eSam, P360, ASTA men ikke aktive eSam/P360.</li>
        <li><strong>Begrunnelse:</strong> Høy risiko for å overse ferske saker. Robot kunne teknisk sett også søkt i nåværende eSam og P360, men det er ingen garanti for at en ny sak fra samme person ikke dukker opp rett etter at roboten har gjort søket.</li>
        <li><strong>Beslutning:</strong> Robot skal ikke implementere søk i aktive systemer foreløpig.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Oppdatert treffsikkerhet – 95 % + forbedringer"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Utfordring:</strong> Noen feil grunnet like fornavn/fødselsdato.</li>
        <li><strong>Forbedring:</strong> Ekstra kontroll på etternavn lagt inn.</li>
        <li><strong>Status:</strong> Små feil kan fortsatt oppdages etter hvert som flere saker behandles.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Løsning: Bedre identifikasjon i historisk eSam"):
        st.markdown("""
        <div class="content-text">
        <ul>
        <li><strong>Forbedring:</strong> Robot kopierer nå etternavn + fornavn + fødselsdato.</li>
        <li><strong>Fordel:</strong> Saksbehandler kan lettere kontrollere om treff er korrekt ved å sammenligne søkerens navn og fødselsdato med treffet fra historisk eSam.</li>
        <li><strong>Viktig:</strong> Hvis mismatch på etternavn, slett denne delen av notatet.</li>
        </ul>
        
        <div class="info-box">
        <strong>Hvorfor ikke søke på etternavn fra starten av?</strong>
        <ul>
        <li>Etternavn er mer sårbart enn fornavn, fordi folk oftere endrer etternavn enn fornavn.</li>
        <li>Hvis vi innfører søk med etternavn, risikerer vi flere falske negative – altså at vi går glipp av treff som faktisk er relevante.</li>
        <li>Målet er å øke sannsynligheten for treff, samtidig som vi gir saksbehandler nok informasjon til å vurdere relevansen selv.</li>
        </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔎 Viktig å være obs på"):
        st.markdown("""
        <div class="content-text">
        <div class="warning-box">
        <ul>
        <li>Når du ser et fyldig notat fra roboten i eSam, betyr det som regel at den har funnet relevante data.</li>
        <li>Men i noen få tilfeller (5 %) kan det være at den har funnet en annen person med samme fornavn og fødselsdato.</li>
        <li>Dobbeltsjekk navn og fødselsdato i alle tilfeller – hvis det ikke stemmer med søkerens opplysninger, kan du slette denne delen av notatet (samme gjelder også resultater fra historisk P360).</li>
        </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("⚠️ Eksempler på rapporterte feil"):
        st.markdown("""
        <div class="content-text">
        <strong>Robotens notat ble ikke ferdigskrevet:</strong>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.image("Screenshot_notat_1.jpg", caption="Eksempel på ufullstendig robotnotat", use_container_width=True)

        st.markdown("""
        <div class="content-text">
        <div class="info-box">
        Jeg mistenker at årsaken er at roboten startet å skrive notatet før eSam-vinduet var ferdig lastet i nettleseren. Dette skjer kun sporadisk, og er derfor litt vanskelig å fange opp. Jeg skal forsøke å justere hastigheten til roboten, slik at den venter litt lenger før den begynner å skrive.
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="content-text">
        <strong>Ufullstendig notat ved ASTA-søk:</strong>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.image("Screenshot_notat_2.jpg", caption="Eksempel på ufullstendig Asta-søk", use_container_width=True)

        st.markdown("""
        <div class="content-text">
        <div class="info-box">
        I enkelte tilfeller har roboten levert et tomt eller mangelfullt notat knyttet til ASTA. Hvis dere ser at det ikke står noe foran ASTA-delen i notatet, betyr det at roboten ikke har klart å gjennomføre søket. Dette skyldes en teknisk begrensning i cache-minnet i nettleseren der ASTA kjører.
        <br><br>
        Mens eSam og P360 håndterer intensiv robotaktivitet godt (opp mot 14–15 timer sammenhengende), er ASTA mer sensitiv. For å løse dette har jeg nå lagt inn en rutine der roboten tømmer cache-minnet hver gang den åpner ASTA. I tillegg vil roboten stoppe hele prosessen hvis den ser at ASTAs hovedside ikke er ferdig lastet. Dette gir oss mulighet til å feilsøke og undersøke problemet nærmere.
        </div>
        </div>
        """, unsafe_allow_html=True)

# Help sidebar with quick tips
with st.sidebar:
    st.markdown("""
    <div style="background-color: #F5F7FF; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="margin: 0 0 10px 0; color: #3772FF;">Hurtigtips 💡</h3>
        <ul style="padding-left: 20px; margin-bottom: 0;">
            <li>Klikk på overskriftene for å utvide/lukke seksjoner</li>
            <li>Bruk prosessknappene øverst for å navigere</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact info
    st.markdown("""
    <div style="background-color: #fff3cd; padding: 15px; border-radius: 10px;">
        <h3 style="margin: 0 0 10px 0; color: #856404;">Kontakt</h3>
        <p style="margin-bottom: 5px;"><strong>RoboGOOP Support:</strong><br>Ta kontakt via Teams</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Versjon 1.1 | © Samad Ismayilov for GOOP divisjonen | HK-dir 2025<br>
    Sist oppdatert: 29. April, 2025
</div>
""", unsafe_allow_html=True)