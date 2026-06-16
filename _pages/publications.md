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

{% for item in site.data.zenodo_stats.records %}
  {% if item.zenodo_id == "10054995" %}
    {% assign software_views = item.views %}
    {% assign software_downloads = item.downloads %}
  {% endif %}
{% endfor %}

<div class="publication-summary publication-summary-main">

  <div class="publication-summary-card">
    <strong>12</strong>
    <span>Journal Articles</span>
  </div>

  <div class="publication-summary-card">
    <strong>9</strong>
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

</div>

<div class="publication-summary publication-summary-software">

  <div class="publication-summary-card">
    <strong>1</strong>
    <span>Software</span>
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

<div class="publication-summary publication-summary-citations">

  <div class="publication-summary-card publication-summary-card-citations">
    <strong id="scholar-total-citations">—</strong>
    <span>Total Citations</span>
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

<script>
(function () {
  function extractCitationValueFromText(text) {
    if (!text) return 0;

    let raw = String(text).replace(/\s+/g, " ").trim();
    let decoded = raw;

    try {
      decoded = decodeURIComponent(raw);
    } catch (e) {
      decoded = raw;
    }

    const candidates = [raw, decoded];

    for (const candidate of candidates) {
      const patterns = [
        /scholar\s*[:\-]?\s*(\d+)/i,
        /google\s*scholar\s*[:\-]?\s*(\d+)/i,
        /cited\s*by\s*(\d+)/i,
        /citations?\s*[:\-]?\s*(\d+)/i,
        /badge\/scholar-(\d+)/i,
        /badge\/google\s*scholar-(\d+)/i,
        /badge\/Google%20Scholar-(\d+)/i,
        /message=(\d+)/i,
        /scholar-(\d+)/i,
        /google-scholar-(\d+)/i,
        /google_scholar-(\d+)/i
      ];

      for (const pattern of patterns) {
        const match = candidate.match(pattern);
        if (match) {
          return parseInt(match[1], 10);
        }
      }
    }

    return 0;
  }

  function extractCitationValueFromElement(el) {
    let best = 0;

    const attributes = [
      "textContent",
      "alt",
      "title",
      "aria-label",
      "data-original-title",
      "href",
      "src"
    ];

    attributes.forEach(function (attr) {
      let value = "";

      if (attr === "textContent") {
        value = el.textContent || "";
      } else {
        value = el.getAttribute(attr) || "";
      }

      const extracted = extractCitationValueFromText(value);
      if (extracted > best) best = extracted;
    });

    return best;
  }

  function extractScholarCitationsFromPublication(publicationElement) {
    let bestValue = 0;

    const fullText = publicationElement.textContent || "";
    const fullTextValue = extractCitationValueFromText(fullText);
    if (fullTextValue > bestValue) bestValue = fullTextValue;

    const elements = publicationElement.querySelectorAll("a, span, img, div, small, button, object, svg");

    elements.forEach(function (el) {
      const value = extractCitationValueFromElement(el);
      if (value > bestValue) bestValue = value;
    });

    return bestValue;
  }

  function updateScholarCitationTotal() {
    const target = document.getElementById("scholar-total-citations");
    if (!target) return;

    let total = 0;

    const publicationItems = document.querySelectorAll(".publications li");

    publicationItems.forEach(function (item) {
      total += extractScholarCitationsFromPublication(item);
    });

    target.textContent = total > 0 ? total : "—";
  }

  function startScholarCitationObserver() {
    const publicationsContainer = document.querySelector(".publications");
    if (!publicationsContainer) return;

    const observer = new MutationObserver(function () {
      updateScholarCitationTotal();
    });

    observer.observe(publicationsContainer, {
      childList: true,
      subtree: true,
      characterData: true,
      attributes: true,
      attributeFilter: ["src", "href", "alt", "title", "aria-label", "data-original-title"]
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    updateScholarCitationTotal();
    startScholarCitationObserver();

    setTimeout(updateScholarCitationTotal, 500);
    setTimeout(updateScholarCitationTotal, 1000);
    setTimeout(updateScholarCitationTotal, 2000);
    setTimeout(updateScholarCitationTotal, 4000);
    setTimeout(updateScholarCitationTotal, 8000);
    setTimeout(updateScholarCitationTotal, 12000);
  });
})();
</script>