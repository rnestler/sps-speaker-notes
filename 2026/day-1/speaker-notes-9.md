---
documentclass: extarticle
fontsize: 20pt
---

# Theodore Tucker — Packaging FOSS Python applications and libraries for Debian

15:40 - 16:10

\newpage

## Biography

Theodore is an early-career software engineer at Codethink Ltd. in Manchester, UK, where he works on the hardware-in-the-loop testing of embedded Linux-based operating systems against functional safety standards. In his spare time, he studies Combined STEM at the UK's Open University, and maintains Debian packages for Apache BuildStream and dependencies along with personal open source Python and Rust projects, FOSS computing being a hobby since the age of 7.

## Abstract

# Packaging FOSS Python applications and libraries for Debian

Debian Linux is deployed on millions of desktops and servers worldwide, renowned for 30 years for its stability and the quality of software packages installable from its archives. Over 1,400 volunteer contributors from around the world serve Debian users and the free software community by maintaining more than 60,000 well-behaved, consistent, secure and up-to-date packages, including Python applications and libraries.

System administrators, software integrators, and scientists can be considerably more certain of the provenance, reliability, and intercompatibility of Python packages from the Debian archives than uploads to PyPi.org, especially at a time where these aspects are coming under greater scrutiny in Europe. For the Python developer, packaging your work for Debian, and therefore satisfying the stringent quality assurance criteria, is a great responsibility, but also a rewarding opportunity to gain more users in higher-integrity contexts, improve your coding practices, and engage with a community of free software experts.

This talk will present case studies of the "Debianisation" of a Python library (pyroaring) and application (Apache BuildStream 2.7.0) recently undertaken by the speaker in their first major FOSS contribution, covering from first principles:
- Preparing upstream sources and Debian-specific metadata and build instructions in compliance with Debian Policy and Free Software Guidelines, both for pure Python libraries and those with Cython extensions and Sphinx documentation
- Guiding a new package through the Debian quality assurance processes (including version control, integration testing, reproducibility, and migration) so it can be included in a release
- Responsibilities of a Debian package maintainer to their users, upstreams, and reverse-dependencies in handling bugs and updates
- Sources of help when contributing to a project as mature as Debian for the first time
