from locust import HttpUser, task, between

class DemoAPIUser(HttpUser):
    wait_time = between(1, 3)  # Simulate user wait time between requests

    @task(3)
    def get_users(self):
        """Fetch the list of users (GET request)"""
        response = self.client.get("/api/users?page=2")
        assert response.status_code == 200, "Failed to fetch users"
    
    @task(2)
    def get_single_user(self):
        """Fetch a single user (GET request)"""
        response = self.client.get("/api/users/2")
        assert response.status_code == 200, "Failed to fetch single user"

    @task(2)
    def create_user(self):
        """Create a new user (POST request)"""
        payload = {"name": "MC Tester", "job": "QA Engineer"}
        response = self.client.post("/api/users", json=payload)
        assert response.status_code == 201, "User creation failed"

    @task(1)
    def delete_user(self):
        """Delete a user (DELETE request)"""
        response = self.client.delete("/api/users/2")
        assert response.status_code in [200, 204], "Failed to delete user"

# Run in headless mode (if needed)
if __name__ == "__main__":
    import os
    os.system("locust -f locust_scripts/locustfile.py --headless -u 10 -r 1 -t 30s --host=https://reqres.in")
