# Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions. This project includes Exploratory Data Analysis (EDA), data preprocessing, model training, evaluation, and a Streamlit-based web application for real-time predictions.

## Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── data/                  # Raw and processed datasets (ignored by git)
├── notebooks/             # Jupyter notebooks for analysis and modeling
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Model_Evaluation.ipynb
│
├── app/                   # Streamlit web application
│   └── streamlit_app.py
│
├── models/                # Trained machine learning model artifacts
│   └── best_model.pkl
│
├── images/                # Visualizations and screenshots
├── README.md              # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore configuration
```

## Setup and Installation

### 1. Clone the repository
```bash
git clone <repository_url>
cd Credit-Card-Fraud-Detection
```

### 2. Set up virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the Jupyter Notebooks
Start the Jupyter server to explore notebooks:
```bash
jupyter notebook
```

### 5. Running the Streamlit App
Launch the web interface for fraud detection:
```bash
streamlit run app/streamlit_app.py
```

## Model Pipeline

1. **EDA**: Analyzing the dataset class imbalance, feature distributions, and correlation.
2. **Preprocessing**: Handling skewness, scaling features, and addressing class imbalance using techniques like SMOTE (Synthetic Minority Over-sampling Technique).
3. **Model Training**: Testing multiple classifiers (e.g., Logistic Regression, Random Forest, XGBoost) and optimizing hyperparameters.
4. **Model Evaluation**: Focus on metrics like Precision, Recall, F1-Score, and Area Under Precision-Recall Curve (AUPRC) due to the highly imbalanced nature of fraud data.
