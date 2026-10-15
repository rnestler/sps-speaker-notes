---
documentclass: extarticle
fontsize: 20pt
---

# Christoph Gietl — Eliminate hidden exceptions via railway-oriented programming

09:45 - 10:15

\newpage

## Biography

Christoph has been working in software engineering and data engineering for 10+ years.

Coming from a mathematical statistics background he discovered his passion for Python in the late 2010s and for railway-oriented programming in the early 2020s.

Christoph's non-technical interests include parenting, craft beer, history, and Bayern Munich.

## Abstract

Python’s dynamic nature makes it easy to miss hidden exceptions and implicit control flow, leading to bugs that static type checkers such as `mypy`, `pyrefly`, `pyright`, or `ty` cannot catch. Railway-oriented programming (ROP) addresses this by making all domain outcomes explicit in function signatures, using a `Result` type instead of exceptions. This talk introduces ROP in Python, showing how it enables type-safe control flow that static analyzers can verify.

We will compare three open-source libraries: `Expression` by Dag Brattli, `returns` by Nikita Sobolev (Drylabs), and `trcks` by the speaker, each offering different approaches to ROP. Special focus will be given to `trcks`, which uniquely supports both object-oriented (method chaining) and functional (pipeline composition) styles while being designed for maximum type safety and interoperability.

Attendees will learn when and how to use ROP in both synchronous and asynchronous code, how to choose the right library, and when ROP is not the best fit. By the end, you will know how to write Python code that is safer, more predictable, and easier to maintain without sacrificing expressiveness. Attendees should be familiar with type annotations and static type checking in Python. A basic understanding of object-oriented programming and of functional programming can be helpful but is not strictly required.
