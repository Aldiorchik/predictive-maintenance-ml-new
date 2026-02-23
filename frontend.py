import streamlit as st
import requests

st.title("🚀 Predictive Maintenance Model")

n_features = 37  # <-- твое число

features = []

for i in range(n_features):
    value = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(value)

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"features": features}
    )

    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        probability = result["probability"]

        st.subheader("Failure Probability")
        st.progress(probability)

        st.write(f"Risk score: {probability:.2f}")

        st.image("feature_importance.png", use_column_width=True, caption="Top Important Sensors")

        if prediction == 1:
            st.error("⚠ High Failure Risk")
        else:
            st.success("✅ Engine Stable")
    else:
        st.error("API Error")

