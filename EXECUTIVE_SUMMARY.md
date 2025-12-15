# Aathman — Executive Summary

## Problem

Machine-learning models increasingly move across teams, systems, and environments. They are trained in one place, stored in another, deployed elsewhere, and often modified along the way. In this process, models can be subtly altered, corrupted, replaced, or tampered with—sometimes unintentionally, sometimes maliciously. These changes may not immediately break functionality, making them hard to detect through behavior alone.

Teams lack a simple, reliable way to answer a basic but critical question: *Is this exactly the same model we intended to use?*

## Why This Problem Is Hard

Model files are complex binary artifacts. Small internal changes can go unnoticed while still producing plausible outputs. Hashing files alone is often insufficient when models are converted, re-saved, or repackaged. Behavioral testing is expensive and unreliable for integrity checks. As a result, provenance and trust in model supply chains are weak by default.

## What Aathman Is

Aathman is a lightweight model-integrity verifier. It provides a deterministic way to identify a model by its internal structure and parameters, and it binds that identity to a cryptographic signature. Anyone can later verify that the model has not changed since it was signed.

Aathman is designed to be simple, fast, and reproducible. It focuses strictly on identity and integrity, not on performance or behavior.

## How It Works (High Level)

- **Deterministic Fingerprinting:** Aathman serializes model parameters in a canonical order to produce a stable, structure-aware fingerprint.
- **Canonical Certification:** The fingerprint is embedded in a canonical JSON certificate that is reproducible byte-for-byte.
- **Cryptographic Signing:** The certificate is signed using Ed25519, binding the model’s identity to a signer.
- **Verification & Diagnostics:** Verification recomputes the fingerprint, checks the signature, and reports pass/fail. If tampering is detected, Aathman highlights the most affected internal regions.

## What Aathman Does Not Do

Aathman does not evaluate model quality, performance, or fairness. It does not inspect training data, detect semantic backdoors, or manage deployment. It does not modify or “fix” models. These are intentional exclusions. Aathman verifies *what the model is*, not *what it does*.

## Why Aathman Is Useful

Aathman is useful wherever model integrity and provenance matter:
- securing model supply chains,
- validating artifacts in CI/CD pipelines,
- auditing deployed models,
- detecting unauthorized or accidental changes,
- establishing trust boundaries between teams or organizations.

Its minimal design makes it easy to adopt without additional infrastructure.

## Limitations

Aathman detects byte-level and parameter-level changes. It cannot detect attacks that leave the model bytes unchanged, nor can it reason about model behavior. It is a foundational integrity primitive, not a complete security solution.

## Closing

Aathman provides a clear, honest mechanism for answering a simple question with confidence: *Is this the exact model we intended to use?*
