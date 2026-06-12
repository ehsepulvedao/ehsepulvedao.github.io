---
layout: page
title: PV-FIT
subtitle: Functional and Time-Frequency Toolkit for Interpretable Anomaly Detection in Photovoltaic Signals
description: FREE 2026 project dedicated to functional data analysis, time-frequency representations and frugal AI for photovoltaic fault diagnosis.
img: assets/img/FREEPVFIT.png
category: energy
importance: 2
period: 2026–2027
status: Ongoing
role: Co-Principal Investigator (Co-PI) / project initiator / Project Coordinator
funding: Fédération de Recherche Energie Environnement (FREE 2043)
related_publications: true
---

# Overview

PV-FIT (Photovoltaic Functional and Time-Frequency Toolkit) is a collaborative research project funded by the Fédération de Recherche Energie Environnement (FREE 2043) and jointly developed by PROMES-CNRS and LAMPS.

The project aims to develop a new generation of interpretable, frugal and deployable diagnostic tools for photovoltaic systems by exploiting only the electrical signals already available within photovoltaic inverters. Unlike approaches relying on additional sensors, infrared inspections or complex instrumentation, PV-FIT focuses on voltage, current and power measurements continuously collected during normal operation.

The project combines functional data analysis, time-frequency signal representations, interpretable machine learning and embedded artificial intelligence to create practical tools for photovoltaic fault diagnosis and predictive maintenance.

# Funding

**Fédération de Recherche Energie Environnement (FREE 2043)**

# Participating Laboratories

**PROMES-CNRS (UPR 8521)**

**LAMPS (EA 4217)**

# Project Team

- Edgar Hernando Sepúlveda-Oviedo (PROMES-CNRS)
- Issam-Ali Moindjié (LAMPS)

# Scientific Context

Photovoltaic systems generate large amounts of electrical signals that contain valuable information regarding their operating conditions and health status.

Current diagnostic approaches frequently rely on:

- Infrared imaging
- Electroluminescence imaging
- I-V curve analysis
- Additional maintenance sensors
- Black-box machine learning models

Although effective, these approaches often require additional hardware, dedicated inspections, high operational costs or exhibit limited interpretability.

PV-FIT proposes an alternative strategy based exclusively on existing inverter measurements. The project explores how functional representations of voltage, current and power signals can reveal fault signatures while preserving interpretability and enabling future embedded implementation.

# Main Objectives

The project pursues the following objectives:

- Develop functional representations of photovoltaic electrical signals.
- Investigate time-frequency representations for anomaly detection.
- Create interpretable diagnostic models.
- Improve robustness against signal variability and operating conditions.
- Develop computationally frugal diagnostic approaches.
- Facilitate future deployment on embedded hardware platforms.
- Build an open-source toolkit for photovoltaic signal analysis.

# Methodology

PV-FIT follows a five-stage methodology ranging from raw signal acquisition to embedded deployment.

<div class="row justify-content-center">
  <div class="col-sm-12 mt-3 mt-md-0">
    {% include figure.liquid
    loading="eager"
    path="assets/img/projects/12.jpg"
    title="PV-FIT Methodology"
    class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="caption">
Overview of the PV-FIT methodology. The framework progresses from photovoltaic signal acquisition to preprocessing, functional and time-frequency representations, interpretable modeling and embedded deployment.
</div>

## Stage 1 – Signal Acquisition

Collection of photovoltaic electrical signals directly from inverter measurements:

- Voltage
- Current
- Power

The approach intentionally avoids additional instrumentation to maintain low deployment costs.

## Stage 2 – Signal Preprocessing

Signal conditioning operations including:

- Filtering
- Denoising
- Normalization
- Standardization

The objective is to obtain robust and comparable signal representations.

## Stage 3 – Functional and Time-Frequency Representations

Transformation of electrical signals into richer representations through:

- Functional Data Analysis (FDA)
- Functional signal representations
- Spectrograms
- Time-frequency decompositions

These representations preserve more information than traditional statistical descriptors.

## Stage 4 – Interpretable Modeling

Development of explainable and physically meaningful diagnostic models using:

- Functional Partial Least Squares (fPLS)
- Hybrid machine learning models
- Interpretable classifiers
- Functional regression techniques

Particular attention is devoted to model transparency and engineering interpretability.

## Stage 5 – Embedded Deployment

Evaluation of computational frugality and deployment capabilities on resource-constrained platforms such as:

- Raspberry Pi
- ESP32
- Edge AI devices
- Smart photovoltaic monitoring systems

# Expected Outcomes

The project is expected to deliver:

- A functional photovoltaic signal analysis framework.
- Novel time-frequency diagnostic indicators.
- Explainable fault diagnosis methodologies.
- Embedded AI implementations.
- Open-source software libraries.
- Scientific publications.
- Conference presentations.
- Foundations for future doctoral projects and ANR proposals.

# Scientific Impact

PV-FIT contributes to the development of interpretable and frugal artificial intelligence for renewable energy systems.

By combining signal processing, functional statistics and explainable AI, the project seeks to improve photovoltaic monitoring while maintaining low computational requirements and practical deployability.

The methodologies developed within PV-FIT may also be transferable to batteries, industrial processes, smart grids and predictive maintenance applications.

# Keywords

Functional Data Analysis · Time-Frequency Analysis · Photovoltaic Systems · Fault Diagnosis · Explainable Artificial Intelligence · Signal Processing · Predictive Maintenance · Embedded AI · Renewable Energy · Functional Statistics

# Project Status

**Ongoing**