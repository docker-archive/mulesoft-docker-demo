The Flask API Server creates a dead simple api server. When `api/products` is called, returns a list of products as JSON. To obtain it, it checks the `redis` cache to see if it exists, and returns that. If it doesn't, it reads `static/api-sample.json`, returns the contents, and also stores it into the `redis` cache.

To build the images, in this directory run:

```
docker-compose build
```

To run in Docker Swarm, first make sure that Swarm is your default orchestrator. In Docker Desktop you can do this from the Kubernetes settings menu. Then create a Swarm and then do a stack deploy:

```
docker swarm init
docker stack deploy -c docker-compose.yml products
```

To run in Kubernetes, first make sure that Swarm is your default orchestrator. In Docker Desktop you can do this from the Kubernetes settings menu. Then do a stack deploy, no need to create a Swarm first:

```
docker stack deploy -c docker-compose .yml products
```