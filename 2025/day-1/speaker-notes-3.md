---
documentclass: extarticle
fontsize: 20pt
---

# Konrad Gawda — Bytecode and .pyc files

11:00 - 11:30

\newpage

## Biography

Python, Linux and Open Source proponent. Cloud Evangelist, Python trainer and programmer. Reportedly seen at Warsaw Python meetups since the first PyWaw meeting ever. Recognized as an Inland Sailor by the Polish Sailing Association and as an inventor by the US Patent Office.

## Abstract

Bytecode, the internal language of instructions used by the interpreter is something that perhaps most Python developers have heard about, but few have dug into. This talk will try to explain the idea behind bytecode and how it works.
We will see how to extract bytecode from functions - with `dis` module, and from `.pyc` files (and what is the idea of `__pycache__` directories). Then, the other way around: we’ll check the possibility of building new functions with raw bytes in runtime.
