import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class AddFamilySize(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.copy()
        X['FamilySize'] = X['SibSp'] + X['Parch']
        return X
model = pickle.load(open('model.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

final_features = ['Fare', 'Age', 'FamilySize', 'Pclass', 'Sex_female', 'SibSp', 'Embarked_S']

st.title("AutoML — Titanic Survival Predictor")


uploaded = st.file_uploader("Upload CSV", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("### Raw Data", df.head())

    # Preprocess
    X_processed = preprocessor.transform(df)
    
    # Fix — hardcode indices instead
    feature_indices = list(range(X_processed.shape[1]))[:len(final_features)]
    X_final = X_processed[:, :len(final_features)]

    # Predict
    preds = model.predict(X_final)
    probs = model.predict_proba(X_final)[:, 1]

    df['Survived_Prediction'] = preds
    df['Survival_Probability'] = (probs * 100).round(2)

    st.write("### Predictions", df[['Name', 'Survived_Prediction', 'Survival_Probability']])

    # SHAP
    st.write("### Feature Importance (SHAP)")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_final)
    fig, ax = plt.subplots()
    shap.summary_plot(shap_values, X_final, feature_names=final_features, show=False)
    st.pyplot(fig)