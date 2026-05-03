# Integrating Hierarchical Clustering with Monte Carlo Simulation

## Toronto Pipe Failure Risk Modeling Project

---

## 1. Overview

This document outlines the integration of **Hierarchical Clustering (HC)** with **Monte Carlo (MC) simulation** to enhance infrastructure risk modeling within the Toronto Pipe Failure project.

The objective is to move beyond independent failure modeling and introduce **structural awareness** into the system by identifying groups of assets (pipes) that behave similarly under shared conditions.

---

## 2. Conceptual Framework

### Monte Carlo Simulation

Monte Carlo methods are used to estimate:

* Probabilistic failure outcomes
* Expected number of failures over time
* Cost distributions under uncertainty

**Key Question Answered:**

> *What could happen?*

---

### Hierarchical Clustering

Hierarchical clustering is used to:

* Identify groups of similar assets
* Capture structural relationships between pipes
* Reveal hidden patterns in failure behavior

**Key Question Answered:**

> *How are assets related?*

---

### Combined Insight

By integrating HC with MC:

> The system models **what could happen** while accounting for **how risk is structurally grouped and correlated**.

---

## 3. Application to Pipe Failure Modeling

### 3.1 Clustering Assets

Pipes can be grouped based on features such as:

* Age
* Material type
* Diameter
* Soil/environmental conditions
* Historical failure frequency

**Outcome:**

* Identification of clusters with similar failure characteristics
* Detection of high-risk groups
* Improved interpretability of system behavior

---

### 3.2 Cluster-Aware Simulation

Instead of treating each pipe independently:

* Assign each pipe a cluster label
* Model dependencies within clusters
* Introduce correlated failure behavior

**Benefits:**

* More realistic simulations
* Captures systemic risk rather than isolated events
* Reflects real-world infrastructure interdependencies

---

### 3.3 Risk Aggregation

Traditional output:

* Total expected failures

Enhanced output:

* Failures by cluster
* High-risk clusters
* Concentrated geographic or structural risk

This enables more targeted decision-making.

---

### 3.4 Scenario Analysis

Cluster-based modeling enables advanced scenario testing:

* Accelerated deterioration within a cluster
* Environmental stress impacts (e.g., soil shifts, weather)
* Deferred maintenance scenarios

**Result:**

* More meaningful stress testing
* Insight into system vulnerabilities

---

## 4. System Architecture

### Pipeline Overview

```
Raw Data
   ↓
Feature Engineering
   ↓
Hierarchical Clustering
   ↓
Cluster Labels
   ↓
Monte Carlo Simulation (cluster-aware)
   ↓
Risk Outputs (cluster-level + system-wide)
```

---

## 5. Implementation Considerations

### 5.1 Clustering Strategy

* Use correlation or feature-based distance metrics
* Evaluate linkage methods (Ward, average, complete)
* Validate cluster stability

---

### 5.2 Feature Selection

Critical to clustering quality. Ensure features are:

* Relevant to failure behavior
* Properly scaled/normalized
* Free of excessive noise

---

### 5.3 Simulation Design

* Incorporate intra-cluster correlation
* Avoid assuming full independence across assets
* Balance realism with computational efficiency

---

## 6. Risks and Pitfalls

### Avoid:

* Adding clustering without clear purpose
* Using clusters without interpretation
* Overcomplicating the model without measurable benefit

---

### Ensure:

* Clear linkage between clusters and simulation outcomes
* Interpretability of cluster behavior
* Justification for modeling assumptions

---

## 7. Value Proposition

This approach transforms the project from:

> “Predicting individual pipe failures”

to:

> “Modeling infrastructure risk as an interconnected system with structural dependencies”

---

## 8. Conclusion

Integrating Hierarchical Clustering with Monte Carlo simulation provides:

* Improved realism in failure modeling
* Better understanding of system-level risk
* Enhanced decision-support capabilities

This positions the project as a **system-level risk modeling framework**, rather than a simple predictive model.

---
