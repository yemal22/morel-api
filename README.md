# Morel Portfolio API

API REST complète pour un portfolio évolutif, construite avec Django Rest Framework, PostgreSQL et Docker.

## 🚀 Fonctionnalités

- **API REST complète** avec CRUD pour portfolio, projets, expériences, éducation, compétences et blog
- **Authentication JWT** avec djangorestframework-simplejwt
- **Documentation OpenAPI/Swagger** automatique avec drf-spectacular
- **Base de données PostgreSQL** pour la production
- **Docker & Docker Compose** pour un déploiement facile
- **CI/CD GitHub Actions** avec tests automatiques, lint et déploiement
- **Tests complets** avec pytest et pytest-django
- **Pagination, recherche et filtres** sur tous les endpoints
- **Health check endpoint** pour le monitoring
- **Gestion des médias** pour images de projets et blog

## 📋 Prérequis

- Docker & Docker Compose
- Python 3.12+ (pour développement local)
- PostgreSQL 16+ (si exécution sans Docker)

## 🛠️ Installation et Configuration

### 1. Cloner le repository

```bash
git clone https://github.com/yemal22/morel-api.git
cd morel-api
```

### 2. Créer le fichier .env

```bash
make env
# ou
cp .env.example .env
```

Éditez le fichier `.env` avec vos valeurs.

### 3. Lancer l'application avec Docker

```bash
# Configuration complète (première fois)
make setup

# Ou étape par étape:
make build          # Construire les images Docker
make up             # Démarrer les conteneurs
make migrate        # Exécuter les migrations
make seed           # Peupler la BD avec des données de test
make createsuperuser # Créer un superutilisateur
```

L'API sera accessible sur:
- **API**: http://localhost:8000
- **Documentation Swagger**: http://localhost:8000/api/docs/
- **Documentation ReDoc**: http://localhost:8000/api/redoc/
- **Admin Django**: http://localhost:8000/admin/

## 📚 Commandes Make Disponibles

```bash
make help              # Afficher toutes les commandes disponibles
make up                # Démarrer les conteneurs Docker
make down              # Arrêter les conteneurs Docker
make restart           # Redémarrer les conteneurs
make build             # Construire les images Docker
make migrate           # Exécuter les migrations
make makemigrations    # Créer de nouvelles migrations
make shell             # Ouvrir le shell Django
make test              # Exécuter les tests
make test-cov          # Tests avec rapport de couverture
make lint              # Vérifier le code avec flake8
make format            # Formater le code avec black et isort
make seed              # Peupler la BD avec des données
make seed-clear        # Vider et peupler la BD
make logs              # Afficher les logs
make clean             # Nettoyer les fichiers cache
make health            # Vérifier la santé de l'application
```

## 🏗️ Architecture

```
morel-api/
├── apps/                       # Applications Django
│   ├── portfolio/              # App principale du portfolio
│   │   ├── models.py           # Modèles (UserProfile, Project, etc.)
│   │   ├── serializers.py      # Serializers DRF
│   │   ├── views.py            # ViewSets API
│   │   ├── urls.py             # Routes API
│   │   ├── admin.py            # Configuration admin
│   │   ├── tests/              # Tests
│   │   └── management/         # Commandes personnalisées
│   ├── blog/                   # App blog (à développer)
│   ├── agenda/                 # App agenda (à développer)
│   ├── cv/                     # App CV (à développer)
│   └── users/                  # App utilisateurs (à développer)
├── config/                     # Configuration Django
│   ├── settings/               # Settings divisés (base, dev, prod)
│   ├── urls.py                 # URLs principales
│   ├── wsgi.py                 # WSGI
│   └── asgi.py                 # ASGI
├── .github/workflows/          # CI/CD GitHub Actions
├── nginx/                      # Configuration Nginx
├── Dockerfile                  # Image Docker
├── docker-compose.yml          # Configuration Docker Compose
├── requirements.txt            # Dépendances Python
├── pytest.ini                  # Configuration pytest
├── Makefile                    # Commandes utiles
└── README.md                   # Documentation

```

## 📊 Modèles de Données

### UserProfile
- Informations personnelles (nom, bio, photo)
- Contact (email, téléphone, localisation)
- Réseaux sociaux (LinkedIn, GitHub, Twitter)
- Informations professionnelles

### Project
- Titre, description, images
- URLs (projet, GitHub, démo)
- Tags et technologies
- Dates de début/fin
- Statut (featured, published)

### Experience
- Entreprise, poste, localisation
- Description des responsabilités
- Dates de début/fin
- Technologies utilisées

### Education
- Institution, diplôme, domaine d'études
- Localisation, description
- Dates, note obtenue

### Skill
- Nom, catégorie, niveau de maîtrise
- Niveau (1-10), années d'expérience
- Icône, featured

### BlogPost
- Titre, contenu, extrait
- Image featured
- Statut (draft, published, archived)
- Tags, temps de lecture
- Méta-données SEO

## 🔌 Endpoints API

### Portfolio
- `GET /api/portfolio/profiles/` - Liste des profils
- `GET /api/portfolio/profiles/{id}/` - Détail d'un profil
- `POST /api/portfolio/profiles/` - Créer un profil (auth)
- `PUT/PATCH /api/portfolio/profiles/{id}/` - Modifier un profil (auth)
- `DELETE /api/portfolio/profiles/{id}/` - Supprimer un profil (auth)

### Projects
- `GET /api/portfolio/projects/` - Liste des projets
- `GET /api/portfolio/projects/{slug}/` - Détail d'un projet
- `GET /api/portfolio/projects/featured/` - Projets mis en avant
- `POST /api/portfolio/projects/` - Créer un projet (auth)

### Experiences
- `GET /api/portfolio/experiences/` - Liste des expériences
- `GET /api/portfolio/experiences/current/` - Expériences actuelles
- `POST /api/portfolio/experiences/` - Créer une expérience (auth)

### Skills
- `GET /api/portfolio/skills/` - Liste des compétences
- `GET /api/portfolio/skills/featured/` - Compétences mises en avant
- `GET /api/portfolio/skills/by_category/` - Compétences par catégorie

### Blog
- `GET /api/portfolio/blog/` - Liste des articles
- `GET /api/portfolio/blog/{slug}/` - Détail d'un article
- `POST /api/portfolio/blog/{slug}/increment_views/` - Incrémenter les vues

### Authentication
- `POST /api/token/` - Obtenir un token JWT
- `POST /api/token/refresh/` - Rafraîchir un token

### Monitoring
- `GET /health/` - Health check

## 🧪 Tests

```bash
# Exécuter tous les tests
make test

# Tests avec couverture
make test-cov

# Tests spécifiques
docker-compose exec web pytest apps/portfolio/tests/test_models.py
docker-compose exec web pytest -k test_project

# Tests par marqueurs
docker-compose exec web pytest -m unit
docker-compose exec web pytest -m api
```

## 🎨 Qualité du Code

```bash
# Vérifier le code
make lint

# Formater le code
make format

# Vérifier le formatage sans modifier
make check-format
```

## 🚀 Déploiement

### Variables Secrets GitHub Actions

Configurez ces secrets dans les settings de votre repository GitHub:

- `DOCKER_USERNAME` - Nom d'utilisateur Docker Hub
- `DOCKER_PASSWORD` - Password Docker Hub
- `VPS_HOST` - IP/hostname du VPS
- `VPS_USERNAME` - Utilisateur SSH du VPS
- `VPS_SSH_KEY` - Clé privée SSH pour le VPS
- `VPS_PORT` - Port SSH (défaut: 22)
- `APP_URL` - URL de l'application déployée

### Déploiement Manuel

```bash
# Sur le serveur VPS
git pull origin main
docker-compose down
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
```

## 📖 Documentation API

Une fois l'application lancée, accédez à:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **Schéma OpenAPI**: http://localhost:8000/api/schema/

## 🔐 Sécurité

- Authentification JWT pour les endpoints protégés
- Permissions configurables par endpoint
- CORS configuré pour les origines autorisées
- Variables sensibles dans `.env` (jamais committées)
- Validation des données avec serializers DRF
- Protection CSRF pour les requêtes modifiant les données

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT.

## 👤 Auteur

Votre Nom - [@morelyemalin](https://twitter.com/morelyemalin)

Lien du projet: [https://github.com/yemal22/morel-api](https://github.com/yemal22/morel-api)

## 🙏 Remerciements

- Django REST Framework
- PostgreSQL
- Docker
- GitHub Actions
