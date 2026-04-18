import numpy as np


def predict_yield(model, input_df):
    """
    Prédit le rendement à partir du modèle entraîné
    """
    prediction = model.predict(input_df)[0]
    return float(prediction)


def compare_to_reference(prediction: float, crop_name: str, reference_stats: dict):
    """
    Compare la prédiction à une moyenne de référence
    """

    mean_global = reference_stats.get("mean_yield_global", np.nan)
    mean_by_crop = reference_stats.get("mean_yield_by_crop", {})

    crop_mean = mean_by_crop.get(crop_name, np.nan)

    # fallback si culture absente
    if np.isnan(crop_mean):
        crop_mean = mean_global

    if prediction > crop_mean:
        level = "supérieur"
        message = f"Le rendement prédit est supérieur à la moyenne pour la culture {crop_name}."
    elif prediction < crop_mean:
        level = "inférieur"
        message = f"Le rendement prédit est inférieur à la moyenne pour la culture {crop_name}."
    else:
        level = "proche"
        message = f"Le rendement prédit est proche de la moyenne pour la culture {crop_name}."

    return {
        "prediction": prediction,
        "crop_mean": crop_mean,
        "global_mean": mean_global,
        "level": level,
        "message": message
    }