import streamlit as st

st.title("👦👧 나의 활동 상태 바꾸기 🚦")
st.markdown("### 📛 본인의 이름을 선택하세요")

names = st.session_state.get("students", [])
if not names:
    st.error("🚫 아직 교사가 명단을 생성하지 않았습니다.")
else:
    name = st.selectbox("이름 선택", names)

    if name:
        current = st.session_state.traffic.get(name, "🔴")
        st.markdown(f"**현재 내 상태는:** {current}")

        if st.button("다음 단계로 이동 🚀"):
            next_state = {"🔴": "🟡", "🟡": "🟢", "🟢": "🟢"}[current]
            st.session_state.traffic[name] = next_state
            st.success(f"✅ 상태가 {next_state}로 변경되었습니다!")
