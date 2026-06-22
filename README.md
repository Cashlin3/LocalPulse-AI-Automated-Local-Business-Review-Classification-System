<div align="center">

# LocalPulse AI
**🏆 Winner of the Productivity Booster Prize 🏆**

### Automated Local Business Review Classification System

*Built for the **ML Empowerment Build Challenge***

**[Live Demo →](https://localpulse-ai-automated-local-business-review-classification-s.streamlit.app/)**

[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-4.0-E25A1C?style=flat-square&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Python](https://img.shields.io/badge/Python-PySpark-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Dataset](https://img.shields.io/badge/Dataset-6.99M%20Reviews-00C49F?style=flat-square)](https://www.yelp.com/dataset)

---

*An end-to-end Big Data NLP pipeline that processes millions of customer reviews to help small local businesses to get actionable insights.*

</div>

---

## The Problem

Small local businesses drown in customer reviews but lack the tools to act on them efficiently. A single unnoticed hygiene complaint can spiral into a reputational crisis before the owner ever sees it.

**LocalPulse AI** solves this by ingesting raw Yelp reviews at scale, cleaning and processing the text, classifying customer sentiment, and **instantly alerting business owners about critical hygiene or safety issues** — helping them protect their reputation before damage is done.

---

## Pipeline Overview

```
Raw Yelp JSON (6.99M Reviews)
           │
           ▼
Spark Data Pipeline
(Cleaning → Tokenization → TF-IDF)
           │
           ▼
Logistic Regression Classifier
(PySpark MLlib)
           │
           ▼
Smart Alert System
(Dual-layer: ML + Keyword Match)
           │
           ▼
Streamlit Dashboard
(Real-time Business Owner View)
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Big Data Processing** | Apache Spark (PySpark 4.0) |
| **NLP Pipeline** | TF-IDF, Tokenizer, StopWordsRemover |
| **ML Model** | Logistic Regression (PySpark MLlib) |
| **Alert System** | Keyword Detection + Sentiment Classification |
| **Dashboard** | Streamlit + Plotly |
| **Environment** | Google Colab, Java 17 |
| **Dataset** | Yelp Academic Dataset (6.99M reviews) |

---

## Dataset & Model Performance

### Dataset Distribution

| Class | Count |
|---|---|
| ⭐ Positive (4–5 stars) | 4,683,961 |
| 😐 Neutral (3 stars) | 691,823 |
| ❌ Negative (1–2 stars) | 1,613,624 |
| **Total** | **6,989,408** |

### Evaluation Metrics

| Metric | Value |
|---|---|
| Training Set | 5,591,291 reviews |
| Test Set | 1,398,117 reviews |
| **Model Accuracy** | **86.20%** |
| 🔴 Critical Alerts Flagged | 11,134 |
| 🟡 Warning Alerts Flagged | 12,487 |

---

## Dual-Layer Smart Alert System

To minimize false alarms, every review passes through a synchronized two-layer validation system before an alert is raised.

```
Review Submitted
      │
      ▼
Layer 1: ML Classification
(Logistic Regression flags negative sentiment)
      │
      ▼
Layer 2: Keyword Detection
(Scans for high-risk terms: cockroach, rat,
 food poisoning, raw chicken, mold, etc.)
      │
      ▼
Both layers agree?
  YES → 🔴 CRITICAL ALERT triggered
   NO → No action needed
```

> **Why dual-layer?** A single ML model can misclassify edge cases. A single keyword scan produces noise. Together, they ensure owners only act on **genuine emergencies**.

---

## Dashboard Structure

| Page | Description |
|---|---|
| 🏠 **Overview** | Platform-wide analytics — total reviews tracked, active businesses monitored, and global alert counts |
| 🔍 **Search Business** | Personalized view where owners enter their Business ID to see tailored sentiment charts and active alerts |
| 🚨 **All Critical Alerts** | A dedicated crisis feed displaying flagged reviews across the platform with exact customer text |

---

## Contributors

| Person | Role | Contributions |
|---|---|---|
| **Mano Rakshitha** ([@ManoRakshithaa](https://github.com/ManoRakshithaa)) | Data Engineer | PySpark infrastructure, 6.99M review data ingestion, NLP preprocessing, TF-IDF feature extraction pipeline, and deployment |
| **Cashlin** ([@Cashlin3](https://github.com/Cashlin3)) | ML Engineer | Logistic Regression classifier training, evaluation tuning, dual-layer smart alert logic, and the interactive Streamlit dashboard |

---

## Challenge & Workflows

This project was developed during the **ML Empowerment Build Challenge**. Beyond building the pipeline, we practiced production-grade Git workflows throughout by isolated feature branches, pull requests, and peer code reviews. Leading to seamless collaboration across our data engineering and ML tracks.
