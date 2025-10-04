# 📡 API Documentation

## Base URL
```
http://localhost:8000/api/
```

## Authentication

Cette API utilise **JWT (JSON Web Tokens)** pour l'authentification.

### Obtenir un token

**Endpoint:** `POST /api/token/`

**Request:**
```json
{
  "username": "demo_user",
  "password": "demo123"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Utiliser le token

Incluez le token dans le header de vos requêtes:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Rafraîchir le token

**Endpoint:** `POST /api/token/refresh/`

**Request:**
```json
{
  "refresh": "YOUR_REFRESH_TOKEN"
}
```

## Endpoints

### 👤 User Profiles

#### Liste des profils
```http
GET /api/portfolio/profiles/
```

**Paramètres de recherche:**
- `search` - Recherche dans nom, bio, titre
- `is_active` - Filtrer par statut actif
- `job_title` - Filtrer par titre de poste
- `ordering` - Trier (ex: `first_name`, `-created_at`)

**Réponse:**
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/portfolio/profiles/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "full_name": "John Doe",
      "bio": "Passionate developer...",
      "profile_photo": "http://localhost:8000/media/profiles/photo.jpg",
      "job_title": "Senior Developer",
      "company": "Tech Corp"
    }
  ]
}
```

#### Détail d'un profil
```http
GET /api/portfolio/profiles/{id}/
```

#### Créer un profil (Auth requise)
```http
POST /api/portfolio/profiles/
```

**Body:**
```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "bio": "Software engineer...",
  "email": "jane@example.com",
  "job_title": "Full Stack Developer",
  "linkedin_url": "https://linkedin.com/in/janesmith"
}
```

---

### 📁 Projects

#### Liste des projets
```http
GET /api/portfolio/projects/
```

**Paramètres:**
- `search` - Recherche dans titre, description, tags
- `is_featured` - Projets mis en avant
- `is_published` - Projets publiés
- `ordering` - Trier (ex: `-start_date`, `title`)

**Réponse:**
```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "title": "E-Commerce Platform",
      "slug": "ecommerce-platform",
      "short_description": "Full-featured e-commerce",
      "image": "/media/projects/ecommerce.jpg",
      "tag_list": ["django", "react", "stripe"],
      "technology_list": ["Django", "React", "PostgreSQL"],
      "is_featured": true,
      "start_date": "2023-01-01",
      "created_at": "2024-01-01T10:00:00Z"
    }
  ]
}
```

#### Détail d'un projet (par slug)
```http
GET /api/portfolio/projects/{slug}/
```

#### Projets mis en avant
```http
GET /api/portfolio/projects/featured/
```

#### Créer un projet (Auth requise)
```http
POST /api/portfolio/projects/
```

**Body:**
```json
{
  "title": "New Amazing Project",
  "slug": "new-amazing-project",
  "description": "Full project description...",
  "short_description": "Brief description",
  "tags": "python, django, docker",
  "technologies": "Django, PostgreSQL, Redis",
  "project_url": "https://project.example.com",
  "github_url": "https://github.com/user/project",
  "is_featured": true,
  "is_published": true
}
```

---

### 💼 Experiences

#### Liste des expériences
```http
GET /api/portfolio/experiences/
```

**Paramètres:**
- `search` - Recherche dans entreprise, poste
- `is_current` - Expériences actuelles
- `company` - Filtrer par entreprise
- `ordering` - Trier (ex: `-start_date`)

#### Expériences actuelles
```http
GET /api/portfolio/experiences/current/
```

#### Créer une expérience (Auth requise)
```http
POST /api/portfolio/experiences/
```

**Body:**
```json
{
  "company": "Tech Company",
  "position": "Senior Developer",
  "location": "Paris, France",
  "description": "Responsibilities and achievements...",
  "start_date": "2020-01-01",
  "end_date": null,
  "is_current": true,
  "technologies": "Python, Django, React",
  "company_url": "https://company.com"
}
```

---

### 🎓 Education

#### Liste des formations
```http
GET /api/portfolio/education/
```

#### Créer une formation (Auth requise)
```http
POST /api/portfolio/education/
```

**Body:**
```json
{
  "institution": "University Name",
  "degree": "Master of Science",
  "field_of_study": "Computer Science",
  "location": "City, Country",
  "description": "Specialized in...",
  "start_date": "2015-09-01",
  "end_date": "2017-06-30",
  "grade": "Distinction"
}
```

---

### 🎯 Skills

#### Liste des compétences
```http
GET /api/portfolio/skills/
```

**Paramètres:**
- `category` - Filtrer par catégorie
- `proficiency` - Filtrer par niveau
- `is_featured` - Compétences mises en avant
- `ordering` - Trier

**Catégories disponibles:**
- `programming` - Langages de programmation
- `framework` - Frameworks
- `database` - Bases de données
- `tool` - Outils
- `language` - Langues
- `soft_skill` - Soft skills
- `other` - Autre

**Niveaux de maîtrise:**
- `beginner` - Débutant
- `intermediate` - Intermédiaire
- `advanced` - Avancé
- `expert` - Expert

#### Compétences mises en avant
```http
GET /api/portfolio/skills/featured/
```

#### Compétences par catégorie
```http
GET /api/portfolio/skills/by_category/
```

**Réponse:**
```json
{
  "Programming": [
    {
      "id": 1,
      "name": "Python",
      "category": "programming",
      "proficiency": "expert",
      "level": 9
    }
  ],
  "Framework": [...]
}
```

#### Créer une compétence (Auth requise)
```http
POST /api/portfolio/skills/
```

**Body:**
```json
{
  "name": "JavaScript",
  "category": "programming",
  "proficiency": "advanced",
  "level": 8,
  "description": "Advanced JavaScript development",
  "years_of_experience": 5.0,
  "icon": "fab fa-js",
  "is_featured": true
}
```

---

### 📝 Blog Posts

#### Liste des articles
```http
GET /api/portfolio/blog/
```

**Paramètres:**
- `search` - Recherche dans titre, contenu, tags
- `status` - Filtrer par statut (draft, published, archived)
- `is_featured` - Articles mis en avant
- `ordering` - Trier (ex: `-published_at`)

**Note:** Les utilisateurs non authentifiés ne voient que les articles publiés.

#### Détail d'un article (par slug)
```http
GET /api/portfolio/blog/{slug}/
```

#### Articles mis en avant
```http
GET /api/portfolio/blog/featured/
```

#### Incrémenter les vues
```http
POST /api/portfolio/blog/{slug}/increment_views/
```

**Réponse:**
```json
{
  "views_count": 42
}
```

#### Créer un article (Auth requise)
```http
POST /api/portfolio/blog/
```

**Body:**
```json
{
  "title": "My New Blog Post",
  "slug": "my-new-blog-post",
  "excerpt": "Short description...",
  "content": "Full article content in Markdown...",
  "status": "published",
  "tags": "django, python, web",
  "read_time": 10,
  "is_featured": false,
  "meta_description": "SEO description"
}
```

---

### 🏥 Health Check

```http
GET /health/
```

**Réponse:**
```json
{
  "status": "healthy",
  "database": "connected",
  "details": {
    "version": "1.0.0"
  }
}
```

---

## Pagination

Toutes les listes sont paginées par défaut (20 items par page).

**Paramètres:**
- `page` - Numéro de page
- `page_size` - Nombre d'items par page (max 100)

**Exemple:**
```http
GET /api/portfolio/projects/?page=2&page_size=10
```

---

## Filtres et Recherche

### Recherche
Utilisez le paramètre `search` pour rechercher dans plusieurs champs:

```http
GET /api/portfolio/projects/?search=django
```

### Filtres
Filtrez par n'importe quel champ disponible:

```http
GET /api/portfolio/projects/?is_featured=true&is_published=true
```

### Tri
Utilisez `ordering` pour trier (préfixez avec `-` pour ordre décroissant):

```http
GET /api/portfolio/projects/?ordering=-start_date
```

---

## Codes de Statut HTTP

- `200 OK` - Succès
- `201 Created` - Ressource créée
- `204 No Content` - Suppression réussie
- `400 Bad Request` - Erreur de validation
- `401 Unauthorized` - Token manquant ou invalide
- `403 Forbidden` - Permissions insuffisantes
- `404 Not Found` - Ressource introuvable
- `500 Internal Server Error` - Erreur serveur

---

## Exemples avec cURL

### Créer un projet
```bash
curl -X POST http://localhost:8000/api/portfolio/projects/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Project",
    "slug": "my-project",
    "description": "Project description",
    "tags": "python, django",
    "technologies": "Django, PostgreSQL"
  }'
```

### Rechercher des projets
```bash
curl "http://localhost:8000/api/portfolio/projects/?search=django&is_published=true"
```

### Upload d'image (multipart/form-data)
```bash
curl -X POST http://localhost:8000/api/portfolio/projects/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "title=Project with Image" \
  -F "slug=project-with-image" \
  -F "description=Description" \
  -F "tags=python" \
  -F "technologies=Django" \
  -F "image=@/path/to/image.jpg"
```

---

## Documentation Interactive

Pour une documentation complète et interactive:
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

Ces interfaces permettent de tester directement l'API depuis le navigateur.
