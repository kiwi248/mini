import streamlit as st
from streamlit_session_browser_storage import SessionStorage


storage = SessionStorage(key="pizza_app_storage")


pizza_types = ["combination Pizza", "Bulgogi Pizza", "pepperoni"]
cheese_types = ["Mozzarella","Cheddar"]
dough_types = ["Thin Crust", "Plain Crust", "Cheese Crust"]
topping_types = ["Pepperoni", "Mushroom"]

def make_pizza(index):
    selected_pizza = pizza_types[index]
    st.session_state.pizza = selected_pizza
    st.toast(f"{selected_pizza}를 선택했습니다.")

if "pizza" not in st.session_state:
    st.session_state.pizza = ""

#-----------------------------------
#화면부
#프론트 기본 형태
st.title("PIZZA ORDER")
P1, P2, P3 = st.columns(3)

with P1:
    if st.button("콤비네이션"):
        make_pizza(0)


with P2:
    if st.button("불고기 피자"):
        make_pizza(1)

with P3:
    if st.button("페퍼로니 피자"):
        make_pizza(2)


# 피자를 선택한 다음에만 옵션 표시
if st.session_state.pizza != "":
    st.info(f"선택한 피자: {st.session_state.pizza}")

    with st.form("pizza_option_form"):
        selected_dough = st.selectbox("도우 선택", dough_types)
        selected_cheese = st.selectbox("치즈 선택", cheese_types)
        selected_topping = st.selectbox("토핑 선택", topping_types)

        submitted = st.form_submit_button("주문하기")

        if submitted:
            order_data = {
                "pizza": st.session_state.pizza,
                "dough": selected_dough,
                "cheese": selected_cheese,
                "topping": selected_topping,
            }

            st.session_state.order_data = order_data
            st.session_state.survey_completed = False
            storage.setItem(
                "order_data",
                order_data,
                key="save_order_data",
            )

            st.switch_page("inhye/survey.py")
#-------------------------------


