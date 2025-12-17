# Aathman

Aathman is an open-source, lightweight system designed to verify whether a machine-learning model is genuine or has been altered. It treats every model file as a structured object whose internal parameters define its identity. By computing a deterministic fingerprint and binding it to a cryptographic signature, Aathman provides a simple, repeatable, and trustworthy integrity check.

Aathman exists to bring clarity and certainty to an ecosystem where models move between systems, pipelines, and hands — and where even small, unnoticed modifications can have significant consequences.

---

## Why Aathman Exists

Modern machine-learning systems rely on models that may be tampered with, subtly corrupted, maliciously injected, replaced during deployment, or altered by unnoticed drift. These changes can occur without obvious failures and may go undetected for long periods of time.

Aathman provides a stable anchor of truth.  
It answers a single, crucial question:

**“Is this the exact model we intended to use?”**

No assumptions.  
No speculation.  
Just deterministic cryptographic verification.

---

## What Aathman Does

Aathman performs three essential tasks.

### 1. Deterministic Fingerprinting

Aathman walks through all model parameters in a stable, canonical order. It serializes each tensor along with its structural information and produces a reproducible, structure-aware fingerprint.

Any change — even a single bit — results in a different fingerprint.

### 2. Cryptographic Signature Binding

The computed fingerprint is bound to an Ed25519 signature. This signature becomes proof of authenticity, linking the model to a known signer and preventing silent replacement or modification.

### 3. Independent Verification

Anyone with:
- the model file,
- the certificate,
- and the signer’s public key

can independently recompute the fingerprint and verify authenticity.

The result is a clear outcome:

**AUTHENTIC**  
or  
**✖ TAMPERED**, with changed regions highlighted when available.

No GPUs.  
No retraining.  
No assumptions about model behavior or architecture.  

Only file-level and tensor-level truth.

---

## Design Principles

Aathman is engineered around the following principles:

**Determinism**  
The same model always produces the same fingerprint.

**Minimalism**  
No training data, gradients, or compute-heavy processes are involved.

**Transparency**  
Certificates are canonical JSON and easy to inspect and audit.

**Reproducibility**  
Verification does not depend on hidden state or environment quirks.

**Security**  
Uses modern, standard cryptography with clear trust boundaries.

---

## What Aathman Does Not Do

Aathman intentionally avoids:

- making claims about model performance or correctness  
- evaluating training data or training procedures  
- modifying or repairing models  
- handling deployment or orchestration logic  
- detecting semantic backdoors that leave model bytes unchanged  

It focuses strictly on **what the model is**, not **how it behaves**.

This narrow scope is what makes Aathman predictable, trustworthy, and easy to adopt.

---

## Editions

### Aathman (Open-Source)

This repository.

Provides:
- deterministic fingerprinting  
- cryptographic signing  
- certificate generation  
- integrity verification  

Freely usable under the Apache License 2.0.

### Aathman Enterprise (Closed-Source)

A commercial edition offering advanced capabilities such as:
- model provenance management  
- large-scale certificate orchestration  
- CI/CD pipeline validation policies  
- advanced diffing and drift analysis  
- enterprise-wide trust dashboards  
- hardware-backed signing (HSM, TPM, KMS)  
- organization-level trust authority features  

The Enterprise edition is not required to understand or evaluate Aathman.  
Enterprise features remain private and are not distributed publicly.

---

Programmatic Use

Aathman Core exposes a verify_model() function for programmatic consumption by policy and governance layers.

This function verifies a model file against its certificate and returns structured verification facts, enabling higher-level systems such as Aathman PaCM to enforce organizational policy.

The existing CLI interface remains unchanged.

---

Ecosystem

Aathman Core is designed to be composable.
Policy enforcement, governance, and authorization are intentionally kept out of the core and handled by external layers such as Aathman PaCM.

---

## Contributing

Community contributions are welcome.

To contribute code, you must sign a Contributor License Agreement (CLA).  
This ensures legal clarity for both contributors and maintainers.

Please review **CLA.md** before submitting any contributions.

---

## License

Aathman is licensed under the **Apache License 2.0**.

Please see the **LICENCE** file for full terms and conditions.

---

Aathman provides a clear and reliable mechanism for verifying machine-learning model authenticity. In an era of opaque model sharing and complex supply chains, Aathman offers a stable anchor of truth — simple, honest, and deterministic.
