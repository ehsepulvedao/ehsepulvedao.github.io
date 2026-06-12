---
layout: page
permalink: /Repositories/
title: Repositories
description: ""
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
- [Zenodo](https://zenodo.org)
- [Zotero](https://www.zotero.org/ehsepulvedao)
