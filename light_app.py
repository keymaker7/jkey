import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import datetime
import base64
import time

# 자동 새로고침: 5초마다
st_autorefresh(interval=5000, limit=None, key="auto-refresh")

st.set_page_config(page_title="신호등 활동 웹앱 🚦", layout="wide")

# 초기 상태
if "students" not in st.session_state:
    st.session_state.students = []
if "traffic" not in st.session_state:
    st.session_state.traffic = {}
if "history" not in st.session_state:
    st.session_state.history = []
if "activities" not in st.session_state:
    st.session_state.activities = ["기본 활동"]
if "activity_data" not in st.session_state:
    st.session_state.activity_data = {}
if "activity_start_times" not in st.session_state:
    st.session_state.activity_start_times = {}
if "activity_durations" not in st.session_state:
    st.session_state.activity_durations = {}
if "activity_active" not in st.session_state:
    st.session_state.activity_active = {}

# 활동별 기본 초기화
for act in st.session_state.activities:
    st.session_state.activity_data.setdefault(act, {})
    st.session_state.activity_start_times.setdefault(act, None)
    st.session_state.activity_durations.setdefault(act, 0)
    st.session_state.activity_active.setdefault(act, False)

# 저장/불러오기 함수
def save_data():
    df = pd.DataFrame({"학생": st.session_state.students})
    for act in st.session_state.activities:
        df[act] = [st.session_state.activity_data[act].get(s, "🔴") for s in st.session_state.students]
    df.to_csv("student_status.csv", index=False)

def load_data():
    try:
        df = pd.read_csv("student_status.csv")
        st.session_state.students = df["학생"].tolist()
        st.session_state.activities = list(df.columns[1:])
        for act in st.session_state.activities:
            st.session_state.activity_data[act] = dict(zip(df["학생"], df[act]))
    except Exception as e:
        st.error(f"불러오기 오류: {str(e)}")

# 소리 재생용 함수
def play_sound():
    sound_base64 = "UklGRiQAAABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAAZGF0YRAAAAD//w=="
    st.markdown(f"<audio autoplay><source src='data:audio/wav;base64,{sound_base64}' type='audio/wav'></audio>", unsafe_allow_html=True)

# 타이머 텍스트
def format_remaining(seconds):
    mins, secs = divmod(max(0, int(seconds)), 60)
    return f"{mins:02d}:{secs:02d}"

# 탭 구성
tab1, tab2 = st.tabs(["👩‍🏫 교사용 화면", "👦👧 학생용 화면"])

# 교사용 화면
def teacher_view():
    st.markdown("""
        <style>
        input, textarea, select, option {
            color: black !important;
        }
        .bg-box {
            background-color: #f8f8f8;
            color: #000000;
            padding: 15px;
            border-radius: 12px;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📋 교사용 학생 활동 대시보드 🚦")
    st.markdown("### ✏️ 학생 명단을 입력하세요 (쉼표로 구분)")
    names_input = st.text_input("예: 지훈, 수아, 민재")

    if st.button("👥 명단 생성"):
        students = [name.strip() for name in names_input.split(",") if name.strip()]
        st.session_state.students = students
        for act in st.session_state.activities:
            st.session_state.activity_data[act] = {name: "🔴" for name in students}
        st.success("✅ 명단이 생성되었습니다!")

    st.markdown("### ⏱️ 기본 활동 타이머 설정 (분 단위)")
    basic_duration = st.number_input("기본 활동 시간", min_value=1, max_value=180, value=10)

    if st.button("🟢 활동 시작"):
        for act in st.session_state.activities:
            for name in st.session_state.students:
                st.session_state.activity_data[act][name] = "🔴"
            if act == "기본 활동":
                st.session_state.activity_start_times[act] = time.time()
                st.session_state.activity_durations[act] = basic_duration * 60
                st.session_state.activity_active[act] = True
        st.success("🟢 활동이 시작되었습니다!")

    st.markdown("### ➕ 활동 추가")
    new_act = st.text_input("새로운 활동명 입력")
    duration_min = st.number_input("활동 시간 (분)", min_value=1, max_value=180, value=10, key="duration")
    if st.button("활동 추가") and new_act and new_act not in st.session_state.activities:
        st.session_state.activities.append(new_act)
        st.session_state.activity_data[new_act] = {name: "🔴" for name in st.session_state.students}
        st.session_state.activity_start_times[new_act] = time.time()
        st.session_state.activity_durations[new_act] = duration_min * 60
        st.session_state.activity_active[new_act] = True
        st.success(f"✅ 활동 '{new_act}'이(가) 추가되었습니다!")

    st.markdown("### 🔄 활동 타이머 초기화")
    selected_reset = st.selectbox("초기화할 활동 선택", st.session_state.activities)
    if st.button("⏹️ 선택한 활동 타이머 초기화"):
        st.session_state.activity_start_times[selected_reset] = time.time()
        st.session_state.activity_active[selected_reset] = True
        st.success(f"'{selected_reset}' 타이머가 초기화되었습니다!")

    st.markdown("### 💾 명단 저장 및 불러오기")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 저장"):
            save_data()
            st.success("✅ 저장되었습니다!")
    with col2:
        if st.button("📂 불러오기"):
            load_data()
            st.success("📂 불러오기 완료!")

    st.markdown("### 🚦 현재 신호등 상태")
    now = time.time()
    for name in st.session_state.students:
        row = f"<div class='bg-box'>🧒 {name}"
        for act in st.session_state.activities:
            state = st.session_state.activity_data[act].get(name, "🔴")
            start = st.session_state.activity_start_times.get(act)
            duration = st.session_state.activity_durations.get(act, 0)
            timer_display = ""
            if start and st.session_state.activity_active[act]:
                elapsed = now - start
                remaining = duration - elapsed
                if remaining <= 0:
                    timer_display = " ⏱️ 00:00"
                    st.session_state.activity_active[act] = False
                    play_sound()
                else:
                    timer_display = f" ⏱️ {format_remaining(remaining)}"
            row += f" | {act}: {state}{timer_display}"
        row += "</div>"
        st.markdown(row, unsafe_allow_html=True)

# 학생용 화면
def student_view():
    st.title("🙋 학생 활동 상태 변경 🚦")
    if not st.session_state.students:
        st.warning("⚠️ 교사가 아직 명단을 생성하지 않았어요.")
    else:
        name = st.selectbox("📛 본인의 이름을 선택하세요", st.session_state.students)
        activity = st.selectbox("📌 활동을 선택하세요", st.session_state.activities)

        if name and activity:
            current = st.session_state.activity_data[activity].get(name, "🔴")
            st.markdown(f"<div style='font-size:26px;'>현재 상태: {current}</div>", unsafe_allow_html=True)

            if st.button("🚀 다음 단계로 이동"):
                next_state = {"🔴": "🟡", "🟡": "🟢", "🟢": "🟢"}[current]
                st.session_state.activity_data[activity][name] = next_state
                st.success(f"✅ {name}의 상태가 {next_state}로 변경되었습니다!")
                if next_state == "🟢":
                    st.balloons()
                    play_sound()

# 탭 연결
with tab1:
    teacher_view()
with tab2:
    student_view()
