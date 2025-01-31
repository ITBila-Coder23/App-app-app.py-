ci-cd-flask-app/
│── app/
│   │── app.py
│   │── requirements.txt
│   │── Dockerfile
│── k8s/
│   │── deployment.yaml
│   │── service.yaml
│── .github/workflows/
│   │── ci-cd-pipeline.yml
│── README.md
  
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Cloud & DevOps! Your app is running on Kubernetes 🎉"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
