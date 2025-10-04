# 🚀 Quick Start Guide

## Démarrage Rapide (5 minutes)

### 1. Prérequis
Assurez-vous d'avoir installé:
- Docker Desktop (ou Docker + Docker Compose)
- Git

### 2. Installation

```bash
# Cloner le projet
git clone https://github.com/yemal22/morel-api.git
cd morel-api

# Créer le fichier d'environnement
cp .env.example .env

# Configuration automatique complète
make setup
```

Cette commande va:
- ✅ Créer le fichier `.env`
- ✅ Construire les images Docker
- ✅ Démarrer les conteneurs (PostgreSQL, Django, Nginx)
- ✅ Exécuter les migrations de base de données
- ✅ Peupler la BD avec des données de test
- ✅ Vous demander de créer un superutilisateur

### 3. Accéder à l'application

Une fois le setup terminé:

- **API**: http://localhost:8000
- **Documentation Interactive (Swagger)**: http://localhost:8000/api/docs/
- **Admin Django**: http://localhost:8000/admin/
- **Health Check**: http://localhost:8000/health/

### 4. Credentials par défaut

**Compte de démo (créé par seed_data):**
- Username: `demo_user`
- Password: `demo123`

**Superuser (créé pendant setup):**
- Utilisez les identifiants que vous avez saisis

## 🎯 Commandes Essentielles

```bash
# Démarrer l'application
make up

# Arrêter l'application
make down

# Voir les logs en temps réel
make logs

# Exécuter les tests
make test

# Ouvrir le shell Django
make shell

# Voir toutes les commandes disponibles
make help
```

## 📝 Tester l'API

### 1. Obtenir un token JWT

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "demo_user", "password": "demo123"}'
```

### 2. Utiliser le token pour accéder aux endpoints protégés

```bash
curl -X GET http://localhost:8000/api/portfolio/projects/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 3. Ou utilisez l'interface Swagger

Allez sur http://localhost:8000/api/docs/ et cliquez sur "Authorize" pour entrer votre token.

## 🐛 Problèmes Courants

### Les ports sont déjà utilisés
Si le port 8000 ou 5432 est déjà utilisé:

```bash
# Modifier docker-compose.yml
# Changer "8000:8000" en "8001:8000" par exemple
```

### Problème de permissions Docker
```bash
# Sur Linux, ajoutez votre utilisateur au groupe docker
sudo usermod -aG docker $USER
# Puis redémarrez votre session
```

### La base de données ne démarre pas
```bash
# Supprimer les volumes et recommencer
docker-compose down -v
make setup
```

## 📚 Next Steps

1. **Explorez l'API**: Visitez http://localhost:8000/api/docs/
2. **Modifiez les modèles**: Éditez `apps/portfolio/models.py`
3. **Créez vos propres données**: Utilisez l'admin Django
4. **Développez d'autres apps**: `apps/blog/`, `apps/cv/`, etc.
5. **Personnalisez les settings**: `config/settings/dev.py`

## 🆘 Besoin d'aide ?

- Consultez le [README.md](README.md) complet
- Vérifiez les logs: `make logs`
- Testez la santé de l'app: `make health`
- Ouvrez une issue sur GitHub

Bon développement ! 🎉
