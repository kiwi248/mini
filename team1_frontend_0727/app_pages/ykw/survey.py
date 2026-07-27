import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("피자 신메뉴 설문 폼")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

with st.form("survey_form"):  # form 영역 안의 입력값은 제출 버튼을 눌렀을 때 한 번에 처리됩니다.
    name = st.text_input("이름")  # 사용자가 입력한 이름을 문자열로 저장합니다.
    topic = st.selectbox("가장 먹고 싶은 새로운 피자", ["포테이토 피자", "고르곤졸라 피자", "스테이크 피자"])  # 목록 중 하나를 선택해 topic 변수에 저장합니다.
    satisfaction = st.slider("기대 가격대", min_value=10000, max_value=50000, value=30000, step=1000)  # 1부터 5 사이의 만족도 점수를 숫자로 저장합니다.
    comment = st.text_area("추가 의견")  # 여러 줄 입력창에 작성한 의견을 문자열로 저장합니다.
    submitted = st.form_submit_button("설문 제출")  # 제출 버튼을 누르면 submitted 값이 True가 됩니다.

#---------------------------------------------------------

if submitted:  # 제출 버튼을 누른 뒤에만 설문 결과를 화면에 표시합니다.
    st.subheader("설문 결과")  # 결과 영역의 제목을 표시합니다.
    st.write(f"이름: {name if name else '미입력'}")  # 이름이 비어 있으면 '미입력'으로 표시합니다.
    st.write(f"가장 먹고 싶은 피자: {topic}")  # 선택한 주제를 화면에 출력합니다.
    st.write(f"기대 가격대: {satisfaction}원")  # 슬라이더로 선택한 기대 가격대를 화면에 출력합니다.
    if comment:  # 추가 의견이 입력된 경우에만 의견 내용을 표시합니다.
        st.caption(comment)  # 보조 설명 형태로 추가 의견을 표시합니다.
else:  # 아직 제출 버튼을 누르지 않은 상태라면 안내 메시지를 표시합니다.
    st.info("설문 내용을 입력한 뒤 '설문 제출' 버튼을 눌러 주세요.")
