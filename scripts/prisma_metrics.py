"""
PRISMA Metrics Aggregation Script
Validates search screening totals across archival databases.
"""

def calculate_prisma_totals():
    databases = {
        "IEEE Xplore": {"raw": 142, "dups": 32},
        "ACM Digital Library": {"raw": 118, "dups": 26},
        "USENIX Association": {"raw": 95, "dups": 21},
        "Scopus": {"raw": 90, "dups": 20},
        "Web of Science": {"raw": 75, "dups": 15}
    }
    
    total_raw = sum(v["raw"] for v in databases.values())
    total_dups = sum(v["dups"] for v in databases.values())
    unique_screened = total_raw - total_dups
    
    # Screening steps
    title_abstract_excluded = 315
    full_text_assessed = unique_screened - title_abstract_excluded
    
    # Full-text exclusion breakdown:
    # - Lack of quantitative metrics for eBPF overhead: 20
    # - Absence of -fomit-frame-pointer analysis: 18
    # - Non-archival or gray literature: 15
    full_text_excluded = 20 + 18 + 15  # Total: 53
    final_included = full_text_assessed - full_text_excluded
    
    print(f"--- PRISMA 2020 Flow Summary ---")
    print(f"Total Raw Records Identified : {total_raw}")
    print(f"Duplicates Removed           : {total_dups}")
    print(f"Unique Records Screened      : {unique_screened}")
    print(f"Full-Text Assessed           : {full_text_assessed}")
    print(f"Full-Text Excluded           : {full_text_excluded}")
    print(f"Final Included Studies       : {final_included}")

if __name__ == "__main__":
    calculate_prisma_totals()
