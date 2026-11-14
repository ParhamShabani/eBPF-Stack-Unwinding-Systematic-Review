# Systematic Review Protocol: Stack Unwinding Mitigations for eBPF-Based Telemetry Under `-fomit-frame-pointer` Optimization

## 1. Background and Rationale
Extended Berkeley Packet Filter (eBPF) technology is foundational for non-invasive cloud-native kernel telemetry and runtime security enforcement. However, aggressive compiler optimizations—specifically `-fomit-frame-pointer`—sever traditional frame-pointer chains, leading to truncated stack traces and telemetry degradation. This protocol outlines the systematic literature review methodology executed in accordance with PRISMA 2020 guidelines.

## 2. Research Questions
- **RQ₁ (Taxonomy and Classification):** What are the prevailing structural paradigms, metadata representation schemes, and architectural workflows utilized to reconstruct call chains in the absence of frame pointers?
- **RQ₂ (Performance Benchmark):** What are the quantitative performance benchmarks—including execution latency overhead, CPU utilization inflation, memory footprint, and verifier compliance—achieved across baseline state-reconstruction approaches?
- **RQ₃ (Challenges and Bottlenecks):** What are the primary methodological and data-level bottlenecks, such as handling stripped binaries, JIT-compiled runtimes, and ring-buffer saturation under high-frequency burst workloads?
- **RQ₄ (Future Directions):** What open research directions, hardware-assisted primitives, and automated verification frameworks are required to advance cloud-native kernel telemetry?

## 3. Information Sources and Search Strategy
Searches were conducted across five primary archival databases:
1. IEEE Xplore
2. ACM Digital Library
3. USENIX Association Proceedings
4. Scopus
5. Web of Science

### Master Search Query String
```text
Query = ("eBPF" OR "Extended Berkeley Packet Filter" OR "kernel telemetry") 
        AND ("stack unwinding" OR "stack walking" OR "call stack reconstruction") 
        AND ("DWARF" OR "ORC unwinder" OR "debug metadata") 
        AND ("-fomit-frame-pointer" OR "compiler optimization" OR "stripped binaries")
