---
documentclass: extarticle
fontsize: 20pt
---

# Emanuele Fabbiani — The hitchhiker's guide to asyncio

## Abstract

asyncio is the de-facto standard for asynchronous programming in Python and enables concurrent operations without using threads or processes.

In this talk, we will delve into the technical details of asyncio and show how it can be used to improve the performance of Python applications. We will start by discussing the difference between threading, multiprocessing and async programming. Then, we will introduce the basic building blocks of asyncio: Event loops and Coroutines. We will dive deep into the way Coroutines work, discussing their origins and how they are linked to Generators.

Next, we will look at Tasks, which are a higher-level abstraction built on top of Coroutines. Tasks make it easy to schedule and manage the execution of Coroutines. We will cover how to create and manage Tasks and how they can be used to write concurrent code.

Finally, we will also cover some more advanced topics such as Async Loops and Context Managers, and how to handle errors and cancellations in asyncio. 

Whether you are new to asyncio or have experience with it, this talk will provide valuable insights and tips for leveraging its full potential. By the end of this talk, you will have a better understanding of how asyncio works, and how to use it to create efficient, high-performing Python applications.

## Biography

Engineer, researcher, entrepreneur. Emanuele earned his PhD in AI by researching time series forecasting. He was a guest researcher at EPFL Lausanne, and he's now the Head of AI at xtream. He published 8 papers in international journals, presented and organized tracks and workshops at international conferences, including AMLD Lausanne, ODSC London, WeAreDevelopers Berlin, PyData Berlin and Paris, PyCon Florence, and lectured in Italy, Switzerland, and Poland.
