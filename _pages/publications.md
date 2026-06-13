---
layout: page
permalink: /Publications/
title: Publications
description: ""
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

<div class="publication-summary">

  <div class="publication-summary-card">
    <strong>12</strong>
    <span>Journal Articles</span>
  </div>

  <div class="publication-summary-card">
    <strong>9</strong>
    <span>Conference Papers</span>
  </div>

  <div class="publication-summary-card">
    <strong>1</strong>
    <span>Patent</span>
  </div>

  <div class="publication-summary-card">
    <strong>2</strong>
    <span>Theses</span>
  </div>

  <div class="publication-summary-card">
    <strong>1</strong>
    <span>Software & Data</span>
  </div>

  <div class="publication-summary-card">
    <strong>25+</strong>
    <span>Total Publications</span>
  </div>

</div>

<div class="publications">

<h2>Journal Articles</h2>

{% bibliography --query @article %}

<h2>Patents</h2>

{% bibliography --query @patent %}

<h2>Conference Papers and Presentations</h2>

{% bibliography --query @inproceedings %}

<h2>Theses</h2>

{% bibliography --query @phdthesis %}
{% bibliography --query @mastersthesis %}

<h2>Software and Data</h2>

{% bibliography --query @softwareversion %}

</div>