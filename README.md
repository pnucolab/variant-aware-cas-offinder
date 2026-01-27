# Variant-aware Cas-OFFinder

**Variant-aware Cas-OFFinder** is an advanced, high-performance tool designed to identify potential off-target sites of RNA-guided genome editors while accounting for genomic variants such as SNPs and indels. This capability is critical for increasing the precision of genome editing, especially when working with genetically diverse populations or patient-specific data.

This repository contains the full source code for:

- A web-based interactive interface
- A command-line interface (CLI)
- A Docker Compose setup for easy local deployment

---

## 🌐 Overview

Cas-OFFinder is widely used for identifying off-target effects in CRISPR experiments. The **variant-aware** version extends this functionality by integrating genetic variation data, allowing for more precise predictions in both research and therapeutic contexts.

Key features include:

- Support unlimited mismatches
- accounting for genetic variants (SNPs and indels)
- Scalable performance
- Easy deployment via Docker for local use

---

## ⚙️ Prerequisites

To run the command-line interface or deploy the web interface locally, you will need:

- An **OpenCL-compatible device** (GPU or CPU)
- Docker and Docker Compose (for web deployment)
- Python 3.10+ (for CLI and backend utilities)
- Optional: Access to variant files in VCF format for personalized analysis

---

## 📚 Documentation

Detailed installation guides and usage instructions are available in our documentation portal:

🔗 [https://rgen-toolkit.readthedocs.io/](https://rgen-toolkit.readthedocs.io/)

Topics covered include:

- Getting started with the CLI and web tool
- Preparing reference genomes and variant data
- Customizing off-target search parameters
- Interpreting output results

---

## 📈 Benchmarks and Performance

Benchmarks comparing Variant-aware Cas-OFFinder to other tools and configurations can be found here:

🔬 [https://github.com/pnucolab/variant-aware-cas-offinder-benchmark](https://github.com/pnucolab/variant-aware-cas-offinder-benchmark)

---

## 🧬 Applications

- **Precision genome editing**: Account for individual variants to reduce unintended edits
- **Therapeutic development**: Ensure off-target risk assessment in diverse or patient-derived genomes
- **Large-scale screening**: Efficiently scan entire genomes, even with complex variant datasets

---

## 📩 Contact

For questions, feedback, or collaboration inquiries, feel free to reach out through the Issues tab.

---


License
=======

Copyright (C) 2024 Mekonnen Abyot Melkamu and Jeongbin Park

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.
