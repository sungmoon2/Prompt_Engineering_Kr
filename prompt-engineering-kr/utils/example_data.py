"""
예제 데이터 제공 모듈

다양한 챕터의 실습에서 사용되는 예제 데이터를 제공합니다.
"""

from typing import Dict, List, Any, Optional

# Part 0-1: 프롬프트 엔지니어링 입문 & 기초 프롬프트 작성법
TOPIC_EXAMPLES = {
    "1": {"name": "IR 자료 분석", "topic": "기업 IR 자료", "level": "비즈니스"},
    "2": {"name": "양자 컴퓨팅", "topic": "양자 컴퓨팅의 기초 개념", "level": "기술"},
    "3": {"name": "행동경제학", "topic": "행동경제학의 넛지 이론", "level": "경제/심리"},
    "4": {"name": "CRISPR 유전자 편집", "topic": "CRISPR 유전자 편집 기술", "level": "생명과학"},
    "5": {"name": "블록체인 기술", "topic": "블록체인과 분산원장 기술", "level": "기술/금융"}
}

# Part 2-3: 복잡한 과제 분해 & 맥락 유지와 대화 관리
TASK_EXAMPLES = {
    "1": {
        "name": "기업 분석 리포트",
        "task": "신생 핀테크 기업의 시장 진입 전략과 경쟁 환경을 분석하는 리포트 작성",
        "domain": "경영/경제"
    },
    "2": {
        "name": "웹 애플리케이션 개발",
        "task": "학생들을 위한 스터디 그룹 매칭 및 일정 관리 웹 애플리케이션 개발",
        "domain": "프로그래밍"
    },
    "3": {
        "name": "연구 계획서 작성",
        "task": "소셜 미디어 사용이 대학생 정신 건강에 미치는 영향에 관한 연구 계획서 작성",
        "domain": "심리학/연구"
    },
    "4": {
        "name": "이벤트 기획",
        "task": "대학 축제에서 학과 홍보를 위한 체험형 부스 기획 및 운영",
        "domain": "이벤트/기획"
    },
    "5": {
        "name": "교육 프로그램 개발",
        "task": "고등학생을 위한 AI 기초 교육 8주 커리큘럼 개발",
        "domain": "교육"
    }
}

# Part 4: 학술 에세이/보고서 작성
ACADEMIC_TOPICS = {
    "1": {
        "name": "인공지능 윤리",
        "topic": "인공지능의 윤리적 활용과 사회적 책임",
        "field": "기술/철학",
        "type": "에세이"
    },
    "2": {
        "name": "지속가능 발전",
        "topic": "기후변화 시대의 지속가능한 경제 발전 모델",
        "field": "환경/경제",
        "type": "보고서"
    },
    "3": {
        "name": "디지털 프라이버시",
        "topic": "빅데이터 시대의 개인정보 보호와 디지털 권리",
        "field": "법학/사회학",
        "type": "논문"
    },
    "4": {
        "name": "원격 교육 효과",
        "topic": "COVID-19 이후 원격 교육의 효과성과 미래 방향",
        "field": "교육학",
        "type": "연구보고서"
    },
    "5": {
        "name": "소셜미디어 영향",
        "topic": "소셜미디어가 청년 정체성 형성에 미치는 영향",
        "field": "심리학/미디어",
        "type": "에세이"
    }
}

# Part 5: 프로그래밍 과제 해결
CODING_TASK_EXAMPLES = {
    "1": {
        "name": "파일 처리 스크립트",
        "task": "폴더 내 모든 CSV 파일을 읽고 데이터를 합친 후 요약 통계를 계산하는 Python 스크립트",
        "language": "Python",
        "level": "중급"
    },
    "2": {
        "name": "간단한 웹 크롤러",
        "task": "지정된 웹사이트에서 뉴스 제목과 요약을 수집하는 웹 크롤러",
        "language": "Python",
        "level": "중급"
    },
    "3": {
        "name": "학생 관리 시스템",
        "task": "학생 정보를 저장, 수정, 검색할 수 있는 간단한 콘솔 애플리케이션",
        "language": "Java",
        "level": "초급"
    },
    "4": {
        "name": "할 일 목록 웹앱",
        "task": "사용자가 할 일을 추가, 완료 표시, 삭제할 수 있는 간단한 웹 애플리케이션",
        "language": "JavaScript/HTML/CSS",
        "level": "초급"
    },
    "5": {
        "name": "데이터 시각화 도구",
        "task": "CSV 데이터를 읽어서 다양한 차트로 시각화하는 대시보드 애플리케이션",
        "language": "Python",
        "level": "중급"
    }
}

# Part 6: 도메인별 프롬프트 최적화
FIELD_SPECIFIC_TASKS = {
    "경영학": [
        {"name": "SWOT 분석", "task": "신규 스타트업의 SWOT 분석 및 전략 제안"},
        {"name": "마케팅 계획", "task": "대학생 타겟 신제품 마케팅 계획 수립"},
        {"name": "경영 사례 연구", "task": "기업의 디지털 전환 성공 사례 분석"}
    ],
    "심리학": [
        {"name": "실험 설계", "task": "스트레스와 학업 성취도 관계에 대한 실험 설계"},
        {"name": "문헌 검토", "task": "인지행동치료의 효과성에 관한 문헌 검토"},
        {"name": "연구 가설", "task": "소셜미디어 사용과 자존감 관계에 대한 연구 가설 개발"}
    ],
    "컴퓨터과학": [
        {"name": "알고리즘 설계", "task": "효율적인 데이터 정렬 알고리즘 설계"},
        {"name": "시스템 아키텍처", "task": "대학 도서관 관리 시스템 아키텍처 설계"},
        {"name": "UX/UI 디자인", "task": "모바일 학습 앱 UI/UX 디자인 가이드라인 개발"}
    ],
    "문학/어학": [
        {"name": "작품 분석", "task": "현대 소설에 나타난 페미니즘적 요소 분석"},
        {"name": "비교 연구", "task": "한국 문학과 일본 문학의 자연 묘사 비교 연구"},
        {"name": "언어 분석", "task": "소셜미디어에서의 청년 언어 사용 패턴 분석"}
    ],
    "의학/생명과학": [
        {"name": "문헌 리뷰", "task": "신종 바이러스 치료법 관련 최신 연구 동향 리뷰"},
        {"name": "사례 연구", "task": "만성질환 관리를 위한 디지털 헬스케어 사례 연구"},
        {"name": "연구 계획", "task": "영양 상태가 면역체계에 미치는 영향 연구 계획 수립"}
    ]
}

# Part 7: 고급 프롬프트 테크닉
ADVANCED_PROMPT_EXAMPLES = {
    "역할 기반": [
        {"role": "심리학 교수", "task": "학습 동기부여 이론 설명"},
        {"role": "경제 분석가", "task": "최근 인플레이션의 원인과 영향 분석"},
        {"role": "UX 디자이너", "task": "사용자 중심 웹사이트 설계 원칙 설명"}
    ],
    "단계적 사고": [
        {"problem": "대학축제 예산 할당 최적화", "complexity": "중간"},
        {"problem": "기후변화 대응 캠퍼스 정책 개발", "complexity": "높음"},
        {"problem": "온라인 강의 참여율 향상 전략", "complexity": "중간"}
    ],
    "형식 및 구조": [
        {"content": "학과 소개 내용", "format": "마케팅 웹페이지"},
        {"content": "연구 결과", "format": "인포그래픽"},
        {"content": "취업 준비 정보", "format": "가이드북"}
    ]
}

# Part 8: 프롬프트 디버깅과 개선
DEBUG_PROMPT_EXAMPLES = {
    "1": {
        "name": "모호한 요청",
        "original": "인공지능에 대해 알려줘.",
        "issue": "너무 광범위하고 모호한 요청"
    },
    "2": {
        "name": "지시 불명확",
        "original": "좋은 에세이를 작성하는 방법을 알려줘.",
        "issue": "평가 기준과 에세이 유형이 불명확함"
    },
    "3": {
        "name": "맥락 부족",
        "original": "이 코드의 문제점을 찾아줘: for i in range(10): print(data[i])",
        "issue": "data 변수 정의와 목적 맥락 부족"
    },
    "4": {
        "name": "전문 용어 남용",
        "original": "RESTful API의 CRUD 구현에서 DTO와 ORM을 활용한 아키텍처 설계를 제안해줘.",
        "issue": "초보자가 이해하기 어려운 전문 용어 과다 사용"
    },
    "5": {
        "name": "목적 불분명",
        "original": "마케팅 전략에 대해 알려줘. 그리고 소셜미디어도 다뤄줘.",
        "issue": "명확한 목적과 요구사항 부재"
    }
}

# 학문 분야 목록
ACADEMIC_FIELDS = [
    "경영학", "경제학", "교육학", "국어국문학", "기계공학", "심리학", "영어영문학", 
    "역사학", "의학", "인공지능", "전산학/컴퓨터공학", "철학", "통계학", "화학공학", 
    "환경공학"
]

# 프로그래밍 언어 목록
PROGRAMMING_LANGUAGES = [
    "Python", "Java", "JavaScript", "C++", "C#", "PHP", "Swift", "Kotlin", 
    "Go", "R", "Ruby", "MATLAB"
]

def get_examples_by_category(category: str) -> Dict:
    """
    카테고리별 예제 데이터 가져오기
    
    Args:
        category: 데이터 카테고리 (topic, task, academic, coding, field, advanced, debug)
        
    Returns:
        해당 카테고리의 예제 데이터
    """
    categories = {
        "topic": TOPIC_EXAMPLES,
        "task": TASK_EXAMPLES,
        "academic": ACADEMIC_TOPICS,
        "coding": CODING_TASK_EXAMPLES,
        "field": FIELD_SPECIFIC_TASKS,
        "advanced": ADVANCED_PROMPT_EXAMPLES,
        "debug": DEBUG_PROMPT_EXAMPLES,
        "academic_fields": ACADEMIC_FIELDS,
        "programming_languages": PROGRAMMING_LANGUAGES
    }
    
    return categories.get(category, {})

def get_random_example(category: str) -> Any:
    """
    카테고리에서 랜덤 예제 가져오기
    
    Args:
        category: 데이터 카테고리
        
    Returns:
        랜덤 예제
    """
    import random
    
    examples = get_examples_by_category(category)
    
    if isinstance(examples, list):
        return random.choice(examples)
    elif isinstance(examples, dict):
        key = random.choice(list(examples.keys()))
        return examples[key]
    else:
        return None