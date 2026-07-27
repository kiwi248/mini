import streamlit as st


def init_state():
    if "selected_stock" not in st.session_state:
        st.session_state.selected_stock = ""
    if "stock_name" not in st.session_state:
        st.session_state.stock_name = ""
    if "order_price" not in st.session_state:
        st.session_state.order_price = ""
    if "order_quantity" not in st.session_state:
        st.session_state.order_quantity = ""


def clear_state():
    st.session_state.selected_stock = ""
    st.session_state.stock_name = ""
    st.session_state.order_price = ""
    st.session_state.order_quantity = ""


def select_samsung():
    st.toast("삼성전자 모의 주문을 선택했습니다.")
    st.session_state.selected_stock = "삼성전자"
    st.session_state.stock_name = "삼성전자"
    st.session_state.order_price = "75000"
    st.session_state.order_quantity = "10"


def select_sk_hynix():
    st.toast("SK하이닉스 모의 주문을 선택했습니다.")
    st.session_state.selected_stock = "SK하이닉스"
    st.session_state.stock_name = "SK하이닉스"
    st.session_state.order_price = "192000"
    st.session_state.order_quantity = "5"


def select_naver():
    st.toast("NAVER 모의 주문을 선택했습니다.")
    st.session_state.selected_stock = "NAVER"
    st.session_state.stock_name = "NAVER"
    st.session_state.order_price = "214000"
    st.session_state.order_quantity = "3"


init_state()

st.title("모의 주식 주문서")
st.info("이 화면은 학습용이며 실제 주식 주문이 실행되지 않습니다.")

if st.session_state.selected_stock:
    st.info(f"선택한 종목은 {st.session_state.selected_stock}입니다.")

samsung_column, sk_hynix_column, naver_column = st.columns(3)

with samsung_column:
    st.button("삼성전자", on_click=select_samsung)

with sk_hynix_column:
    st.button("SK하이닉스", on_click=select_sk_hynix)

with naver_column:
    st.button("NAVER", on_click=select_naver)

with st.form("stock_order_form"):
    stock_name = st.text_input("종목명", key="stock_name")
    order_price = st.text_input("모의 주문 가격", key="order_price")
    order_quantity = st.text_input("모의 주문 수량", key="order_quantity")

    submit_column, reset_column = st.columns(2)

    with submit_column:
        submitted = st.form_submit_button("모의 주문 제출")

    with reset_column:
        st.form_submit_button("초기화", on_click=clear_state)

if submitted:
    st.subheader("모의 주문 내역")
    st.write(
        f"선택한 종목: "
        f"{stock_name if stock_name else '종목을 입력하지 않았습니다.'}"
    )
    st.write(
        f"모의 주문 가격: "
        f"{order_price + '원' if order_price else '주문 가격을 입력하지 않았습니다.'}"
    )
    st.write(
        f"모의 주문 수량: "
        f"{order_quantity + '주' if order_quantity else '주문 수량을 입력하지 않았습니다.'}"
    )
else:
    st.info("종목을 선택하거나 주문 내용을 입력해 주세요.")
