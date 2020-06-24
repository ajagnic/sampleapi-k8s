# Kubernetes Sample API
Practice Kubernetes deployment of a psuedo-API, consists of a MongoDB server and the Flask web framework.

### Author
Adrian Agnic https://www.github.com/ajagnic

#### Run
```sh
pip install -r requirements.txt
python app.py
```

#### Run locally with Docker
```sh
docker-compose up -d --build
```

#### Deploy to Kubernetes
```sh
kubectl apply -f ./api-config.yml
kubectl apply -f ./db-deploy.yml
kubectl apply -f ./api-deploy.yml
```

### Inserting Dummy Data (Docker or K8s)
```sh
docker exec -it sampleapi-k8s_api_1 python
```
```sh
kubectl exec -it pod/api -- python
```
```python
import os
from storage.dummy_data import insert_dummy_data
insert_dummy_data(os.environ.get('MONGODB_URI'))
```
