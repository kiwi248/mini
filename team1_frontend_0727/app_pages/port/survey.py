import streamlit as st


st.title("주식투자 성향 설문")
st.info("이 설문은 Streamlit 학습용이며 실제 투자 자문이나 금융상품 추천이 아닙니다.")

with st.form("investment_survey_form"):
    name = st.text_input("이름 또는 닉네임")
    experience = st.selectbox(
        "투자 경험",
        ["처음 시작", "1년 미만", "1년 이상", "3년 이상"],
    )
    investment_period = st.selectbox(
        "투자 예정 기간",
        ["1년 미만", "1년~3년", "3년 이상"],
    )
    preferred_sector = st.selectbox(
        "관심 있는 업종",
        ["반도체", "인터넷", "자동차", "바이오", "금융"],
    )
    acceptable_loss = st.slider(
        "감당 가능한 손실 범위(%)",
        min_value=0,
        max_value=30,
        value=10,
    )
    comment = st.text_area("추가 의견")
    submitted = st.form_submit_button("설문 제출")

if submitted:
    # 감당 가능한 손실 범위를 기준으로 투자 성향을 구분합니다.
    if acceptable_loss <= 5:
        investment_type = "안정형"
    elif acceptable_loss <= 15:
        investment_type = "중립형"
    else:
        investment_type = "공격형"

    st.subheader("투자 성향 설문 결과")
    st.write(f"이름: {name if name else '미입력'}")
    st.write(f"투자 경험: {experience}")
    st.write(f"투자 예정 기간: {investment_period}")
    st.write(f"관심 업종: {preferred_sector}")
    st.write(f"감당 가능한 손실: {acceptable_loss}%")
    st.write(f"투자 성향: {investment_type}")

    if comment:
        st.caption(comment)
else:
    st.info("설문 내용을 입력한 뒤 '설문 제출' 버튼을 눌러 주세요.")
