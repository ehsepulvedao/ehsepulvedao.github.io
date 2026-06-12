---
layout: page
permalink: /Publications/
title: Publications
description: ""
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

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
