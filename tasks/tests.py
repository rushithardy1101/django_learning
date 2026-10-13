from django.test import TestCase, Client
from django.urls import reverse
from .models import Tasks

class TasksModelTest(TestCase):
    def setUp(self):
        # Create a sample task for model testing
        self.task = Tasks.objects.create(
            title="Database Test Task",
            description="Testing model fields",
            status="Pending",
            priority="High"
        )

    def test_task_creation(self):
        """Test that the task fields are saved correctly in the database"""
        task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Database Test Task")
        self.assertEqual(task.description, "Testing model fields")
        self.assertEqual(task.status, "Pending")
        self.assertEqual(task.priority, "High")
        self.assertIsNotNone(task.created_at)


class TasksViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample task to show up in the view
        self.task = Tasks.objects.create(
            title="View Test Task",
            description="Testing the web page view",
            status="In Progress",
            priority="Low"
        )
        # Uses the URL name defined in your app's urls.py
        self.url = reverse('task_list')

    def test_task_list_view_status_code(self):
        """Test that the task list page loads successfully (HTTP 200)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_displays_tasks(self):
        """Test that the task title and description appear on the rendered page"""
        response = self.client.get(self.url)
        self.assertContains(response, "View Test Task")
        self.assertContains(response, "Testing the web page view")
        
    def test_pipeline_sanity_check(self):
        self.assertTrue(True)