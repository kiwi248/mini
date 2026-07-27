import streamlit as st
import pandas as pd


# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="레슨 현황 대시보드",
    page_icon="🎵",
    layout="wide"
)


# --------------------------------------------------
# 페이지 제목
# --------------------------------------------------
st.title("🎵 랩·자작곡 레슨 현황 대시보드")
st.caption(
    "수강생의 레슨 현황, 음악 작업 진행 상황, "
    "월별 레슨 시간과 수익을 확인할 수 있습니다."
)


# --------------------------------------------------
# 수강생 기본 데이터
# --------------------------------------------------
student_data = {
    "이름": [
        "김민수",
        "이서연",
        "박지훈",
        "최유진",
        "정현우",
        "한지민"
    ],
    "레슨 유형": [
        "취미 랩 레슨",
        "자작곡 레슨",
        "취미 랩 레슨",
        "믹싱·마스터링 레슨",
        "자작곡 레슨",
        "작곡 레슨"
    ],
    "선호 장르": [
        "붐뱁",
        "R&B",
        "트랩",
        "멜로딕 랩",
        "발라드",
        "힙합 R&B"
    ],
    "주간 레슨 시간": [
        1,
        2,
        1,
        2,
        1,
        2
    ],
    "누적 레슨 시간": [
        8,
        20,
        6,
        24,
        12,
        30
    ],
    "완성 곡 수": [
        1,
        4,
        1,
        5,
        3,
        7
    ],
    "발매 곡 수": [
        0,
        1,
        0,
        2,
        1,
        4
    ],
    "현재 작업 단계": [
        "랩 가사와 플로우 연습",
        "후렴 멜로디와 가사 수정",
        "발음과 호흡 훈련",
        "보컬 밸런스와 공간계 조정",
        "가이드 보컬 녹음",
        "코드 진행과 편곡 구성"
    ],
    "피드백": [
        "박자에 맞춰 가사를 끊어 읽고 여러 가지 플로우로 연습해보세요.",
        "후렴의 핵심 문장을 단순하게 정리하면 곡의 인상이 더 선명해집니다.",
        "긴 문장을 한 번에 읽기보다 호흡 위치를 나누어 연습해보세요.",
        "보컬이 반주에 묻히지 않도록 볼륨과 리버브 양을 다시 조절해보세요.",
        "멜로디의 음정과 가사 발음을 확인하면서 가이드 녹음을 반복해보세요.",
        "코드 진행을 기준으로 곡의 도입부, 벌스, 후렴 구성을 정리해보세요."
    ]
}

df = pd.DataFrame(student_data)


# --------------------------------------------------
# 월별 레슨 데이터
# --------------------------------------------------
monthly_lesson_data = {
    "월": [
        "3월", "3월", "3월", "3월", "3월", "3월",
        "4월", "4월", "4월", "4월", "4월", "4월",
        "5월", "5월", "5월", "5월", "5월", "5월",
        "6월", "6월", "6월", "6월", "6월", "6월"
    ],
    "이름": [
        "김민수", "이서연", "박지훈", "최유진", "정현우", "한지민",
        "김민수", "이서연", "박지훈", "최유진", "정현우", "한지민",
        "김민수", "이서연", "박지훈", "최유진", "정현우", "한지민",
        "김민수", "이서연", "박지훈", "최유진", "정현우", "한지민"
    ],
    "월 레슨 시간": [
        4, 8, 4, 8, 4, 8,
        4, 6, 4, 8, 4, 8,
        3, 8, 4, 6, 4, 10,
        4, 8, 3, 8, 4, 8
    ],
    "시간당 레슨비": [
        50000, 60000, 50000, 70000, 60000, 65000,
        50000, 60000, 50000, 70000, 60000, 65000,
        50000, 60000, 50000, 70000, 60000, 65000,
        50000, 60000, 50000, 70000, 60000, 65000
    ]
}

monthly_df = pd.DataFrame(monthly_lesson_data)


# 레슨 시간 × 시간당 레슨비
monthly_df["레슨 수익"] = (
    monthly_df["월 레슨 시간"]
    * monthly_df["시간당 레슨비"]
)


# 학생 기본정보에서 레슨 유형을 월별 데이터에 추가
monthly_df = monthly_df.merge(
    df[["이름", "레슨 유형"]],
    on="이름",
    how="left"
)


# 월 정렬 순서
month_order = ["3월", "4월", "5월", "6월"]

monthly_df["월"] = pd.Categorical(
    monthly_df["월"],
    categories=month_order,
    ordered=True
)

monthly_df = monthly_df.sort_values(
    ["월", "이름"]
).reset_index(drop=True)


# --------------------------------------------------
# 사이드바 필터
# --------------------------------------------------
with st.sidebar:
    st.header("🔍 조회 조건")

    lesson_type = st.selectbox(
        "레슨 유형",
        ["전체"] + list(df["레슨 유형"].unique())
    )

    selected_month = st.selectbox(
        "수익 조회 월",
        ["전체"] + month_order
    )

    st.divider()

    st.write("#### 전체 등록 현황")
    st.write(f"수강생: **{len(df)}명**")
    st.write(
        f"전체 누적 레슨: "
        f"**{monthly_df['월 레슨 시간'].sum():,}시간**"
    )
    st.write(
        f"전체 레슨 수익: "
        f"**{monthly_df['레슨 수익'].sum():,}원**"
    )


# --------------------------------------------------
# 학생 데이터 필터링
# --------------------------------------------------
if lesson_type == "전체":
    filtered_df = df.copy()
    filtered_monthly_df = monthly_df.copy()
else:
    filtered_df = df[
        df["레슨 유형"] == lesson_type
    ].copy()

    filtered_monthly_df = monthly_df[
        monthly_df["레슨 유형"] == lesson_type
    ].copy()


# 선택한 월 필터 적용
if selected_month == "전체":
    selected_month_df = filtered_monthly_df.copy()
else:
    selected_month_df = filtered_monthly_df[
        filtered_monthly_df["월"] == selected_month
    ].copy()


# --------------------------------------------------
# 현재 조회 조건
# --------------------------------------------------
filter_text = f"레슨 유형: **{lesson_type}**"

if selected_month != "전체":
    filter_text += f" / 수익 조회 월: **{selected_month}**"

st.info(f"현재 조회 조건 — {filter_text}")


# --------------------------------------------------
# 핵심 현황
# --------------------------------------------------
st.subheader("📌 핵심 현황")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "수강생 수",
        f"{len(filtered_df)}명"
    )

with col2:
    st.metric(
        "누적 레슨 시간",
        f"{filtered_df['누적 레슨 시간'].sum():,}시간"
    )

with col3:
    st.metric(
        "완성 곡 수",
        f"{filtered_df['완성 곡 수'].sum():,}곡"
    )

with col4:
    st.metric(
        "발매 곡 수",
        f"{filtered_df['발매 곡 수'].sum():,}곡"
    )

with col5:
    st.metric(
        "조회 기간 수익",
        f"{selected_month_df['레슨 수익'].sum():,}원"
    )


st.divider()


# --------------------------------------------------
# 탭 구성
# --------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 수강생 목록",
    "📊 레슨 통계",
    "💰 월별 레슨·수익",
    "💬 작업 단계 및 피드백"
])


# --------------------------------------------------
# 탭 1: 수강생 목록
# --------------------------------------------------
with tab1:
    st.subheader("수강생 목록")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "주간 레슨 시간": st.column_config.NumberColumn(
                "주간 레슨 시간",
                format="%d시간"
            ),
            "누적 레슨 시간": st.column_config.NumberColumn(
                "누적 레슨 시간",
                format="%d시간"
            ),
            "완성 곡 수": st.column_config.NumberColumn(
                "완성 곡 수",
                format="%d곡"
            ),
            "발매 곡 수": st.column_config.NumberColumn(
                "발매 곡 수",
                format="%d곡"
            )
        }
    )


# --------------------------------------------------
# 탭 2: 레슨 통계
# --------------------------------------------------
with tab2:
    if len(filtered_df) >= 2:
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("누적 레슨 시간")

            lesson_chart_data = filtered_df.set_index("이름")[
                ["누적 레슨 시간"]
            ]

            st.bar_chart(
                lesson_chart_data,
                use_container_width=True
            )

        with chart_col2:
            st.subheader("곡 작업 현황")

            song_chart_data = filtered_df.set_index("이름")[
                ["완성 곡 수", "발매 곡 수"]
            ]

            st.bar_chart(
                song_chart_data,
                use_container_width=True
            )

    else:
        student = filtered_df.iloc[0]

        st.subheader(f"{student['이름']} 수강생 통계")

        personal_col1, personal_col2, personal_col3, personal_col4 = (
            st.columns(4)
        )

        with personal_col1:
            st.metric(
                "주간 레슨",
                f"{student['주간 레슨 시간']}시간"
            )

        with personal_col2:
            st.metric(
                "누적 레슨",
                f"{student['누적 레슨 시간']}시간"
            )

        with personal_col3:
            st.metric(
                "완성 곡",
                f"{student['완성 곡 수']}곡"
            )

        with personal_col4:
            st.metric(
                "발매 곡",
                f"{student['발매 곡 수']}곡"
            )

        st.info(
            "현재 선택한 레슨 유형에 수강생이 1명이므로 "
            "차트 대신 개인 통계를 표시합니다."
        )

    st.divider()

    st.subheader("통계 요약")

    summary_df = filtered_df[
        [
            "이름",
            "레슨 유형",
            "누적 레슨 시간",
            "완성 곡 수",
            "발매 곡 수"
        ]
    ]

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "누적 레슨 시간": st.column_config.NumberColumn(
                "누적 레슨 시간",
                format="%d시간"
            ),
            "완성 곡 수": st.column_config.NumberColumn(
                "완성 곡 수",
                format="%d곡"
            ),
            "발매 곡 수": st.column_config.NumberColumn(
                "발매 곡 수",
                format="%d곡"
            )
        }
    )


# --------------------------------------------------
# 탭 3: 월별 레슨 시간과 수익
# --------------------------------------------------
with tab3:
    st.subheader("월별 레슨 및 수익 현황")

    # 월별 합계 계산
    monthly_summary = (
        filtered_monthly_df
        .groupby("월", observed=False)[
            ["월 레슨 시간", "레슨 수익"]
        ]
        .sum()
        .reset_index()
    )

    # 데이터가 없는 월 제거
    monthly_summary = monthly_summary[
        monthly_summary["월 레슨 시간"] > 0
    ]

    total_monthly_hours = monthly_summary[
        "월 레슨 시간"
    ].sum()

    total_monthly_revenue = monthly_summary[
        "레슨 수익"
    ].sum()

    average_monthly_revenue = monthly_summary[
        "레슨 수익"
    ].mean()

    revenue_per_hour = 0

    if total_monthly_hours > 0:
        revenue_per_hour = (
            total_monthly_revenue
            / total_monthly_hours
        )

    revenue_col1, revenue_col2, revenue_col3, revenue_col4 = (
        st.columns(4)
    )

    with revenue_col1:
        st.metric(
            "총 레슨 시간",
            f"{total_monthly_hours:,.0f}시간"
        )

    with revenue_col2:
        st.metric(
            "총 레슨 수익",
            f"{total_monthly_revenue:,.0f}원"
        )

    with revenue_col3:
        st.metric(
            "월평균 수익",
            f"{average_monthly_revenue:,.0f}원"
        )

    with revenue_col4:
        st.metric(
            "시간당 평균 수익",
            f"{revenue_per_hour:,.0f}원"
        )

    st.divider()

    # 월별 레슨 시간과 수익 차트
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("월별 총 레슨 시간")

        lesson_hours_chart = monthly_summary.set_index("월")[
            ["월 레슨 시간"]
        ]

        st.bar_chart(
            lesson_hours_chart,
            use_container_width=True
        )

    with chart_col2:
        st.subheader("월별 레슨 수익 변화")

        revenue_chart = monthly_summary.set_index("월")[
            ["레슨 수익"]
        ]

        st.line_chart(
            revenue_chart,
            use_container_width=True
        )

    st.divider()

    # 학생별 월간 기록
    st.subheader("학생별 월간 레슨 현황")

    student_monthly_pivot = filtered_monthly_df.pivot_table(
        index="월",
        columns="이름",
        values="월 레슨 시간",
        aggfunc="sum",
        fill_value=0,
        observed=False
    )

    st.bar_chart(
        student_monthly_pivot,
        use_container_width=True
    )

    st.divider()

    # 선택한 월 상세 정보
    if selected_month == "전체":
        detail_title = "전체 월간 상세 기록"
    else:
        detail_title = f"{selected_month} 상세 기록"

    st.subheader(detail_title)

    monthly_detail = selected_month_df[
        [
            "월",
            "이름",
            "레슨 유형",
            "월 레슨 시간",
            "시간당 레슨비",
            "레슨 수익"
        ]
    ].copy()

    st.dataframe(
        monthly_detail,
        use_container_width=True,
        hide_index=True,
        column_config={
            "월 레슨 시간": st.column_config.NumberColumn(
                "월 레슨 시간",
                format="%d시간"
            ),
            "시간당 레슨비": st.column_config.NumberColumn(
                "시간당 레슨비",
                format="%d원"
            ),
            "레슨 수익": st.column_config.NumberColumn(
                "레슨 수익",
                format="%d원"
            )
        }
    )


# --------------------------------------------------
# 탭 4: 작업 단계 및 피드백
# --------------------------------------------------
with tab4:
    st.subheader("수강생별 작업 현황")

    selected_student = st.selectbox(
        "수강생을 선택하세요.",
        filtered_df["이름"].tolist(),
        key="student_select"
    )

    student_info = filtered_df[
        filtered_df["이름"] == selected_student
    ].iloc[0]

    student_monthly_data = monthly_df[
        monthly_df["이름"] == selected_student
    ].copy()

    info_col1, info_col2 = st.columns(2)

    with info_col1:
        st.write("#### 기본 정보")
        st.write(f"**이름:** {student_info['이름']}")
        st.write(f"**레슨 유형:** {student_info['레슨 유형']}")
        st.write(f"**선호 장르:** {student_info['선호 장르']}")
        st.write(
            f"**주간 레슨 시간:** "
            f"{student_info['주간 레슨 시간']}시간"
        )

    with info_col2:
        st.write("#### 누적 작업 현황")
        st.write(
            f"**누적 레슨 시간:** "
            f"{student_info['누적 레슨 시간']}시간"
        )
        st.write(
            f"**완성 곡 수:** "
            f"{student_info['완성 곡 수']}곡"
        )
        st.write(
            f"**발매 곡 수:** "
            f"{student_info['발매 곡 수']}곡"
        )
        st.write(
            f"**총 레슨 수익:** "
            f"{student_monthly_data['레슨 수익'].sum():,}원"
        )

    st.write("#### 현재 작업 단계")
    st.info(student_info["현재 작업 단계"])

    st.write("#### 피드백")
    st.success(student_info["피드백"])

    st.divider()

    st.write("#### 학생별 월간 레슨 시간")

    selected_student_chart = student_monthly_data.set_index("월")[
        ["월 레슨 시간"]
    ]

    st.line_chart(
        selected_student_chart,
        use_container_width=True
    )

    st.write("#### 학생별 월간 레슨 기록")

    st.dataframe(
        student_monthly_data[
            [
                "월",
                "월 레슨 시간",
                "시간당 레슨비",
                "레슨 수익"
            ]
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "월 레슨 시간": st.column_config.NumberColumn(
                "월 레슨 시간",
                format="%d시간"
            ),
            "시간당 레슨비": st.column_config.NumberColumn(
                "시간당 레슨비",
                format="%d원"
            ),
            "레슨 수익": st.column_config.NumberColumn(
                "레슨 수익",
                format="%d원"
            )
        }
    )