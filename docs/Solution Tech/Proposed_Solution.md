>==Functionalities & Use Cases of proposed solution==
>External components that the solution will interact with and that it will alter
>Dependencies of the current solution
>Pros and cons of the proposed  solution

## Functioniality
1. Phase:
[p.84, Practitioner2Practitioner Communication](https://www.bertelsmann-stiftung.de/fileadmin/files/BSt/Publikationen/GrauePublikationen/VV_eEPA_Expertise_final.pdf)
Functionality | Description
--|--
Review of EHR|easy & needs-based Browsing with intuitive GUI
EHR-Browser / EHR-Timeline | View for all EHR (or specific/filtered/content-sensitive) of a patient
patient-related Communication|easy communication & references to specific EHR (link, objekt-id, ...)
task communication | easy communication what has to be done by whom
treatment management | transparent planning, control, execution & documentation of all steps of a patient

Functionality | Description
--|--
Third-party practitioner | easy & selectable export & transfer to third-party practitioner under controlled data privacy
CRUD EHR | Easy & intuitive creation, editing and deleting with logs of EHR
Reviewing & Validating EHR|easy & visible way + indication, if EHR was reviewed by staff


2. Phase:
[p.84, Practitioner2Practitioner Communication](https://www.bertelsmann-stiftung.de/fileadmin/files/BSt/Publikationen/GrauePublikationen/VV_eEPA_Expertise_final.pdf)
Functionality | Description
--|--
In-Browser Insight | easy and navigatable insight into EHR, espacially imaging diagnostic
Tele-Board | Execution of tele-boards for shared insight in EHR on remote video call
Review-Function Github-style | log and visualization what has been worked on and reviewed already


# Scenarios / Use-Cases
### Registration of Patient
The 1. Phase of the [[Project generals#EHR Portal for Cancer Patients|EHR Portal]] focuses on supporting the daily work of staff for processing and working with EHR of their cancer patients. Therefore, it will provide functionality for creating/importing EHR, mostly provided as images, scanned images or via data transfer from third-party systems, e.g. [https://wetransfer.com](wetransfer), or via mail. After filling all of the EHR, the staff should see a transparent, structured overview on what is the medical history of a patient. On a second step, a staff member will start to validate (if it was not done while creating each single EHR) and in some cases, based on the selected practitioner to be consultated, translate the original reports. The staff member will fill the Patient File with all available EHEs (Electronic Health Entry). 

### Transfer to third-party practitioner
A EHR for a patient was created and validated by a staff member. A suitable third-party practitioner was selected by staff for consultation of the patients case. All relevant EHE are selected and have to be transfered with a sidenote on the task (e.g. second opinion, validation, informationshare, ..) to be performed with the provided information. The task should be transfered to the third-party practitioner via mail (triggered by application). Two scenarios have to be supported: 
1. compressed transfer of relevant EHR via mail -> export of selected EHE required 
2. activation for third-party practitioner for reviewing selected EHE of patient in application

### Continous extension of Patient file
Staff member will updated and add EHE during a customer life cycle continously. A graphical overview of the existing EHE and which were communicated/transfered to third-party practitioner have to be logged. A continous data transfer can be useful, if required.