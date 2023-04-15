apiVersion: apps/v1
kind: Deployment
metadata:
  name: emotion-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: emotion-app
  template:
    metadata:
      labels:
        app: emotion-app
    spec:
      containers:
      - name: emotion-container
        image: gcr.io/<project-id>/<image-name>
        ports:
        - containerPort: 5000
      imagePullSecrets:
      - name: gcr-json-key
