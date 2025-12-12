# Aathman Core

Aathman Core is an open-source, lightweight system designed to prove whether a
machine-learning model is genuine or has been altered. It treats every model file
as a structured object whose internal bytes define its identity. By reducing the
model to a deterministic fingerprint and binding it to a cryptographic signature,
Aathman provides a simple, repeatable, and trustworthy integrity check.

Aathman exists to bring clarity and certainty to an ecosystem where models move
between systems, pipelines, and hands — and where even small, unnoticed
modifications can have significant consequences.



## Why Aathman Exists

Modern ML systems depend on models that can be:

- tampered with,
- subtly corrupted,
- maliciously injected,
- replaced during deployment,
- or affected by unnoticed drift.

Aathman provides a stable anchor of truth.  
It answers a single crucial question:

> **“Is this the exact model we intended to use?”**

No assumptions.  
No speculation.  
Just deterministic cryptographic verification.



## What Aathman Core Does

Aathman Core performs three essential tasks:

### **1. Deterministic Fingerprinting**
Aathman walks through all model parameters in a stable, canonical order.
It serializes each tensor, normalizes its bytes, and produces a reproducible,
structure-aware hash.

Any change — even a single bit — produces a different fingerprint.

### **2. Cryptographic Signature Binding**
The computed fingerprint is bound to an Ed25519 signature.
This signature becomes proof of authenticity, linking the model to a known signer.

### **3. Independent Verification**
Anyone with:

- the model file,
- the public key,
- and the certificate

can independently recompute the fingerprint and verify authenticity.

The result is a simple:

- **AUTHENTIC**  
or  
- ✖ **TAMPERED**, with changed regions highlighted (if available).

No GPUs.  
No retraining.  
No assumptions about framework or architecture.  
Just file-level and tensor-level truth.



## Design Principles

Aathman Core is engineered around these principles:

### **Determinism**
Fingerprinting logic always produces the same result for the same model.

### **Minimalism**
No training data, gradients, or compute-heavy processes are used.

### **Transparency**
The certificate format is canonical JSON, easy to inspect and audit.

### **Reproducibility**
Verification does not depend on platform quirks or environment differences.

### **Portability**
Works across frameworks and supports multiple model formats.

### **Security**
Uses standard, modern cryptography with clear trust boundaries.



## What Aathman Does *Not* Do

Aathman intentionally avoids:

- making claims about model performance,
- evaluating data or training steps,
- modifying the model,
- handling deployment logic,
- requiring confidential or proprietary data.

It looks strictly at **what the model *is***, not how it behaves.

This narrow scope is what makes Aathman predictable, trustworthy, and easy to adopt.



## Editions

Aathman is available in two editions:

### **Aathman Core (open-source)**  
This repository.  
Provides:

- deterministic fingerprinting  
- cryptographic signing  
- certificate generation  
- integrity verification  

Freely usable under the Apache License 2.0.

### **Aathman Enterprise (closed-source)**  
A commercial edition offering advanced capabilities such as:

- model provenance management  
- large-scale certificate orchestration  
- CI/CD pipeline validation policies  
- advanced diffing and drift analysis  
- enterprise-wide trust dashboards  
- hardware-backed signing (HSM, TPM, KMS)  
- organization-level trust authority features  

Enterprise features remain private and are not distributed publicly.



## Contributing

Community contributions are welcome!

To contribute code, you must sign a Contributor License Agreement (CLA).  
This ensures legal clarity for both contributors and maintainers.

See **[`CLA.md`](./CLA.md)** for details.



## 📄 License

Aathman Core is licensed under the **Apache License 2.0**.  
See [`LICENCE`](./LICENCE) for more information.



Aathman provides a clear, reliable mechanism for verifying machine-learning model
authenticity. In an era of opaque model-sharing and complex supply chains,
Aathman offers a stable anchor of truth — simple, honest, and deterministic.
