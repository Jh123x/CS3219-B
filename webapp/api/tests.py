import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import TodoItems


# Create your tests here.
class TodoItemTestCase(TestCase):

    def setUp(self):
        TodoItems.objects.create(
            description="Test 1",
            is_completed=False
        )
        TodoItems.objects.create(
            description="Test 2",
            is_completed=True
        )

    def testTodoSerialisesCorrectly(self):
        test2 = TodoItems.objects.get(is_completed=True)
        expected = {"id": test2.id, "description": "Test 2","is_completed": True}
        assert test2.to_dict() == expected, f"{test2.to_dict()}, {expected}"

    def testTodoPrintCorrectly(self):
        test1 = TodoItems.objects.get(is_completed=False)
        expected = f"TodoItem {test1.id}: {test1.description}. Status: {test1.is_completed}"
        assert test1.__repr__() == expected



class EndPointTestCase(TestCase):
    def setUp(self):
        
        # Create mock data
        TodoItems.objects.create(
            description="Test 1",
            is_completed=False
        )
        TodoItems.objects.create(
            description="Test 2",
            is_completed=True
        )

        self.default_get = [{"id": 1, "description": "Test 1", "is_completed": False}, {"id": 2, "description": "Test 2", "is_completed": True}]

        # Create the client for testing
        self.client = Client()

    def testGetEndpoint(self):
        response = self.client.get('/todo')
        assert response.status_code == 200, r1.status_code
        assert response.headers.get("Content-Type") == "application/json", response.content
        assert response.json() == self.default_get

    def testPutEndpointSuccess(self):
        r1 = self.client.put("/todo/1")
        assert r1.status_code == 200, r1.status_code
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": True}

        response = self.client.get("/todo")
        assert response.json() == [{"id": 1, "description": "Test 1", "is_completed": True}, {"id": 2, "description": "Test 2", "is_completed": True}]

    def testPutEndpointFailure(self):
        r1 = self.client.put("/todo/4") # Does not exist
        assert r1.status_code == 200, r1.status_code
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": False}

        response = self.client.get("/todo")
        assert response.json() == self.default_get

    def testDeleteEndpointSuccess(self):
        r1 = self.client.delete("/todo/1")
        assert r1.status_code == 200, r1.status_code
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": True}

        response = self.client.get("/todo")
        assert response.json() == [{"id": 2, "description": "Test 2", "is_completed": True}]

    def testDeleteEndpointFailure(self):
        r1 = self.client.delete("/todo/4") # Does not exist
        assert r1.status_code == 200, r1.status_code
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": False}

        response = self.client.get("/todo")
        assert response.json() == self.default_get


    def testPostEndpointSuccess(self):
        r1 = self.client.post("/todo",{
                "description": "Hello world"
            })
        assert r1.status_code == 200, r1.status_code
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": True}

        response = self.client.get("/todo")
        assert response.json() == self.default_get + [{"id": 3, "description": "Hello world", "is_completed": False}]

    def testPostEndpointFailure(self):
        r1 = self.client.post("/todo")
        assert r1.status_code == 200
        assert r1.headers.get("Content-Type") == "application/json", r1.content
        assert r1.json() == {"is_success": False}
        
        response = self.client.get("/todo")
        assert response.json() == self.default_get

        

