# Top Trumps: mongoDB

This repository contains the database for our Application: Top Trumps

## Build docker image

```
docker build -t ase_db .
```

## run docker container
```
docker run -p 27017:27017 -d ase_db
```
