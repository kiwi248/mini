# port comment 기능 안내

## 담당 기능

- 프로젝트 이름: `port`
- 담당 기능: 게시글 댓글(comment) CRUD
- 저장 방식: Supabase를 사용하지 않는 임시 메모리 저장소

## 파일 구성

```text
app/
  routers/comment_router.py    # 댓글 API 주소
  schemes/comment_scheme.py    # 댓글 요청·응답 데이터 형식
  services/comment_service.py  # 댓글 CRUD 처리와 임시 데이터
  port.py                      # 로컬 실행 전용(.gitignore로 업로드 제외)
```

`app/main.py`, chat, product, Supabase 관련 파일은 수정하지 않았습니다.

## 댓글 데이터 형식

| 필드 | 설명 |
| --- | --- |
| `comment_id` | 댓글 번호 |
| `post_id` | 댓글이 작성된 게시글 번호 |
| `user_id` | 댓글 작성자 번호 |
| `content` | 댓글 내용 |
| `created_at` | 댓글 생성 시각 |

## API 목록

| 메서드 | 주소 | 기능 |
| --- | --- | --- |
| POST | `/comment/create` | 댓글 생성 |
| GET | `/comment/getall` | 전체 댓글 조회 |
| GET | `/comment/get/{comment_id}` | 댓글 한 개 조회 |
| GET | `/comment/post/{post_id}` | 게시글별 댓글 조회 |
| PUT | `/comment/put` | 댓글 수정 |
| DELETE | `/comment/delete/{comment_id}` | 댓글 삭제 |

### 댓글 생성 요청 예시

```json
{
  "post_id": 1,
  "user_id": 3,
  "content": "새로운 댓글입니다."
}
```

### 댓글 수정 요청 예시

```json
{
  "comment_id": 1,
  "content": "수정한 댓글입니다."
}
```

## 로컬 실행

프로젝트 최상위 폴더에서 다음 명령을 실행합니다.

```powershell
uvicorn app.port:app --reload
```

실행 후 `http://127.0.0.1:8000/docs`에서 API를 확인할 수 있습니다.

`app/port.py`는 개인 확인용 파일이므로 `.gitignore`에 등록되어 Git에 업로드되지 않습니다.

## 팀 공용 앱 연결

팀장이 기능을 합칠 때 공용 `app/main.py`에 다음 내용을 추가합니다.

```python
# port 담당 comment 기능 추가
from app.routers.comment_router import comment_router

app.include_router(comment_router)
```

## Render 배포 참고

현재 comment 기능은 Supabase가 아닌 서버 메모리에 댓글을 보관합니다. Render 서버가 재시작되거나 다시 배포되면 변경된 댓글은 사라지고 코드에 작성된 초기 임시 데이터로 돌아갑니다.
