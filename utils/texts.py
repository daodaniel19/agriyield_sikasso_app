def get_model_limitations():
    return """
    ### Limites du modèle

    Le modèle repose uniquement sur les données EAC disponibles.
    Il n’intègre pas encore :

    - les données climatiques,
    - les données pédologiques,
    - les données détaillées sur les engrais et les pesticides.

    Les résultats doivent donc être interprétés comme un **outil d’aide à la décision**
    et non comme une vérité absolue.
    """


def get_explanation_text():
    return """
    ### Interprétation générale

    Le modèle Random Forest identifie principalement l’influence de :
    - la culture pratiquée,
    - l’intensité de semis,
    - la superficie,
    - certaines caractéristiques simples de l’exploitant.

    Dans ce prototype, l’explication affichée repose sur l’importance globale des variables
    dans le modèle, et non encore sur une explication locale spécifique à chaque parcelle.
    """


def get_institutional_text():
    return """
    Cette application peut être mobilisée comme un prototype d’aide à la décision pour :
    - les services techniques de l’État,
    - les ONG et projets de développement,
    - les institutions de financement agricole,
    - les conseillers agricoles de terrain.
    """