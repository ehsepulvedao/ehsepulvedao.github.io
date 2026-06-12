---
layout: page
title: SCODE
subtitle: Supervisory Control Deployment Environment
description: Framework for deploying supervisory control theory into PLC code and validating industrial automation through digital twins.
img: assets/img/scode.jpg
category: education
importance: 2
period: 2022–ongoing
status: Submitted research
role: Scientific Collaborator
related_publications: true
---

# Overview

SCODE (Supervisory Control Deployment Environment) is a research project dedicated to bridging the gap between formal supervisory control theory and practical industrial automation.

The project develops a reproducible framework for transforming discrete-event supervisory models into executable PLC code and validating the resulting control logic through digital twin environments.

SCODE connects formal methods, programmable logic controllers, digital twins and Industry 4.0 education.

# Scientific Context

Supervisory Control Theory provides a rigorous mathematical framework for the synthesis of correct-by-construction supervisors for discrete-event systems.

However, its practical deployment in industrial automation remains limited because formal supervisors are often difficult to translate into executable PLC programs.

Industrial control engineers usually implement logic manually in IEC 61131-3 languages, which can be time-consuming, error-prone and difficult to verify formally.

SCODE addresses this gap by proposing an end-to-end pipeline from formal synthesis to PLC implementation and digital twin validation.

# Main Objectives

The project pursues the following objectives:

- Operationalize Supervisory Control Theory in industrial automation.
- Automatically translate discrete-event supervisors into PLC code.
- Generate IEC 61131-3 Structured Text implementations.
- Validate supervisory control strategies in digital twin environments.
- Improve reproducibility of industrial control deployment.
- Support engineering education in automation and discrete-event systems.

# Methodology

SCODE follows a complete model-to-deployment pipeline.

<div class="row justify-content-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid
    loading="eager"
    path="assets/img/projects/scode_framework.png"
    title="SCODE Framework"
    class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="caption">
SCODE framework connecting supervisory control synthesis, automatic PLC code generation and digital twin validation.
</div>

## Stage 1 – Formal Modeling

Industrial systems are represented as discrete-event models using:

- Plant automata
- Specification automata
- Controllable events
- Uncontrollable events
- Marked states
- Forbidden states

## Stage 2 – Supervisor Synthesis

Supervisors are synthesized using Supervisory Control Theory.

The synthesis process ensures:

- Safety
- Nonblocking behavior
- Deterministic operation
- Compliance with specifications

## Stage 3 – PLC Code Generation

The synthesized supervisor is translated into executable industrial code.

The framework focuses on:

- IEC 61131-3 Structured Text
- PLC scan-cycle compatibility
- Deterministic execution
- Reproducible implementation

## Stage 4 – Digital Twin Validation

The generated control logic is validated using a digital twin architecture based on:

- OpenPLC
- Factory I/O
- Real-time closed-loop simulation
- Industrial case studies

# Main Contributions

SCODE contributes to:

- Bridging formal control and industrial automation.
- Reproducible PLC code generation.
- Digital twin validation of supervisory control.
- Correct-by-construction automation.
- Teaching of discrete-event systems and PLC programming.
- Industry 4.0 educational platforms.

# Educational Impact

SCODE provides a powerful framework for teaching automation beyond traditional manual PLC programming.

It allows students to understand the complete chain:

Formal model → supervisor synthesis → PLC implementation → digital twin validation.

This makes it particularly relevant for engineering education in automation, industrial maintenance and cyber-physical systems.

# Keywords

Supervisory Control Theory · Discrete-Event Systems · PLC · Structured Text · Digital Twin · OpenPLC · Factory I/O · Industrial Automation · Industry 4.0 · Engineering Education

# Project Status

**Submitted research**