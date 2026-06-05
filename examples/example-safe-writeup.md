# Example Safe Write-up

## Summary

A fictional lab application exposed a debug page that displayed non-sensitive configuration information.

## Scope

- Target: Local lab application
- Asset: http://localhost:8000
- Date tested: YYYY-MM-DD
- Authorization: Personal lab

## Impact

If this occurred in a real production system, exposed debug information could help an attacker understand the application environment.

## Steps to Reproduce

1. Start the local lab application.
2. Visit /debug.
3. Observe that environment details are displayed.

## Evidence

No real target data included.

## Recommended Fix

Disable debug routes outside of local development environments.

## Disclosure Status

Lab-only example. No disclosure needed.
