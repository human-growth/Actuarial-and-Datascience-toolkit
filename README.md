# ACTUARIAT & DATASCIENCE 

Ma collection de projets et outils pour l'actuariat

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ton-username/actuarial-toolkit)]()

---

## À propos

Ce repository regroupe mes projets académiques et personnels en **science actuarielle** et en **science de la donnée** (Machine learning et IA).

**Objectifs** :
- Documenter mes apprentissages
- Implémenter les concepts théoriques en code Python
- Créer des outils réutilisables pour l'actuariat


---

## Projets principaux

### 1. Modélisation des Distributions
Implémentation des lois de probabilité utilisées en actuariat :
- **Discrètes** : Binomiale, Poisson, Binomiale Négative
- **Continues** : Exponentielle, Gamma, Normale, Pareto

[📂 Voir le code](01_distributions/) | [📓 Notebook](notebooks/01_intro_distributions.ipynb)

---

### 2. Tarification (Pricing)
**Projet** : Modèle de tarification auto avec GLM

- Méthode fréquence-coût
- Modèles linéaires généralisés (GLM)
- Segmentation par profil de risque

[📂 Voir le code](02_pricing/) | [📓 Notebook](notebooks/02_case_study_auto_insurance.ipynb)


---

### 3. Modélisation de la Fréquence
**Projet** : Prédiction du nombre de sinistres

- Loi de Poisson
- Poisson non-homogène
- Détection de la surdispersion

[📂 Voir le code](03_claims_modeling/)

---

### 4. Gestion des Risques
**Projet** : Simulation de la probabilité de ruine

- Modèle de Cramér-Lundberg
- Processus de Poisson composé
- Copules pour la dépendance

[📂 Voir le code](04_risk_management/) | [📓 Notebook](notebooks/03_ruin_probability.ipynb)

**Visualisation** :
![Simulation de ruine](assets/ruin_simulation.png)

---

### 5. Assurance Vie
**Projet** : Construction de tables de mortalité

- Calcul de probabilités de décès
- Lissage et ajustement
- Tarification d'une assurance décès temporaire

[📂 Voir le code](05_life_insurance/)

