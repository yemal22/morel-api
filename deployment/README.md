# 🚀 Deployment with Ansible

Ce dossier contient les playbooks Ansible pour déployer et gérer l'application Morel API sur un VPS.

## 📋 Prérequis

### Sur votre machine locale:
```bash
# Installer Ansible
pip install ansible

# Ou avec apt (Ubuntu/Debian)
sudo apt install ansible
```

### Sur le serveur VPS:
- Ubuntu 20.04+ ou Debian 10+
- Accès SSH avec clé
- Droits sudo

## 🔧 Configuration

### 1. Créer l'inventaire

```bash
cp inventory.ini.example inventory.ini
```

Éditez `inventory.ini`:
```ini
[production]
your-server-ip ansible_user=root ansible_port=22

[production:vars]
ansible_python_interpreter=/usr/bin/python3
docker_username=your_docker_username
docker_password=your_docker_password
```

### 2. Créer le fichier de variables

Créez `vars.yml` avec vos secrets:
```yaml
---
secret_key: "your-django-secret-key"
db_name: "morel_api"
db_user: "postgres"
db_password: "your-db-password"
allowed_hosts: "yourdomain.com,www.yourdomain.com"
cors_origins: "https://yourdomain.com"
email_host: "smtp.gmail.com"
email_port: "587"
email_user: "your-email@gmail.com"
email_password: "your-email-password"
```

**⚠️ Important:** Ajoutez `vars.yml` à `.gitignore` !

### 3. Configurer la clé SSH

```bash
# Copier votre clé SSH sur le serveur
ssh-copy-id user@your-server-ip

# Ou spécifier la clé dans l'inventaire
# ansible_ssh_private_key_file=~/.ssh/id_rsa
```

## 📚 Playbooks Disponibles

### 🚀 Deploy - Déploiement complet

Déploie la dernière version de l'application:

```bash
ansible-playbook -i inventory.ini deploy.yml \
  -e "docker_image=username/morel-api:latest" \
  -e "@vars.yml"
```

**Ce que fait ce playbook:**
- ✅ Installe les dépendances système (Docker, Git, etc.)
- ✅ Créé une sauvegarde de la base de données
- ✅ Clone/met à jour le code depuis Git
- ✅ Configure les variables d'environnement
- ✅ Pull la dernière image Docker
- ✅ Redémarre les conteneurs
- ✅ Exécute les migrations
- ✅ Collecte les fichiers statiques
- ✅ Vérifie la santé de l'application
- ✅ Nettoie les anciennes images Docker

### 🔄 Rollback - Restauration

Restaure la base de données depuis un backup:

```bash
ansible-playbook -i inventory.ini rollback.yml
```

**Ce que fait ce playbook:**
- 📋 Liste les backups disponibles
- ⏪ Restaure la dernière sauvegarde
- 🔄 Redémarre les conteneurs
- ✅ Vérifie que tout fonctionne

### 💾 Backup - Sauvegarde manuelle

Créé une sauvegarde de la base de données:

```bash
ansible-playbook -i inventory.ini backup.yml

# Télécharger le backup localement
ansible-playbook -i inventory.ini backup.yml -e "download_backup=true"
```

### 🏥 Health Check - Vérification de santé

Vérifie l'état de l'application et du serveur:

```bash
ansible-playbook -i inventory.ini health-check.yml
```

**Informations fournies:**
- 🐳 État de Docker
- 📦 Conteneurs en cours d'exécution
- 🌐 Santé de l'API web
- 🗄️ Connectivité base de données
- 💾 Utilisation disque
- 🧠 Utilisation mémoire

## 🔒 Variables Secrètes pour GitHub Actions

Configurez ces secrets dans GitHub Settings → Secrets and variables → Actions:

### Serveur VPS
- `VPS_HOST` - Adresse IP ou hostname du VPS
- `VPS_USERNAME` - Utilisateur SSH (ex: root)
- `VPS_SSH_KEY` - Clé privée SSH (contenu du fichier `~/.ssh/id_rsa`)
- `VPS_PORT` - Port SSH (par défaut: 22)

### Docker Hub
- `DOCKER_USERNAME` - Nom d'utilisateur Docker Hub
- `DOCKER_PASSWORD` - Mot de passe ou token Docker Hub

### Application
- `APP_URL` - URL complète de l'application (ex: https://api.example.com)
- `DJANGO_SECRET_KEY` - Clé secrète Django
- `DB_NAME` - Nom de la base de données
- `DB_USER` - Utilisateur PostgreSQL
- `DB_PASSWORD` - Mot de passe PostgreSQL
- `ALLOWED_HOSTS` - Hosts autorisés (séparés par virgule)
- `CORS_ORIGINS` - Origines CORS autorisées

### Email (optionnel)
- `EMAIL_HOST` - Serveur SMTP
- `EMAIL_PORT` - Port SMTP
- `EMAIL_USER` - Utilisateur email
- `EMAIL_PASSWORD` - Mot de passe email

## 🎯 Déploiement Automatique (CI/CD)

Le workflow GitHub Actions utilise Ansible automatiquement:

1. **Push sur main** → Déclenche le pipeline
2. **Tests passent** → Build de l'image Docker
3. **Image pushée** → Déploiement Ansible automatique
4. **Health check** → Vérification finale

## 📖 Commandes Utiles

### Test de connexion
```bash
ansible -i inventory.ini production -m ping
```

### Exécuter une commande sur le serveur
```bash
ansible -i inventory.ini production -a "docker ps"
```

### Mode debug (verbose)
```bash
ansible-playbook -i inventory.ini deploy.yml -vvv
```

### Dry run (simulation)
```bash
ansible-playbook -i inventory.ini deploy.yml --check
```

### Déployer sur un serveur spécifique
```bash
ansible-playbook -i inventory.ini deploy.yml --limit=server1
```

## 🔧 Personnalisation

### Modifier les variables par défaut

Éditez `deploy.yml` et ajustez les variables:
```yaml
vars:
  app_name: morel-api
  app_dir: /app/{{ app_name }}
  repo_url: https://github.com/yourusername/morel-api.git
  max_backups: 5  # Nombre de backups à garder
```

### Ajouter des tâches personnalisées

Ajoutez des tâches dans la section `tasks:` de n'importe quel playbook:
```yaml
- name: My custom task
  shell: echo "Hello World"
```

## 🐛 Dépannage

### Erreur de connexion SSH
```bash
# Vérifier la connexion SSH
ssh user@your-server-ip

# Vérifier les permissions de la clé
chmod 600 ~/.ssh/id_rsa
```

### Erreur Docker
```bash
# Se connecter au serveur
ssh user@your-server-ip

# Vérifier les logs Docker
docker-compose -f /app/morel-api/docker-compose.yml logs
```

### Permission denied
```bash
# Exécuter avec sudo
ansible-playbook -i inventory.ini deploy.yml --become --ask-become-pass
```

## 📚 Documentation Ansible

- [Documentation officielle Ansible](https://docs.ansible.com/)
- [Ansible Docker modules](https://docs.ansible.com/ansible/latest/collections/community/docker/)
- [Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)

## 🆘 Support

En cas de problème:
1. Vérifiez les logs: `make logs` sur le serveur
2. Exécutez le health check: `ansible-playbook -i inventory.ini health-check.yml`
3. Consultez les backups: `ls /app/backups/`
4. Ouvrez une issue sur GitHub

---

**Note**: Ces playbooks sont conçus pour Ubuntu/Debian. Des adaptations peuvent être nécessaires pour d'autres distributions.
