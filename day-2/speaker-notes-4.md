---
documentclass: extarticle
fontsize: 20pt
---

# Emanuele Fabbiani — From SHAP to EBM: Explain your Gradient Boosting Models in Python

11:25 - 11:55

 * It's a pleasure to welcome **Emanuele** the **second time** on stage this
   conference!
 * He earned his **PhD in AI**, focusing on **time series forecasting** and is now the
   Head of AI at **xtream**.
 * After showing us the details of asyncio yesterday, he will introduce SHAP and
   EBM which help you explaining gradient boosting models.

## Biography

Engineer, researcher, entrepreneur. Emanuele earned his PhD in AI by researching time series forecasting. He was a guest researcher at EPFL Lausanne, and he's now the Head of AI at xtream. He published 8 papers in international journals, presented and organized tracks and workshops at international conferences, including AMLD Lausanne, ODSC London, WeAreDevelopers Berlin, PyData Berlin and Paris, PyCon Florence, and lectured in Italy, Switzerland, and Poland.

\newpage

## Abstract

**XGBoost** is considered a state-of-the-art model for regression, classification, and learning-to-rank problems on tabular data. Unfortunately, tree-based ensemble models are notoriously **difficult to explain**, limiting their application in critical fields. Techniques like SHapley Additive exPlanations (SHAP) and Explainable Boosting Machine (EBM) have become common methods for assessing how much each feature contributes to the model prediction.

This talk will introduce SHAP and EBM, **explaining the theory** behind their mechanisms in an accessible way and **discussing the pros and cons** of both techniques. We will also comment on Python snippets where SHAP and EBM are used to explain a gradient boosting model.

Attendees will walk away with an understanding of how SHAP and EBM work, the limitations and merits of both techniques, and a tutorial on how to use these methods in Python, courtesy of the [shap](https://shap.readthedocs.io/en/latest/) and [interpret-ml](https://interpret.ml/docs/ebm.html) packages.

Talk outline:

- A brief reminder about gradient boosting and XGBoost (5 mins)
- The challenge of explainability (5 mins)
- EBM: theory and applications (10 mins)
- SHAP: theory and applications (10 mins)
