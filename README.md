# Top Trumps: mongoDB

This repository contains the database for our Application: Top Trumps

### Docker
To locally build the Database docker image, please run command:

```
docker build -t ase_db .
```

To run the built Database docker image, please run command: 
```
docker run -p 27017:27017 -d ase_db
```
