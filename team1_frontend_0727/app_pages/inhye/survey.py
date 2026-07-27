import streamlit as st


# pizza.py에서 저장한 주문 정보를 가져옵니다.
order_data = st.session_state.get("order_data", {})
order_menu = order_data.get("pizza", "주문 메뉴 없음")


st.title("PIZZA SATISFACTION SURVEY")
st.info(f"주문 메뉴: {order_menu}")


with st.form("survey_form"):
    nickname = st.text_input("닉네임")

    taste_score = st.radio(
        "맛 점수",
        [1, 2, 3, 4, 5],
        horizontal=True,
    )

    evaluation = st.text_area("평가")
    reorder = st.checkbox("재주문 의향이 있습니다.")

    submitted = st.form_submit_button("설문 제출")


if submitted:
    if nickname == "":
        st.warning("닉네임을 입력해주세요.")

    else:
        survey_data = {
            "nickname": nickname,
            "order_menu": order_menu,
            "taste_score": taste_score,
            "평가": evaluation,
            "재주문여부": "O" if reorder else "X",
        }

        st.session_state.survey_data = survey_data

        st.success("설문이 제출되었습니다.")
        st.write(survey_data)
