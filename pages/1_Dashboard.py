import streamlit as st
import pandas as pd
from utils.load_assets import load_reference_stats, load_model_performance
from utils.texts import get_institutional_text

st.set_page_config(page_title="Tableau de Bord", page_icon="📊", layout="wide")

st.markdown('<h1 style="color: #1a4a38;">📊 Tableau de Bord Global</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #538d6b; font-size: 1.1rem; margin-bottom: 2rem;">Vue synthétique historique et métriques de performance du modèle</p>', unsafe_allow_html=True)

reference_stats = load_reference_stats()
model_performance = load_model_performance()

crop_means = reference_stats.get("mean_yield_by_crop", {})
mean_global = reference_stats.get("mean_yield_global", None)

st.markdown("### 🏆 Chiffres Clés")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if mean_global is not None:
        st.metric("Rendement Moyen (Ttes cultures)", f"{mean_global:.2f} t/ha")
with c2:
    maize_yield = crop_means.get('mais', 0)
    st.metric("Rendement Maïs Moyen", f"{maize_yield:.2f} t/ha", delta="Majoritaire")
with c3:
    st.metric("Algorithme Retenu", "Random Forest ✨")
with c4:
    st.metric("Précision (R²)", f"{model_performance['random_forest']['r2'] * 100:.1f}%")

st.markdown("---")

col_chart, col_perf = st.columns([1.5, 1])

with col_chart:
    st.markdown("### 🌾 Rendements Moyens par Culture de Référence")
    crop_df = pd.DataFrame({
        "Culture": [str(c).capitalize() for c in crop_means.keys()],
        "Rendement (t/ha)": list(crop_means.values())
    }).sort_values("Rendement (t/ha)", ascending=True)
    st.bar_chart(crop_df.set_index("Culture"), color="#538d6b")

with col_perf:
    st.markdown("### 🧠 Performance des Modèles")
    perf_df = pd.DataFrame([
        {"Modèle": "Random Forest", "R²": model_performance["random_forest"]["r2"]},
        {"Modèle": "XGBoost", "R²": model_performance["xgboost"]["r2"]},
        {"Modèle": "Régression Linéaire", "R²": model_performance["linear_regression"]["r2"]}
    ])
    st.dataframe(
        perf_df.style.background_gradient(cmap="Greens", subset=["R²"]),
        use_container_width=True,
        hide_index=True
    )
    st.info("Le modèle Random Forest a été retenu pour sa stabilité et sa meilleure capacité de généralisation sur les données EAC.")

with st.expander("Partenaires & Utilisation potentielle"):
    st.markdown(get_institutional_text())
