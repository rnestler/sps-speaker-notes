---
documentclass: extarticle
fontsize: 20pt
---

# Gaweng Tan — How to make Django insecure

10:20 - 10:50

\newpage

## Biography

I am a Software Architect at a manufacturing company, specializing in building reliable products and establishing solid DevOps practices with Python from the ground up. Driven by curiosity and hands-on experimentation, I love tackling complex technical challenges and optimizing workflows. Outside of engineering, I run coding side projects, share thoughts on my personal blog, and enjoy deep conversations about technology and society, valuing individuality as much in tech as in everyday life.

## Abstract

Django is one of the most security-conscious web frameworks in any language. SQL injection, cross-site scripting, CSRF, password hashing — Django handles all of it out of the box, often before you even know the attack exists. But what does Django actually *do*? And what happens when you — accidentally or on purpose — turn those protections off?

This talk walks through the OWASP by doing everything wrong first. For each vulnerability, I'll show you the insecure version — the f-string in a raw SQL query, the `|safe` on user input, the `@csrf_exempt` on a money transfer, the `DEBUG = True` in production — and then open Django's source code to show you exactly how the framework prevents it. Not as a black box, but line by line: how the ORM keeps parameters separate from SQL, how the template engine escapes every variable, how the CSRF middleware validates tokens, and why Django hashes your passwords 870,000 times.

By the end you'll know where Django protects you, where it can't, and what one management command to run before every deployment.
