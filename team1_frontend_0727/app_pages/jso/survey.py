import streamlit as st

# 페이지 제목
st.title("🎤 자작곡 랩 레슨 상담 신청서")

# 페이지 설명
st.write("간단한 정보를 입력하면 상담 신청 내용을 확인할 수 있습니다.")

# -------------------------------
# 기본 정보 입력
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("👤 기본 정보")

# 이름 입력
name = st.text_input(
    "이름",
    placeholder="홍길동"
)

# 연락처 입력
phone = st.text_input(
    "연락처",
    placeholder="010-1234-5678"
)

# 나이 입력
# value=20 : 처음 표시되는 기본값
# step=1 : 1씩 증가/감소
age = st.number_input(
    "나이",
    min_value=10,
    max_value=100,
    value=20,
    step=1
)

# 거주 지역 입력
region = st.text_input(
    "거주 지역",
    placeholder="예: 서울시 관악구"
)

# -------------------------------
# 음악 활동 경험
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🎵 음악 활동 경험")

# 해당 경험이 있다면 체크
recording = st.checkbox("랩 또는 보컬을 녹음해 본 적이 있어요")
lyrics = st.checkbox("가사를 써 본 적이 있어요")
release = st.checkbox("음원을 발매해 본 적이 있어요")
performance = st.checkbox("무대에서 공연해 본 적이 있어요")

# -------------------------------
# 레슨 목표
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🎯 레슨 목표")

# 가장 중요한 목표를 하나 선택
goal = st.selectbox(
    "가장 중요한 목표",
    [
        "선택해주세요.",
        "취미·랩 실력 향상",
        "개인 소장용 자작곡 완성",
        "음원 발매",
        "공연·오디션 준비",
        "기타"
    ]
)

# 배우고 싶은 내용을 여러 개 선택
lesson_topics = st.multiselect(
    "배우고 싶은 내용(여러 개 선택 가능)",
    [
        "랩·보컬 녹음",
        "가사 쓰기와 자작곡",
        "비트 메이킹과 작곡",
        "믹싱과 마스터링"
    ]
)

# -------------------------------
# 추가 정보
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📝 추가 정보")

# 좋아하는 아티스트 입력
favorite_artist = st.text_input(
    "좋아하는 아티스트",
    placeholder="예: 빈지노, 창모"
)

# 상담하고 싶은 내용을 자유롭게 입력
message = st.text_area(
    "상담하고 싶은 내용",
    placeholder="현재 고민이나 배우고 싶은 내용을 자유롭게 작성해주세요."
)

st.markdown("<br>", unsafe_allow_html=True)

# 상담 신청 버튼
submit = st.button(
    "상담 신청",
    use_container_width=True  # 버튼을 화면 너비에 맞게 표시
)

# -------------------------------
# 상담 신청 버튼을 눌렀을 때 실행
# -------------------------------
if submit:

    # 필수 입력값 검사
    if not name.strip():
        st.warning("이름을 입력해주세요.")

    elif not phone.strip():
        st.warning("연락처를 입력해주세요.")

    elif goal == "선택해주세요.":
        st.warning("레슨 목표를 선택해주세요.")

    elif not lesson_topics:
        st.warning("배우고 싶은 내용을 한 개 이상 선택해주세요.")

    else:

        # 체크한 음악 활동 경험을 저장할 리스트
        experiences = []

        # 체크한 항목만 리스트에 추가
        if recording:
            experiences.append("랩·보컬 녹음")

        if lyrics:
            experiences.append("작사")

        if release:
            experiences.append("음원 발매")

        if performance:
            experiences.append("공연")

        # 아무것도 선택하지 않았다면 경험 없음으로 표시
        if not experiences:
            experiences.append("경험 없음")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("✅ 상담 신청 내용")

        # 사용자가 입력한 내용을 화면에 출력
        st.write(f"**이름:** {name.strip()}")
        st.write(f"**연락처:** {phone.strip()}")
        st.write(f"**나이:** {age}세")
        st.write(f"**거주 지역:** {region.strip() or '미입력'}")

        # join()을 이용해 리스트를 쉼표로 연결해서 출력
        st.write(f"**음악 활동 경험:** {', '.join(experiences)}")
        st.write(f"**레슨 목표:** {goal}")
        st.write(f"**배우고 싶은 내용:** {', '.join(lesson_topics)}")

        # 입력하지 않은 경우 '미입력' 표시
        st.write(f"**좋아하는 아티스트:** {favorite_artist.strip() or '미입력'}")
        st.write(f"**상담 내용:** {message.strip() or '미입력'}")

        # 실제 DB 저장은 하지 않고 화면에만 출력
        st.success("상담 신청 내용을 확인했습니다.")