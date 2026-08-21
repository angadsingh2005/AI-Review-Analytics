# 📊 AI-Powered Customer Review Analytics

An end-to-end data engineering and Natural Language Processing (NLP) pipeline that extracts **Aspect-Based Sentiment Analysis (ABSA)** from unstructured customer reviews using local Large Language Models (LLMs).

## 🚀 Project Overview

Modern businesses receive thousands of reviews, but standard star-ratings don't explain *why* a customer is unhappy. This project moves beyond basic sentiment analysis by identifying exactly **what feature** the customer is talking about (e.g., "battery life", "UI", "customer support") and the specific emotion tied to it.

Built to run entirely on local consumer hardware (optimized for 16GB system RAM and 6GB GPU VRAM), this system bypasses expensive cloud APIs by leveraging Ollama and lightweight LLMs for rapid, batched inference.

## ⚙️ Key Features

*   **Aspect-Based Extraction:** Utilizes zero-shot prompting with `qwen2:1.5b` to parse unstructured text and output strict, structured JSON data.
*   **Local GPU Inference:** Completely offline NLP processing using Ollama, ensuring zero data-privacy leaks and zero API costs.
*   **Robust Data Pipeline:** Efficiently processes data batches using Python dictionaries and lists before structuring into Pandas DataFrames for downstream analytics.
*   **Interactive BI Dashboard:** A Streamlit-powered frontend utilizing Plotly for dynamic, real-time data visualization of product pain points and feature successes.

## 🛠️ Tech Stack

*   **Language:** Python 3.12
*   **AI/NLP Engine:** Ollama (Qwen2 1.5B)
*   **Data Processing:** Pandas
*   **Frontend/Visualization:** Streamlit, Plotly Express
*   **Environment:** Python Virtual Environment (`.venv`)

## 🏗️ System Architecture

1.  **Data Ingestion:** Reads raw customer reviews (CSV).
2.  **AI Processing Engine:** Iterates through text data, passing prompts to the local LLM to extract JSON-formatted aspects and sentiments.
3.  **Data Transformation:** Normalizes the LLM outputs and merges them with original metadata.
4.  **Business Intelligence UI:** Serves an interactive web dashboard for real-time exploratory data analysis.

## 💻 Local Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/angadsingh2005/AI-Review-Analytics.git
cd AI-Review-Analytics
