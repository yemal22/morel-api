.PHONY: help install up down build migrate makemigrations shell test test-cov lint format clean seed createsuperuser logs

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Show this help message
	@echo '$(BLUE)Morel API - Available Commands$(NC)'
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Install Python dependencies
	@echo '$(BLUE)Installing dependencies...$(NC)'
	pip install -r requirements.txt

env: ## Create .env file from .env.example
	@if [ ! -f .env ]; then \
		echo '$(YELLOW)Creating .env file from .env.example...$(NC)'; \
		cp .env.example .env; \
		echo '$(GREEN).env file created! Please update it with your values.$(NC)'; \
	else \
		echo '$(YELLOW).env file already exists$(NC)'; \
	fi

up: ## Start Docker containers
	@echo '$(BLUE)Starting Docker containers...$(NC)'
	docker-compose up -d
	@echo '$(GREEN)Containers started!$(NC)'
	@echo 'API: http://localhost:8000'
	@echo 'API Docs: http://localhost:8000/api/docs/'
	@echo 'Admin: http://localhost:8000/admin/'

down: ## Stop Docker containers
	@echo '$(BLUE)Stopping Docker containers...$(NC)'
	docker-compose down

stop: down ## Alias for down

build: ## Build Docker images
	@echo '$(BLUE)Building Docker images...$(NC)'
	docker-compose build

rebuild: ## Rebuild Docker images without cache
	@echo '$(BLUE)Rebuilding Docker images...$(NC)'
	docker-compose build --no-cache

restart: down up ## Restart Docker containers

migrate: ## Run database migrations
	@echo '$(BLUE)Running migrations...$(NC)'
	docker-compose exec web python manage.py migrate

makemigrations: ## Create new migrations
	@echo '$(BLUE)Creating migrations...$(NC)'
	docker-compose exec web python manage.py makemigrations

shell: ## Open Django shell
	docker-compose exec web python manage.py shell

dbshell: ## Open database shell
	docker-compose exec db psql -U postgres -d morel_api

test: ## Run tests
	@echo '$(BLUE)Running tests...$(NC)'
	docker-compose exec web pytest

test-cov: ## Run tests with coverage
	@echo '$(BLUE)Running tests with coverage...$(NC)'
	docker-compose exec web pytest --cov --cov-report=term --cov-report=html

test-local: ## Run tests locally (without Docker)
	@echo '$(BLUE)Running tests locally...$(NC)'
	pytest

lint: ## Run code linters
	@echo '$(BLUE)Running linters...$(NC)'
	flake8 apps config --max-line-length=120 --exclude=migrations,__pycache__
	@echo '$(GREEN)Linting complete!$(NC)'

format: ## Format code with black and isort
	@echo '$(BLUE)Formatting code...$(NC)'
	black apps config --exclude migrations
	isort apps config --skip migrations
	@echo '$(GREEN)Code formatted!$(NC)'

check-format: ## Check code formatting
	@echo '$(BLUE)Checking code formatting...$(NC)'
	black --check apps config --exclude migrations
	isort --check-only apps config --skip migrations

clean: ## Clean up Python cache files
	@echo '$(BLUE)Cleaning up...$(NC)'
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@echo '$(GREEN)Cleanup complete!$(NC)'

seed: ## Seed database with sample data
	@echo '$(BLUE)Seeding database...$(NC)'
	docker-compose exec web python manage.py seed_data
	@echo '$(GREEN)Database seeded!$(NC)'

seed-clear: ## Clear and seed database
	@echo '$(YELLOW)Clearing and seeding database...$(NC)'
	docker-compose exec web python manage.py seed_data --clear
	@echo '$(GREEN)Database cleared and seeded!$(NC)'

createsuperuser: ## Create Django superuser
	docker-compose exec web python manage.py createsuperuser

collectstatic: ## Collect static files
	@echo '$(BLUE)Collecting static files...$(NC)'
	docker-compose exec web python manage.py collectstatic --noinput

logs: ## Show Docker logs
	docker-compose logs -f

logs-web: ## Show web container logs
	docker-compose logs -f web

logs-db: ## Show database container logs
	docker-compose logs -f db

ps: ## Show running containers
	docker-compose ps

exec-web: ## Execute bash in web container
	docker-compose exec web bash

exec-db: ## Execute bash in db container
	docker-compose exec db bash

backup-db: ## Backup database
	@echo '$(BLUE)Backing up database...$(NC)'
	docker-compose exec -T db pg_dump -U postgres morel_api > backup_$(shell date +%Y%m%d_%H%M%S).sql
	@echo '$(GREEN)Database backed up!$(NC)'

restore-db: ## Restore database from backup (usage: make restore-db FILE=backup.sql)
	@echo '$(YELLOW)Restoring database from $(FILE)...$(NC)'
	docker-compose exec -T db psql -U postgres morel_api < $(FILE)
	@echo '$(GREEN)Database restored!$(NC)'

setup: env build up migrate seed createsuperuser ## Complete setup (first time)
	@echo '$(GREEN)Setup complete!$(NC)'
	@echo 'Access the API at: http://localhost:8000'
	@echo 'Access API docs at: http://localhost:8000/api/docs/'

dev: up logs ## Start development environment

health: ## Check application health
	@echo '$(BLUE)Checking application health...$(NC)'
	@curl -s http://localhost:8000/health/ | python -m json.tool

schema: ## Generate OpenAPI schema
	docker-compose exec web python manage.py spectacular --color --file schema.yml
	@echo '$(GREEN)Schema generated at schema.yml$(NC)'

# Default target
.DEFAULT_GOAL := help
