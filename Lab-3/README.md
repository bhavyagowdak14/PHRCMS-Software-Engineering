# Lab 3: Component Modeling & Architectural Pattern Selection

**Name:** Bhavya K  
**SRN:** PES1UG24AM066  
**Section:** B  
**Course:** Software Engineering  

---

## Project

**Patient Health Record Consent Management System (Problem Statement #13, Healthcare & Telemedicine).**

A patient-centric health data gateway where patients manage time-bound consent for clinic doctors to access their medical and diagnostic records. Patients can grant or revoke consent and view a complete audit trail of consent and record-access activities.

---

## Folder Contents

| File Name | Description |
| :--- | :--- |
| **`Lab3_Component_Diagram.png`** | UML Component Diagram illustrating the Layered Architecture and component interfaces. |
| **`PES1UG24AM066_Justification.pdf`** | Technical justification for selecting Layered Architecture over Microservices and Client-Server architectures. |
| **`README.md`** | Overview of the system, components, interfaces, and architectural reasoning. |

---

## Architectural Choice: Layered Architecture

The **Patient Health Record Consent Management System** follows a layered architecture where responsibilities are separated into presentation, business/service, and data layers.

### 1. Presentation Layer

Contains the **Patient / Clinic Portal**, which provides the interface for:

- Patient login and registration
- Viewing and managing consent
- Granting and revoking time-bound consent
- Viewing audit history
- Clinic/doctor access requests

### 2. Business / Service Layer

Contains the core services responsible for system functionality:

- **Authentication & Authorization Service** – Handles user authentication, role verification, access control, and authorization.
- **Consent Management Service** – Handles consent granting, revocation, expiry, consent validation, and access decisions.
- **Health Record Service** – Retrieves and provides medical and diagnostic records to authorized users.
- **Notification Service** – Sends consent-expiry reminders and access-related notifications.
- **Audit Trail Service** – Records consent grants, revocations, and record-access activities.

### 3. Data Layer

Maintains persistent system data through:

- **Patient Health Records Database** – Stores patient medical history and diagnostic records.
- **Audit Log Database** – Stores append-only audit records of consent and access events.

---

## Key Architectural Justifications

* **Clear Separation of Responsibilities:** The presentation, business, and data responsibilities are separated, making the system easier to understand, maintain, and modify.

* **Single Enforcement Point for Consent Rules:** Consent validation is handled by the **Consent Management Service** before health records are accessed. This prevents direct access from the portal to protected health-record data.

* **Security & Authorization:** The **Authentication & Authorization Service** verifies user identity and role before access is permitted. The separation between authorization, consent management, and health-record access provides clear security boundaries.

* **Auditability:** The **Audit Trail Service** records consent grants, revocations, and record-access events. The **Audit Log Database** maintains these records as an append-only audit trail to support accountability and compliance.

* **Performance:** Consent and authorization checks are performed before requesting medical records, avoiding unnecessary database access and supporting efficient record retrieval.

* **Maintainability:** Individual services such as authentication, consent management, notifications, auditing, and health-record access have clearly defined responsibilities, allowing them to be maintained independently.

* **Controlled Data Access:** The Health Record Service accesses the Patient Health Records Database, rather than allowing the presentation layer to directly access sensitive patient data.
