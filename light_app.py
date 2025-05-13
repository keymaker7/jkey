import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="신호등 활동 웹앱 🚦", layout="wide")

# 초기 상태 설정
if "students" not in st.session_state:
    st.session_state.students = []
if "traffic" not in st.session_state:
    st.session_state.traffic = {}
if "history" not in st.session_state:
    st.session_state.history = []

# 탭 나누기
tab1, tab2 = st.tabs(["👩‍🏫 교사용 화면", "👦👧 학생용 화면"])

# ------------------------------
# 👩‍🏫 교사용 화면
# ------------------------------
with tab1:
    st.markdown(
        """
        <style>
        .big-font { font-size:30px !important; }
        .bg-box {
            background-color: #fff3cd;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("📋 교사용 학생 활동 대시보드 🚦")
    st.markdown("### ✏️ 학생 명단을 입력하세요 (쉼표로 구분)")
    names_input = st.text_input("예: 지훈, 수아, 민재", key="input")

    if st.button("👥 명단 생성"):
        students = [name.strip() for name in names_input.split(",") if name.strip()]
        st.session_state.students = students
        st.session_state.traffic = {name: "🔴" for name in students}
        st.session_state.history.append((datetime.datetime.now(), "명단 생성"))
        st.success("✅ 명단이 생성되었습니다!")

    if st.button("🟢 활동 시작"):
        st.session_state.traffic = {name: "🔴" for name in st.session_state.students}
        st.session_state.history.append((datetime.datetime.now(), "활동 시작"))
        st.success("🟢 활동을 시작했습니다! 모든 학생은 🔴로 초기화됩니다.")

    st.markdown("---")
    st.markdown("### 🚦 현재 신호등 상태")

    if st.session_state.students:
        for student in st.session_state.students:
            st.markdown(f"<div class='bg-box big-font'>🧒 <b>{student}</b>: {st.session_state.traffic.get(student, '🔴')}</div>", unsafe_allow_html=True)
    else:
        st.info("👆 먼저 명단을 입력하고 생성해 주세요.")

    st.markdown("---")
    st.markdown("### 🕘 활동 히스토리")
    for time, action in reversed(st.session_state.history[-5:]):
        st.markdown(f"{time.strftime('%H:%M:%S')} - {action}")

# ------------------------------
# 👦👧 학생용 화면
# ------------------------------
with tab2:
    st.title("🙋 학생 활동 상태 변경 🚦")
    if not st.session_state.students:
        st.warning("⚠️ 교사가 아직 명단을 생성하지 않았어요.")
    else:
        name = st.selectbox("📛 본인의 이름을 선택하세요", st.session_state.students)

        if name:
            current = st.session_state.traffic.get(name, "🔴")
            st.markdown(f"<div class='big-font'>현재 상태: {current}</div>", unsafe_allow_html=True)

            if st.button("🚀 다음 단계로 이동"):
                next_state = {"🔴": "🟡", "🟡": "🟢", "🟢": "🟢"}[current]
                st.session_state.traffic[name] = next_state
                st.session_state.history.append((datetime.datetime.now(), f"{name} 상태 변경: {current} → {next_state}"))
                st.success(f"✅ {name}의 상태가 {next_state}로 변경되었습니다!")

            st.markdown("---")
            st.image("https://i.imgur.com/DzHr9Xy.png", caption="신호등 예시 이미지", use_column_width=True)

# QR 코드 접속은 별도 배포 주소에서 브라우저 즐겨찾기 또는 휴대폰으로 접속 시 해결 가능합니다.
# 외부 공유 필요시 cloud 또는 ngrok 이용한 공개 주소 사용 권장
