
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


## plan

1. create app 'user'
    1. create the models for users by leveraging apis from Django
    2. create files for app 'user'
        1. forms.py
        2. serializers.py
        3. urls.py
    3. create api related files for app 'user'
        1. api_urls.py
        2. api_views.py
    4. create tests
2. create app 'ai_workload'
    1. create model for ai workload queue?
    1. Kafka or RMQ?
    2. separate server from app ai_workload?
    3. implement ai related stuff
    4. ???
3. dockerize (with cuda enabled)
4. ???

## plan 1.5

1. separated api, users, ai_workload and webapp

## plan 2

2. create app 'ai_workload'
    1. create model for ai workload queue. done
    1. Kafka. done
    2. separate server from app ai_workload. done

used djangorestframework_simplejwt instead of just pyjwt and the large amount of work

## plan 2.1

1. according to these newly created pages:
    - databases
      ~~1. 누적 칼로리(탄, 단, 지)~~
        2. 누적 운동기록들
            - 운동시간
        3. 당뇨 지표
            4. 혈압: 년월일, 수축기, 이완기 (실제 건강 기준: 위험, 경계, 정상)
            5. 혈당: 년월일, 아침, 점심, 저녁 (식전/식후), 공복
            6. 당화혈색소: 년월일, 당화혈색소(%)
        4. 식단기록(이미지 업로드): 년월일, (아침,점심,저녁,간식), (칼로리, 탄수화물, 단백질, 지방)

2. integrate the new databases with the existing ones
3. ???
4. Profit

## plan 2.1.1

1. create the databases from plan 2.1
2. gomin on 'webapp'
    1. import the functions and classes from 'ai_workload'
    2. separate module for shared functions
    3. diango signals
    4. a service layer
    5. ???
    6. i should experiment by using git branches i guess
    7. no wait just do what i planned in keep

-> went for approach number 1: import the functions and classes from 'ai_workload'

## plan 3

1. implement ai related stuff
    1. ???
2. dockerize stuff
    1. add service and build to 2 folders: django app and api server for ai
    2. added logging stack (elk)
    3. ~~added monitoring stack (prometheus, grafana)~~
    4. ???
    5. ~~SSL everything~~

## plan 2.2 (hardening website)

2. hardening the website!
    1. ~~[x] edit and delete 운동 기록~~
    2. ~~edit and delete 혈압~~
    3. ~~edit and delete 혈당~~
    4. ~~디자인 나오는거 기달..~~
    5. all done!

1. hardening the webapp
    2. ~~edit and delete 운동 기록~~
    3. ~~edit and delete 혈압~~
    4. ~~edit and delete 혈당~~
    5. ~~edit and delete 당화혈색소~~
    6. all done!

#### plan 2.2.7

7. 누적 칼로리(탄, 단, 지)

현재 보고서 반 정도 완성 (그래프)

안된 것:

8. 일일 뽑아내기 / 주간 뽑아내기
9. 전체 유저의 상위 n%입니다 표식

사소한 것:

- 나이 생년월일 맞춰야 하기? 아니면 둘 중 하나만 받기

### plan 3.4

go back to plan 3 and do the money involving stuff

## plan 개입.1

### deploying

### storage and database

#### firebase

oh crap. not supported.

I think it is better to use a cloud service for this.

since cloud service is expensive, it may be better off to use a local storage and sqlite3.

no wait i can do free postgresql with supabase!

thinking of supabase, it actually is a firebase alternative. and it provides stuff for storage and database.

instead of boto3, i can use the supabase python sdk.
django-storage?

for now i will use sqlite3. but in this case migration must be done.

#### monitoring(not enabled yet)

- prometheus
- grafana

#### logging

- elk stack
- ???

#### ci/cd

- github actions

##### deployment destination

- aws ec2 (https://aws.amazon.com/ec2/instance-types/)
    - instance type: arm64 or x86?
- gcp compute engine ($300 free credit)
    - **GCP 기본 MTU가 1460이라서 docker 서비스도 1460으로 맞춰줘야 함!!**

may be better off sticking with one cloud provider. done!

# plan 3.5 (do this before doing all the money involving stuff in plan 3.1)

0. use environment variables for secrets
1. vulnerabilities (thinking about something to exploit when money is applied)
    1. image upload
        1. (excluding the malware scanning and the like)
        2. infinitity problem
            1. upload size
            2. upload count
        3. preventing XSS
    2. ???

# plan 3.6

1. completed setting up the environment variables for secrets
2. completed deployment setup (aws ec2)
3. completed stuff below
    - a bad apple pizza
    - removed age from input form
    - pill alarm storage
    - hospital appointment data storage
    - graph for blood stats
    - form errrors
    - any maybe few other things

# plan 3.8 (doing this before plan 3.5)

1. switched from kafka to redis with celery for ai workload, since kafka is overkill and not fit for this purpose
2. added a new django app for SSE (name 'events')
    3. currently has /events/ endpoint for the frontend to connect to
    4. you can test notifications by going to /events/trigger_test_alarm/
    5. specialized js is in `home.html` for now
3. ???
4. password reset (with email)

# gomin 3.5 아 아서 귑지안네 칼로리랑 개별 음식

해결!

```python
 # remove this after edit.
# {
# "predictions": [
# {"name": "\uc54c\ubc25", "class": 0, "confidence": 0.49618, "box": {"x1": 0.0, "y1": 2.75024, "x2": 630.64661, "y2": 465.27628}},
# {"name": "\uc794\uce58\uad6d\uc218", "class": 20, "confidence": 0.42703, "box": {"x1": 0.0, "y1": 2.15228, "x2": 623.83264, "y2": 468.37524}}
# ],
# "food_info": [
# {"food_name": "\uc54c\ubc25", "energy_kcal": "607", "weight_g": "400", "carbohydrates_g": "92", "protein_g": "15", "fat_g": "3", "diabetes_risk_classification": "0"},
# {"food_name": "\uc794\uce58\uad6d\uc218", "energy_kcal": "484", "weight_g": "600", "carbohydrates_g": "90", "protein_g": "17", "fat_g": "5", "diabetes_risk_classification": "0"}
# ]
# }
# TODO: when result_predictions saves, automatically change result_names_comma_separated!
# TODO: if there is a better method than this...
```

# 일단 위의 고민이 결론이 나면 이거 밑에 적힌거 해

# views파일 수정하기..

### passwords to copy yada yada

```shell
=??uQq9qEjChT?8
```

## 비고

노트북 8기가 램으론 동시실행하기에는 버거움

일라스틱 최신버전으로 업데이트하니 토큰방식 로그인같은걸 요구함. 절차를 잘 따라주면 됨 배포할때 참고...

elasticsearch 컨테이너로 가서 `bin/elasticsearch-reset-password auto [-u <유저네임>]` 입력해서 비밀번호 설정 해야함..

^ 이걸 다시 .env에 넣어놓고 셋업 완료해야 함.

가동될때까지 노트북에서 70초, 성능좋은 데탑에서 30초정도 걸림

## ~~reset kafka topic~~

```shell
docker-compose exec kafka kafka-topics --delete --topic inference_tasks --bootstrap-server localhost:9092 #(or
kafka:9092)
```

#### query dsl

이거랑 message, container.name

```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match_phrase": {
            "container.name": "inference_app"
          }
        },
        {
          "match_phrase": {
            "container.name": "django_app"
          }
        },
        {
          "match_phrase": {
            "container.name": "celery-worker"
          }
        },
        {
          "match_phrase": {
            "container.name": "caddy"
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}
```
