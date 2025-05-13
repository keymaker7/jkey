import streamlit as st
import random

# 웹앱 제목 꾸미기
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>📚✨ 귀염뽀짝 국어 글쓰기 예시 생성기 ✨📚</h1>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stSelectbox label, .stButton button, .stTextInput label, .stTextArea label {
        font-size: 20px !important;
        color: #FF6F61;
    }
</style>
""", unsafe_allow_html=True)

# 선택 옵션 정의
grades = ['1학년 🐣', '2학년 🐥', '3학년 🐤', '4학년 🐦', '5학년 🐧', '6학년 🦜']
writing_types = ['편지글 💌', '논설문 🗣️', '설명문 📘', '시 ✨', '소설 📖', '수필 🌸', '독후감 📚']

# 사용자 입력 받기
st.sidebar.markdown("### 🧸 학년과 글 종류를 골라보세요!")
selected_grade = st.sidebar.selectbox("📚 학년 선택", grades)
selected_type = st.sidebar.selectbox("📝 글의 종류 선택", writing_types)

# 예시 글 데이터베이스 (추가됨)
examples = {
    '1학년': {
        '편지글': ["엄마에게💌: 엄마, 사랑해요! 언제나 맛있는 밥 해줘서 고마워요! 💖"],
        '시': ["🌼봄🌼\n꽃이 피었어요.\n나비가 날아요.\n봄이 왔어요!"],
        '설명문': ["우산은 비를 막아주는 물건이에요. 비 오는 날 꼭 필요해요 ☔"]
    },
    '2학년': {
        '수필': ["나는 오늘 학교에서 친구와 놀았다. 그 순간이 너무 행복했다 😊"],
        '시': ["✨별빛✨\n하늘에 반짝이는 별\n나의 꿈도 반짝반짝"]
    },
    '3학년': {
        '논설문': ["📢 학교 급식에 과일을 더 넣어야 해요! 건강해지고 기분도 좋아져요!"],
        '설명문': ["🧠 뇌는 우리 몸을 조절하는 중요한 기관이에요. 생각하고 움직이고 기억해요!"],
        '수필': ["할머니 댁에 다녀왔다. 고양이도 보고, 시골 공기도 마셨다 🏡"]
    },
    '4학년': {
        '소설': ["🌲숲 속의 비밀 문\n지민이는 나무 뒤에 숨어 있는 빛나는 문을 발견했다..."],
        '편지글': ["친구에게💌: 오늘 같이 놀아서 즐거웠어! 다음에도 놀자~"]
    },
    '5학년': {
        '소설': ["🐱 고양이 루루의 모험\n루루는 숲 속에서 반짝이는 구슬을 찾으러 떠났어요..."],
        '독후감': ["📚 『강아지 똥』을 읽고\n작은 강아지 똥도 소중한 일을 할 수 있다는 걸 알게 되었어요."],
        '논설문': ["모두가 환경을 지켜야 해요. 작은 실천이 큰 변화를 만들어요 🌏"]
    },
    '6학년': {
        '설명문': ["태양계는 여러 행성으로 이루어져 있어요. 지구는 세 번째 행성이에요 🌍"],
        '논설문': ["청소년도 사회에 의견을 낼 수 있어야 해요. 목소리를 낼 권리가 있어요! 🗣️"]
    }
}

# 학년 정리 (1학년 -> '1학년')
grade_key = selected_grade[0] + '학년'
writing_key = selected_type.split(' ')[0]

# 글 자동 생성 (AI 대체용 랜덤 생성)
def generate_random_sentence(wtype, grade):
    starters = ["오늘은", "나는", "우리 반은", "모두가"]
    middles = ["즐거운 일을", "생각을", "중요한 사실을", "느낀 점을"]
    endings = ["기록했다.", "느꼈다.", "전하고 싶다.", "설명하고 싶다."]
    return f"{random.choice(starters)} {random.choice(middles)} {random.choice(endings)} ({grade} {wtype})"

# 출력
st.markdown("### 🎉 생성된 글 예시 ✍️")
if grade_key in examples and writing_key in examples[grade_key]:
    result = random.choice(examples[grade_key][writing_key])
    st.markdown(f"""
    <div style='background-color:#FFF0F5; padding: 20px; border-radius: 15px; font-size: 20px;'>
    {result}
    </div>
    """, unsafe_allow_html=True)
else:
    ai_generated = generate_random_sentence(writing_key, grade_key)
    st.markdown(f"💡 AI 자동 생성 예시: {ai_generated}")

# 직접 글 써보기
st.markdown("---")
st.markdown("### ✏️ 나만의 글을 직접 써 보세요!")
user_input = st.text_area("💌 여기에 글을 써보세요 (주제: {} {})".format(selected_grade, selected_type))
if user_input:
    st.success("✅ 글이 잘 저장되었어요! 멋진 글이에요~ ✨")
    st.markdown(f"""
    <div style='background-color:#E6E6FA; padding: 20px; border-radius: 15px;'>
    <strong>🖍️ 나의 글:</strong><br>{user_input}
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
---
<div style='text-align:center;'>
    <p>🎈 매일매일 다양한 글을 써 보며 멋진 작가가 되어봐요! ✏️🧸</p>
</div>
""", unsafe_allow_html=True)
