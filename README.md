# 🏏 IPL Win Predictor

A web application built with Streamlit that predicts the winning probability of IPL teams in real-time based on match context. The prediction is powered by a trained machine learning pipeline (`pipe.pkl`) using match data.

## 🚀 Features

- Interactive UI to select batting & bowling teams  
- Enter match location, target score, current score, overs completed, and wickets lost  
- Displays real-time win/loss probabilities  
- Visually styled interface using emojis and modern layout  
- Background image and dark mode styling for an enhanced user experience

## 📸 App Preview

![App Screenshot](assets/Screenshot%202025-07-12%20015010.png)

## 🧰 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit pandas scikit-learn
```

## ▶️ How to Run the App

Run the Streamlit app from the terminal:

```bash
streamlit run app.py
```

Replace `app.py` with your Python filename if different.

---

## 📂 Project Structure

```
.
├── app.py                                 # Main Streamlit app
├── pipe.pkl                               # Trained ML pipeline
├── Screenshot 2025-07-12 015010.png       # App UI screenshot
├── requirements.txt                       # Python dependencies
└── README.md                              # Project documentation
```

## 📌 Notes

- The model should be a `sklearn` pipeline compatible with `.predict_proba()`  
- Ensure all team and city names are preprocessed the same as training data  
- You can customize the background using Streamlit's `st.markdown()` + CSS injection

---

## 🌐 Author

Made with ❤️ by [@harkiratchahal](https://github.com/harkiratchahal)
