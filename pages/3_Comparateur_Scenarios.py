import streamlit as st
from utils.load_assets import load_model
from utils.preprocessing import build_model_input
from utils.prediction import predict_yield
import pandas as pd

st.set_page_config(page_title="Comparateur Scénarios", page_icon="⚖️", layout="wide")

st.markdown('<h1 style="color: #1a4a38;">⚖️ Comparateur de Scénarios</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #538d6b; font-size: 1.1rem; margin-bottom: 2rem;">Évaluez l’impact d’un changement de pratiques (semences, superficies...) sur le rendement final.</p>', unsafe_allow_html=True)

model = load_model()

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 🌿 Scénario A (Référence)")
    with st.container(border=True):
        cult_a = st.selectbox("Culture A", ["mais", "mil", "sorgho", "riz", "niebe", "arachide"])
        sem_a = st.number_input("Semences A (kg/ha)", 0.0, value=20.0, step=0.5)
        sup_a = st.number_input("Superficie A (ha)", 0.01, value=1.0, step=0.1)

with col_b:
    st.markdown("### 🔬 Scénario B (Alternative)")
    with st.container(border=True):
        cult_b = st.selectbox("Culture B", ["mais", "mil", "sorgho", "riz", "niebe", "arachide"], index=0)
        sem_b = st.number_input("Semences B (kg/ha)", 0.0, value=25.0, step=0.5)
        sup_b = st.number_input("Superficie B (ha)", 0.01, value=1.0, step=0.1)

# Default base inputs for the rest to simplify the UX
base_inputs = {
    "ha_parcelle": 1.2, "crop_share_on_plot": 0.8,
    "manager_age": 35, "manager_sex": "Masculin", "seed_type_name": "locales"
}

if st.button("🚀 Comparer les Résultats", use_container_width=True, type="primary"):
    in_a = base_inputs.copy(); in_a.update({"culture_name": cult_a, "seed_used_per_ha": sem_a, "ha_culture": sup_a})
    in_b = base_inputs.copy(); in_b.update({"culture_name": cult_b, "seed_used_per_ha": sem_b, "ha_culture": sup_b})

    pred_a = predict_yield(model, build_model_input(in_a))
    pred_b = predict_yield(model, build_model_input(in_b))
    
    diff = pred_b - pred_a
    pct_diff = (diff / pred_a) * 100 if pred_a > 0 else 0

    st.markdown("---")
    st.markdown("### 📊 Résultats de la Comparaison")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Rendement Scénario A", f"{pred_a:.3f} t/ha")
    c2.metric("Rendement Scénario B", f"{pred_b:.3f} t/ha")
    
    c3.metric("Bénéfice de l'Alternative", f"{diff:+.3f} t/ha", f"{pct_diff:+.1f}%")
    
    # Progress visualization
    st.markdown("**Comparaison Visuelle**")
    df_chart = pd.DataFrame({"Scénario": ["Scénario A", "Scénario B"], "Rendement": [pred_a, pred_b]})
    st.bar_chart(df_chart.set_index("Scénario"), color=["#8ba89a"])
    
    if diff > 0:
        st.success("✨ L'alternative B semble être un choix plus performant sur le plan agronomique selon le modèle.")
    else:
        st.warning("⚠️ L'alternative B ne montre pas de gain significatif ou est moins performante.")
