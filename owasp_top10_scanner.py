#!/usr/bin/env python3
"""
OWASP Top 10 Automated Scanner

This script provides a starting point for performing automated checks
based on the OWASP Top 10 risks. It is intended for educational
purposes and for use in authorized penetration tests only.
Use responsibly and only against systems you are permitted to test.
"""

import requests
import sys
import json


def test_injection(target_url):
    """Check for basic SQL injection vulnerabilities."""
    payload = "' OR '1'='1"
    try:
        response = requests.get(target_url, params={'q': payload}, timeout=5)
        if payload.strip("'") in response.text:
            return True
    except Exception as exc:
        return f"Error: {exc}"
    return False


def test_xss(target_url):
    """Check for basic reflected XSS."""
    payload = "<script>alert('xss')</script>"
    try:
        response = requests.get(target_url, params={'q': payload}, timeout=5)
        if payload in response.text:
            return True
    except Exception as exc:
        return f"Error: {exc}"
    return False


def test_security_headers(target_url):
    """Check if common security headers are missing."""
    missing = []
    try:
        response = requests.get(target_url, timeout=5)
        required = [
            'Content-Security-Policy',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'Strict-Transport-Security',
        ]
        for header in required:
            if header not in response.headers:
                missing.append(header)
    except Exception as exc:
        return f"Error: {exc}"
    return missing


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <target_url>")
        sys.exit(1)
    target = sys.argv[1]
    results = {
        'injection': test_injection(target),
        'xss': test_xss(target),
        'security_headers_missing': test_security_headers(target),
    }
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
