# 🎉 Configuration Complète - Ansible CI/CD

## ✅ Modifications Apportées

### 1. GitHub Actions CI/CD amélioré

**Fichier:** `.github/workflows/ci-cd.yml`

**Améliorations:**
- ✨ Utilisation d'**Ansible** au lieu de commandes SSH brutes
- 🔒 Gestion sécurisée des secrets avec création dynamique d'inventaire
- 📊 Tests de connexion Ansible avant déploiement
- 🎯 Exécution du playbook avec variables externes
- 🧹 Nettoyage automatique des fichiers sensibles
- 💚 Health check amélioré avec parsing JSON
- 📢 Notifications de statut de déploiement

**Workflow:**
1. Lint → 2. Test → 3. Build Docker → 4. Deploy avec Ansible → 5. Health Check

### 2. Playbook Ansible de Déploiement Principal

**Fichier:** `deployment/deploy.yml`

**Fonctionnalités:**
- 🔧 Installation automatique des dépendances système
- 💾 **Backup automatique de la base de données** avant déploiement
- 🗄️ Rotation des backups (garde les 5 derniers)
- 📦 Gestion complète du cycle de vie Docker
- 🔄 Redémarrage gracieux des conteneurs
- ⏱️ Attentes avec timeout pour DB et Web
- 🩺 Health checks multiples
- 🧹 Nettoyage des images/volumes inutilisés
- 📝 Logs rotatifs configurés
- 📊 Rapport détaillé de déploiement

**Sections:**
- `pre_tasks`: Affichage des informations
- `tasks`: 15+ tâches de déploiement
- `post_tasks`: Résumé final
- `handlers`: Gestion des redémarrages

### 3. Playbook de Rollback

**Fichier:** `deployment/rollback.yml`

**Fonctionnalités:**
- 📋 Liste tous les backups disponibles
- ⏪ Restaure automatiquement le dernier backup
- 🔄 Redémarre les services
- ✅ Vérifie que la restauration a réussi

**Usage:**
```bash
ansible-playbook -i inventory.ini rollback.yml
```

### 4. Playbook de Backup Manuel

**Fichier:** `deployment/backup.yml`

**Fonctionnalités:**
- 💾 Créé un backup horodaté de la base de données
- 🗜️ Compression automatique (gzip)
- 📊 Affichage de la taille du backup
- ⬇️ Option pour télécharger le backup localement

**Usage:**
```bash
# Backup sur le serveur
ansible-playbook -i inventory.ini backup.yml

# Backup + téléchargement local
ansible-playbook -i inventory.ini backup.yml -e "download_backup=true"
```

### 5. Playbook de Health Check

**Fichier:** `deployment/health-check.yml`

**Fonctionnalités:**
- 🐳 État de Docker
- 📦 Conteneurs en cours d'exécution
- 🌐 Santé de l'API
- 🗄️ État de PostgreSQL
- 💾 Utilisation du disque
- 🧠 Utilisation mémoire
- ❌ Échec si problème détecté

**Usage:**
```bash
ansible-playbook -i inventory.ini health-check.yml
```

### 6. Documentation Complète

**Fichier:** `deployment/README.md`

**Contenu:**
- 📚 Guide d'installation d'Ansible
- 🔧 Configuration de l'inventaire
- 🔒 Gestion des secrets
- 📖 Documentation de chaque playbook
- 💡 Commandes utiles
- 🐛 Section de dépannage
- 🎯 Exemples d'utilisation

### 7. Fichier .gitignore Complet

**Fichier:** `.gitignore`

**Ajouts:**
- Python et Django complets
- Docker et DevOps
- IDEs multiples
- Secrets et certificats
- Backups et logs
- Tests et couverture
- 180+ patterns d'exclusion

## 🚀 Secrets GitHub Actions Requis

### VPS & SSH
```
VPS_HOST=192.168.1.100
VPS_USERNAME=root
VPS_SSH_KEY=<contenu de id_rsa>
VPS_PORT=22
```

### Docker
```
DOCKER_USERNAME=votre_username
DOCKER_PASSWORD=votre_password_ou_token
```

### Application
```
APP_URL=https://api.example.com
DJANGO_SECRET_KEY=votre-clé-secrète-django
DB_NAME=morel_api
DB_USER=postgres
DB_PASSWORD=votre-mot-de-passe-db
ALLOWED_HOSTS=example.com,www.example.com
CORS_ORIGINS=https://example.com,https://www.example.com
```

### Email (optionnel)
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=votre@email.com
EMAIL_PASSWORD=votre-mot-de-passe
```

## 📊 Architecture de Déploiement

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   Lint   │→ │   Test   │→ │  Build   │→ │  Deploy  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                 ↓             │
│                                          Ansible Playbook    │
└─────────────────────────────────────────────────────────────┘
                                                 ↓
                          ┌─────────────────────────────┐
                          │    Serveur VPS/Cloud        │
                          │  ┌─────────────────────┐   │
                          │  │   Ansible Tasks     │   │
                          │  │  - Backup DB        │   │
                          │  │  - Git pull         │   │
                          │  │  - Docker pull      │   │
                          │  │  - Restart          │   │
                          │  │  - Migrate          │   │
                          │  │  - Health Check     │   │
                          │  └─────────────────────┘   │
                          │                             │
                          │  ┌──────┐  ┌──────┐       │
                          │  │ Web  │  │  DB  │       │
                          │  └──────┘  └──────┘       │
                          │  ┌──────┐                  │
                          │  │Nginx │                  │
                          │  └──────┘                  │
                          └─────────────────────────────┘
```

## 🎯 Avantages d'Ansible vs SSH Direct

### ❌ Avant (SSH direct)
```bash
ssh user@server << EOF
  cd /app
  docker pull image
  docker-compose up -d
EOF
```

**Problèmes:**
- Pas de gestion d'erreurs
- Pas de rollback
- Pas d'idempotence
- Difficile à maintenir
- Pas de réutilisabilité

### ✅ Maintenant (Ansible)
```yaml
- name: Deploy application
  community.docker.docker_compose:
    project_src: "{{ app_dir }}"
    state: present
  register: result
```

**Avantages:**
- ✨ **Idempotent** - Peut être exécuté plusieurs fois
- 🔄 **Réutilisable** - Playbooks modulaires
- 🐛 **Gestion d'erreurs** - Handlers et rescue
- 📊 **Reporting** - Logs structurés
- 🔒 **Sécurisé** - Gestion des secrets
- 🧪 **Testable** - Mode dry-run
- 📚 **Documenté** - Format YAML lisible
- 🎯 **Flexible** - Variables et conditions

## 🔥 Fonctionnalités Clés

### 1. Déploiement Zero-Downtime
- Backup avant déploiement
- Rollback automatique si échec
- Health checks multiples
- Redémarrage gracieux

### 2. Gestion des Backups
- Backups automatiques avant chaque déploiement
- Rotation (garde les 5 derniers)
- Compression automatique
- Téléchargement local possible

### 3. Monitoring & Alerting
- Health check complet (API, DB, système)
- Vérification de l'état des conteneurs
- Utilisation ressources (CPU, RAM, disque)
- Notifications de statut

### 4. Sécurité
- Pas de mots de passe en clair
- Variables chiffrées possibles (Ansible Vault)
- Clés SSH sécurisées
- Nettoyage des fichiers sensibles

## 📝 Commandes Rapides

### Déploiement Manuel
```bash
cd deployment
ansible-playbook -i inventory.ini deploy.yml \
  -e "docker_image=username/morel-api:latest"
```

### Test de Connexion
```bash
ansible -i inventory.ini production -m ping
```

### Health Check
```bash
ansible-playbook -i inventory.ini health-check.yml
```

### Backup
```bash
ansible-playbook -i inventory.ini backup.yml
```

### Rollback
```bash
ansible-playbook -i inventory.ini rollback.yml
```

## 🎓 Prochaines Étapes

1. ✅ Configurez les secrets GitHub Actions
2. ✅ Créez `deployment/inventory.ini`
3. ✅ Testez la connexion Ansible
4. ✅ Faites un premier déploiement manuel
5. ✅ Push sur `main` pour déclencher le CI/CD
6. ✅ Surveillez les logs du workflow
7. ✅ Vérifiez l'application déployée

## 📚 Ressources

- [Documentation Ansible](https://docs.ansible.com/)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [GitHub Actions + Ansible](https://github.com/marketplace/actions/run-ansible-playbook)
- [Docker with Ansible](https://docs.ansible.com/ansible/latest/collections/community/docker/)

---

**🎉 Infrastructure production-ready avec CI/CD Ansible automatisé !**
