import streamlit as st
import pandas as pd

# 초기 상태 저장
if "students" not in st.session_state:
    st.session_state.students = []
if "traffic" not in st.session_state:
    st.session_state.traffic = {}

st.title("🚦 학생 활동 신호등 대시보드")
st.markdown("### 👩‍🏫 명단을 입력하세요 (쉼표로 구분)")
names_input = st.text_input("예: 지훈, 수아, 민재", key="input")

if st.button("👥 명단 생성"):
    students = [name.strip() for name in names_input.split(",") if name.strip()]
    st.session_state.students = students
    st.session_state.traffic = {name: "🔴" for name in students}
    st.success("✅ 명단이 생성되었습니다!")

if st.button("🟢 활동 시작"):
    st.session_state.traffic = {name: "🔴" for name in st.session_state.students}

st.markdown("---")
st.markdown("### 🚦 현재 신호등 상태")
for student in st.session_state.students:
    st.markdown(f"**{student}**: {st.session_state.traffic.get(student, '🔴')}")

st.markdown("---")
st.markdown("📱 학생 화면 주소: `/student`")
