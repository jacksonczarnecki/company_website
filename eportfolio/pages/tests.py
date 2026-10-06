from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Callan EPortfolio</h1>")

class AboutpageTests(SimpleTestCase):
    def test_url_available_by_name(self):
            response = self.client.get(reverse("about"))
            self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Callan Czarnecki</h1>")

class ExperiencepageTests(SimpleTestCase):
    def test_url_available_by_name(self):
        response = self.client.get(reverse("experience"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/experience/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("experience"))
        self.assertTemplateUsed(response, "experience.html")

    def test_template_content(self):
        response = self.client.get(reverse("experience"))
        self.assertContains(response, "<h1>My Skills and Experience!</h1>")

class ProjectspageTests(SimpleTestCase):
    def test_url_available_by_name(self):
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("projects"))
        self.assertTemplateUsed(response, "projects.html")

    def test_template_content(self):
        response = self.client.get(reverse("projects"))
        self.assertContains(response, "<h1>Callan's Projects</h1>")

class ContactpageTests(SimpleTestCase):
    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1>Contact Me!</h1>")