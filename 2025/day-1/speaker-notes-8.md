---
documentclass: extarticle
fontsize: 20pt
---

# Saransh Chopra — Using Python's array API standard for ESA's Euclid mission

15:50 - 16:20

\newpage

## Biography

Saransh is a "generalist" research software engineer at UCL’s Advanced Research Computing Centre (at the time of writing this proposal), where he works on Python, HPC, DevOps, and Education projects. Before UCL, he was a research fellow at CERN working on computational physics software, and he will be joining EPFL as a graduate student this fall. Moreover, he develops and maintains several open-source scientific software, which he believes are the key to collaborative and reproducible research.

## Abstract

Over the years, the lack of an array data type in Python has resulted in the creation of numerous array libraries, each specializing in unique niches but still having some interoperability between each other. NumPy has become the de facto array library of Python, and the other array libraries try to keep their API close to that of NumPy. However, this often becomes infeasible, and the libraries deviate out of necessity. To make Python's array libraries shake hands with each other without any inconsistencies, the Consortium for Python Data API Standards has formalised an Array API standard for libraries offering array creation and manipulation operations.

The Array API standard allows users to write and use the same code for arrays belonging to any of the standard-conforming libraries. Through this talk, we will explore the need for such standardisation and discuss its salient features in detail. We will primarily delve into the example of using this standard to make specific parts of European Space Agency's Euclid space mission's code GPU and autodiff compatible. Besides cosmology, we will also take a look at a few other examples, mostly sourced from my experience working with and on several Python array libraries for scientific computing. Ultimately, the audience can expect to leave the room with the knowledge of both, the software engineering and the research side of the array API standard.
