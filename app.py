import streamlit as st

st.set_page_config(
    page_title="AgriYield Sikasso",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for the whole app
st.markdown("""
<style>
/* Global styling */
[data-testid="stAppViewContainer"] {
    background-color: #f7fcf4;
}
[data-testid="stSidebar"] {
    border-right: 1px solid #e1e9db;
}
[data-testid="stHeader"] {
    background-color: transparent;
}
.css-1d391kg {
    font-family: 'Inter', sans-serif;
}

/* Premium Cards */
div.stCard {
    background: #ffffff;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    border: 1px solid #ebf1e6;
    margin-bottom: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div.stCard:hover {
    transform: translateY(-2px);
    box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.08);
}

/* Typography */
.main-title {
    color: #1a4a38;
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
}
.sub-title {
    color: #538d6b;
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 2rem;
}
.card-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 1rem;
    border-bottom: 2px solid #538d6b;
    padding-bottom: 0.5rem;
    display: inline-block;
}

/* Metrics customization */
[data-testid="stMetricValue"] {
    color: #1a4a38;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>🌾</h1>", unsafe_allow_html=True)
    st.markdown("## AgriYield Sikasso")
    st.markdown("*Outil d’aide à la décision agricole*")
    st.markdown("---")
    st.markdown("**Version Premium** 🚀")
    st.info("Sélectionnez une page ci-dessus pour commencer.")

st.markdown('<div class="main-title">🌾 AgriYield Sikasso</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Intelligence artificielle au service de la prédiction de rendement agricole</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        <div class="stCard">
            <div class="card-title">Bienvenue sur AgriYield</div>
            <p style="font-size: 1.05rem; color: #4a5568; line-height: 1.6;">
            AgriYield est un prototype innovant d'aide à la décision conçu pour l'agriculture malienne. 
            En exploitant les données de l'Enquête Agricole de Conjoncture (EAC) et des algorithmes de <strong>Machine Learning (Random Forest)</strong>, 
            cet outil permet d'estimer avec précision le rendement à l'échelle de la parcelle.
            </p>
            <p style="font-size: 1.05rem; color: #4a5568; line-height: 1.6;">
            Il s'adresse aux <strong>conseillers agricoles, planificateurs, ONG et institutions financières</strong> pour appuyer leurs décisions stratégiques et opérationnelles.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="stCard">
            <div class="card-title">Fonctionnalités</div>
            <ul style="color: #4a5568; line-height: 1.8;">
                <li>📊 <strong>Tableau de Bord :</strong> Vue synthétique des rendements.</li>
                <li>🌱 <strong>Simulateur :</strong> Prédiction personnalisée sur parcelle.</li>
                <li>⚖️ <strong>Comparateur :</strong> Analyse d'impact des pratiques.</li>
                <li>📖 <strong>Méthodologie :</strong> Explication du modèle IA.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
