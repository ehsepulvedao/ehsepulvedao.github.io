---
layout: page
permalink: /Publications/
title: Publications
description: Publications by type in reverse chronological order.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

{% include bib_search.liquid %}

<div class="publications">

## Journal Articles

{% bibliography --query @article %}

## Conference Papers and Presentations

{% bibliography --query @inproceedings %}
{% bibliography --query @misc %}

## Theses

{% bibliography --query @phdthesis %}
{% bibliography --query @mastersthesis %}

## Software

{% bibliography --query @softwareversion %}

</div>