---
documentclass: extarticle
fontsize: 20pt
---

# Pavel Sulimov and Sergey Eremeykin — Before you open that OSS issue: evidence-first triage

09:10 - 09:40

\newpage

## Biography

Lecturer and Head of Quantum Lab at Zurich University of Applied Sciences, and Academic Lead of the Innosuisse AI Booster Expert Group on Quantum Algorithms. Pavel has 9+ years in applied data science across bioinformatics, banking, network analysis, and online gambling services. He has a PhD in Theoretical Computer Science, and before moving into research and teaching, he led data science teams in the gambling and banking industries.

None

## Abstract

You found a gap in a library you use. Should you open an issue, write an RFC, or spend a month on a pull request? Most teams answer this in a one-off chat with an LLM, get a confident two-sentence verdict, and only later discover the closed duplicate issue or the adjacent API that already solves the problem.

This talk is a case study, not a product pitch. I walk through how we evaluated whether reviving PyTorch's prototype torch.masked module was worth a multi-month upstream contribution. The decision changed once we gathered evidence: old and closed GitHub issues, maintainer activity on the code path, and alternatives such as NestedTensor and FlexAttention. The useful output was not "yes" or "no" - it was a short, cited brief that a teammate could verify in ten minutes.

From that workflow I distill a repeatable method any Python team can use before writing a spec: what to retrieve (issues, merged PRs, module git history, ecosystem docs), what not to trust (verdict-first LLM answers, unvalidated "library X already does this"), and how to structure the result so humans keep the final call.

I briefly show the shape of a Python CLI we are building to automate retrieval and synthesis with mandatory citations - Typer, httpx, GitHub API, local indexing - but the talk stands alone: you leave with a checklist you can run tomorrow with ripgrep, gh, and a markdown template.

Audience: contributors, maintainers tired of duplicate feature requests, and teams choosing where to invest OSS effort. Intermediate level; no PyTorch expertise required (since the Data Science Day is only tomorrow).
