---
documentclass: extarticle
fontsize: 20pt
---

# Olena Kutsenko — Keeping data private in real-time pipelines

12:10 - 12:40

\newpage

## Biography

Olena is a Staff Developer Advocate at Confluent and a recognized expert in data streaming and analytics. With two decades of experience in software engineering, she has built mission-critical applications, led high-performing teams, and driven large-scale technology adoption at industry leaders.

## Abstract

We all love real-time data — clicks, payments, rides, messages — but most of it comes with a catch: it contains personal information we’re not supposed to leak, such as names, emails, locations, or even small clues that can identify someone. The challenge: how do we keep streaming data useful and safe at the same time?

In this talk, we’ll explore practical ways to protect privacy in streaming systems using Apache Kafka, Apache Flink, and Apache Iceberg. We’ll cover:
- simple tricks like masking and tokenizing PII;
- why “anonymous” data often isn’t anonymous (the re-identification problem);
- techniques like bucketing, k-anonymity, and adding noise;
- how to balance privacy with data utility (too much hiding makes data useless).

Along the way, we’ll look at real-world stories: from public data leaks to surprising deanonymization attacks, and show live demos of pipelines that anonymize data before it’s written to storage.
If you’ve ever wondered how to build privacy-aware pipelines, this talk will give you practical patterns you can use right away.
