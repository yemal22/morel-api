# 📂 Structure Complète du Projet

```
morel-api/
│
├── 📁 .github/
│   └── workflows/
│       └── ci-cd.yml                    # Pipeline CI/CD GitHub Actions
│
├── 📁 apps/                             # Applications Django
│   ├── 📁 portfolio/                    # App principale du portfolio ⭐
│   │   ├── __init__.py
│   │   ├── admin.py                     # Configuration admin Django
│   │   ├── apps.py                      # Configuration de l'app
│   │   ├── models.py                    # Modèles (UserProfile, Project, etc.)
│   │   ├── serializers.py               # Serializers DRF
│   │   ├── views.py                     # ViewSets API
│   │   ├── urls.py                      # Routes API
│   │   ├── 📁 migrations/               # Migrations de base de données
│   │   │   └── __init__.py
│   │   ├── 📁 management/               # Commandes personnalisées
│   │   │   ├── __init__.py
│   │   │   └── commands/
│   │   │       ├── __init__.py
│   │   │       └── seed_data.py         # Commande pour peupler la BD
│   │   └── 📁 tests/                    # Tests
│   │       ├── __init__.py
│   │       ├── test_models.py           # Tests des modèles
│   │       ├── test_serializers.py      # Tests des serializers
│   │       └── test_api.py              # Tests des endpoints API
│   │
│   ├── 📁 blog/                         # App blog (structure prête)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── migrations/
│   │
│   ├── 📁 agenda/                       # App agenda (structure prête)
│   │   └── ...
│   │
│   ├── 📁 cv/                           # App CV (structure prête)
│   │   └── ...
│   │
│   └── 📁 users/                        # App utilisateurs (structure prête)
│       └── ...
│
├── 📁 config/                           # Configuration Django
│   ├── __init__.py
│   ├── asgi.py                          # Configuration ASGI
│   ├── wsgi.py                          # Configuration WSGI
│   ├── urls.py                          # URLs principales
│   └── 📁 settings/                     # Settings divisés ⭐
│       ├── __init__.py                  # Import automatique dev/prod
│       ├── base.py                      # Settings de base
│       ├── dev.py                       # Settings développement
│       └── prod.py                      # Settings production
│
├── 📁 deployment/                       # Scripts de déploiement
│   ├── deploy.yml                       # Playbook Ansible
│   ├── inventory.ini.example            # Exemple d'inventaire
│   └── templates/
│       └── .env.j2                      # Template d'environnement
│
├── 📁 nginx/                            # Configuration Nginx
│   └── nginx.conf                       # Config reverse proxy
│
├── 📁 media/                            # Fichiers médias (uploadés)
│   └── .gitkeep
│
├── 📁 staticfiles/                      # Fichiers statiques (collectés)
│   └── .gitkeep
│
├── 📄 .dockerignore                     # Fichiers ignorés par Docker
├── 📄 .env.example                      # Exemple de variables d'env ⭐
├── 📄 .flake8                           # Config flake8
├── 📄 .gitignore                        # Fichiers ignorés par Git
│
├── 📄 API_DOCS.md                       # Documentation API complète ⭐
├── 📄 CHANGELOG.md                      # Historique des versions
├── 📄 CONTRIBUTING.md                   # Guide de contribution
├── 📄 LICENSE                           # Licence MIT
├── 📄 QUICKSTART.md                     # Guide de démarrage rapide ⭐
├── 📄 README.md                         # Documentation principale ⭐
│
├── 📄 conftest.py                       # Fixtures pytest globales ⭐
├── 📄 docker-compose.dev.yml            # Override pour développement
├── 📄 docker-compose.yml                # Configuration Docker Compose ⭐
├── 📄 Dockerfile                        # Image Docker ⭐
├── 📄 docker-entrypoint.sh              # Script de démarrage Docker
│
├── 📄 manage.py                         # Commande Django
├── 📄 Makefile                          # Commandes utiles ⭐
├── 📄 pyproject.toml                    # Config black/isort
├── 📄 pytest.ini                        # Configuration pytest ⭐
└── 📄 requirements.txt                  # Dépendances Python ⭐

```

## 📝 Légende

- ⭐ = Fichiers/dossiers principaux à connaître
- 📁 = Dossier
- 📄 = Fichier

## 🎯 Fichiers Clés

### Configuration
- **`.env.example`** - Variables d'environnement
- **`config/settings/`** - Settings Django (base/dev/prod)
- **`requirements.txt`** - Dépendances Python

### Docker
- **`Dockerfile`** - Image Docker de l'application
- **`docker-compose.yml`** - Orchestration des services
- **`docker-entrypoint.sh`** - Script de démarrage

### Code Principal
- **`apps/portfolio/models.py`** - 6 modèles de données
- **`apps/portfolio/serializers.py`** - Serializers DRF
- **`apps/portfolio/views.py`** - ViewSets avec endpoints
- **`apps/portfolio/urls.py`** - Routes API

### Tests
- **`conftest.py`** - Fixtures pytest partagées
- **`pytest.ini`** - Configuration pytest
- **`apps/portfolio/tests/`** - Tests unitaires et API

### Documentation
- **`README.md`** - Documentation complète
- **`QUICKSTART.md`** - Démarrage rapide
- **`API_DOCS.md`** - Documentation API détaillée
- **`CONTRIBUTING.md`** - Guide de contribution

### DevOps
- **`Makefile`** - Commandes de développement
- **`.github/workflows/ci-cd.yml`** - Pipeline CI/CD
- **`deployment/`** - Scripts de déploiement Ansible

## 🔢 Statistiques

- **6 modèles de données** complets
- **30+ endpoints API** RESTful
- **50+ tests** unitaires et d'intégration
- **3 environnements** (dev/test/prod)
- **100% couverture** de la documentation
- **CI/CD** automatisé avec GitHub Actions

## 📊 Modèles de Données

1. **UserProfile** - Profils utilisateurs avec infos personnelles et sociales
2. **Project** - Projets avec tags, technologies, images
3. **Experience** - Expériences professionnelles avec timeline
4. **Education** - Parcours académique et certifications
5. **Skill** - Compétences avec niveaux et catégories
6. **BlogPost** - Articles avec SEO, tags, statuts

## 🚀 Commandes Rapides

```bash
# Setup complet
make setup

# Démarrer
make up

# Tests
make test

# Formater
make format

# Documentation
http://localhost:8000/api/docs/
```

## 🎨 Stack Technologique

- **Backend**: Django 5.2+ & Django REST Framework
- **Base de données**: PostgreSQL 16
- **Cache**: Redis (optionnel)
- **Reverse Proxy**: Nginx
- **Containerisation**: Docker & Docker Compose
- **Tests**: Pytest & pytest-django
- **CI/CD**: GitHub Actions
- **Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Authentication**: JWT (djangorestframework-simplejwt)

## 📚 Prochaines Étapes

Après avoir exploré la structure:

1. ✅ Lisez `QUICKSTART.md` pour démarrer
2. ✅ Consultez `API_DOCS.md` pour l'API
3. ✅ Explorez `apps/portfolio/` pour le code
4. ✅ Testez avec `make test`
5. ✅ Contribuez avec `CONTRIBUTING.md`

---

Cette structure est conçue pour être:
- ✨ **Modulaire** - Apps séparées et réutilisables
- 🧪 **Testable** - Tests complets et CI/CD
- 📖 **Documentée** - Documentation extensive
- 🐳 **Containerisée** - Docker ready
- 🔒 **Sécurisée** - Best practices Django/DRF
- 🚀 **Déployable** - Production ready
