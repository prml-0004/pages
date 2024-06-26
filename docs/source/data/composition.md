<br>

# Composition

{octicon}`comment;1em;sd-text-info` <span style="color: #276be9">In Progress</span>

**An introduction to case documents**: The system will expect, will focus on <abbr title="Portable Document">PDF</abbr> documents.  However, the agency has a variety of document types, as summarised in the table below.

<br>

Standalone:

<table style="width: 65%; font-size: small; margin-left: 35px;">
    <colgroup>
        <col span="1" style="width: 7.0%;">
        <col span="1" style="width: 21.5%;">
        <col span="1" style="width: 21.5%;">
    </colgroup>
    <thead><tr style="text-align: left"><th>type</th><th>description</th><th>note</th></tr></thead>
    <tr><td>.msg</td><td>An Outlook message file</td><td>The team can provide<br>the `.pdf` format.  Investigate auto text extraction.</td></tr>
    <tr><td>.pdf</td><td>A Portable Document Format<br> file</td><td></td></tr>
    <tr><td>.docx</td><td>A Windows Word file</td><td></td></tr>
    <tr><td>.xlsx</td><td>A Windows Excel file </td><td></td></tr>
</table>


<br>

Embedded:

<table style="width: 65%; font-size: small; margin-left: 35px;">
    <colgroup>
        <col span="1" style="width: 7.0%;">
        <col span="1" style="width: 21.5%;">
        <col span="1" style="width: 21.5%;">
    </colgroup>
    <thead><tr style="text-align: left"><th>type</th><th>description</th><th>note</th></tr></thead>
    <tr><td>.png, .jpg,<br>etc.</td><td>Images</td><td></td></tr>
</table>


<br>

Further Investigations/Notes:

* Auto-extraction of text from a variety of document types.
* The prevalence of Excel documents, and their content.
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
