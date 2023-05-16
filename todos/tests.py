from django.test import TestCase
from .models import Todo

# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.my_test = Todo.objects.create(
            title="First Todo",
            body="A body of text here",
        )

    def test_model_content(self):
        self.assertEqual(self.my_test.title, "First Todo")
        self.assertEqual(self.my_test.body, "A body of text here")
        self.assertEqual(str(self.my_test), "First Todo")
