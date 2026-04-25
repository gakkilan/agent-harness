# Agent Harness Results

This directory contains test results and reports.

## Structure

```
results/
├── reports/           # Summary reports
└── run_YYYYMMDD_HHMMSS/  # Individual test runs
    ├── unit_*.txt
    ├── integration_*.txt
    ├── benchmark_*.txt
    └── report.md
```

## Viewing Results

```bash
# Latest report
cat results/run_*/report.md

# Specific test output
cat results/run_*/unit_test-code-generation.txt
```
