
# Adult Income Prediction using Mac7hine Learning Pipeline

This project aims to develop a Machine Learning pipeline to predict income levels based on the Adult Income Census dataset. The pipeline includes various components such as a custom logging system, custom exception handling and deliverables ensuring robust and transparent operation throughout the ML workflow.





## Dataset

Becker, B. & Kohavi, R. (1996). Adult [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.


## Features

- **Data Ingestion**: Collecting and loading the dataset for processing.
- **Exploratory Data Analysis (EDA)**: Analyzing the dataset to identify patterns, distributions, and correlations.
- **Data Transformation**: Preprocessing and transforming the data for model readiness.
- **Model Training**: Training various models to predict income levels.
- **Model Evaluation**: Evaluating model performance using appropriate metrics.
- **Model Deployment**: Deploying the model to a Flask server for making predictions on new data.
- **Logger and Exception Handler**: Custom logging and exception handling mechanisms are integrated to provide transparency, easy debugging, and robust error management across the pipeline.
- **Artifacts/Deliverables**: All key artifacts such as preprocessed data transformations, trained models, and important EDA insights are saved and versioned in the artifacts/ directory for reproducibility and further analysis.
The project demonstrates end-to-end model development and deployment while leveraging custom logging and error handling for a production-ready solution.


## Tech Stack
![My Skills](https://simpleskill.icons.workers.dev/svg?i=python,anaconda,jupyter,numpy,scikitlearn,flask)
## Virtual Environment Setup

Install [Anaconda](https://www.anaconda.com/download) to manage project dependencies.

Open Anaconda Terminal, create a new envrionment with python 3.10 installed.

```bash
conda create -p env/ python=3.10
```

Navigate to folder where *env* is located. Activate conda envrionment.
```bash
conda activate env/
```

You should see the path of the enviroment on the leftmost hand side, indicating successfull activation.
    
## Install Dependencies

Clone the [project](https://github.com/Tryd3x/ml-pipeline.git)

```bash
  git clone https://github.com/Tryd3x/ml-pipeline.git
```

Go to the project directory

```bash
  cd ml-pipeline
```

Activate conda environment

```bash
conda activate env/
```

Install dependencies using pip

```bash
  pip install -r "requirements.txt"
```

Start the Flask server

```bash
  python app.py
```


## Inquiries

If you have any feedback, please reach out to us at htelegraphy@gmail.com

