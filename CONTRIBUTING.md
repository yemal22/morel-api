# 🤝 Contributing to Morel API

Merci de votre intérêt pour contribuer à Morel API ! Ce document explique comment contribuer au projet.

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Standards de Code](#standards-de-code)
- [Workflow Git](#workflow-git)
- [Tests](#tests)
- [Documentation](#documentation)

## Code de Conduite

En participant à ce projet, vous acceptez de maintenir un environnement respectueux et inclusif pour tous.

## Comment Contribuer

### Signaler des Bugs

Si vous trouvez un bug:

1. Vérifiez que le bug n'a pas déjà été signalé dans les [Issues](https://github.com/yemal22/morel-api/issues)
2. Créez une nouvelle issue avec:
   - Un titre descriptif
   - Les étapes pour reproduire le bug
   - Le comportement attendu vs. observé
   - Votre environnement (OS, version Python, etc.)
   - Des captures d'écran si pertinent

### Proposer des Fonctionnalités

Pour proposer une nouvelle fonctionnalité:

1. Ouvrez une issue avec le label `enhancement`
2. Décrivez la fonctionnalité et son utilité
3. Proposez une implémentation si possible
4. Attendez les retours de la communauté

### Soumettre des Modifications

1. **Fork** le repository
2. **Créez une branche** depuis `develop`:
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
3. **Faites vos modifications**
4. **Commitez** avec des messages clairs
5. **Poussez** vers votre fork
6. **Créez une Pull Request**

## Standards de Code

### Style Python

Nous suivons les conventions PEP 8 avec quelques adaptations:

- **Longueur de ligne**: 120 caractères max
- **Formatage**: Utilisez `black` et `isort`
- **Linting**: Le code doit passer `flake8`

```bash
# Formater automatiquement
make format

# Vérifier le style
make lint
```

### Conventions de Nommage

- **Variables/Fonctions**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Fichiers**: `snake_case.py`

### Documentation du Code

```python
def calculate_total(items: list, tax_rate: float = 0.2) -> float:
    """
    Calculate the total price including tax.
    
    Args:
        items: List of item prices
        tax_rate: Tax rate as decimal (default: 0.2 for 20%)
    
    Returns:
        Total price including tax
    
    Raises:
        ValueError: If items list is empty
    """
    if not items:
        raise ValueError("Items list cannot be empty")
    
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)
```

## Workflow Git

### Branches

- `main` - Production, code stable uniquement
- `develop` - Développement, intégration des features
- `feature/nom` - Nouvelles fonctionnalités
- `bugfix/nom` - Corrections de bugs
- `hotfix/nom` - Corrections urgentes pour production

### Commits

Utilisez des messages de commit descriptifs:

```bash
# ✅ Bon
git commit -m "Add user authentication with JWT"
git commit -m "Fix pagination bug in projects list"
git commit -m "Update README with Docker setup instructions"

# ❌ Mauvais
git commit -m "fix"
git commit -m "update"
git commit -m "wip"
```

Format recommandé:
```
[Type] Brief description

Detailed explanation if needed

Fixes #123
```

Types:
- `feat:` - Nouvelle fonctionnalité
- `fix:` - Correction de bug
- `docs:` - Documentation
- `style:` - Formatage, pas de changement de code
- `refactor:` - Refactoring
- `test:` - Ajout/modification de tests
- `chore:` - Tâches de maintenance

### Pull Requests

Une bonne PR doit:

1. **Avoir un titre clair**: `Add JWT authentication to API`
2. **Décrire les changements**: Quoi, pourquoi, comment
3. **Lier les issues**: `Fixes #123` ou `Closes #456`
4. **Inclure des tests**: Pour les nouvelles fonctionnalités
5. **Mettre à jour la doc**: Si nécessaire
6. **Passer les CI checks**: Tests, linting, etc.

Template de PR:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Tests

### Écrire des Tests

Tous les nouveaux codes doivent inclure des tests:

```python
import pytest
from apps.portfolio.models import Project

@pytest.mark.django_db
class TestProject:
    def test_create_project(self, user):
        """Test creating a project."""
        project = Project.objects.create(
            user=user,
            title='Test Project',
            slug='test-project',
            description='Test description',
            tags='test',
            technologies='Django'
        )
        
        assert project.title == 'Test Project'
        assert project.slug == 'test-project'
```

### Exécuter les Tests

```bash
# Tous les tests
make test

# Tests avec couverture
make test-cov

# Tests spécifiques
pytest apps/portfolio/tests/test_models.py
pytest -k test_create_project

# Tests par marqueur
pytest -m unit
pytest -m api
```

### Couverture de Code

Maintenez une couverture de code > 80%:

```bash
# Vérifier la couverture
make test-cov

# Voir le rapport HTML
open htmlcov/index.html
```

## Documentation

### Documentation du Code

- Documentez toutes les classes et fonctions publiques
- Utilisez des docstrings au format Google
- Ajoutez des type hints

### Documentation Utilisateur

Si vous ajoutez une fonctionnalité:

1. Mettez à jour `README.md` si nécessaire
2. Ajoutez des exemples dans `API_DOCS.md`
3. Créez un guide dans `docs/` si complexe

### Commentaires

```python
# ✅ Bon commentaire - Explique le POURQUOI
# Using exponential backoff to avoid overwhelming the API
retry_delay = 2 ** attempt

# ❌ Mauvais commentaire - Répète ce que fait le code
# Multiply retry_delay by 2
retry_delay = retry_delay * 2
```

## Configuration de Développement

### Setup Initial

```bash
# Cloner le repo
git clone https://github.com/yemal22/morel-api.git
cd morel-api

# Configurer l'environnement
make setup

# Installer pre-commit hooks (optionnel)
pip install pre-commit
pre-commit install
```

### Environnement de Développement

```bash
# Démarrer en mode dev
make up

# Suivre les logs
make logs

# Accéder au shell Django
make shell

# Formater le code avant commit
make format

# Vérifier le style
make lint
```

## Revue de Code

Lors de la revue de code, vérifiez:

- [ ] Le code suit les standards du projet
- [ ] Les tests passent et couvrent les changements
- [ ] La documentation est à jour
- [ ] Pas de code dupliqué
- [ ] Pas de dépendances inutiles
- [ ] Les messages de commit sont clairs
- [ ] Pas de secrets ou données sensibles

## Questions ?

Si vous avez des questions:

1. Consultez la documentation existante
2. Cherchez dans les issues fermées
3. Ouvrez une nouvelle issue avec le label `question`
4. Contactez les mainteneurs

## Remerciements

Merci de contribuer à Morel API ! Chaque contribution, grande ou petite, est appréciée. 🙏

---

**Note**: Ce guide peut évoluer. N'hésitez pas à proposer des améliorations !
