
# Adult Income Prediction using Machine Learning Pipeline

This project develops a complete Machine Learning pipeline to predict income levels based on the Adult Income Census dataset. It includes custom logging, exception handling, and modular deliverables to ensure robust, transparent, and production-ready workflows across all ML stages.

## 📊 Dataset

Becker, B. & Kohavi, R. (1996). [Adult Dataset – UCI Machine Learning Repository](https://doi.org/10.24432/C5XW20)

## 🚀 Features

- **Data Ingestion**: Loads raw data into the pipeline using Pandas.
- **Exploratory Data Analysis (EDA)**: Identifies patterns, distributions, and correlations.
- **Data Transformation**: Applies preprocessing steps for model readiness (encoding, scaling, etc.).
- **Model Training**: Trains models including Random Forest, Decision Tree, and Logistic Regression.
- **Model Evaluation**: Assesses accuracy, precision, recall, and other relevant metrics.
- **Model Deployment**: Serves the model through a Flask API for real-time predictions.
- **Logging & Exception Handling**: Implements custom logging and error handling to support observability and easy debugging.
- **Artifacts & Deliverables**: Stores preprocessed datasets, trained models, and EDA outputs in an `artifacts/` directory for reproducibility.

> This project demonstrates an end-to-end ML workflow from raw data to deployment, emphasizing transparency and maintainability in production.

## 🛠️ Tech Stack

![My Skills](https://simpleskill.icons.workers.dev/svg?i=python,anaconda,jupyter,numpy,scikitlearn,flask)

## ⚙️ Virtual Environment Setup

Install [Anaconda](https://www.anaconda.com/download) to manage project dependencies.

Create a new environment with Python 3.10:

```bash
conda create -p env/ python=3.10
```

Activate the environment:

```bash
conda activate env/
```

You should see the environment path on the terminal, indicating successful activation.

## 📦 Install Dependencies

Clone the project:

```bash
git clone https://github.com/Tryd3x/ml-pipeline.git
```

Navigate into the project directory:

```bash
cd ml-pipeline
```

Activate your conda environment:

```bash
conda activate env/
```

Install all required Python packages:

```bash
pip install -r requirements.txt
```

## ▶️ Start the Flask Server

Launch the Flask app for prediction:

```bash
python app.py
```

## 📬 Inquiries

If you have any questions or feedback, feel free to reach out:  
**📧 htelegraphy@gmail.com**
