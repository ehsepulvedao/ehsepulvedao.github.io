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

{% assign teaching_views = 0 %}
{% assign teaching_downloads = 0 %}
{% assign teaching_unique_downloads = 0 %}
{% assign teaching_count = 0 %}

{% for item in site.data.zenodo_stats.records %}

  {% if item.key contains "motioncontrol" %}

    {% assign teaching_count = teaching_count | plus: 1 %}
    {% assign teaching_views = teaching_views | plus: item.views %}
    {% assign teaching_downloads = teaching_downloads | plus: item.downloads %}
    {% assign teaching_unique_downloads = teaching_unique_downloads | plus: item.unique_downloads %}

  {% endif %}

{% endfor %}

<div class="zenodo-summary">

  <div class="zenodo-summary-card">
    <strong>{{ teaching_count }}</strong>
    <span>Open Educational Resources</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ teaching_views }}</strong>
    <span>Views</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ teaching_downloads }}</strong>
    <span>Downloads</span>
  </div>

  <div class="zenodo-summary-card">
    <strong>{{ teaching_unique_downloads }}</strong>
    <span>Unique Downloads</span>
  </div>

</div>

<div class="publications">

<h2>Open Educational Resources</h2>

<p>
The following open educational resources correspond to laboratory guides and technical teaching materials developed for industrial automation, motion control and servomechanism training using the Allen-Bradley CompactLogix industrial platform.
</p>

{% bibliography --query @misc[type=Laboratory Guide] %}

</div>

<h2>Usage Statistics</h2>

<p>
The following table summarizes Zenodo usage statistics for the educational resources listed above.
</p>

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

  {% if item.key contains "motioncontrol" %}

<tr>
<td>
<a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">
{{ item.title }}
</a>
</td>
<td>{{ item.views }}</td>
<td>{{ item.downloads }}</td>
<td>{{ item.unique_downloads }}</td>
</tr>

  {% endif %}

{% endfor %}

</tbody>
</table>
</div>