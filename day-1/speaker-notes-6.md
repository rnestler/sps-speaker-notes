---
documentclass: extarticle
fontsize: 20pt
---

# Vita Midori — Parallel Python at last? Subinterpreters & free-threading in practice

## Abstract

Python has never been good at parallel computing. Multi-threading doesn't scale beyond a handful of threads because of the notorious GIL (Global Interpreter Lock). Multi-processing feels like a cumbersome workaround that increases complexity and overhead. And yet, we're firmly in an era of multicore machines, big data, and massive ML models that require all the compute they can get. Python, otherwise the star of data science and ML, doesn't really shine when it comes to parallel workloads. 

But that is finally changing! There is more focus and progress happening in this area than ever before, and promising leaps forward are on the horizon. Subinterpreters, already merged in 3.12, offer a tentative step towards making the GIL less than "global"... while the free-threading build of Python 3.13 offers a path towards removing the GIL entirely in the future. Let's explore these new developments and look at how they work, what they do and do not solve, and how we can take advantage of them.

## Biography

I led the development of a stock-trading platform for 8 years. Some bits of C++ and Cython aside, the platform was mainly a Python-based distributed system. Scaling and performance optimisation became not just a necessity but a passion for me. I've since returned to my freelance & consulting roots, and still enjoy helping clients with tough Python problems. Strangely, I've never studied computer science and often run away from all technology into the mountains, forests, and seas of our planet.
