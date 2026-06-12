---
layout: page
title: ALARMES
subtitle: Automatic Alarm Extraction and Modeling of Photovoltaic Operational Events
description: Explainable event-based representation and automatic alarm extraction for photovoltaic systems.
img: assets/img/alarmes.png
category: energy
importance: 3
period: 2025–ongoing
status: Ongoing
role: Scientific Lead
funding: PROMES-CNRS CSPG
related_publications: true
---

# Overview

ALARMES (Automatic Alarm Extraction and Modeling of Photovoltaic Operational Events) is a research project developed within the CSPG (Centrales Solaires de Prochaines Générations) thematic area at PROMES-CNRS.

The project aims to bridge the gap between continuous signal analysis and operational decision-making by transforming complex photovoltaic system dynamics into interpretable operational alarms.

Rather than directly relying on raw electrical measurements, ALARMES seeks to construct structured representations of photovoltaic behavior that can be interpreted by engineers, operators and diagnostic systems.

The project represents the intermediate layer between signal processing and intelligent decision support within the broader diagnostic ecosystem developed at PROMES-CNRS.

# Funding

PROMES-CNRS – CSPG Research Activities

# Host Institution

PROMES-CNRS (UPR 8521)

Université de Perpignan Via Domitia (UPVD)

# Scientific Context

Modern photovoltaic systems continuously generate large quantities of electrical measurements, including current, voltage and power signals.

Although these measurements contain valuable information regarding system health, they generally provide only an aggregated view of system behavior. As a consequence, subtle internal phenomena often remain hidden within continuous signal trajectories.

Current diagnostic approaches frequently rely on global indicators or machine learning classifiers that provide limited interpretability.

ALARMES addresses this limitation by introducing an event-based representation capable of translating continuous photovoltaic dynamics into meaningful operational events and alarms.

# Main Objectives

The project pursues several complementary objectives:

- Develop interpretable representations of photovoltaic dynamics.
- Model photovoltaic systems as interacting subsystems.
- Detect characteristic behavioral transitions.
- Transform continuous trajectories into symbolic events.
- Generate operational alarms automatically.
- Improve diagnostic interpretability.
- Facilitate explainable maintenance decisions.

# Methodology

The methodology is based on the progressive transformation of continuous electrical signals into structured operational knowledge.

<div class="row justify-content-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid
    loading="eager"
    path="assets/img/projects/alarmes_methodology.png"
    title="ALARMES Methodology"
    class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="caption">
Transformation of continuous photovoltaic degradation trajectories into interpretable symbolic event sequences and operational alarms.
</div>

## Stage 1 – Multi-Component System Modeling

The photovoltaic system is first decomposed into interacting subsystems:

- Photovoltaic modules
- Strings
- Power conversion stages
- Energy storage systems
- Monitoring infrastructure

This decomposition enables a more detailed understanding of internal system dynamics.

## Stage 2 – Dynamic Signal Analysis

Continuous electrical trajectories are analyzed to identify:

- Abrupt transitions
- Progressive drifts
- Sustained anomalies
- Recovery phases
- Oscillatory behaviors

The objective is to characterize the temporal organization of degradation mechanisms.

## Stage 3 – Event Extraction

Detected signal variations are transformed into symbolic events.

The current event alphabet includes:

- N → Nominal operation
- D → Progressive drift
- J → Abrupt jump
- A → Anomaly state
- O → Oscillatory behavior
- R → Recovery phase

This representation converts continuous trajectories into compact symbolic descriptions.

## Stage 4 – Alarm Generation

The extracted events are automatically transformed into operational alarms.

Examples include:

- Abrupt fault alarms
- Progressive degradation alarms
- Recovery notifications
- Persistent anomaly alerts

The generated alarms provide a direct and interpretable description of system behavior.

## Stage 5 – Explainable Decision Support

The final objective is to provide operators with interpretable information rather than simple fault labels.

The generated alarms preserve temporal information and facilitate understanding of degradation mechanisms.

# Example Event Sequences

Representative degradation trajectories can be described as:

### Open-Circuit Fault

N → J → A

### Short-Circuit Fault

N → A → R → N

### Progressive Degradation

N → D → D → A

These symbolic sequences provide a compact description of the temporal evolution of degradation phenomena.

# Scientific Contributions

The project introduces several original concepts:

- Event-based representation of photovoltaic degradation.
- Symbolic abstraction of continuous trajectories.
- Automatic alarm generation.
- Explainable photovoltaic diagnostics.
- Temporal modeling of degradation mechanisms.
- Integration of signal processing and decision support.

# Position within the Research Roadmap

ALARMES occupies the intermediate layer of the diagnostic chain:

SOL-DAQ → PV-FIT → ALARMES → SOL-MIND

where:

- SOL-DAQ provides diagnostic-oriented data acquisition.
- PV-FIT extracts interpretable signal representations.
- ALARMES transforms signals into operational events.
- SOL-MIND constructs cognitive maps and explainable decision spaces.

# Expected Outcomes

The project is expected to deliver:

- Event extraction algorithms.
- Alarm generation methodologies.
- Symbolic trajectory representations.
- Explainable diagnostic tools.
- Scientific publications.
- Integration into future monitoring platforms.

# Scientific Impact

ALARMES contributes to the development of explainable artificial intelligence for photovoltaic systems by introducing interpretable intermediate representations between raw signals and final diagnostic decisions.

The methodology may also be transferred to:

- Battery systems
- Smart grids
- Industrial monitoring
- Prognostics and Health Management (PHM)
- Cyber-physical systems

# Keywords

Photovoltaics · Alarm Management · Event-Based Systems · Explainable AI · Symbolic Trajectories · Fault Diagnosis · Prognostics and Health Management · Degradation Analysis · Decision Support

# Project Status

**Ongoing**