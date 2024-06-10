from locust import HttpUser, task, between

class SentimentAnalysisUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between task executions

    @task(1)
    def analyze_sentiment(self):
        self.client.post("/analyze", json={"text": "This is a test text for sentiment analysis."})

    @task(2)
    def get_history(self):
        self.client.get("/history")

    def on_start(self):
        """Called when a simulated user starts running. Useful for setup tasks."""
        self.client.post("/analyze", json={"text": "Initial setup text."})

# To run this Locust file, save it as `locustfile.py` and run the following command in your terminal:
# locust -f locustfile.py --host http://139.59.228.185:5000
