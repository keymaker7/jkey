import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("⚾ 발야구 전략 시뮬레이터")

# 스코어 초기화
if "scoreA" not in st.session_state:
    st.session_state["scoreA"] = 0
if "scoreB" not in st.session_state:
    st.session_state["scoreB"] = 0

# 점수판
st.markdown("## 🧮 팀 점수")
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.write(f"**팀 A 점수:** {st.session_state['scoreA']}")
    if st.button("A +1"):
        st.session_state["scoreA"] += 1
with col2:
    st.write(f"**팀 B 점수:** {st.session_state['scoreB']}")
    if st.button("B +1"):
        st.session_state["scoreB"] += 1

# 모드 선택
mode = st.radio("⚙️ 모드 선택", ["공격 모드", "수비 모드", "기본 수비전략"])

# 이름 변경
st.markdown("### 👤 선수 이름 변경")
player_options = ["선수 1", "선수 2", "선수 3"]
selected_player = st.selectbox("선수 선택", player_options)
new_name = st.text_input("새 이름 입력")
if st.button("이름 변경"):
    st.success(f"{selected_player} → {new_name} (시각적으로는 아래 필드에서 직접 수정해야 함)")

# 발야구 필드 (HTML)
st.markdown("## 🏟️ 전략 필드")
components.html(f"""
    <style>
        .field {{
            position: relative;
            width: 100%;
            max-width: 800px;
            height: 500px;
            margin: auto;
            background: url('https://i.imgur.com/o2T2snL.png'); /* 임시 야구장 배경 */
            background-size: cover;
            border: 2px solid #333;
        }}
        .player {{
            position: absolute;
            width: 50px; height: 50px;
            border-radius: 50%;
            line-height: 50px; text-align: center;
            font-size: 12px;
            font-weight: bold;
            background-color: #ff9999;
        }}
        .ball {{
            position: absolute;
            width: 50px; height: 50px;
            border-radius: 50%;
            line-height: 50px; text-align: center;
            font-size: 12px;
            font-weight: bold;
            background-color: yellow;
        }}
    </style>

    <div class="field">
        <div class="player" style="top: 400px; left: 370px;">선수 1</div>
        <div class="player" style="top: 200px; left: 100px;">선수 2</div>
        <div class="player" style="top: 150px; left: 500px;">선수 3</div>
        <div class="ball" style="top: 400px; left: 390px;">발야구 공</div>
    </div>
""", height=550)

# 규칙 설명 섹션
st.markdown("## 📖 발야구 규칙 설명")
if "rules" not in st.session_state:
    st.session_state["rules"] = [
        "1루, 2루, 3루, 홈이 있음",
        "공을 차면 주자를 보낼 수 있음"
    ]

new_rule = st.text_input("규칙 추가")
if st.button("규칙 추가"):
    if new_rule.strip():
        st.session_state["rules"].append(new_rule.strip())

if st.button("마지막 규칙 삭제"):
    if st.session_state["rules"]:
        st.session_state["rules"].pop()

st.markdown("### 현재 규칙 목록")
for idx, rule in enumerate(st.session_state["rules"], 1):
    st.markdown(f"- {idx}. {rule}")
