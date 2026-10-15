---
documentclass: extarticle
fontsize: 20pt
---

# Almudena Barreiro Carrillo — Did we break up? Auditing Instagram data with Python

15:40 - 16:10

\newpage

## Biography

Co-founder of Data for Good Madrid, a non-profit leveraging data for social impact, and Consultant & Data Scientist at Next Digital, where she leads responsible AI projects. She combines a background in mathematics and statistics with technical expertise and a critical view on algorithmic systems. She also contributes to Sesgo404 (Sirviendo Código YouTube), analyzing AI ethics and its social impact for a broader audience.

## Abstract

Instagram logs every interaction: likes, messages, stories viewed, searches, and follower changes. Even if you post nothing, your activity leaves a digital footprint.

In this talk, we will explore how to access and analyze the personal data Instagram collects about you. We will use Python, with libraries like pandas or polars, to clean and structure the information downloaded directly from the platform's privacy portal.

Next, we will build an interactive dashboard using Dash to visualize behavioral patterns over time. We will apply time-series anomaly detection techniques (such as rolling z-score, IsolationForest, or DBSCAN) and supervised classifiers (RandomForestClassifier, LogisticRegression) to identify potentially significant shifts in your digital activity—like a breakup.

Finally, we will reflect on the economic value of this data, the inferences platforms can make about our personal lives, and briefly discuss the European AI Act's relevance to privacy protection.
