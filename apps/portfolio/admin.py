"""
Admin configuration for portfolio app.
"""

from django.contrib import admin

from .models import (
    BlogPost,
    Education,
    Experience,
    Project,
    Skill,
    UserProfile,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "job_title", "company", "is_active", "created_at"]
    list_filter = ["is_active", "created_at"]
    search_fields = ["first_name", "last_name", "email", "bio"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        ("Personal Information", {"fields": ("user", "first_name", "last_name", "bio", "profile_photo")}),
        ("Contact Information", {"fields": ("email", "phone", "location")}),
        ("Social Media", {"fields": ("linkedin_url", "github_url", "twitter_url", "website_url")}),
        ("Professional", {"fields": ("job_title", "company")}),
        ("Status", {"fields": ("is_active", "created_at", "updated_at")}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "user", "is_featured", "is_published", "start_date", "created_at"]
    list_filter = ["is_featured", "is_published", "created_at", "start_date"]
    search_fields = ["title", "description", "tags", "technologies"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ["is_featured", "is_published"]
    date_hierarchy = "start_date"
    ordering = ["-is_featured", "order", "-start_date"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["position", "company", "user", "is_current", "start_date", "end_date"]
    list_filter = ["is_current", "start_date"]
    search_fields = ["company", "position", "description"]
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ["is_current"]
    date_hierarchy = "start_date"
    ordering = ["-is_current", "-start_date"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["degree", "field_of_study", "institution", "user", "start_date", "end_date"]
    list_filter = ["degree", "start_date"]
    search_fields = ["institution", "degree", "field_of_study"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "start_date"
    ordering = ["-start_date"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "proficiency", "level", "user", "is_featured", "years_of_experience"]
    list_filter = ["category", "proficiency", "is_featured"]
    search_fields = ["name", "description"]
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ["is_featured", "level"]
    ordering = ["category", "-is_featured", "order", "name"]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "status", "is_featured", "published_at", "views_count"]
    list_filter = ["status", "is_featured", "published_at", "created_at"]
    search_fields = ["title", "excerpt", "content", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["views_count", "created_at", "updated_at"]
    list_editable = ["status", "is_featured"]
    date_hierarchy = "published_at"
    ordering = ["-published_at", "-created_at"]

    fieldsets = (
        ("Content", {"fields": ("title", "slug", "excerpt", "content", "featured_image")}),
        ("Publishing", {"fields": ("status", "published_at", "is_featured", "author")}),
        ("Metadata", {"fields": ("tags", "read_time", "views_count")}),
        ("SEO", {"fields": ("meta_description", "meta_keywords"), "classes": ("collapse",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
