---
documentclass: extarticle
fontsize: 20pt
---

# Das	Indrashis — Gompertz Linear Units (GoLU)

15:15 - 15:45

 * As you may have noticed we needed to **change the schedule**
 * Luckily we have **Indrashis** as a **back up speaker**
 * He is a **machine learning engineer** at **AICONIX** in Freiburg, with a
   Master's in Computer Science, specializing in AI.
 * Who knows what an activation function is?
 * Indrashis will give as an introduction to a  new kind of activation function
   called the GoLU and explain it's unique properties, enjoy! 

## Biography

Hello! I'm Indrashis Das from India. I'm a Machine Learning Engineer at AICONIX in Freiburg, Germany. I hold a Master's in Computer Science (AI specialization) from the University of Freiburg, where I also served as a Teaching Assistant in Prof. Frank Hutter's ML lab for 2.5 years and worked on GoLU as my Master's Thesis.

\newpage

## Abstract

Activation functions are fundamental elements of deep learning architectures as they significantly influence training dynamics. ReLU, while widely used, is prone to the dying neuron problem, which has been mitigated by variants such as LeakyReLU, PReLU, and ELU that better handle negative neuron outputs. Recently, self-gated activations like GELU and Swish have emerged as state-of-the-art alternatives, leveraging their smoothness to ensure stable gradient flow and prevent neuron inactivity.

In this work, we introduce the Gompertz Linear Unit (GoLU), a novel self-gated activation function defined as `GoLU(x) = x Gompertz(x)`, where `Gompertz(x) = exp(-exp(-x))`. The GoLU activation leverages the asymmetry in the Gompertz function to reduce variance in the latent space more effectively compared to GELU and Swish, while preserving robust gradient flow. Extensive experiments across diverse tasks, including Image Classification, Language Modeling, Semantic Segmentation, Object Detection, Instance Segmentation, and Diffusion, highlight GoLU's superior performance relative to state-of-the-art activation functions, establishing GoLU as a robust alternative to existing activation functions.

QA: 15:40 - 15:45
