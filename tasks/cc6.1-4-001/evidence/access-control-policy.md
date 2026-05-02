# Access Control Policy

**Document ID:** POL-AC-004
**Version:** 3.5
**Effective Date:** June 1, 2025
**Owner:** Security Team

---

## 1. Scope

All personnel accessing Vantage Corp production systems, cloud infrastructure (GCP), and SaaS applications.

## 2. Provisioning

- All access requests via ServiceNow.
- RBAC via Google Cloud Identity.
- Provisioning within 24 hours of approved request.

## 3. Authentication

- Google Workspace is the centralized IdP.
- MFA enforced for all users via Google Advanced Protection Program.
- FIDO2 security keys required for all privileged accounts.

## 4. Privileged Access

- Privileged GCP access brokered via IAP (Identity-Aware Proxy).
- Direct service account key creation is prohibited; workload identity federation required.
- Break-glass access requires two-person authorization and triggers a PagerDuty alert.

## 5. Service Accounts

- All service accounts registered in CMDB with designated owner.
- Service account keys must not be created manually; workload identity federation is the standard.
- Exceptions require CISO approval and are tracked in the exception register.

## 6. Access Reviews

- Quarterly reviews by system owners.
- Service accounts reviewed quarterly.
- Privileged access reviewed monthly by CISO.

## 7. Termination

- HR triggers automated offboarding in ServiceNow.
- Google Workspace account suspended within 2 hours.
- All GCP IAM bindings removed within 24 hours.

---

**Approved by:** Tom Reeves, CISO
