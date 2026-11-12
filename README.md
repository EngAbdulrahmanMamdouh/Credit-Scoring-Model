# 💳 Credit Scoring & Delinquency Prediction

### Machine Learning-Based Credit Risk Assessment System

A Machine Learning project that predicts the likelihood of a customer experiencing serious financial delinquency within the next two years based on their financial information, credit history, and repayment behavior.

The project combines data analysis, machine learning, feature engineering, and an interactive Streamlit application to support credit risk assessment.

---

## 🎯 Project Overview

The main objective of this project is to build a predictive model that helps identify customers who may be at risk of serious financial delinquency.

The system analyzes customer-related features and classifies them into two categories:

- **Low Risk (0):** The customer is not predicted to experience serious delinquency.
- **High Risk (1):** The customer is predicted to experience serious delinquency.

The application also displays the predicted risk probability to provide additional insight into the model's decision.

## ✨ Key Features

- Data Cleaning and Preprocessing.
- Exploratory Data Analysis (EDA).
- Missing Values Handling.
- Feature Selection and Feature Engineering.
- Random Forest Classification.
- Model Evaluation using Classification Metrics.
- Risk Probability Estimation.
- Interactive Streamlit Web Application.
- Model Serialization using Joblib.

## 📊 Dataset Information

The project uses a credit risk dataset containing **150,000 customer records**.

The dataset includes financial and credit-related information such as:

| Feature | Description |
|---|---|
| Age | Customer's age |
| MonthlyIncome | Monthly income |
| DebtRatio | Debt-to-income ratio |
| RevolvingUtilizationOfUnsecuredLines | Credit utilization ratio |
| NumberOfOpenCreditLinesAndLoans | Number of active credit lines and loans |
| NumberOfTime30-59DaysPastDueNotWorse | Number of payment delays between 30–59 days |
| NumberOfTime60-89DaysPastDueNotWorse | Number of payment delays between 60–89 days |
| NumberOfTimes90DaysLate | Number of payments delayed by 90 days or more |
| NumberRealEstateLoansOrLines | Number of real estate loans |
| NumberOfDependents | Number of dependents |

**Target Variable:** `SeriousDlqin2yrs`

## ⚙️ Machine Learning Workflow

The project follows these main steps:

1. **Data Loading:** Importing and exploring the credit scoring dataset.
2. **Data Cleaning:** Removing unnecessary columns and handling missing values using median imputation.
3. **Exploratory Data Analysis:** Understanding feature distributions and relationships.
4. **Feature Selection:** Separating independent variables from the target variable.
5. **Feature Engineering:** Creating additional financial indicators in the prediction application.
6. **Model Training:** Training a Random Forest Classifier.
7. **Model Evaluation:** Evaluating predictions using classification metrics.
8. **Deployment:** Building an interactive application using Streamlit.

## 🤖 Model & Evaluation

**Selected Algorithm:** Random Forest Classifier

The model was trained using the following configuration:

- Number of Estimators: 100
- Maximum Depth: 10
- Random State: 42
- Train-Test Split: 80% Training / 20% Testing

### Evaluation Results

The model achieved the following results on the test dataset:

| Metric | Class 0 | Class 1 |
|---|---:|---:|
| Precision | 0.94 | 0.62 |
| Recall | 0.99 | 0.17 |
| F1-Score | 0.97 | 0.27 |

**Overall Accuracy: 94%**

*Note: The dataset is imbalanced. Although the overall accuracy is high, the model has limited recall for the high-risk class. Improving the detection of delinquent customers is an important area for future development.*

## 🖥️ Interactive Web Application

The project includes a Streamlit application that allows users to enter customer financial information and receive a credit risk prediction.

### Application Capabilities

- Customer Information Input.
- Financial and Credit History Analysis.
- Automatic Feature Calculation.
- Credit Risk Classification.
- Predicted Risk Probability.

### Prediction Outputs

- 🟢 Low Risk
- 🔴 High Risk

## 🛠️ Technologies & Libraries

- **Python** – Main programming language.
- **Pandas** – Data manipulation and analysis.
- **NumPy** – Numerical computing.
- **Scikit-learn** – Machine Learning and model evaluation.
- **Matplotlib** – Data visualization.
- **Seaborn** – Statistical data visualization.
- **Streamlit** – Interactive web application.
- **Joblib** – Saving and loading trained models.
- **Jupyter Notebook** – Model development and experimentation.

## 📁 Project Structure

```text
Credit-Scoring-Model/
│
├── Credit Scoring Model.ipynb
│
├── app.py
│
├── credit_scoring_model.pkl
│
├── model_features.pkl
│
├── requirements.txt
│
└── README.md
```

## 🚀 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/EngAbdulrahmanMamdouh/Credit-Scoring-Model.git
```

### 2. Navigate to the Project Directory

```bash
cd Credit-Scoring-Model
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

**Important:** The trained model files (`credit_scoring_model.pkl` and `model_features.pkl`) must remain in the project root directory.

To run the Jupyter Notebook from scratch, provide the original `cs-training.csv` dataset in the appropriate working directory.

## 🔮 Future Improvements

- Improve recall for high-risk customers.
- Apply advanced techniques to handle class imbalance.
- Experiment with XGBoost and other classification algorithms.
- Perform hyperparameter optimization.
- Add more comprehensive model evaluation.
- Improve the user interface and application experience.
- Deploy the application online.

## 👨‍💻 Author

**Abdulrahman Mamdouh**

Machine Learning Engineer | AI Enthusiast

- GitHub: [EngAbdulrahmanMamdouh](https://github.com/EngAbdulrahmanMamdouh)
- LinkedIn: [Abdulrahman Mamdouh](https://linkedin.com/in/abdulrahman-mamdouh-3ab8343bb/)

---

⭐ If you find this project interesting, feel free to explore the repository and give it a star!

*This project is developed for educational and demonstration purposes. Predictions should not be used as the sole basis for real-world lending or financial decisions.*
