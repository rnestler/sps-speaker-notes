---
documentclass: extarticle
fontsize: 20pt
---

# Farid Mirzayev — Profiling Python: From cProfile to Sampling

14:30 - 15:00

\newpage

## Biography

By day, he works as a Python Software Developer at Ørsted, helping automate simulation workflows for power engineers. By curiosity, he enjoys exploring Python internals, performance tools, and the strange ways developers convince themselves their code is fast before measuring it.

## Abstract

Python developers have long faced a frustrating tradeoff: the more precisely you measured performance, the more you risked changing it.

Traditional profilers like `profile` and `cProfile` trace every function call, providing exact call counts and instrumented timings at the cost of significant overhead.

The ecosystem fought back. Tools like `py-spy` and `austin` embraced statistical sampling, attaching to running processes and gathering useful insights with minimal impact. Yet statistical sampling remained outside the Python standard library.

Python 3.15 changes that.

The new `profiling.sampling` module, also known as Tachyon, brings statistical profiling into the standard library, building on years of community experimentation.

In this talk, we'll compare tracing and sampling profilers, exploring how each approach works, where it struggles, and how sampled stacks become flame graphs.

By profiling the same code with different tools, we'll see how each profiler reveals a different picture of performance — and why choosing the right tool matters.

## Problem Statement

Most Python developers reach for `cProfile` because it's built in, often without realizing its limitations or knowing modern alternatives exist. Sampling profilers have been available for years, but many developers have not encountered them. This talk closes that gap.

## Attendees will leave knowing

- Deterministic vs statistical profiling and why it matters
- When `cProfile` helps — and when it can mislead
- How and when to use Python 3.15's `profiling.sampling`
- How to choose the right profiler for the job
