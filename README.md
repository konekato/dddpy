# Python DDD example using FastAPI

*NOTE: This repository is an example to explain 'how to implement DDD architecture on Python web applicaiton'. If you will to use this as a reference, add your implementation of authentication and security before deploying to the real world!!*

## Code Architecture

For this implementation, I've adopted the [Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/).

Directory structure:

```tree
├── dddpy
│   ├── domain
│   │   └── book
│   │       ├── book.py # Entity
│   │       └── book_repository.py  # Repository Interface
│   ├── infrastructure
│   │   └── sqlite
│   │       ├── book
│   │       │   ├── book_dto.py  # DTO
│   │       │   └── book_repository.py  # Repository implementation
│   │       └── database.py  # Settings for SqlAlchemy
│   ├── presentation
│   │   └── schema  # Schemas for the RESTful API
│   │       └── book
│   │           └── book_schema.py
│   └── usecase
│       └── book
│           └── book_usecase.py
├── main.py
└── tests
```

### DTO (Data Transfer Object)

DTO (Data Transfer Object) is a good practice to isolate domain objects from the infrastructuer layer.

On a minimum MVC architecture, models often inherit a base class provided by a O/R Mappaer. But in that case, the domain layer would be dependent on the outer layer. The same can be said for Python applications using SqlAlchemy.

To solve this problem, we can simply set two rules:

1. A Domain layer classes (such as an Entity or a Value Object) **DO NOT** extend SqlAlchemy Base class.
2. A Data transfer Objects extend the O/R mapper class.

### UoW (Unit of Work)

Even if we succeed in isolating the domain layer, some issues remains. One of them is how to manage transactions.

UoW (Unit of Work) Pattern can be the solution.

*TBD*

## Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Poetry](https://python-poetry.org/)
* [Docker](https://www.docker.com/)

## How to work

1. Clone and open this repostiroy using VSCode
2. Run Remote-Container 
3. Run `make dev` on the Docker container terminal
4. Access http://127.0.0.1:8000/docs
