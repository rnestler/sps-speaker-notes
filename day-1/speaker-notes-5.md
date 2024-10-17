---
documentclass: extarticle
fontsize: 20pt
---

# Konrad Gawda — Float - Everything You Wanted to Know About

 * Konrad describes himself as a cloud evangelist, Python trainer and programmer.
 * He is part of the **Warsaw Python community** and likes Linux and Open Source
 * If you ever **struggled** with **floating point numbers** behaving in weird
   ways or encountered numbers that tell you they are **Not a Number** this
   talk will be for you!


## Biography

Cloud Evangelist, Python trainer and programmer (since 2008). Warsaw Python community member. Author of patents in Orange Labs. Linux and Open Source proponent.

\newpage

## Abstract

It is common knowledge that floating point numbers (`float`) are tricky. When misused, floats may lead to construction disaster - I will mention some notable accidents. But mainly, I will dig the topic from Python interface and rounding methods (`int` vs `round`, `divmod`, `math` library), via special symbols (`NaN`, `Inf`, `-0.0`, …), invoking different processor modes (`FLT_ROUNDS`), down to the bits of IEEE 754 standard.
