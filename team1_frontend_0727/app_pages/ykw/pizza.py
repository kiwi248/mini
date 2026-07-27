import streamlit as st

def init_state():
    if "pizza" not in st.session_state:
        st.session_state.pizza = ""
    if "dow" not in st.session_state:
        st.session_state.dow = ""
    if "cheeze" not in st.session_state:
        st.session_state.cheeze = ""
    if "toping" not in st.session_state:
        st.session_state.toping = ""
def clear_state():
    st.session_state.dow = ""
    st.session_state.cheeze = ""
    st.session_state.toping = ""

init_state()

def make_p1():
    st.toast("치즈 피자 만듭니다(๑´ڡ`๑)")
    st.session_state.pizza = "치즈 피자🧀"
    st.session_state.dow = "밀가루 도우"
    st.session_state.cheeze = "4가지 치즈"
    st.session_state.toping = "치즈"
def make_p2():
    st.toast("콤비네이션 피자 만듭니다(っ˘ڡ˘ς)")
    st.session_state.pizza = "콤비네이션 피자🔴🥓"
    st.session_state.dow = "밀가루 도우"
    st.session_state.cheeze = "모짜렐라 치즈"
    st.session_state.toping = "페퍼로니"
def make_p3():
    st.toast("불고기 피자 만듭니다ᕦ( ᐛ )ᕡ")
    st.session_state.pizza = "불고기 피자🔥🥩"
    st.session_state.dow = "밀가루 도우"
    st.session_state.cheeze = "모짜렐라 치즈"
    st.session_state.toping = "불고기"
# ------------------------------------------------------------

st.title("트레이더스 Pizza🍕")

if st.session_state.pizza != "":
    st.info(f"당신이 선택한 피자는: {st.session_state.pizza}")

p1, p2 , p3 = st.columns(3)
with p1:
    st.button("치즈 피자🧀", on_click= make_p1)
with p2:
    st.button("콤비네이션 피자🔴🥓", on_click= make_p2)
with p3:
    st.button("불고기 피자🔥🥩", on_click= make_p3)

with st.form("pizza_form"):
    input_dow = st.text_input("도우 선택", key="dow")
    input_cheeze = st.text_input("치즈 선택", key="cheeze")
    input_toping = st.text_input("토핑 선택" , key="toping")
    submit = st.form_submit_button("제출")
    reset = st.form_submit_button("초기화", on_click=clear_state)

# --------------------------------------------------------------

if submit:
    st.subheader(f"당신이 선택한 피자는 {st.session_state.pizza}")
    st.info(f"{input_dow} {input_cheeze} {input_toping}")