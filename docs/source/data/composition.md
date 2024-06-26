<br>

# Composition

{octicon}`comment;1em;sd-text-info` <span style="color: #276be9">In Progress</span>

**An introduction to case documents**: The system will expect, will focus on <abbr title="Portable Document">PDF</abbr> documents.  However, the agency has a variety of document types, as summarised in the table below.

<br>

Standalone:

| type            | description                         | note                                       |
|:----------------|:------------------------------------|:-------------------------------------------|
| .msg            | An Outlook message file             | The team can provide<br>the `.pdf` format. |
| .pdf            | A Portable Document Format<br> file |                                            |
| .docx           | A Windows Word file                 | The team can provide<br>the `.pdf` format. |
| .xlsx           | A Windows Excel file                |                                            |


<br>

Embedded:

| type            | description                         | note                                       |
|:----------------|:------------------------------------|:-------------------------------------------|
| .png, .jpg, etc | Image files                         |                                            |



<br>

Important:

* The prevalence of Excel documents.
* Note
    * **Images will be out of scope** if an efficient pre-trained model for both text & image redaction is not possible.  Highly probable.
    * In the case of images-out-of-scope, in future the system's pipeline should include an image redaction model module, which will probably depend on contextual details from the entity & phrase redaction model module.


<br>
<br>

```{toctree}
:caption: TABLE OF CONTENTS
:maxdepth: 1
:glob:

composition/instances
composition/sampling
composition/lineage
composition/anomalies
composition/duties
composition/distressing
composition/costs
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
