from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ExperiencePageView, ProjectsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("experience/", ExperiencePageView.as_view(), name="experience"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
]