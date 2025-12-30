import streamlit as st

# 페이지 설정
st.set_page_config(page_title="나의 인생 취미 찾기", page_icon="🎨")

# 1. 취미 데이터 정의 (특성별 점수 매칭)
# 특성: social(혼자/같이), location(실내/실외), energy(활동적/차분함), hand(손재주), effort(꾸준함), budget(비용)
hobbies = [
    {
        "name": "독서",
        "description": "다양한 세계관과 지식을 책을 통해 접하는 정적인 활동입니다.",
        "reason": "혼자 실내에서 차분하게 즐기는 것을 선호하시고 비용 부담이 적은 활동을 원하셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
    },
    {
        "name": "등산",
        "description": "자연을 느끼며 정상에 오르는 성취감을 느끼는 활동입니다.",
        "reason": "실외에서 활동적으로 움직이는 것을 좋아하시고 건강한 땀방울을 흘리는 타입이라 추천해요!",
        "tags": {"social": "상관없음", "location": "실외", "energy": "활동적", "hand": "아니요", "effort": "중요함", "budget": "저렴함"}
    },
    {
        "name": "가죽 공예",
        "description": "세상에 하나뿐인 나만의 지갑이나 소품을 직접 만드는 취미입니다.",
        "reason": "실내에서 손으로 무언가 만드는 것을 좋아하시고 꾸준한 연습을 통해 결과물을 내는 것을 즐기셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "네", "effort": "중요함", "budget": "투자 가능"}
    },
    {
        "name": "풋살",
        "description": "팀원들과 호흡을 맞춰 뛰며 스트레스를 해소하는 구기 종목입니다.",
        "reason": "여럿이서 활발하게 소통하며 뛰어노는 실외 활동을 선호하셔서 추천해요!",
        "tags": {"social": "같이", "location": "실외", "energy": "활동적", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
    },
    {
        "name": "유튜브 영상 편집",
        "description": "촬영한 영상을 나만의 감성으로 편집하여 공유하는 생산적인 활동입니다.",
        "reason": "실내에서 차분하게 작업하며 꾸준히 실력을 쌓아가는 것을 즐기셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "아니요", "effort": "중요함", "budget": "상관없음"}
    }
]

# 앱 타이틀
st.title("🔍 나에게 딱 맞는 취미 찾기")
st.write("간단한 설문을 통해 당신의 성향을 분석하고 최적의 취미를 추천해 드릴게요!")

st.divider()

# 2. 사용자 질문 (설문)
with st.form("hobby_survey"):
    q1 = st.radio("1. 혼자 하는 게 좋아? 같이 하는 게 좋아?", ["혼자", "같이", "상관없음"])
    q2 = st.radio("2. 선호하는 장소는 어디인가요?", ["실내", "실외"])
    q3 = st.radio("3. 평소 성향이 어떠신가요?", ["활동적인 편", "차분한 편"])
    q4 = st.radio("4. 손으로 무언가 만드는 것을 좋아하시나요?", ["네", "아니요"])
    q5 = st.radio("5. 실력이 늘기 위해 꾸준히 연습하는 과정이 중요한가요?", ["중요함", "상관없음"])
    q6 = st.radio("6. 취미에 어느 정도 비용을 투자할 수 있나요?", ["저렴함", "투자 가능", "상관없음"])
    
    submitted = st.form_submit_button("나의 취미 확인하기")

# 3. 답변 바탕 취미 점수 계산 및 추천
if submitted:
    user_answers = {
        "social": q1,
        "location": q2,
        "energy": q3.replace("적인 편", "").replace("한 편", ""), # 활동적, 차분함으로 변환
        "hand": q4,
        "effort": q5,
        "budget": q6
    }
    
    scores = []
    for hobby in hobbies:
        score = 0
        # 각 항목이 일치할 때마다 점수 부여
        for key in user_answers:
            if hobby["tags"][key] == user_answers[key] or hobby["tags"][key] == "상관없음":
                score += 1
        scores.append(score)
    
    # 최고 점수를 받은 취미 선택
    best_match_idx = scores.index(max(scores))
    recommendation = hobbies[best_match_idx]

    # 4. 결과 출력
    st.balloons()
    st.header(f"🎉 추천 취미: [{recommendation['name']}]")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # 이미지가 있다면 여기에 st.image()를 넣을 수 있습니다.
        st.metric(label="매칭 점수", value=f"{max(scores)} / 6")
    
    with col2:
        st.subheader("📌 어떤 취미인가요?")
        st.write(recommendation['description'])
        
        st.subheader("💡 왜 추천됐나요?")
        st.info(recommendation['reason'])

    st.divider()
    st.write("결과가 마음에 드시나요? 다시 테스트하려면 설문 내용을 바꾸고 버튼을 눌러보세요!")
