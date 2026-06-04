---
layout: page
permalink: /Publications/
title: Publications
description: Publications organized by research area.
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

<div class="publications">

## Artificial Intelligence & Fault Diagnosis

{% bibliography --query @*[keywords~=fault-diagnosis] %}

## Renewable Energy Systems

{% bibliography --query @*[keywords~=renewable-energy] %}

## Biomedical Systems Modeling

{% bibliography --query @*[keywords~=biomedical] %}

## Conferences & Workshops

{% bibliography --query @inproceedings %}

## Theses & Software

{% bibliography --query @mastersthesis %}
{% bibliography --query @phdthesis %}
{% bibliography --query @softwareversion %}

</div>