---
documentclass: extarticle
fontsize: 20pt
---

# Michael Inden — Your Code Is Slower Than Expected - Hidden Performance Traps

09:10 - 09:40

\newpage

## Biography

Michael Inden ist Java- und Python-Enthusiast mit über 25 Jahren Berufserfahrung. Er hat bei diversen internationalen Firmen in verschiedenen Rollen etwa als Software-entwickler, -architekt, Teamleiter, CTO, Head of Development und Trainer gearbeitet. Derzeit ist er als Dozent für Software Engineering an der FH OST in Rapperswil tätig. 

Darüber hinaus spricht er auf Konferenzen und schreibt Fachbücher wie "Java Challenge» / «Python Challenge" und "Einfach Java" / "Einfach Python".

## Abstract

Python makes it easy to write clean and expressive code — but it also makes it easy to write code that is unexpectedly slow.

In this talk, we’ll look at everyday Python patterns that seem harmless but can have serious performance implications. Why is x in list sometimes dramatically slower than expected? What’s the real difference between append(), +=, and +? And when does a simple data structure choice turn an O(n) solution into O(n²)?

Instead of focusing on micro-optimizations, we’ll go one level deeper: how Python’s core data structures (lists, sets, dictionaries) actually work under the hood — and how that directly impacts runtime behavior.

You’ll leave with a practical mental model and a small set of rules of thumb that help you write code that is not just correct and readable, but also efficient — without premature optimization.
