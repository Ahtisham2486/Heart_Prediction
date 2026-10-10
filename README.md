# ❤️ Heart Risk Prediction System

A Machine Learning project that predicts heart-related risk based on user-provided health information. The project uses a trained classification model and a Streamlit web interface to display prediction results interactively.

## 🚀 Project Overview

The Heart Risk Prediction System allows users to enter health-related details and receive a model-generated risk prediction.

The application uses **Logistic Regression** for classification and Streamlit to provide a simple, interactive user interface.

> ⚠️ **Disclaimer:** This project is intended for educational and research purposes only. Predictions are not medical diagnoses and must not replace professional medical advice.

## ✨ Features

* ❤️ Interactive web interface built with Streamlit.
* 🧠 Machine Learning-based risk prediction.
* 📊 KNN classification model.
* ⚙️ Feature scaling using `StandardScaler`.
* 🔄 Consistent feature ordering using saved column information.
* 📈 User-friendly prediction results.
* 🚨 High-risk and low-risk result messages.
* 💾 Saved model and preprocessing objects for inference.

## 🛠️ Tech Stack

| Technology          | Purpose                                    |
| ------------------- | ------------------------------------------ |
| Python              | Core programming language                  |
| Pandas              | Data manipulation and preprocessing        |
| Scikit-learn        | Machine Learning and preprocessing         |
| k Nearest neighbor  | Classification model                       |
| Streamlit           | Web application interface                  |
| Joblib              | Saving and loading trained model artifacts |

## 📂 Project Structure

```text
Heart-Prediction/
│
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

**File descriptions:**

* `app.py` — Streamlit application that accepts user input and displays predictions.
* `KNN.pkl` — Saved KNN model.
* `scaler.pkl` — Saved feature scaler used during training.
* `columns.pkl` — Saved feature-column information used to maintain the expected input format.
* `requirements.txt` — Python dependencies required to run the project.
* `README.md` — Project documentation.

*Note: Adjust the file names and structure if your actual project differs.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project directory:

```bash
cd Heart-Prediction
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the main dependencies:

```bash
pip install streamlit pandas scikit-learn joblib
```

### 4. Run the Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to use the application.

## 🧠 Machine Learning Workflow

The project follows a typical supervised Machine Learning workflow:

1. **Data Collection:** Obtain a dataset containing relevant health attributes and the target variable.
2. **Data Preprocessing:** Clean the dataset and handle missing or inconsistent values.
3. **Feature Engineering:** Encode categorical features into numerical representations.
4. **Feature Scaling:** Apply the fitted `StandardScaler` to the input features.
5. **Model Training:** Train a Logistic Regression classifier using the training dataset.
6. **Model Evaluation:** Evaluate the trained model using appropriate classification metrics.
7. **Model Persistence:** Save the trained model and preprocessing objects using Joblib.
8. **Prediction:** Load the saved objects and process user input using the same preprocessing steps.
9. **Result Display:** Display the predicted class in the Streamlit interface.

## 📊 Prediction Process

```text
User Input
    |
    v
Input Validation
    |
    v
Feature Encoding
    |
    v
Feature Alignment
    |
    v
Feature Scaling
    |
    v
KNN  Model
    |
    v
Predicted Class
    |
    v
Streamlit Result Display
```

**Important:** The inference pipeline must use the same feature names, column ordering, encoding strategy, and fitted scaler as the training pipeline.

## 📈 Model Evaluation

The model should be evaluated using metrics appropriate for medical risk classification.

| Metric               | Purpose                                                |
| -------------------- | ------------------------------------------------------ |
| Accuracy             | Measures the proportion of correct predictions         |
| Precision            | Measures how many positive predictions are correct     |
| Recall (Sensitivity) | Measures how many actual positive cases are identified |
| F1-Score             | Balances precision and recall                          |
| Confusion Matrix     | Shows correct and incorrect predictions by class       |

For a medical risk prediction project, **recall and false-negative rates deserve particular attention**, because failing to identify a genuinely high-risk case can have serious consequences.

Actual model performance should be documented here after evaluation on an appropriate test dataset.

## 🔮 Future Improvements

* 📊 Add interactive visualizations for health attributes.
* 📈 Display prediction probabilities where appropriate.
* 🧪 Compare Logistic Regression with other classification algorithms.
* 🎯 Improve model evaluation and threshold selection.
* 🎨 Enhance the Streamlit interface with custom result cards.
* ☁️ Deploy the application to a hosting platform.
* 🔐 Add input validation and better error handling.
* 🩺 Validate the model using appropriate independent clinical data before considering any real-world medical use.

## ⚠️ Disclaimer

This application is an educational Machine Learning project. It has not been established as a clinically validated diagnostic tool.

The predictions depend on the dataset, training process, input quality, and model limitations. A low-risk prediction does not rule out heart disease, and a high-risk prediction does not establish a diagnosis.

Consult a qualified healthcare professional for medical assessment and decisions.

## 👨‍💻 Author

** Ahtisham ul haq**

* GitHub: https://github.com/Ahtisham2486.
* LinkedIn: https://www.linkedin.com/in/ahtisham-ul/.

---

⭐ If you find this project interesting, consider giving the repository a star!

