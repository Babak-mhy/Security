# Security

This repository contains utilities for basic penetration testing.

## OWASP Top 10 Scanner

`owasp_top10_scanner.py` is a small script that performs a few example checks
inspired by the OWASP Top 10 risks.

### Usage

```
python owasp_top10_scanner.py <target_url>
```

The script performs simple tests for SQL injection, reflected XSS, and missing
security headers. Results are printed in JSON format.

**Warning**: Run this script only against systems you have permission to test.
