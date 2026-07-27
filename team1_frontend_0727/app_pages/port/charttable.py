import altair as alt
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="주식 데이터 차트와 표",
    layout="wide",
)

st.title("주식 데이터 차트와 표")
st.info("이 페이지의 데이터는 학습용 모의 데이터이며 실제 투자 정보가 아닙니다.")

stock_price_df = pd.DataFrame(
    {
        "날짜": ["1일", "2일", "3일", "4일", "5일"],
        "삼성전자": [72000, 73000, 71500, 74000, 75000],
        "SK하이닉스": [185000, 188000, 190000, 187000, 192000],
        "NAVER": [210000, 208000, 212000, 215000, 214000],
    }
)

st.subheader("종목별 주가 표")
st.dataframe(stock_price_df)

selected_stock = st.selectbox(
    "가격 변화를 확인할 종목",
    ["삼성전자", "SK하이닉스", "NAVER"],
)

st.subheader(f"{selected_stock} 가격 변화")

# 기본 st.line_chart는 날짜 글자를 세로로 회전하거나 순서를 자동으로 바꿀 수 있습니다.
# labelAngle=0은 날짜를 가로로 표시하고, sort=None은 1일부터 5일까지의 순서를 유지합니다.
# title=None은 Y축의 숫자 눈금은 유지하면서 긴 종목 제목만 숨겨 글자가 겹치지 않게 합니다.
stock_price_chart = (
    alt.Chart(stock_price_df)
    .mark_line()
    .encode(
        x=alt.X("날짜:N", sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y(
            f"{selected_stock}:Q",
            axis=alt.Axis(title=None),
        ),
    )
)

st.altair_chart(stock_price_chart, width="stretch")

trading_volume_df = pd.DataFrame(
    {
        "종목": ["삼성전자", "SK하이닉스", "NAVER"],
        "거래량": [1250000, 860000, 540000],
    }
)

st.subheader("종목별 거래량 비교")
st.dataframe(trading_volume_df)

# 기본 st.bar_chart는 종목 이름을 세로로 회전하거나 순서를 자동으로 바꿀 수 있습니다.
# labelAngle=0은 종목 이름을 가로로 표시하고, sort=None은 작성한 종목 순서를 유지합니다.
# title=None은 Y축의 숫자 눈금은 유지하면서 거래량 제목만 숨겨 글자가 겹치지 않게 합니다.
trading_volume_chart = (
    alt.Chart(trading_volume_df)
    .mark_bar()
    .encode(
        x=alt.X("종목:N", sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y(
            "거래량:Q",
            axis=alt.Axis(title=None),
        ),
    )
)

st.altair_chart(trading_volume_chart, width="stretch")
