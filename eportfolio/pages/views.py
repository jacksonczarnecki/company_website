from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class ExperiencePageView(TemplateView):
    template_name = "experience.html"

class ProjectsPageView(TemplateView):
    template_name = "projects.html"