"""
URL configuration for portfolio app.
"""

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    BlogPostViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProjectViewSet,
    SkillViewSet,
    UserProfileViewSet,
)

app_name = "portfolio"

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet, basename="profile")
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"experiences", ExperienceViewSet, basename="experience")
router.register(r"education", EducationViewSet, basename="education")
router.register(r"skills", SkillViewSet, basename="skill")
router.register(r"blog", BlogPostViewSet, basename="blogpost")

urlpatterns = [
    path("", include(router.urls)),
]
