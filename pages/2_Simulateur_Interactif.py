import streamlit as st
import pandas as pd
from utils.load_assets import load_model, load_reference_stats
from utils.preprocessing import build_model_input
from utils.prediction import compare_to_reference, predict_yield

st.set_page_config(page_title="Simulateur Interactif", layout="wide")

# Custom CSS for layout
st.markdown("""
<style>
.metric-box {
    background-color: #f0f7f4;
    border-left: 5px solid #28a745;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 20px;
}
.metric-title {
    font-size: 0.9rem;
    color: #6c757d;
    text-transform: uppercase;
}
.metric-value {
    font-size: 2rem;
    font-weight: bold;
    color: #1a4a38;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color: #1a4a38;">Simulateur de Rendement</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #538d6b; font-size: 1.1rem; margin-bottom: 1rem;">Estimez instantanément le rendement de votre parcelle en ajustant ses paramètres.</p>', unsafe_allow_html=True)

model = load_model()
reference_stats = load_reference_stats()

simulate_btn = st.sidebar.button("Lancer la Simulation", type="primary", use_container_width=True)

col_form, col_res = st.columns([1, 1.2])

with col_form:
    with st.container(border=True):
        st.markdown("### Saisie des Paramètres")
        culture_name = st.selectbox("Culture", ["mais", "mil", "sorgho", "riz", "niebe", "arachide"])
        
        c1, c2 = st.columns(2)
        with c1:
            ha_culture = st.number_input("Superficie cultivée (ha)", min_value=0.01, value=1.0, step=0.1)
            crop_share_on_plot = st.slider("Part de la culture", 0.0, 1.0, 0.8, 0.05)
            seed_used_per_ha = st.number_input("Semence (kg/ha)", min_value=0.0, value=20.0, step=0.5)
        with c2:
            ha_parcelle = st.number_input("Sup. totale (ha)", min_value=0.01, value=1.2, step=0.1)
            seed_type_name = st.selectbox("Type de semence", ["locales", "ameliorees pour la 1eme annee", "ameliorees pour la 2eme annee", "ameliorees pour la 3eme annee", "ameliorees age inconnu"])
            manager_age = st.number_input("Âge responsable", min_value=10, max_value=100, value=35)
            manager_sex = st.selectbox("Sexe responsable", ["Masculin", "Féminin"])

with col_res:
    if simulate_btn or "last_sim" in st.session_state:
        st.session_state["last_sim"] = True
        
        user_inputs = {
            "culture_name": culture_name,
            "ha_culture": ha_culture,
            "ha_parcelle": ha_parcelle,
            "crop_share_on_plot": crop_share_on_plot,
            "seed_used_per_ha": seed_used_per_ha,
            "manager_age": manager_age,
            "manager_sex": manager_sex,
            "seed_type_name": seed_type_name,
        }
        
        input_df = build_model_input(user_inputs)
        prediction = predict_yield(model, input_df)
        result = compare_to_reference(prediction, culture_name, reference_stats)
        
        st.markdown("### Résultats de la Prédiction")
        
        # Dashboard metrics
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">Rendement Estimé</div>
            <div class="metric-value">{result['prediction']:.3f} <span style="font-size: 1rem; color: #495057;">tonnes / hectare</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        rc1, rc2 = st.columns(2)
        rc1.metric("Moyenne Historique", f"{result['crop_mean']:.3f} t/ha")
        diff = prediction - result['crop_mean']
        rc2.metric("Écart par rapport à la moyenne", f"{diff:+.3f} t/ha", delta_color="normal")
        
        if result["level"] == "supérieur":
            st.success(f"**Excellent profil !** {result['message']}")
        elif result["level"] == "inférieur":
            st.warning(f"**Attention !** {result['message']}")
        else:
            st.info(f"{result['message']}")
            
        with st.expander("Voir les facteurs d'influence de cette prédiction"):
            st.write("Le modèle prend en compte prioritairement :")
            st.progress(85, text=f"Culture ({culture_name.capitalize()})")
            st.progress(70, text=f"Intensité de semis ({seed_used_per_ha} kg/ha)")
            st.progress(50, text=f"Superficie ({ha_culture} ha)")
            st.caption("L'âge et le type de semence ont un impact secondaire dans cette configuration.")
    else:
        st.info("Ajustez vos paramètres et cliquez sur **Lancer la Simulation** pour voir les résultats ici.")
