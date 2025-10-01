"""
Implémentation de la loi de Poisson
Cours de Statistique Actuarielle - Master 1
------------------------------------------------
Dans ce fichier je définie des fonctions simples et commentées
pour comprendre la loi de Poisson et l'appliquer à des cas d'assurance.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

# Définissons la fonction masse de probabilité de la Poisson
def poisson_pmf(k, lam):
    """
    Loi de Poisson : probabilité que N = k
    Formule :
        P(N=k) = (λ^k * e^(-λ)) / k!
    """
    return (lam**k * exp(-lam)) / factorial(k)

# Elaborons une fonction qui nous permettra de simuler les réalisation d'une Poisson
def simulate_poisson(lam, n):
    """
    Simuler n réalisations d'une loi de Poisson(λ).
    """
    return np.random.poisson(lam, size=n)

# Enfin créons une fonction de génération de graphique qui nous évitera de rédiger du code redondant
def plot_poisson(lam, k_max=20):
    """
    Visualiser la loi de Poisson jusqu'à k_max.
    """
    ks = range(0, k_max+1)
    probs = [poisson_pmf(k, lam) for k in ks]
    plt.bar(ks, probs)
    plt.title(f"Loi de Poisson (λ={lam})")
    plt.xlabel("k (nombre de sinistres)")
    plt.ylabel("P(N=k)")
    plt.show()

