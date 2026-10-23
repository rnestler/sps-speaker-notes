---
documentclass: extarticle
fontsize: 20pt
---

# Emmanuel Okedele — From Open Weights to Trusted Models

14:30 - 15:00

 * Emmanuel is **a machine learning engineer** at **Coefficient AI**
 * They building **bespoke AI** for the **public and private** sectors
 * Recent projects were about **evaluating LLMs**, auditing **Gemma 4** for emergent
   **misalignment** for example or **deepfake detection**.
 * The talk will be about **alternatives to frontier models**: **Open weights models**
   and how we can **decide** if they are good enough for **our tasks**.

\newpage

## Biography

A machine learning engineer at Coefficient AI, a consultancy building bespoke AI for the public and private sectors. With recent projects centred on evaluating large language models, from auditing Gemma 4 for emergent misalignment to building benchmark evaluations for the UK government, including one for deepfake detection

## Abstract

APIs of frontier models are the fast way to ship, but rarely the cheapest place to stay. Open weights are a real alternative: you pay for compute instead of per-token rent, the model runs on your own machines so the data never leaves, residency and governance are yours to set.

The open question is whether an open-weight model is actually good enough for your use case, and which one. A leaderboard won't tell you. It measures someone else's tasks, not yours, and an agent that runs over many turns and calls tools can score well on a benchmark and still fail the real job.

This talk is about answering that for yourself, with two open-source Python tools: Inspect, the UK AI Security Institute's evaluation framework, and Petri, Anthropic's auditor built on top of it. Between them they let you judge an open-weight agent on your own traffic and on the failures you'd never think to collect, so you can put a number on the open-versus-frontier trade-off and decide on evidence.

**Takeaways**

By the end you'll be able to decide whether an open-weight model is good enough to replace a frontier API for your use case, and which one. You'll be able to:

- Build an evaluation from your own traffic, then let Petri's auditor extend it, so you test the cases you've seen and the ones you haven't.
- Score candidates against your current model on real agent work, across many turns and tool calls, not on a single tidy reply.
- Turn the result into a decision: a number on the quality-versus-cost, latency.
