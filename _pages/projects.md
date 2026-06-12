---
layout: page
title: ""
permalink: /Projects/
description: ""
nav: true
nav_order: 1
display_categories: [energy, biomedical, education]
horizontal: true
---

<!-- pages/projects.md -->

<style>
  .projects .category {
    color: var(--global-text-color);
    font-size: 2.1rem;
    font-weight: 400;
    margin-top: 2.5rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--global-divider-color);
  }

  .projects .category-description {
    margin-bottom: 1.8rem;
    color: var(--global-text-color);
    font-size: 1rem;
    line-height: 1.6;
  }
</style>

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}

  {% for category in page.display_categories %}

  {% if category == "energy" %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">Artificial Intelligence for Energy Systems</h2>
  </a>
  <p class="category-description">
    Projects focused on artificial intelligence, fault diagnosis, predictive maintenance, instrumentation, digital twins, photovoltaic systems, batteries, smart grids and resilient energy systems.
  </p>

  {% elsif category == "biomedical" %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">Biomedical and Physiological Modeling</h2>
  </a>
  <p class="category-description">
    Projects dedicated to biological systems modeling, neonatal and fetal physiological simulation, clinical protocols, medical digital twins and open-source biomedical software.
  </p>

  {% elsif category == "education" %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">Engineering Education and Digital Learning</h2>
  </a>
  <p class="category-description">
    Pedagogical projects connecting research, digital laboratories, IoT, predictive maintenance, automation and active learning in engineering education.
  </p>
  {% endif %}

  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}

  <div class="row row-cols-1 row-cols-md-3 mb-5">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>

  {% endfor %}

{% else %}

{% assign sorted_projects = site.projects | sort: "importance" %}

<div class="row row-cols-1 row-cols-md-3">
  {% for project in sorted_projects %}
    {% include projects.liquid %}
  {% endfor %}
</div>

{% endif %}
</div>