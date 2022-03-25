# Test project for Eastridge

## Frameworks and libraries

This project is a test project with only a few endpoints written in python.
- FastAPI: backend framework
- Sqlalchemy[asyncio] + asyncpg: async database orm
- Postgres: database


## How to run the project
This project is based on docker and you can run the project using docker composer. However, before running the docker, you have to set some environment variables
```
    POSTGRES_USER - postgres user name
    POSTGRES_PASSWORD - postgres login password
    POSTGRES_DB - postgres db
```

### On Windows
```
    set POSTGRES_USER=andrii
    set POSTGRES_PASSWORD=andrii123
    set POSTGRES_DB=testdb
```

### On Unix systems
```
    export POSTGRES_USER=andrii
    export POSTGRES_PASSWORD=andrii123
    export POSTGRES_DB=testdb
```

In case you want to run the product version, you need to set additional variable `WORKERS`. This variable indicates how many threads will be used for the service.
```
    set WORKERS=4     # on Windows
    export WORKERS=4  # on Unix
```

Once you've setup environment variables, you can run the project using docker commands as belows.

### Dev version(auto-reload)
```
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

### Product version(using nginx)
```
    docker-compose -f docker-compose.yml -f docker-compose.nginx.yml build
    docker-compose -f docker-compose.yml -f docker-compose.nginx.yml up
```

In both cases, you don't need to run docker build command every time. Only when dockerfile was changed, you need to run that command.

## API Endpoints
You can find the swagger UI at /docs. The swagger URL is http://localhost:8000/docs for dev version, and http://localhost/docs for prod version.

You can test all endpoints on the swagger UI.