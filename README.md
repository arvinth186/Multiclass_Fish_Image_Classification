<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<body>

<h1>🐟 Multiclass Fish Image Classification (Streamlit App)</h1>

<p>
This project is a <b>Deep Learning–powered Fish Species Classifier</b> built using 
<b>TensorFlow</b>, <b>Keras</b>, and <b>Streamlit</b>.  
The application allows users to upload an image of a fish and instantly get predictions 
about the fish species, along with confidence scores and a probability visualization chart.
</p>

<h2>🚀 Features</h2>
<ul>
<li>Upload fish images (jpg, jpeg, png)</li>
<li>Deep learning CNN model predictions</li>
<li>Displays confidence score</li>
<li>Plotly visualization of all class probabilities</li>
<li>Warning shown for low-confidence predictions</li>
</ul>

<h2>🧠 Model Information</h2>
<ul>
<li>TensorFlow/Keras CNN model</li>
<li>Softmax output for probability distribution</li>
<li>Label-category mapping stored in <code>class_labels.json</code></li>
</ul>

<h2>📁 Project Structure</h2>
<div class="code-block">
📦 Fish-Classifier<br>
├── app.py<br>
├── cnn_fish_model.h5<br>
├── class_labels.json<br>
├── requirements.txt<br>
└── README.html
</div>

<h2>🛠️ Installation & Setup</h2>

<h3>1️⃣ Clone Repository</h3>
<div class="code-block">
git clone https://github.com/your-username/Fish-Classifier.git<br>
cd Fish-Classifier
</div>

<h3>2️⃣ Install Dependencies</h3>
<div class="code-block">pip install -r requirements.txt</div>

<h3>3️⃣ Run Application</h3>
<div class="code-block">streamlit run app.py</div>

<h2>💡 How It Works</h2>
<ol>
<li>User uploads an image.</li>
<li>The image is resized to <b>224×224</b> to match the model input.</li>
<li>The CNN model predicts class probabilities.</li>
<li>The UI shows:</li>
<ul>
<li>Predicted species</li>
<li>Confidence (%)</li>
<li>Plotly-based probability bar chart</li>
</ul>
</ol>

<h2>📌 Future Enhancements</h2>
<ul>
<li>Deploy to Streamlit Cloud / AWS / GCP</li>
<li>Support multiple image uploads</li>
<li>Add Grad-CAM heatmaps for better explainability</li>
<li>Expand dataset for improved model accuracy</li>
</ul>

<h2>🤝 Contributing</h2>
<p>Pull requests and improvements are welcome.</p>

<h2>📝 License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>

</body>
</html>
