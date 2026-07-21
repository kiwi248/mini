# 02 Mini Project

FastAPI 기반의 간단한 백엔드 프로젝트입니다. Gemini API를 이용한 챗봇형 엔드포인트와 상품 관련 API를 제공하며, 테스트 코드도 포함되어 있습니다.

## 프로젝트 개요

이 프로젝트는 다음 기능을 포함합니다.

- Gemini 기반 챗봇 응답 API
- 상품 생성/조회 API
- FastAPI 라우터 구조 분리
- pytest 기반 테스트 코드

## 기술 스택

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- pytest
- Google GenAI SDK

## 프로젝트 구조

```text
app/
  main.py
  core/
    chat_config.py
  routers/
    chat_router.py
    product_router.py
  schemes/
    chat_scheme.py
    product_scheme.py
  services/
    chat_service.py
    product_service.py
tests/
  test_chat_router.py
  test_product_router.py
```

## 설치 방법

1. 가상환경 생성

```bash
python -m venv .venv
```

2. 가상환경 활성화

```bash
.venv\Scripts\activate
```

3. 의존성 설치

```bash
pip install -r requirements.txt
```

## 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 아래 값을 설정합니다.

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
```

## 실행 방법

서버를 실행하려면 다음 명령을 사용합니다.

```bash
uvicorn app.main:app --reload
```

이후 브라우저 또는 API 테스트 도구에서 아래 주소로 접근할 수 있습니다.

- http://127.0.0.1:8000/docs

## API 엔드포인트

### 사용자

- `POST /users`: 사용자 생성
- `GET /users`: 사용자 전체 조회
- `GET /users/{user_id}`: 사용자 한 명 조회
- `PUT /users/{user_id}`: 사용자 수정
- `DELETE /users/{user_id}`: 사용자 삭제

비밀번호는 생성과 수정 요청으로만 받고 응답에는 포함하지 않습니다.

### 채팅

- POST /chat/gemini
  - 요청 본문 예시

```json
{
  "user_id": "user-1",
  "prompt": "안녕"
}
```

### 상품

- POST /product/create
- GET /product/get/{product_id}
- GET /product/getall

## 테스트 실행

```bash
pytest
```

사용자 CRUD만 실행하려면 다음 명령을 사용합니다.

```bash
pytest tests/test_user_router.py -v
```

## Render 배포

저장소 루트의 `render.yaml`을 사용하는 Render Blueprint 배포를 지원합니다.

1. 변경 내용을 GitHub 저장소에 push합니다.
2. Render에서 **New > Blueprint**를 선택하고 저장소를 연결합니다.
3. 필요하면 `GEMINI_API_KEY` 값을 입력합니다.
4. 배포가 끝나면 `/health`와 `/docs`에서 상태와 Swagger 문서를 확인합니다.

Render 설정에는 프로젝트 루트(`team1_0721`), 설치 명령, `$PORT` 기반 실행 명령이 이미 포함되어 있습니다.

## 참고 사항

- 현재 상품 API는 예시용으로 동작하며, 실제 데이터베이스 연동은 없습니다.
- Gemini 응답은 환경 변수로 설정된 API 키를 사용합니다.
