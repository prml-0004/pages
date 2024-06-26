<br>

# Performance Metrics

:::{important}
:class: dropdown

These are the technical metrics.  The data scientists must explain the appropriate range of metrics to the business team, especially its domain experts.  The strengths and weaknesses of each metric must be outlined in detail.  Subsequently, the business team, domain experts, might suggest that one or more of the metrics are inappropriate due to certain reasons.
:::

<br>


<project-issue-item:68005831>

<project-issue:6>

<br>

## The Metrics

{octicon}`comment;1em;sd-text-info` <span style="color: #276be9">In Progress</span>

Based on the <b>(a)</b> error matrix measures, i.e., True Positive, False Negative, False Positive, True Negative, and <b>(b)</b> a threshold defined as either

- [ ] max$\bigl( {tr}_{c}\bigl[{precision}_{c} \cap {sensitivity}_{c}\bigr] \bigr)$
- [ ] max$\bigl( {tr}_{c}\bigl[max(mcc_{c})\bigr] \bigr)$

The expected criteria, per class, are: 

> Precision > 0.9, Sensitivity (True Positive Rate) > 0.9, Specificity (True Negative Rate) > 0.9, Youden's J Statistic > 0.9, and False Positive Rate < 0.1. 

Note, $tr$ denotes threshold, and $mcc$ denotes Matthews Correlation Coefficient.[^metrics]

<br>

## The Model Card

{octicon}`comment;1em;sd-text-info` <span style="color: #276be9">Pending</span>

This is for auditing purposes.  A model's model card summarises the artefacts of a model.

<ul class="disc">
    <li class="disc"><a href="https://arxiv.org/abs/1810.03993" target="_blank">Model Cards for Model Reporting</a></li>
    <li class="disc"><a href="https://modelcards.withgoogle.com/about">Model Cards for Model Reporting: Prototypes</a></li>
</ul>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>


[^metrics]: **N**: # of negative cases, **P**: # of positive cases. | **TN**: True Negative, **FP**: False Positive, **FN**: False Negative, **TP**: True Positive | **TNR = TN/N**: True Negative Rate (specificity) | **FPR = FP/N**: False Positive Rate (fall out) | **FNR = FN/P**: False Negative Rate (miss rate) | **TPR = TP/P**: True Positive Rate (hit rate, sensitivity, recall)


<br>
<br>
