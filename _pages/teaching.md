---
layout: page
permalink: /Teaching/
title: Teaching
description: ""
nav: true
nav_order: 3
---

{% include bib_search.liquid %}

Teaching activities, course materials, laboratory resources and pedagogical projects developed in the fields of industrial engineering, automation, artificial intelligence, renewable energy systems and maintenance engineering.

<div class="zenodo-summary">

  <div class="zenodo-summary-card">
    <strong>{{ site.data.zenodo_stats.totals.records }}</strong>
    <span>Open Resources</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ site.data.zenodo_stats.totals.views }}</strong>
    <span>Zenodo Views</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ site.data.zenodo_stats.totals.downloads }}</strong>
    <span>Zenodo Downloads</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ site.data.zenodo_stats.totals.unique_downloads }}</strong>
    <span>Unique Downloads</span>
  </div>

</div>

<div class="publications">

<h2>Open Educational Resources</h2>

The following open educational resources correspond to laboratory guides and technical teaching materials developed for industrial automation, motion control and servomechanism training using the Allen-Bradley CompactLogix industrial platform.

{% bibliography --query @misc[keywords~=teaching-material] %}

</div>

<h2>Zenodo Usage Statistics</h2>

<div class="table-responsive">
<table class="table table-sm table-striped">
<thead>
<tr>
<th>Resource</th>
<th>Views</th>
<th>Downloads</th>
<th>Unique Downloads</th>
</tr>
</thead>
<tbody>
{% for item in site.data.zenodo_stats.records %}
<tr>
<td><a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">{{ item.title }}</a></td>
<td>{{ item.views }}</td>
<td>{{ item.downloads }}</td>
<td>{{ item.unique_downloads }}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>