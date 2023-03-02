from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text="This is a test data")
    
    def test_model_content(self):
        self.assertEqual(self.post.text,"This is a test data")
    
    def test_url_exists_at_correct_loction(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "This is a test")
        self.assertTemplateUsed(response,"home.html")
