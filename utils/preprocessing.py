import numpy as np
import pandas as pd


def build_model_input(user_inputs: dict) -> pd.DataFrame:
    """
    Transforme les données saisies en entrée utilisateur
    en format compatible avec le modèle ML.
    """

    ha_culture = float(user_inputs["ha_culture"])
    ha_parcelle = float(user_inputs["ha_parcelle"])
    seed_used_per_ha = float(user_inputs["seed_used_per_ha"])
    crop_share_on_plot = float(user_inputs["crop_share_on_plot"])
    manager_age = float(user_inputs["manager_age"])
    manager_sex = str(user_inputs["manager_sex"])
    culture_name = str(user_inputs["culture_name"])
    seed_type_name = str(user_inputs["seed_type_name"])

    row = {
        "ha_culture": ha_culture,
        "ha_parcelle": ha_parcelle,
        "seed_used_per_ha": seed_used_per_ha,
        "crop_share_on_plot": crop_share_on_plot,
        "manager_age": manager_age,
        "manager_sex": manager_sex,
        "culture_name": culture_name,
        "seed_type_name": seed_type_name,
        "log_ha_culture": np.log1p(ha_culture),
        "log_seed_used_per_ha": np.log1p(seed_used_per_ha),
        "interaction_surface_semence": ha_culture * seed_used_per_ha,
    }

    return pd.DataFrame([row])