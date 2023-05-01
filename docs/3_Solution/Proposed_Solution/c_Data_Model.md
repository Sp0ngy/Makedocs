>Schema definitions
>New data models
>Data validation methods

### References
[Datenmodell ePA gematik](https://fachportal.gematik.de/fachportal-import/files/gemSpec_DM_ePA_V1.10.1.pdf)
[Bundesamt für Justiz, §341 Elektronische Patientenakte](https://www.gesetze-im-internet.de/sgb_5/__341.html)

### Value Sets
[Full value set](https://github.com/gematik/api-ePA/tree/ePA-2.5.2/src/vocabulary/value_sets)
[Page 76 Recommendation on shortend value sets for certain users](https://fachportal.gematik.de/fachportal-import/files/gemSpec_DM_ePA_V1.10.1.pdf)
- [ ] Extract related values from Full value set
- [ ] translate german values to english

### Document Entry Data Model
[Page 12 Datenmodell ePA](https://fachportal.gematik.de/fachportal-import/files/gemSpec_DM_ePA_V1.10.1.pdf)
- [ ] Extract related fields from Datenmodell ePA
- [ ] create new DB schema for extracted datamodel

**07.03.2023**: At this point, only Documents and Policy Documents (IHE XDS.b Document Entry) are relevant; Submission Sets can be relevant for future extension
**10.03.2023**: After evaluation of NoSQL DB (MongoDB), ==decision for SQL DB==:
- Developer first (no experience with NoSQL)
- NoSQL unstructured files can be hard to manage in digital health context
- scalability requirement low priority
- SQL DB like PostgreSQL supports JSON files, if required

### IHE ITI TF relevant Profiles

**Prio 1**
- [Cross-Enterprise Document Sharing (XDS.b) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-10.html)

**Prio 2**
- [Advanced Patient Privacy Consents (APPC) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-43.html)
- [Cross-Community Access (XCA) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-18.html)
- [Cross-Community Document Reliable Interchange (XCDR) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-40.html)
- [Cross-Enterprise Document Media Interchange (XDM) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-16.html)
>Required in case of absence of XDS
- [Cross-Enterprise Document Reliable Interchange (XDR) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-15.html) 
- [Cross-Enterprise User Assertion (XUA) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-13.html)
- [Remove Metadata and Documents (RMD) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-44.html)
- [Restricted Metadata Update (RMU) Profile](https://profiles.ihe.net/ITI/TF/Volume1/ch-48.html)