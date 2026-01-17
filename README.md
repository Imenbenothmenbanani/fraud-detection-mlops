# Fraud Detection MLOps Project

## 📋 Description
Ce projet implémente un système de détection de fraude en utilisant les meilleures pratiques MLOps. Il a été développé dans le cadre du **TP1 - Maîtrise de Git** pour démontrer la gestion de projets ML avec Git.

## 🎯 Objectifs du TP
- Maîtriser Git pour la gestion de projets ML
- Appliquer Git dans un workflow MLOps
- Gérer les branches, conflits, et opérations avancées (merge, rebase)

## 📁 Structure du Projet
```
fraud-detection-mlops/
├── eda.py              # Script d'analyse exploratoire des données
├── requirements.txt    # Dépendances Python
├── ANSWERS.md         # Réponses aux questions du TP
├── README.md          # Documentation du projet
└── data/              # Dossier pour les datasets
```

## 🚀 Installation
```bash
# Cloner le repository
git clone git@github.com:Imenbenothmenbanani/fraud-detection-mlops.git
cd fraud-detection-mlops

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Usage
```bash
# Exécuter l'analyse exploratoire
python eda.py
```

Le script génère:
- Statistiques descriptives
- Histogrammes des features
- Heatmap de corrélation

## 📚 Travail Réalisé (TP1)

### ✅ Partie 1: Préparation de l'environnement Git
- Configuration SSH et Git
- Connexion aux dépôts distants

### ✅ Partie 2: Création du projet
- Création du repository sur GitHub
- Clone et configuration initiale

### ✅ Partie 3: Concepts de base
- Commits, staging, historique
- Gestion des modifications

### ✅ Partie 4: Collaboration
- Création et gestion de branches
- Résolution de conflits (merge)
- Push vers dépôt distant

### ✅ Partie 5: Rebase
- Rebase de `experiment-eda` sur `main`
- Intégration propre sans commit de merge

## 🌿 Branches Utilisées
- `main` - Branche principale
- `experiment-eda` - Développement de visualisations (fusionnée)
- `feature-rebase` - Démonstration du rebase (fusionnée)

## 📊 Historique Git
```
* 8a88fb6 Update README with project information
* ac59747 Add requirements.txt
* ee4350f Add data folder structure
*   ee5feca Résolution du conflit entre main et experiment-eda
|\
| * db15845 Modification de experiment-eda: ajout visualisations
* | e892cb9 Modification dans main: changement de source de données
|/
* fa24b3c Premier commit : ajout de eda.py
```

## 📝 Documentation Complète
Toutes les réponses aux questions du TP sont disponibles dans **[ANSWERS.md](ANSWERS.md)**.

## 👤 Auteur
**Imen BEN OTHMEN BANANI**  
Étudiant en MLOps - 2025

## 🔗 Repository
https://github.com/Imenbenothmenbanani/fraud-detection-mlops

---
*Projet réalisé dans le cadre du cours MLOps - TP1: Maîtrise de Git*
