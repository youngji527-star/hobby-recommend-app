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
    },
    {
        "name": "도자기 공예",
        "description": "흙을 빚어 나만의 식기를 만드는 예술적인 활동입니다.",
        "reason": "차분하게 손으로 무언가를 만드는 것을 좋아하시고, 정성을 들이는 과정을 즐기셔서 추천해요!",
        "tags": {"social": "상관없음", "location": "실내", "energy": "차분함", "hand": "네", "effort": "중요함", "budget": "투자 가능"}
    },
    {
        "name": "베이킹",
        "description": "달콤한 향기와 함께 직접 빵과 디저트를 구워내는 취미입니다.",
        "reason": "실내에서 활동적으로 움직이며 손맛을 느낄 수 있는 창의적인 활동이라 추천드려요!",
        "tags": {"social": "상관없음", "location": "실내", "energy": "활동적", "hand": "네", "effort": "중요함", "budget": "투자 가능"}
    },
    {
        "name": "디지털 드로잉",
        "description": "태블릿을 이용해 언제 어디서든 나만의 그림을 그리는 취미입니다.",
        "reason": "장소에 구애받지 않고 손재주를 발휘하며 차분하게 집중하는 시간을 선호하셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "네", "effort": "상관없음", "budget": "상관없음"}
    },
    {
        "name": "가드닝 (식물 키우기)",
        "description": "작은 씨앗이 자라나는 과정을 지켜보며 정서적 안정을 찾는 활동입니다.",
        "reason": "차분하게 손길을 내어 생명을 돌보는 보람을 느끼는 타입이라 추천해 드립니다!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "네", "effort": "중요함", "budget": "저렴함"}
    },
    {
        "name": "실내 클라이밍",
        "description": "암벽을 등반하며 근력과 성취감을 동시에 잡는 익스트림 스포츠입니다.",
        "reason": "실내에서도 역동적으로 움직이며 목표를 달성하는 도전을 좋아하셔서 추천해요!",
        "tags": {"social": "상관없음", "location": "실내", "energy": "활동적", "hand": "아니요", "effort": "중요함", "budget": "투자 가능"}
    },
    {
        "name": "서핑",
        "description": "바다에서 파도를 타며 자연과 하나가 되는 짜릿한 레포츠입니다.",
        "reason": "시원한 야외에서 활동적인 에너지를 발산하는 것을 즐기셔서 강력 추천합니다!",
        "tags": {"social": "상관없음", "location": "실외", "energy": "활동적", "hand": "아니요", "effort": "상관없음", "budget": "투자 가능"}
    },
    {
        "name": "러닝 크루",
        "description": "사람들과 모여 정해진 코스를 달리며 건강을 관리하는 활동입니다.",
        "reason": "야외에서 사람들과 소통하며 활기차게 에너지를 얻는 것을 좋아하셔서 추천해요!",
        "tags": {"social": "같이", "location": "실외", "energy": "활동적", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
    },
    {
        "name": "요가",
        "description": "몸의 유연성을 기르고 내면의 평화를 찾는 심신 수련 활동입니다.",
        "reason": "실내에서 차분하게 자신에게 집중하며 몸을 움직이는 시간을 원하셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "아니요", "effort": "중요함", "budget": "상관없음"}
    },
    {
        "name": "영화 비평 (블로그)",
        "description": "영화 관람 후 나만의 시각으로 분석하고 기록을 남기는 활동입니다.",
        "reason": "실내에서 차분하게 생각하고 기록하는 것을 선호하시는 분석적인 타입이라 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
    },
    {
        "name": "우쿨렐레 연주",
        "description": "작고 배우기 쉬운 악기로 좋아하는 곡을 연주하는 취미입니다.",
        "reason": "실내에서 차분하게 손을 움직이며 결과물을 만들어내는 예술적 성향에 딱 맞아요!",
        "tags": {"social": "상관없음", "location": "실내", "energy": "차분함", "hand": "네", "effort": "중요함", "budget": "투자 가능"}
    },
    {
        "name": "외국어 회화 스터디",
        "description": "다양한 사람들과 만나 외국어로 소통하며 문화를 배우는 활동입니다.",
        "reason": "사람들과 어울려 활동적으로 소통하며 자기계발을 하는 것을 즐기셔서 추천해요!",
        "tags": {"social": "같이", "location": "실내", "energy": "활동적", "hand": "아니요", "effort": "중요함", "budget": "상관없음"}
    },
    {
        "name": "보드게임",
        "description": "친구들이나 모임원들과 전략적인 두뇌 싸움을 즐기는 게임입니다.",
        "reason": "실내에서 사람들과 활발하게 소통하며 즐거운 시간을 보내고 싶어 하셔서 추천해요!",
        "tags": {"social": "같이", "location": "실내", "energy": "활동적", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
    },
    {
        "name": "캠핑",
        "description": "자연 속에서 텐트를 치고 요리하며 여유를 즐기는 힐링 활동입니다.",
        "reason": "야외에서 손수 무언가를 준비하며 활동적으로 시간을 보내는 것을 즐기셔서 추천해요!",
        "tags": {"social": "상관없음", "location": "실외", "energy": "활동적", "hand": "네", "effort": "상관없음", "budget": "투자 가능"}
    },
    {
        "name": "사진 출사",
        "description": "카메라를 들고 아름다운 풍경이나 순간을 담으러 떠나는 활동입니다.",
        "reason": "야외를 돌아다니며 세상을 바라보는 나만의 시선을 남기고 싶어 하셔서 추천해요!",
        "tags": {"social": "상관없음", "location": "실외", "energy": "활동적", "hand": "아니요", "effort": "상관없음", "budget": "상관없음"}
    },
    {
        "name": "명상",
        "description": "하루의 복잡한 생각을 비우고 오로지 현재에 집중하는 마음 공부입니다.",
        "reason": "가장 적은 비용으로 실내에서 차분하게 내면을 돌보는 시간을 원하셔서 추천해요!",
        "tags": {"social": "혼자", "location": "실내", "energy": "차분함", "hand": "아니요", "effort": "상관없음", "budget": "저렴함"}
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
    
   # 점수순으로 정렬하여 상위 3개 추출
    import numpy as np
    indexed_scores = list(enumerate(scores))
    sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)
    top_3_indices = [x[0] for x in sorted_scores[:3]]

    st.balloons()
    st.header("✨ 당신에게 어울리는 취미 TOP 3")
    
    for idx in top_3_indices:
        rec = hobbies[idx]
        with st.expander(f"🏆 추천: {rec['name']} (매칭 점수: {scores[idx]}/6)", expanded=True):
            st.write(f"**어떤 취미인가요?** {rec['description']}")
            st.info(f"**추천 이유:** {rec['reason']}")

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
