import streamlit as st


# ============================================================
# 1. 페이지 기본 설정
# ============================================================
# 반드시 다른 Streamlit 명령어보다 먼저 작성해야 한다.
# layout="wide"를 사용하면 화면을 넓게 활용할 수 있다.
st.set_page_config(
    page_title="AI 랩 레슨 설계 프로그램",
    page_icon="🎤",
    layout="wide"
)


# ============================================================
# 2. session_state 초기화 함수
# ============================================================
def init_state():
    """
    프로그램에서 사용할 값을 session_state에 처음 등록하는 함수다.

    Streamlit은 버튼을 누르거나 입력값을 바꾸면
    코드가 위에서부터 다시 실행된다.

    session_state를 사용하면 코드가 다시 실행되어도
    사용자가 선택한 레슨 정보가 유지된다.
    """

    # 선택한 레슨 유형
    if "lesson_type" not in st.session_state:
        st.session_state.lesson_type = ""

    # 수강생 이름
    if "student_name" not in st.session_state:
        st.session_state.student_name = ""

    # 수강 목적
    if "lesson_goal" not in st.session_state:
        st.session_state.lesson_goal = ""

    # 레슨 시간
    if "lesson_hours" not in st.session_state:
        st.session_state.lesson_hours = 1

    # 시간당 레슨비
    if "hourly_price" not in st.session_state:
        st.session_state.hourly_price = 50000

    # 예상 수강 기간
    if "lesson_period" not in st.session_state:
        st.session_state.lesson_period = "1개월"

    # 레슨 커리큘럼
    if "curriculum" not in st.session_state:
        st.session_state.curriculum = ""

    # 준비물
    if "materials" not in st.session_state:
        st.session_state.materials = ""

    # 추가 요청사항
    if "request_message" not in st.session_state:
        st.session_state.request_message = ""


# ============================================================
# 3. 입력값 초기화 함수
# ============================================================
def clear_state():
    """
    초기화 버튼을 누르면 실행되는 함수다.

    모든 입력값을 처음 상태로 되돌린다.
    """

    st.session_state.lesson_type = ""
    st.session_state.student_name = ""
    st.session_state.lesson_goal = ""
    st.session_state.lesson_hours = 1
    st.session_state.hourly_price = 50000
    st.session_state.lesson_period = "1개월"
    st.session_state.curriculum = ""
    st.session_state.materials = ""
    st.session_state.request_message = ""

    st.toast("입력한 레슨 정보가 초기화되었습니다.")


# ============================================================
# 4. 취미 랩 레슨 프리셋 함수
# ============================================================
def make_hobby_rap_lesson():
    """
    취미 랩 레슨 버튼을 누르면 실행된다.

    취미 수강생에게 적합한 기본 레슨 정보를
    session_state에 자동으로 입력한다.
    """

    st.session_state.lesson_type = "취미 랩 레슨"
    st.session_state.lesson_goal = (
        "좋아하는 곡을 자연스럽게 따라 부르고 "
        "자신만의 랩 가사를 완성하는 것이 목표입니다."
    )
    st.session_state.lesson_hours = 1
    st.session_state.hourly_price = 50000
    st.session_state.lesson_period = "2개월"
    st.session_state.curriculum = (
        "박자 이해 → 가사 끊어 읽기 → 발음과 호흡 → "
        "플로우 연습 → 랩 녹음"
    )
    st.session_state.materials = (
        "연습하고 싶은 랩 음악, 작성한 가사, "
        "이어폰 또는 헤드폰"
    )

    st.toast("취미 랩 레슨을 선택했습니다.")


# ============================================================
# 5. 자작곡 레슨 프리셋 함수
# ============================================================
def make_songwriting_lesson():
    """
    자작곡 레슨 버튼을 누르면 실행된다.

    작사, 멜로디, 곡 구성 중심의 레슨 정보를
    자동으로 입력한다.
    """

    st.session_state.lesson_type = "자작곡 레슨"
    st.session_state.lesson_goal = (
        "자신의 생각과 경험을 가사와 멜로디로 표현하고 "
        "한 곡을 완성하는 것이 목표입니다."
    )
    st.session_state.lesson_hours = 2
    st.session_state.hourly_price = 60000
    st.session_state.lesson_period = "3개월"
    st.session_state.curriculum = (
        "곡 주제 정하기 → 가사 작성 → 멜로디 만들기 → "
        "벌스와 후렴 구성 → 가이드 녹음"
    )
    st.session_state.materials = (
        "작성한 가사나 메모, 참고하고 싶은 음악, "
        "녹음 가능한 스마트폰"
    )

    st.toast("자작곡 레슨을 선택했습니다.")


# ============================================================
# 6. 작곡 레슨 프리셋 함수
# ============================================================
def make_composition_lesson():
    """
    작곡 레슨 버튼을 누르면 실행된다.

    코드 진행, 멜로디, 편곡 구성 중심의 정보를
    자동으로 입력한다.
    """

    st.session_state.lesson_type = "작곡 레슨"
    st.session_state.lesson_goal = (
        "코드와 멜로디의 관계를 이해하고 "
        "직접 곡의 기본 구조를 만드는 것이 목표입니다."
    )
    st.session_state.lesson_hours = 2
    st.session_state.hourly_price = 65000
    st.session_state.lesson_period = "3개월"
    st.session_state.curriculum = (
        "기초 음악 이론 → 코드 진행 → 멜로디 작성 → "
        "곡 구조 설계 → 악기 구성과 편곡"
    )
    st.session_state.materials = (
        "노트북, DAW 프로그램, 이어폰 또는 헤드폰, "
        "참고하고 싶은 음악"
    )

    st.toast("작곡 레슨을 선택했습니다.")


# ============================================================
# 7. 믹싱·마스터링 레슨 프리셋 함수
# ============================================================
def make_mixing_lesson():
    """
    믹싱·마스터링 레슨 버튼을 누르면 실행된다.

    녹음 파일의 밸런스와 음질을 정리하는 과정에 맞춘
    기본 정보를 자동으로 입력한다.
    """

    st.session_state.lesson_type = "믹싱·마스터링 레슨"
    st.session_state.lesson_goal = (
        "녹음한 보컬과 반주의 밸런스를 조절하고 "
        "완성된 음원의 기본 음질을 개선하는 것이 목표입니다."
    )
    st.session_state.lesson_hours = 2
    st.session_state.hourly_price = 70000
    st.session_state.lesson_period = "2개월"
    st.session_state.curriculum = (
        "볼륨 밸런스 → EQ → 컴프레서 → 리버브와 딜레이 → "
        "마스터링 기초"
    )
    st.session_state.materials = (
        "노트북, DAW 프로그램, 개별 트랙 파일, "
        "이어폰 또는 헤드폰"
    )

    st.toast("믹싱·마스터링 레슨을 선택했습니다.")


# ============================================================
# 8. session_state 초기화 실행
# ============================================================
# 위에서 함수를 만들기만 해서는 실행되지 않는다.
# 아래와 같이 호출해야 실제 초기값이 만들어진다.
init_state()


# ============================================================
# 9. 페이지 제목과 설명
# ============================================================
st.title("🎤 AI 랩 레슨 설계 프로그램")

st.write(
    "원하는 레슨 유형을 선택하면 목표, 커리큘럼, "
    "준비물과 예상 레슨비가 자동으로 입력됩니다."
)

st.caption(
    "자동으로 입력된 내용은 수강생의 상황에 맞게 직접 수정할 수 있습니다."
)


# ============================================================
# 10. 레슨 유형 선택 버튼
# ============================================================
st.subheader("1️⃣ 레슨 유형 선택")

st.write(
    "아래 버튼 중 하나를 누르면 해당 레슨의 기본 정보가 "
    "신청서에 자동으로 입력됩니다."
)

# 화면을 가로로 4칸 나눈다.
lesson_col1, lesson_col2, lesson_col3, lesson_col4 = st.columns(4)


# 취미 랩 레슨 버튼
with lesson_col1:
    st.button(
        "🎤 취미 랩 레슨",
        on_click=make_hobby_rap_lesson,
        use_container_width=True
    )


# 자작곡 레슨 버튼
with lesson_col2:
    st.button(
        "✍️ 자작곡 레슨",
        on_click=make_songwriting_lesson,
        use_container_width=True
    )


# 작곡 레슨 버튼
with lesson_col3:
    st.button(
        "🎹 작곡 레슨",
        on_click=make_composition_lesson,
        use_container_width=True
    )


# 믹싱·마스터링 레슨 버튼
with lesson_col4:
    st.button(
        "🎧 믹싱·마스터링",
        on_click=make_mixing_lesson,
        use_container_width=True
    )


# 현재 선택된 레슨이 있으면 화면에 표시한다.
if st.session_state.lesson_type:
    st.success(
        f"현재 선택한 레슨: {st.session_state.lesson_type}"
    )
else:
    st.info("먼저 원하는 레슨 유형을 선택해주세요.")


st.divider()


# ============================================================
# 11. 레슨 신청서 form
# ============================================================
st.subheader("2️⃣ 레슨 정보 확인 및 수정")

# st.form 안에 있는 입력값은 제출 버튼을 누르기 전까지
# 한 번에 모아서 처리할 수 있다.
with st.form("lesson_design_form"):

    # --------------------------------------------------------
    # 수강생 기본정보
    # --------------------------------------------------------
    st.write("### 👤 수강생 기본정보")

    basic_col1, basic_col2 = st.columns(2)

    with basic_col1:
        student_name = st.text_input(
            "수강생 이름",
            key="student_name",
            placeholder="이름을 입력하세요."
        )

    with basic_col2:
        lesson_type = st.text_input(
            "선택한 레슨 유형",
            key="lesson_type",
            placeholder="위에서 레슨 유형을 선택하세요."
        )


    # --------------------------------------------------------
    # 수강 목표
    # --------------------------------------------------------
    lesson_goal = st.text_area(
        "수강 목표",
        key="lesson_goal",
        height=100,
        placeholder="수강생이 레슨을 통해 이루고 싶은 목표를 입력하세요."
    )


    # --------------------------------------------------------
    # 레슨 시간과 가격
    # --------------------------------------------------------
    st.write("### 💰 레슨 시간 및 비용")

    price_col1, price_col2, price_col3 = st.columns(3)

    with price_col1:
        lesson_hours = st.number_input(
            "주간 레슨 시간",
            min_value=1,
            max_value=10,
            step=1,
            key="lesson_hours"
        )

    with price_col2:
        hourly_price = st.number_input(
            "시간당 레슨비",
            min_value=0,
            max_value=500000,
            step=10000,
            key="hourly_price"
        )

    with price_col3:
        lesson_period = st.selectbox(
            "예상 수강 기간",
            [
                "1개월",
                "2개월",
                "3개월",
                "4개월",
                "5개월",
                "6개월 이상"
            ],
            key="lesson_period"
        )


    # --------------------------------------------------------
    # 예상 비용 계산
    # --------------------------------------------------------
    # 한 달을 평균 4주로 계산한다.
    estimated_monthly_price = lesson_hours * hourly_price * 4

    st.info(
        f"예상 월 레슨비: "
        f"{lesson_hours}시간 × {hourly_price:,}원 × 4주 "
        f"= {estimated_monthly_price:,}원"
    )


    # --------------------------------------------------------
    # 커리큘럼과 준비물
    # --------------------------------------------------------
    st.write("### 📚 레슨 구성")

    curriculum = st.text_area(
        "추천 커리큘럼",
        key="curriculum",
        height=120,
        placeholder="레슨에서 진행할 내용을 입력하세요."
    )

    materials = st.text_area(
        "준비물",
        key="materials",
        height=100,
        placeholder="레슨에 필요한 준비물을 입력하세요."
    )


    # --------------------------------------------------------
    # 추가 요청사항
    # --------------------------------------------------------
    request_message = st.text_area(
        "추가 요청사항",
        key="request_message",
        height=100,
        placeholder=(
            "배우고 싶은 곡, 현재 실력, 사용 중인 프로그램 등 "
            "추가 내용을 입력하세요."
        )
    )


    # --------------------------------------------------------
    # 제출 및 초기화 버튼
    # --------------------------------------------------------
    submit_col, reset_col = st.columns(2)

    with submit_col:
        submit_clicked = st.form_submit_button(
            "✅ 레슨 설계 완료",
            use_container_width=True
        )

    with reset_col:
        reset_clicked = st.form_submit_button(
            "🔄 전체 초기화",
            on_click=clear_state,
            use_container_width=True
        )


# ============================================================
# 12. 제출 결과 출력
# ============================================================
# 레슨 설계 완료 버튼을 눌렀을 때만 결과가 출력된다.
if submit_clicked:

    # 필수 입력값 검사
    if student_name.strip() == "":
        st.error("수강생 이름을 입력해주세요.")

    elif lesson_type.strip() == "":
        st.error("레슨 유형을 먼저 선택해주세요.")

    elif lesson_goal.strip() == "":
        st.error("수강 목표를 입력해주세요.")

    else:
        st.toast("레슨 설계가 완료되었습니다.")

        st.divider()

        st.subheader("🎉 최종 레슨 설계 결과")

        # ----------------------------------------------------
        # 핵심 정보 metric 출력
        # ----------------------------------------------------
        result_col1, result_col2, result_col3, result_col4 = (
            st.columns(4)
        )

        with result_col1:
            st.metric(
                "수강생",
                student_name
            )

        with result_col2:
            st.metric(
                "주간 레슨",
                f"{lesson_hours}시간"
            )

        with result_col3:
            st.metric(
                "시간당 레슨비",
                f"{hourly_price:,}원"
            )

        with result_col4:
            st.metric(
                "예상 월 레슨비",
                f"{estimated_monthly_price:,}원"
            )


        # ----------------------------------------------------
        # 최종 설계 내용 출력
        # ----------------------------------------------------
        summary_col1, summary_col2 = st.columns(2)

        with summary_col1:
            st.write("### 🎤 레슨 기본정보")

            st.write(f"**수강생 이름:** {student_name}")
            st.write(f"**레슨 유형:** {lesson_type}")
            st.write(f"**예상 수강 기간:** {lesson_period}")
            st.write(f"**주간 레슨 시간:** {lesson_hours}시간")
            st.write(f"**시간당 레슨비:** {hourly_price:,}원")

        with summary_col2:
            st.write("### 💳 예상 비용")

            st.write(
                f"**주간 예상 비용:** "
                f"{lesson_hours * hourly_price:,}원"
            )

            st.write(
                f"**월 예상 비용:** "
                f"{estimated_monthly_price:,}원"
            )

            st.caption(
                "월 예상 비용은 한 달을 4주로 계산한 금액입니다."
            )


        # ----------------------------------------------------
        # 수강 목표
        # ----------------------------------------------------
        st.write("### 🎯 수강 목표")
        st.info(lesson_goal)


        # ----------------------------------------------------
        # 커리큘럼
        # ----------------------------------------------------
        st.write("### 📚 추천 커리큘럼")
        st.success(curriculum)


        # ----------------------------------------------------
        # 준비물
        # ----------------------------------------------------
        st.write("### 🎒 준비물")
        st.warning(materials)


        # ----------------------------------------------------
        # 추가 요청사항
        # ----------------------------------------------------
        st.write("### 📝 추가 요청사항")

        if request_message.strip():
            st.write(request_message)
        else:
            st.write("추가 요청사항이 없습니다.")


        # ----------------------------------------------------
        # 최종 안내문
        # ----------------------------------------------------
        st.divider()

        st.success(
            f"{student_name}님의 {lesson_type} 설계가 완료되었습니다. "
            "수강생의 실력과 목표에 따라 커리큘럼은 조정될 수 있습니다."
        )