---
documentclass: extarticle
fontsize: 20pt
---

# Florian Wilhelm — Sentinel Values in Python: Why None Is Not Enough

11:35 - 12:05

\newpage

## Biography

Florian is Head of Data Science & Mathematical Modeling at inovex GmbH, an IT project center driven by innovation and quality, focusing its services on ‘Digital Transformation’. He holds a PhD in mathematics, has more than 10 years of experience in predictive & prescriptive analytics use-cases and likes everything math

## Abstract

Every Python developer has used `None` as a default but what happens when `None` is also a valid value? This talk explores sentinel values as a first-class concept in Python. We'll uncover why `None` is semantically overloaded, how built-in sentinels like `NotImplemented` and `...` (Ellipsis) quietly power Python's object model, and what happens when you try to create your own. The central challenge: Python's type system has no good answer for sentinel values. We'll walk through why `Optional`, `Literal`, and custom classes all fall short, look at real-world workarounds including Pydantic's experimental MISSING, and discuss what PEP 661's deferral means for your code today. You'll leave with a clear mental model and practical guidance for handling absence in typed Python.
