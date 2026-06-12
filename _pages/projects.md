---
layout: page
title: Projects
permalink: /projects/
description: ""
nav: true
nav_order: 1
display_categories: [energy, biomedical, education]
horizontal: true
---

<!-- pages/projects.md -->

<style>

  /* Oculta el título principal "Projects" de la página */
  .post-header {
    display: none;
  }

  /* Títulos de categorías */
  .projects .category {
    color: var(--global-text-color);
    font-size: 2.2rem;
    font-weight: 500;
    margin-top: 3rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--global-divider-color);
  }

  /* Descripción debajo de cada categoría */
  .projects .category-description {
    margin-bottom: 2rem;
    color: var(--global-text-color);
    opacity: 0.85;
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 1000px;
  }

</style>

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}

  {% for category in page.display_categories %}

  {% if category == "energy" %}
  <a id="{{ category }}" href="#{{ category }}">
    <h2 class="category">Artificial Intelligence for Energy Systems</h2>
  </a>
  <p class="category-description">
    Research projects focused on artificial intelligence, fault diagnosis, predictive maintenance, instrumentation, digital twins, photovoltaic systems, battery storage, smart grids and resilient energy infrastructures.
  </p>

  {% elsif category == "biomedical" %}
  <a id="{{ category }}" href="#{{ category }}">
    <h2 class="category">Biomedical and Physiological Modeling</h2>
  </a>
  <p class="category-description">
    Research activities dedicated to physiological simulation, neonatal and fetal modeling, biomedical digital twins, computational medicine and open-source biomedical software development.
  </p>

  {% elsif category == "education" %}
  <a id="{{ category }}" href="#{{ category }}">
    <h2 class="category">Engineering Education and Digital Learning</h2>
  </a>
  <p class="category-description">
    Educational innovation projects connecting research, IoT technologies, automation, predictive maintenance, digital laboratories and active learning methodologies in engineering education.
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