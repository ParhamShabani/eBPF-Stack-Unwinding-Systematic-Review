
# A Systematic Review of Stack Unwinding Mitigations for eBPF-Based Telemetry Under `-fomit-frame-pointer` Optimization

[![PRISMA 2020](https://img.shields.io/badge/PRISMA-2020%20Compliant-blue.svg)](https://www.prisma-statement.org/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Archived Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24235281-blue)](https://doi.org/10.5281/zenodo.24235281)

This repository contains the complete supplementary materials, search strings, screening protocols, and data extraction matrices for the systematic literature review titled **"A Systematic Review of Stack Unwinding Mitigations for eBPF-Based Telemetry Under `-fomit-frame-pointer` Optimization"**. 

---

##  Repository Overview

Extended Berkeley Packet Filter (eBPF) telemetry pipelines rely heavily on accurate call-chain reconstruction. However, aggressive compiler optimizations—specifically `-fomit-frame-pointer`—sever traditional frame-pointer chains, leading to truncated stacks and telemetry degradation in production environments.
This repository provides a fully reproducible artifact package adhering strictly to **PRISMA 2020 guidelines**, evaluating alternative state-reconstruction mechanisms (including DWARF CFI tables, ORC unwinders, compact metadata structures, and out-of-band asynchronous tracing) across peer-reviewed literature published between January 2020 and October 2026.

---

##  Directory Structure

```text
├── README.md               # Repository landing page and documentation
├── PRISMA/                 # PRISMA protocol, eligibility criteria, and flowchart data
│   ├── protocol.md         # Archival review protocol
│   └── screening_log.csv   # Title/abstract and full-text screening records
├── search-logs/            # Database queries and raw result counts
│   ├── ieee_xplore.txt     # Search string and export log for IEEE Xplore
│   ├── acm_dl.txt          # Search string and export log for ACM Digital Library
│   ├── usenix.txt          # Search string and export log for USENIX proceedings
│   ├── scopus.txt          # Search string and export log for Scopus
│   └── wos.txt             # Search string and export log for Web of Science
├── extraction/             # Data extraction and quality appraisal matrices
│   ├── primary_studies.csv # Synthesized metadata for included studies (n = 41)
│   └── quality_appraisal.csv# Risk of bias and methodological rigor assessments
├── scripts/                # Analysis and automation utilities
│   └── prisma_metrics.py   # Script for aggregating search screening totals
└── LICENSE                 # Open-source licensing terms

```

---

##  PRISMA Search & Screening Methodology

The review executed a systematic search across five primary digital libraries (`IEEE Xplore`, `ACM Digital Library`, `USENIX Association`, `Scopus`, and `Web of Science`), yielding an initial pool of $520$ raw records. Following duplicate removal ($114$ records pruned) and multi-pass PRISMA screening, a final corpus of **$41$ synthesized studies** ($n_1 = 11$ peer-reviewed archival papers and $n_2 = 30$ supporting architectural references/technical documents) was established.

### Master Search Query String

```text
Query = ("eBPF" OR "Extended Berkeley Packet Filter" OR "kernel telemetry") 
        AND ("stack unwinding" OR "stack walking" OR "call stack reconstruction") 
        AND ("DWARF" OR "ORC unwinder" OR "debug metadata") 
        AND ("-fomit-frame-pointer" OR "compiler optimization" OR "stripped binaries")

```

---

##  Replication & Setup Instructions

To inspect data extraction spreadsheets or run verification scripts locally:

1. **Clone the Repository:**
```bash
git clone [https://github.com/Parhamshabani/eBPF-Stack-Unwinding-Systematic-Review.git](https://github.com/Parhamshabani/eBPF-Stack-Unwinding-Systematic-Review.git)
cd repository-name

```


2. **Explore Extraction Data:**
The primary study extraction matrix is available in CSV format under `extraction/primary_studies.csv`. You can open this file using standard spreadsheet software (LibreOffice Calc, Microsoft Excel) or inspect it programmatically using Python:
```python
import pandas as pd

df = pd.read_csv("extraction/primary_studies.csv")
print(df.head())

```


3. **Verify Search Metrics:**
To verify PRISMA screening totals and generate summary metrics:
```bash
python3 scripts/prisma_metrics.py

```



---

##  Citation

If you reference this dataset, protocol, or review findings in your research, please cite the paper as follows:

```bibtex
@article{shabani2026systematic,
  author    = {Parham Shabani},
  title     = {A Systematic Review of Stack Unwinding Mitigations for eBPF-Based Telemetry Under \texttt{-fomit-frame-pointer} Optimization},
  journal   = {IEEE Access},
  year      = {2026},
  volume    = {11},
  pages     = {1--17},
  doi       = {10.1109/ACCESS.2026.XXXXXXX}
}

```

---

##  License

This repository is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

```

```
