---
layout: page
permalink: /Publications/
title: Publications
description: ""
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

{% assign journal_articles = site.data.bibliography.references | where: "type", "article" %}
{% assign patents = site.data.bibliography.references | where: "type", "patent" %}
{% assign conferences = site.data.bibliography.references | where: "type", "inproceedings" %}
{% assign misc = site.data.bibliography.references | where: "type", "misc" %}
{% assign phd_theses = site.data.bibliography.references | where: "type", "phdthesis" %}
{% assign master_theses = site.data.bibliography.references | where: "type", "mastersthesis" %}
{% assign software = site.data.bibliography.references | where: "type", "softwareversion" %}

<div class="publication-summary">

  <div class="publication-summary-card">
    <strong>{{ journal_articles | size }}</strong>
    <span>Journal Articles</span>
  </div>

  <div class="publication-summary-card">
    <strong>{{ conferences | size }}</strong>
    <span>Conference Papers</span>
  </div>

  <div class="publication-summary-card">
    <strong>{{ patents | size }}</strong>
    <span>Patents</span>
  </div>

  <div class="publication-summary-card">
    <strong>{{ software | size }}</strong>
    <span>Software</span>
  </div>

  <div class="publication-summary-card">
    <strong>{{ phd_theses | size | plus: master_theses.size }}</strong>
    <span>Theses</span>
  </div>

</div>

<div class="publications">

<h2>Journal Articles</h2>

{% bibliography --query @article %}

<h2>Patents</h2>

{% bibliography --query @patent %}

<h2>Conference Papers and Presentations</h2>

{% bibliography --query @inproceedings %}
{% bibliography --query @misc %}

<h2>Theses</h2>

{% bibliography --query @phdthesis %}
{% bibliography --query @mastersthesis %}

<h2>Software</h2>

{% bibliography --query @softwareversion %}

</div>