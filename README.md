# Eating_shot

당뇨병 환자를 대상으로 한 건강 관리 서비스

## 명령어 (윈도 리눅스 맥 모두)

젯브레인계열에서 프로젝트 파일이 안 뜨면 invalidate cache and restart 하면 해결됨 왜 그런지 모르겠음

- `poetry install` : 프로젝트 요구사항 설치 (윈도우 한정 3.12로는 안되는 듯 하고, 3.11, 3.10 로는 잘 되는 것을 확인)
- `python manage.py makemigrations ai_workload users events` : (없으면) 마이그레이션 생성
- `python manage.py migrate` : 마이그레이션 적용
- `python manage.py runserver` : 서버 실행


- `./manage.py import_food_kaloh` : 칼로리 데이터 불러오기(추론 서버 동시에 켜야 함)
- `celery -A core worker -l info -Q ai_queue -c 1`: ai worker
- `celery -A core worker -l info`: ai 제외 알림 스케줄링 등 worker

## 명령어 (도커)

### 하기 전에

```dotenv
# .env
DJANGO_SECRET_KEY=
STACK_VERSION=8.15.1

ELASTIC_PASSWORD=
LOGSTASH_PASSWORD=
KIBANA_PASSWORD=

POSTGRES_HOST=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# Set to 'basic' or 'trial' to automatically start the 30-day trial  
LICENSE=basic
#LICENSE=trial

```

## 볼륨 생성

```shell
for volume in caddy_data caddy_config esdata certs; do
  docker volume create $volume
done
```

# docker

- `docker compose up -f docker-compose.dev.yml -d` : 개발용 실행(~~카프카~~redis, 임시db)

- `docker compose up -d` : 전부 실행 (파일이 바뀌었을 시 `--build` 옵션을 붙이면 됨) 30초 정도 걸림.
- `docker compose up [서비스 이름 (공백으로 복수 서비스 기입 가능)]` : 서비스들 실행
- `docker compose down` : 전부 종료 (-v 옵션을 붙이면 볼륨도 삭제). ~~재시작(`--force-recreate` 등) 시 kafka가 자기 자기를 지우지 못하고 재시작되니 주의.~~


- ~~- `docker compose up -d` : 카프카~~

# 각자 디렉토리에서)

- ~~`python -m run_consumer` : 카프카 먹기 시작~~
- `python -m main` : 간이 서버 시작
- `celery -A core worker -l info` : celery worker 시작 (나중에 셸 스크립트로 묶을 예정)

## url

(docker-compose로 실행시 포트 없음)

- ~~`http://localhost:8000/admin/` : 관리자 페이지~~
- `http://localhost:8000/docs` : swagger 페이지
- `http://localhost:8000/redoc` : redoc 페이지
- `http://localhost:8000/schema` : schema 파일

- `https://localhost:5601` : kibana


