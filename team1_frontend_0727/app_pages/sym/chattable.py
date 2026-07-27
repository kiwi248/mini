import pandas as pd  # 상품 목록을 표 형태의 데이터로 다루기 위해 pandas를 불러옵니다.
import streamlit as st  # Python 코드로 웹 대시보드 화면을 만들기 위해 Streamlit을 불러옵니다.

# 브라우저 탭에 표시할 제목을 정하고, 대시보드를 화면 너비에 맞게 넓게 표시합니다.
st.set_page_config(page_title="쇼핑몰 월별 판매현황 ", layout="wide")

# 상품 이름, 색상, 사이즈 정보를 DataFrame으로 만듭니다.
# DataFrame은 행과 열로 구성된 표 형태의 데이터입니다.
df = pd.DataFrame(
    [
        {"name": "셔츠", "color": "white", "size": 90},
        {"name": "반팔", "color": "white", "size": 105},
        {"name": "바지", "color": "black", "size": 100},
        {"name": "자켓", "color": "red", "size": 95},
    ]
)

# 대시보드 상단에 제목을 표시합니다.
st.title("쇼핑몰 월별 판매현황")

# 상품 선택 상자를 만듭니다.
# "전체" 뒤에 DataFrame의 상품 이름을 정렬하여 선택 항목으로 추가합니다.
selected_item = st.selectbox("항목", ["전체"] + sorted(df["name"].unique()))

# 원본 데이터를 변경하지 않도록 복사본을 만들어 필터링에 사용합니다.
filtered_df = df.copy()

# 특정 상품을 선택하면 해당 상품과 이름이 같은 행만 남깁니다.
# "전체"를 선택한 경우에는 모든 상품을 그대로 표시합니다.
if selected_item != "전체":
    filtered_df = filtered_df[
        filtered_df["name"] == selected_item
    ]

# 주요 정보를 나란히 표시하기 위해 화면을 세 개의 열로 나눕니다.
col_count, col_progress, col_score = st.columns(3)

# 첫 번째 열에는 현재 필터 결과에 포함된 상품의 개수를 표시합니다.
with col_count:
    st.metric("구매자 수", len(filtered_df))

# 두 번째 열에는 가장 자주 등장하는 색상을 표시합니다.
# mode()는 가장 많이 등장한 값을 찾고, 결과가 없으면 "-"를 사용합니다.
with col_progress:
    popular_color = (
        filtered_df["color"].mode().iloc[0]
        if not filtered_df.empty
        else "-"
    )
    st.metric("가장 많이 찾는 색상", popular_color)

# 세 번째 열에는 가장 자주 등장하는 사이즈를 표시합니다.
with col_score:
    popular_size = (
        filtered_df["size"].mode().iloc[0]
        if not filtered_df.empty
        else "-"
    )
    st.metric("가장 많이 찾는 사이즈", popular_size)

# 상세 데이터와 차트를 각각 볼 수 있도록 화면을 두 개의 탭으로 나눕니다.
tab_table, tab_chart = st.tabs(["상세목록", "구매자 차트"])

# 첫 번째 탭에는 필터링된 상품 정보를 표로 표시합니다.
with tab_table:
    st.dataframe(filtered_df,use_container_width=True)

# 두 번째 탭에는 상품별 사이즈를 막대 차트로 표시합니다.
with tab_chart:
    # 필터 결과가 있을 때만 상품 이름을 기준으로 사이즈 차트를 만듭니다.
    if not filtered_df.empty:
        chart_df = filtered_df.set_index("name")[["size"]]
        st.bar_chart(chart_df)
    # 필터 결과가 비어 있으면 차트 대신 안내 메시지를 표시합니다.
    else:
        st.warning("필터 조건에 맞는 데이터가 없습니다.")
