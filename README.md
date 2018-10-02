## Mongo

This project uses Docker to run a local MongoDB instance.




### Start MongoDB

```
docker-compose up
```

### Stop MongoDB

Stop MongoDB container but do not clear data (start with same data on container restarts).

### Destroy MongoDB

Stop MongoDB container and clear data (start with fresh data on container restart).

```
docker-compose down -v
```
