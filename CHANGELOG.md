# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### À venir
- Système de notifications en temps réel
- Export de CV en PDF
- Intégration avec services de calendrier pour l'agenda
- Système de commentaires pour le blog
- API de recherche full-text avec Elasticsearch

## [1.0.0] - 2024-01-01

### Ajouté
- API REST complète pour portfolio
- Modèles de données:
  - UserProfile - Profils utilisateurs
  - Project - Gestion de projets
  - Experience - Expériences professionnelles
  - Education - Parcours académique
  - Skill - Compétences et expertises
  - BlogPost - Articles de blog
- Authentication JWT avec djangorestframework-simplejwt
- Documentation OpenAPI/Swagger automatique
- ViewSets DRF avec pagination, recherche et filtres
- Tests unitaires et d'intégration avec pytest
- Configuration Docker et docker-compose
- CI/CD GitHub Actions
- Health check endpoint pour monitoring
- Commande de seed pour données de test
- Configuration en environnements (dev, prod)
- Makefile avec commandes utiles
- Documentation complète (README, API_DOCS, QUICKSTART)
- Configuration Nginx pour reverse proxy
- Scripts de déploiement Ansible
- Code formatting avec black et isort
- Linting avec flake8

### Sécurité
- Validation des données avec serializers DRF
- Protection CSRF activée
- Permissions configurables par endpoint
- Variables sensibles dans .env
- Headers de sécurité en production

## [0.1.0] - 2023-12-01

### Ajouté
- Structure initiale du projet Django
- Configuration de base de Django REST Framework
- Setup PostgreSQL
- Configuration Docker basique

---

## Types de Changements

- `Ajouté` - Pour les nouvelles fonctionnalités
- `Modifié` - Pour les changements aux fonctionnalités existantes
- `Déprécié` - Pour les fonctionnalités qui seront retirées
- `Retiré` - Pour les fonctionnalités retirées
- `Corrigé` - Pour les corrections de bugs
- `Sécurité` - Pour les mises à jour de sécurité

[Unreleased]: https://github.com/yemal22/morel-api/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yemal22/morel-api/releases/tag/v1.0.0
[0.1.0]: https://github.com/yemal22/morel-api/releases/tag/v0.1.0
