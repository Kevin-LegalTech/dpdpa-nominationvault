# 🏛️ NomineeVault: DPDP Section 14 Digital Estate & Privacy Engine

> **Modern Legal Engineering:** A specialized, multi-portal web application bridging statutory privacy mandates under India's **Digital Personal Data Protection Act (DPDPA) 2023** with scalable Python software architecture.

---

## ⚖️ Executive Summary & Market Gap

While global privacy compliance frameworks (such as the EU GDPR and US state laws) have mature tooling like OneTrust for handling standard Data Subject Access Requests (DSARs), they completely lack native mechanisms for localized regional mandates—such as **Section 14 of India's DPDPA 2023 (Right to Nominate)**.

Section 14 establishes the statutory "digital will" provision, allowing a Data Principal to designate an individual (*Nominee*) to exercise their data rights in the event of their death or incapacity. **NomineeVault** is built to solve this exact compliance gap, offering an enterprise-grade simulator that operationalizes digital survivorship, cryptographic identity verification, escrowed nominations, and formal adjudication workflows.

---

## 🏛️ Architectural Overview & User Portals

NomineeVault is engineered using a directory-based, multi-portal architecture accessed via a left-hand navigation clipboard to enforce strict role-based separation and compliance gating:

1. **Data Principal Portal (Digital Will & Nomination Registry):**
   * Enables active users to register a designated nominee, pre-authorize statutory scopes (*e.g., Full Account Erasure, RoPA Access, or Correction*), and view active digital estate escrow tokens.
   * Features a **Statutory Modification & Revocation Guardrail** requiring explicit compliance confirmation and warning notices before revoking or replacing active escrow rights.

2. **Nominee Portal (Proxy Claims & Rights Execution):**
   * Integrates a simulated **Government Intermediary Verification Gateway (DigiLocker / Aadhaar e-KYC)** ensuring secure cryptographic identity authentication before dashboard access is granted.
   * Enforces strict **Sequential Compliance Gates**:
     * *Escrow Phase:* Unlocks incident notification triggers (*Death* or *Incapacity*) only when necessary.
     * *Evidentiary Upload:* Allows secure document transmission to enterprise compliance officers with a persistent transmission receipt.
     * *Active Proxy Workspace:* Automatically clears verification gates upon manager approval, unlocking pre-authorized statutory scopes to execute mandates like Section 12 Right to Erasure.
     * *Direct Denial Reflection:* Instantly surfaces formal statutory denial notices and Section 32 Grievance Officer escalation pathways if a claim is rejected.

3. **Enterprise Privacy Manager (Adjudication & Access Control Gateway):**
   * A secure compliance workbench where privacy officers review incoming nomination claims, examine DigiLocker-transmitted evidentiary proofs, and issue binding determinations.
   * Features a **Legal Denial Notice Generator** that auto-drafts concise, legally valid statutory denial pleadings citing lack of statutory nexus and routing appeals directly to the designated Enterprise Grievance Officer (`grievance.officer@enterprise.in`).

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.8+
* **Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Styling:** Custom Cyber-Legal Dark Theme (`#0b0f19`) via CSS Injection

---

## 🚀 Installation & Local Execution

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/nominee-vault.git](https://github.com/your-username/nominee-vault.git)
cd nominee-vault
