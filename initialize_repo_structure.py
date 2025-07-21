# initialize_repo_structure.py

import os

# Root project folder (run from the root of your repo)
PROJECT_NAME = "clinical-trials-multimodal-pipeline"

# Folder structure based on functionality
folders = [
    f"{PROJECT_NAME}/src/data_processing",
    f"{PROJECT_NAME}/src/fingerprinting",
    f"{PROJECT_NAME}/src/embeddings",
    f"{PROJECT_NAME}/src/multimodal",
    f"{PROJECT_NAME}/src/utils",
    f"{PROJECT_NAME}/data/raw",
    f"{PROJECT_NAME}/data/processed",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/tests"
]

# Boilerplate files
boilerplate_files = {
    f"{PROJECT_NAME}/requirements.txt": """pandas
numpy
scikit-learn
torch
transformers
rdkit-pypi
tqdm
requests""",

    f"{PROJECT_NAME}/.gitignore": """__pycache__/
*.pyc
*.pkl
*.joblib
*.ipynb_checkpoints
data/raw/*
data/processed/*
""",

    f"{PROJECT_NAME}/README.md": f"""# Clinical Trials Multimodal Pipeline

This repository contains a modular and multimodal machine learning pipeline for clinical trial data analysis, integrated with BERT-based text embeddings, structured data, and molecular fingerprints.

## 🔁 Execution Order

1. `src/data_processing/data_collection.py`
2. `src/data_processing/data_preprocessing.py`
3. `src/embeddings/text_encoder.py`
4. `src/multimodal/structured_features.py`
5. `src/multimodal/feature_fusion.py`
6. `src/multimodal/model_training.py`
7. `src/multimodal/model_evaluation.py`
8. `src/multimodal/shap_analysis.py`
9. `src/multimodal/model_export.py`
10. `src/multimodal/model_predict_demo.py`

## 📂 Directory Structure

- `src/data_processing/` - Raw collection and clinical data cleaning
- `src/fingerprinting/` - Drug fingerprint generation from SMILES
- `src/embeddings/` - Textual BERT-based encodings
- `src/multimodal/` - Feature fusion, training & evaluation
- `src/utils/` - Reusable helpers and text utilities
- `data/` - Local data store (`raw` and `processed`)
- `notebooks/` - Colab or Jupyter workflows
- `tests/` - Unit tests for components
""",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create placeholder files
for filepath, content in boilerplate_files.items():
    with open(filepath, "w") as f:
        f.write(content)

print(f"✅ Project structure for '{PROJECT_NAME}' created.")
