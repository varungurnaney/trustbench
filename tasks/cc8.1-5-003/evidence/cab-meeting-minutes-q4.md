# CAB Meeting Minutes -- Q4 2025

## October 8, 2025
**Attendees:** Hana Otsuki (VP Eng), Raj Mehta (SRE Director), Karen Liu (Security & Compliance Lead), Dr. James Park (Clinical Data Manager)
**Quorum:** Met (4/4)

- CHG-901: Approved. Patient portal session timeout update. Medium risk.

## October 15, 2025
**Attendees:** Hana Otsuki (VP Eng), Raj Mehta (SRE Director), Karen Liu (Security & Compliance Lead), Dr. James Park (Clinical Data Manager)
**Quorum:** Met (4/4)

- CHG-902: Approved. FHIR R4 lab results endpoint. High risk. Security review confirmed HL7 FHIR compliance. PHI data flow validated — lab results encrypted at rest and in transit. Dr. Park confirmed clinical data mapping accuracy.

## November 19, 2025
**Attendees:** Hana Otsuki (VP Eng), Raj Mehta (SRE Director), Karen Liu (Security & Compliance Lead)
**Quorum:** Met (3/4)

- CHG-907: Approved. PHI access audit trail. High risk. Karen confirmed implementation aligns with HIPAA audit requirements (45 CFR 164.312(b)).

## November 26, 2025
**Attendees:** Hana Otsuki (VP Eng), Raj Mehta (SRE Director), Karen Liu (Security & Compliance Lead), Dr. James Park (Clinical Data Manager)
**Quorum:** Met (4/4)

- CHG-908: Approved. Timezone fix for appointment scheduler. Medium risk.

## December 11, 2025
**Attendees:** Hana Otsuki (VP Eng), Raj Mehta (SRE Director), Karen Liu (Security & Compliance Lead), Dr. James Park (Clinical Data Manager)
**Quorum:** Met (4/4)

- CHG-911: Approved. Patient consent management workflow. High risk. Karen reviewed consent data handling for HIPAA compliance. Dr. Park validated consent form clinical accuracy.
- Discussion: Karen raised a concern about CHG-905 and CHG-910 being processed as standard changes. CHG-905 (Express.js 4.x to 5.0) and CHG-910 (PostgreSQL 14.9 to 15.4) are both major version upgrades. SC-003 specifies "patch versions only (x.y.Z)" and "Third-party library patch updates only." Major version bumps (4.x→5.0, 14→15) arguably exceed the catalog scope. Hana acknowledged the concern and noted that CI tests passed for both. Raj added that no issues were observed post-deployment. Karen recommended a review of the standard change catalog classification criteria. Action item: Hana to circulate updated SC-003 language clarifying version scope.
