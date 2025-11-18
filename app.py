import streamlit as st
import tensorflow as tf
import pandas as pd
from keras.preprocessing import image
import numpy as np
import json
from PIL import Image
import plotly.express as px

# -----------------------------
# ⚙️ App Configuration
# -----------------------------
st.set_page_config(page_title="🐟 Fish Classifier", page_icon="🐠", layout="wide")
st.title("🐟 Multiclass Fish Image Classification")
st.markdown("Upload an image of a fish and the model will predict its species!")

# -----------------------------
# 🔍 Load Model and Labels
# -----------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("cnn_fish_model.h5")
    with open("class_labels.json", "r") as f:
        labels = json.load(f)
    return model, labels

model, class_labels = load_model()
st.success("✅ Model and class labels loaded successfully!")

# -----------------------------
# 📤 Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload a fish image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="📷 Uploaded Image", use_container_width=250)

    # -----------------------------
    # 🧠 Preprocess Image
    # -----------------------------
    img_resized = img.resize((224, 224))  # match your model input size
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension

    # -----------------------------
    # 🧾 Model Prediction
    # -----------------------------
    preds = model.predict(img_array)
    preds_percent=preds[0]*100
    pred_index = np.argmax(preds[0])
    pred_label = class_labels[pred_index]
    confidence = preds_percent[pred_index]

    # -----------------------------
    # 🏁 Display Results
    # -----------------------------
    st.markdown("---")
    st.subheader("🎯 Prediction Results")
    st.write(f"🎯 Predicted Class: {pred_label}")
    st.write(f"💪 Confidence: {confidence:.2f}%")

    # Bar visualization
    prob_df = pd.DataFrame({
        "Fish Category": class_labels,
        "Confidence (%)": preds_percent
    }).sort_values("Confidence (%)", ascending=False)

    fig = px.bar(
        prob_df,
        x="Fish Category",
        y="Confidence (%)",
        color="Confidence (%)",
        color_continuous_scale="Blues",
        text_auto=".2f",
        title="Class vs Confidence (%)"
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Fish Category",
        yaxis_title="Confidence (%)",
        xaxis_tickangle=-45,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=12)
    )

    st.plotly_chart(fig, use_container_width=True)

    if confidence < 40:
        st.warning("⚠️ Model is not very confident — image may be unclear or similar to another species.")

else:
    st.info("👆 Upload a fish image to begin classification.")

