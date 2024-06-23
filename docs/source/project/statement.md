<br>

# Problem Statement

{issue}`1`

The agency is the custodian a large number of case documents, and the agency has to share its case documents due to

* FOI SA (Freedom of Information Scotland Act) / EIR (Environmental Information Regulations) requests.
* Data sharing agreements with externally parties
* Publishing responsibilities.

However, aspects of these documents are <abbr title="protected by law or regulation">confidential</abbr> and/or sensitive, therefore must be redacted prior to document sharing.  Thus far, the agency has redacted documents manually, which is time-consuming, costly, repetitive, and error-prone.  Additionally, it hinders the agency's ability to proactively publish case documents, and hence reduce the number of *freedom of information* requests it receives; enhance its trustworthiness and reliability.  Consequently, the agency is in search of a near-real-time solution that automatically redacts the latest case documents on schedule.

A few commercial redaction technologies/services exist, e.g.,

* <a href="https://www.blackout.one" target="_blank">BLACKOUT</a>
* <a href="https://brighter.ai/product">brighterAI</a> (images)


These services/technologies identify and redact Personal Identifiable Information (PII) and Sensitive Personal Information (SPI).  However, the redaction requirements of the agency are beyond PII and SPI, it also includes phrases that exhibit particular contextual information.  The agency estimates that the commercial solutions might be able to address 90% of our redaction requirements; the solutions will struggle to identify and redact the business / environmentally sensitive information.  Hence, we are opting for an in-house solution that includes an adaptable custom/fine-tuned *entity and phrase identification & redaction model*.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>