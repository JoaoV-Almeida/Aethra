# ✈️ Aethra I

**Intelligent prediction of flight delay and cancellation risks**

A Streamlit application that combines **Machine Learning (XGBoost)** and **Generative AI (Google Gemini)** to analyze flight routes and generate personalized travel recommendations based on 10 traveler personas.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Traveler Personas](#traveler-personas)
- [Technical Notes](#technical-notes)
- [Useful Links](#useful-links)
- [License](#license)

---

## 📌 Overview

**Aethra I** helps travelers anticipate risks before booking flights.  
It predicts delays and cancellations using historical route data and provides tailored recommendations based on traveler profile, cost sensitivity, and flexibility.

---

## 🚀 Features

- 📊 **Predictive Risk Analysis** — Estimates delay probability from historical route patterns  
- 👤 **10 Traveler Personas** — Personalized insights and recommendations  
- 🤖 **AI Chatbot** — Conversational assistant powered by Gemini 2.5 Flash  
- 💰 **Opportunity Cost Analysis** — Financial impact of delays by persona  
- 🛡 **Insurance Quotes** — Dynamic pricing based on risk level  
- 🔎 **Cascading Filters** — City → Departure Airport → Destination  
- 🛫 **391 Real Airports** — Complete dataset of U.S. airports  

---

## 🎥 Demo

Run locally and open:

http://localhost:8501

---

## ⚙️ Installation

### Requirements
- Python 3.13+
- Gemini API key

---

### Option 1 — Using existing virtual environment
```bash
c:/Users/Juliano.jcs/dev/Project-X/.venv/Scripts/python.exe -m streamlit run app.py
