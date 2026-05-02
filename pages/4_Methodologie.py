import streamlit as st
import pandas as pd
from utils.texts import get_explanation_text, get_model_limitations

st.set_page_config(page_title="Méthodologie", layout="wide")

st.markdown('<style>[data-testid="stHeaderActionElements"] {display: none;}</style>', unsafe_allow_html=True)
st.markdown('<h1 style="color: #1a4a38;">Méthodologie et Limites</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #538d6b; font-size: 1.1rem; margin-bottom: 2rem;">Comprendre comment l\'IA raisonne et quelles sont ses contraintes.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown(get_explanation_text())
        st.markdown(get_model_limitations())

with col2:
    with st.container(border=True):
        st.markdown("### Importance des Variables")
        st.markdown("Ce graphique illustre le poids de chaque caractéristique dans la décision finale de l'algorithme :")
        importance_data = pd.DataFrame({
            "Variable": ["Maïs", "Riz", "Intéra. Sem Sup", "Âge Exploitant", "Semence/ha", "Superficie", "Semence Locale"],
            "Importance (%)": [39.4, 12.8, 8.6, 8.6, 6.8, 4.0, 1.2]
        }).sort_values("Importance (%)", ascending=True)
        
        st.bar_chart(importance_data.set_index("Variable"), color="#538d6b")
        st.info("**A noter :** Le type de culture domine fortement, suivi de l'interaction entre les pratiques de semis et la superficie.")

st.markdown("---")
st.caption("Développé dans le cadre d'un projet de recherche et mémoire académique.")
