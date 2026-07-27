import streamlit as st

def init_state():
    if "hambuger" not in st.session_state:
        st.session_state.hambuger = ""
    if "patti" not in st.session_state:
        st.session_state.patti = ""
    if "cheeze" not in st.session_state:
        st.session_state.cheeze = ""
    if "drink" not in st.session_state:
        st.session_state.drink = ""
def clear_state():
    st.session_state.hambuger = ""
    st.session_state.cheeze = ""
    st.session_state.drink = ""

init_state()

def make_p1():
    st.toast("P1 햄버거를 만듭니다.")
    st.session_state.hambuger = "불고기버거"
    st.session_state.patti = "소고기패티"
    st.session_state.cheeze = "모짜렐라치즈"
    st.session_state.drink = "제로콜라"
def make_p2():
    st.toast("P2 햄버거를 만듭니다.")
    st.session_state.hambuger = "새우버거"
    st.session_state.patti = "더블패티"
    st.session_state.cheeze = "아메리칸치즈"
    st.session_state.drink = "사이다"
def make_p3():
    st.toast("P3 햄버거를 만듭니다.")
    st.session_state.hambuger = "빅맥"
    st.session_state.patti = "패티3장"
    st.session_state.cheeze = "cheeze"
    st.session_state.drink = "트레비"
# ------------------------------------------------------------

st.title("hambuger")

if st.session_state.hambuger != "":
    st.info(f"당신이 선택한 햄버거는: {st.session_state.hambuger}")

p1, p2 , p3 = st.columns(3)
with p1:
    p1_clicked = st.button("P1", on_click= make_p1)
with p2:
    p2_clicked = st.button("P2", on_click= make_p2)
with p3:
    p3_clicked = st.button("P3", on_click= make_p3)

with st.form("hambuger_form"):
    input_hambuger = st.text_input("버거 선택", key="hambuger")
    input_cheeze = st.text_input("치즈 선택", key="cheeze")
    input_drink = st.text_input("음료 선택", key="drink")
    submit = st.form_submit_button("주문하기")
    reset = st.form_submit_button("초기화", on_click=clear_state)


# --------------------------------------------------------------

if submit:
    st.subheader(f"당신이 선택한 햄버거는 {st.session_state.hambuger}")
    st.info(f"{input_hambuger}에 {input_cheeze}, {input_drink}")
    