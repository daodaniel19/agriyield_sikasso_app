from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "best_model_rf.joblib"
FEATURES_PATH = ARTIFACTS_DIR / "model_features.joblib"
REFERENCE_PATH = ARTIFACTS_DIR / "reference_stats.joblib"
PERFORMANCE_PATH = ARTIFACTS_DIR / "model_performance.joblib"


def load_model():
    return joblib.load(MODEL_PATH)


def load_features():
    return joblib.load(FEATURES_PATH)


def load_reference_stats():
    return joblib.load(REFERENCE_PATH)


def load_model_performance():
    return joblib.load(PERFORMANCE_PATH)