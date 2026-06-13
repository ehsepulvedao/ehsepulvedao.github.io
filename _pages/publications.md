---
layout: page
permalink: /Publications/
title: Publications
description: ""
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

{% assign software_views = 0 %}
{% assign software_downloads = 0 %}
{% assign software_unique_downloads = 0 %}

{% for item in site.data.zenodo_stats.records %}
  {% if item.zenodo_id == "10054995" %}
    {% assign software_views = item.views %}
    {% assign software_downloads = item.downloads %}
    {% assign software_unique_downloads = item.unique_downloads %}
  {% endif %}
{% endfor %}

<div class="publication-summary">

  <div class="publication-summary-card">
    <strong>23</strong>
    <span>Journal Articles</span>
  </div>

  <div class="publication-summary-card">
    <strong>15</strong>
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
    <strong>{{ software_downloads }}</strong>
    <span>Software Downloads</span>
  </div>

  <div class="publication-summary-card">
    <strong>{{ software_views }}</strong>
    <span>Software Views</span>
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