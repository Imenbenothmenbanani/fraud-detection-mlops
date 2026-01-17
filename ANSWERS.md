# TP1 Git - Answers Document
**Student:** Imen BEN OTHMEN BANANI
**Date:** JANVIER 17, 2026

---

## PARTIE 1: Préparation de l'environnement Git

### Question 4: Vérifier la configuration actuelle de Git

**Question:** Comment vérifier la configuration actuelle de Git sur votre machine, notamment le nom d'utilisateur et l'adresse e-mail ?

**Réponse:**
```bash
git config --list
git config --global user.name
git config --global user.email
```

**Résultat:**
```
git version 2.35.0.windows.1
user.name=Imenbenothmenbanani
user.email=imenbenothmen@gmail.com
```

---

### Question 5: Modifier l'adresse e-mail

**Question:** Comment modifier votre adresse e-mail si vous l'avez mal configurée lors de l'installation de Git ?

**Réponse:**
```bash
git config --global user.email "nouvelle@email.com"
```

**Vérification:**
```bash
git config --global user.email
```

---

## PARTIE 2: Création d'un nouveau projet

### Question 6: Ajouter README.md après coup

**Question:** Si vous avez oublié de créer un fichier README.md lors de l'initialisation du projet, comment pouvez-vous l'ajouter après coup et committer les changements ?

**Réponse:**
```bash
# Créer le fichier README.md
echo "# Fraud Detection MLOps Project" > README.md

# Ajouter au staging
git add README.md

# Committer
git commit -m "Add README.md"

# Pousser vers GitHub
git push origin main
```

---

### Question 7: Définir un dépôt distant

**Question:** Comment définir un dépôt distant si vous n'en avez pas configuré un lors de la création du projet ?

**Réponse:**
```bash
# Ajouter un dépôt distant
git remote add origin git@github.com:username/repo-name.git

# Vérifier les dépôts distants
git remote -v

# Résultat:
# origin  git@github.com:Imenbenothmenbanani/fraud-detection-mlops.git (fetch)
# origin  git@github.com:Imenbenothmenbanani/fraud-detection-mlops.git (push)
```

---

## PARTIE 3: Concepts de base de Git

### Question 3: Annuler les modifications locales

**Question:** Comment annuler les modifications locales d'un fichier avant de les ajouter à l'index ?

**Réponse:**
```bash
# Méthode moderne (Git 2.23+)
git restore filename

# Ancienne méthode
git checkout -- filename

# Exemple:
git restore eda.py
```

**Explication:** Cette commande restaure le fichier à l'état du dernier commit, annulant toutes les modifications locales non staged.

---

### Question 4: Visualiser les fichiers en staging

**Question:** Comment visualiser les fichiers qui sont prêts à être committés dans Git (staging) ?

**Réponse:**
```bash
# Voir le statut général
git status

# Voir les différences des fichiers en staging
git diff --staged

# Alternative
git diff --cached

# Voir uniquement les noms des fichiers en staging
git diff --staged --name-only
```

**Exemple de sortie:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   eda.py
```

---

## PARTIE 4: Collaborer sur Git

### Question 4: Suivre un dépôt distant

**Question:** Comment suivre (track) un dépôt distant et récupérer toutes les branches de ce dépôt ?

**Réponse:**
```bash
# Ajouter un dépôt distant (ex: upstream)
git remote add upstream git@github.com:original-owner/repo.git

# Récupérer toutes les branches du dépôt distant
git fetch upstream

# Ou récupérer de tous les remotes
git fetch --all

# Lister toutes les branches (locales et distantes)
git branch -a

# Lister uniquement les branches distantes
git branch -r
```

**Résultat actuel:**
```
  experiment-eda
  feature-rebase
* main
  remotes/origin/experiment-eda
  remotes/origin/main
```

---

### Question 5: Supprimer une branche locale

**Question:** Comment supprimer une branche locale après l'avoir fusionnée dans master ?

**Réponse:**
```bash
# Supprimer une branche fusionnée (safe)
git branch -d branch-name

# Forcer la suppression (si pas fusionnée)
git branch -D branch-name

# Supprimer une branche distante
git push origin --delete branch-name

# Exemple:
git branch -d feature-rebase
git push origin --delete experiment-eda
```

---

## PARTIE 5: Rebase d'une branche sur 'master'

### Question 8: Interrompre un rebase

**Question:** Comment interrompre un rebase en cours si vous avez commis une erreur ?

**Réponse:**
```bash
# Annuler complètement le rebase en cours
git rebase --abort
```

**Explication:** Cette commande:
- Annule toutes les modifications du rebase
- Retourne au point avant le début du rebase
- Restaure l'état initial de la branche

**Autres commandes utiles pendant un rebase:**
```bash
# Continuer après résolution de conflit
git rebase --continue

# Sauter le commit actuel
git rebase --skip

# Voir l'état du rebase
git status
```

---

### Question 9: Lister les commits avant rebase

**Question:** Comment lister les commits qui vont être rebasés avant de lancer un rebase ?

**Réponse:**
```bash
# Méthode 1: Voir les commits entre deux branches
git log main..feature-branch

# Méthode 2: Format compact (recommandé)
git log --oneline main..feature-branch

# Méthode 3: Avec graphe visuel
git log --oneline --graph main..feature-branch

# Méthode 4: Compter le nombre de commits
git log --oneline main..feature-branch | wc -l
```

**Exemple réalisé:**
```bash
git log --oneline main..feature-rebase
# Résultat:
# cc733dd Update README with project information
# ea284a8 Add requirements.txt
```

**Explication:** 
- `main..feature-branch` montre les commits dans `feature-branch` mais PAS dans `main`
- Ces commits seront "rejoués" sur main lors du rebase

---

## RÉSUMÉ DES COMMANDES EFFECTUÉES

### Historique complet du projet:
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

### Fichiers créés:
1. eda.py - Script d'analyse exploratoire
2. requirements.txt - Dépendances Python
3. README.md - Documentation du projet
4. data/.gitkeep - Structure de dossiers

### Branches utilisées:
- main (branche principale)
- experiment-eda (développement de fonctionnalités)
- feature-rebase (démonstration du rebase)

### Opérations Git réalisées:
✅ Configuration SSH
✅ Clone du repository
✅ Commits multiples
✅ Création de branches
✅ Merge avec résolution de conflits
✅ Rebase
✅ Push vers GitHub

---

## CONCEPTS CLÉS APPRIS

1. **Workflow Git de base:**
   - Working Directory → Staging (git add) → Repository (git commit)

2. **Branches:**
   - Permettent le développement isolé de fonctionnalités
   - Se fusionnent via merge ou rebase

3. **Merge vs Rebase:**
   - **Merge:** Garde l'historique complet, crée un commit de merge
   - **Rebase:** Historique linéaire, "rejoue" les commits

4. **Conflits:**
   - Se produisent quand des modifications touchent les mêmes lignes
   - Nécessitent une résolution manuelle

5. **Remote:**
   - origin: Votre dépôt (ou fork)
   - upstream: Dépôt original (pour contributions open source)

---

**Repository GitHub:** https://github.com/Imenbenothmenbanani/fraud-detection-mlops

**Date de soumission:** 30 octobre 2025
