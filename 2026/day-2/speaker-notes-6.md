---
documentclass: extarticle
fontsize: 20pt
---

# Dominik Traxl — No more model training? TabPFN v3 vs. tuned trees.

13:55 - 14:25

\newpage

## Biography

I am a Senior Data Scientist and Engineer at inovex GmbH with a Ph.D. in Theoretical Physics and a strong foundation in complex systems, non-linear dynamics and mathematical modeling. Following an extensive academic career researching computational neuroscience and earth sciences, I transitioned into the tech industry to focus on end-to-end machine learning solutions.

## Abstract

What if you never had to train or tune a model again? That is the pitch behind
tabular foundation models: state-of-the-art predictions with no training, no
hyperparameter search, no feature engineering. Just call .fit() and .predict().
The headliner, TabPFN, whose earlier version was published in Nature, now adds
claims aimed straight at the gradient-boosted trees most of us reach for by
default. TabPFN v3 promises to ingest raw text natively, scale toward a million
rows, support multi-class classification natively and offer a
"thinking mode" for extra quality. Too good to be true? I put it on trial.

This talk walks through a systematic, reproducible Python benchmark that puts
TabPFN, exactly as it ships, up against a best-effort, Optuna-tuned pipeline of
XGBoost, LightGBM, and CatBoost on the messy public Steam Dataset 2025:
numerics, booleans, categoricals, date-times, free-text, embeddings, skewed
distributions, NaNs. The case spans three tasks: binary sentiment classification,
multi-class publisher prediction, and Metacritic-score regression.

We stress-test each vendor claim one at a time: raw text versus sentence
embeddings versus no text, out-of-the-box versus cleaned data, default versus
thinking mode, small samples up to large, few to many classes.

But the real takeaway is the method: how to benchmark a hyped claim fairly, why
the metric you pick can quietly decide the winner, and the data-leakage traps you
must defuse before you trust a single result.

The honest answer to "Too good to be true?" is: "it depends". And knowing what
it depends on is the point. You'll leave with a feel for when a tabular
foundation model earns its keep, when a tuned tree still wins, and how to put
the next "no training required" promise on trial yourself.
