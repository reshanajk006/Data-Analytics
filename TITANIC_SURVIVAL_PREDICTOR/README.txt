# 🚢 Titanic Survival Predictor — AutoML Pipeline

An end-to-end Machine Learning pipeline built from scratch to predict 
Titanic passenger survival using automated preprocessing, hyperparameter 
tuning, ensembling, and explainability.

## 🎯 Project Highlights
- Built complete ML pipeline without AutoML libraries
- Achieved 84.13% accuracy using Optuna-tuned XGBoost
- SHAP explainability showing WHY each prediction was made
- Benchmarked 3 models: Random Forest, XGBoost, LightGBM

## 🛠️ Tech Stack
- **Data & Cleaning** → Pandas, NumPy
- **Modeling** → Scikit-learn, XGBoost, LightGBM
- **Hyperparameter Tuning** → Optuna (Bayesian optimization)
- **Explainability** → SHAP
- **UI** → Streamlit

## 📊 Pipeline Steps
1. Exploratory Data Analysis (EDA)
2. Data Cleaning & Feature Engineering
3. Feature Selection (LightGBM importance + RFE)
4. Hyperparameter Tuning with Optuna
5. Model Comparison & Selection
6. Ensembling (Voting + Stacking)
7. SHAP Explainability
8. Streamlit Web App

## 🏆 Model Leaderboard
| Model              | Accuracy |
------------------------------- 
| XGBoost (Optuna)   | 84.13% |
| LightGBM (Optuna)  | 83.99% |
| RandomForest(Optuna) | 83.42% |
| Stacking Ensemble  | 83.00% |
| Voting Ensemble    | 82.86% |

## 🔍 Key Findings (SHAP)
- **Sex** → Most impactful feature (females survived more)
- **Pclass** → 1st class had significantly higher survival
- **Fare** → Higher fare = better survival odds
- **Age** → Younger passengers had slight advantage

## 📁 Project Structure
automl_project/
├── autoflow.ipynb    ← Full pipeline notebook
├── app.py            ← Streamlit web app
├── model.pkl         ← Saved XGBoost model
├── preprocessor.pkl  ← Saved preprocessing pipeline


## 🚀 Run Locally
# Install dependencies
pip install pandas numpy scikit-learn xgboost lightgbm optuna shap streamlit

# Run app
streamlit run app.py

## 📖 What I Learned
- How to build production-ready ML pipelines
- Bayesian hyperparameter optimization with Optuna
- When ensembling helps vs hurts performance
- Model explainability with SHAP values
- Real-world lesson: best single model sometimes beats ensembles

## 📊 Dataset
- Source: Kaggle Titanic Dataset
- 891 training samples, 12 features
- Binary classification (Survived: 0/1)
