---
layout: page
permalink: /Repositories/
title: Repositories
description: Open-source software, datasets, academic profiles, and research repositories.
nav: true
nav_order: 4
---

## GitHub Profile

{% if site.data.repositories.github_users %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>
{% endif %}

<br>

---

<br>

## Research Repositories

{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}

<br>

---

<br>

## Open Science & Academic Profiles

- [Google Scholar](https://scholar.google.com/citations?user=LbUy08MAAAAJ)
- [ORCID](https://orcid.org/0000-0002-9947-3259)
- [Scopus Author ID](https://www.scopus.com/authid/detail.uri?authorId=57468381700)
- [Semantic Scholar](https://www.semanticscholar.org/author/2076554609)
- [ResearchGate](https://www.researchgate.net/profile/Edgar-Sepulveda-Oviedo)
- [HAL](https://hal.science/search/index/q/*/authFullName_s/Edgar%20Hernando%20Sep%C3%BAlveda-Oviedo)
- [Zenodo](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Sep%C3%BAlveda-Oviedo%2C%20Edgar%20Hernando%22&l=list&p=1&s=10&sort=bestmatch)
- [Zotero](https://www.zotero.org/ehsepulvedao)

<br>

---

<br>

## Featured Resource

### PatientEvoPhysio

Open-source Modelica library for the simulation of neonatal, fetal, pediatric and adult physiological systems, including cardiovascular and respiratory dynamics.

- GitHub Repository: https://github.com/ehsepulvedao/PatientEvoPhysio
- DOI: https://doi.org/10.5281/zenodo.10054995