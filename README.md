# hipsterate-server

- 개발 환경은 Docker로 이루어져 있습니다.
- 배포 환경은 [Zappa](https://www.zappa.io/)를 사용합니다.
- 메인 데이터베이스는 MySQL 5.6을 사용합니다. ([AWS Aurora Serverless](https://aws.amazon.com/ko/rds/aurora/serverless/)와의 호환성 때문입니다)
- 파이썬 관련 주요 환경은 다음과 같습니다.
    - Python 3.7
    - [Flask](http://flask.pocoo.org/)
    - [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)
    - [SQLAlchemy](https://www.sqlalchemy.org/)
    - [Alembic](https://alembic.sqlalchemy.org/en/latest/)
    - [Pytest](https://docs.pytest.org/en/latest/)

## 설치 & 실행

```sh
docker-compose up -d --build
```

## 설정 생성

- `app/config/secret.ini` 파일이 있어야 합니다.
- `ENVIRONMENT` 환경 변수에 따라 설정을 생성합니다.
    - 가능한 `ENVIRONMENT` 값은 현재 `local`, `test`입니다.
    - 컨테이너가 실행될 때 `local` 값으로 실행됩니다.
    - 테스트를 실행할 때는 `export ENVIRONMENT=test`와 함께 실행합니다.

## 로그

```sh
docker attach hipsterate-flask
```

## DB Schema 최신화

```sh
docker exec -i hipsterate-flask /bin/sh -c ". /venv/bin/activate; alembic upgrade head"
```

## 테스트

```sh
docker exec -i hipsterate-flask /bin/sh -c ". /venv/bin/activate; export ENVIRONMENT=test; pytest -vs"
```
