"""
예제 제공 모듈

다양한 챕터에서 활용할 수 있는 예제 프롬프트와 샘플 데이터를 제공합니다.
"""

import os
import json
import random
from typing import Dict, List, Any, Optional, Union

# 챕터별 예제 프롬프트
CHAPTER_EXAMPLES = {
    # 1.1 리포트 품질 향상 기법 예제
    "1.1": {
        "topic_analysis": [
            {
                "topic": "디지털 트랜스포메이션이 기업 경쟁력에 미치는 영향",
                "field": "경영학",
                "output_preview": "# 디지털 트랜스포메이션이 기업 경쟁력에 미치는 영향\n\n## 핵심 개념 및 중요성\n디지털 트랜스포메이션은 기업이 디지털 기술을 활용하여 비즈니스 모델, 운영 프로세스, 고객 경험 등을 근본적으로 변화시키는 과정을 의미합니다..."
            },
            {
                "topic": "인공지능 윤리의 현재와 미래",
                "field": "철학/컴퓨터과학",
                "output_preview": "# 인공지능 윤리의 현재와 미래\n\n## 핵심 개념 및 중요성\n인공지능 윤리는 AI 시스템의 개발과 활용 과정에서 발생할 수 있는 윤리적 문제와 이에 대한 가이드라인을 다루는 분야입니다..."
            }
        ],
        "logical_structure": [
            {
                "topic": "기후변화가 생태계에 미치는 영향",
                "key_points": "1. 해수면 상승, 2. 극단적 기상현상 증가, 3. 생물다양성 감소",
                "report_type": "학술 에세이",
                "output_preview": "# 기후변화가 생태계에 미치는 영향: 학술 에세이 구조\n\n## 서론\n- 기후변화의 정의와 현황\n- 생태계에 미치는 영향의 중요성\n- 논문의 목적과 범위..."
            }
        ],
        "citation_optimization": [
            {
                "reference_info": "저자: 김철수, 이영희\n제목: 인공지능 기술의 발전과 사회적 영향\n출판: 한국정보학회지\n발행일: 2023년 3월\n볼륨: 45권 2호\n페이지: 112-145",
                "citation_style": "APA",
                "output_preview": "# APA 스타일 인용 최적화\n\n## 본문 내 인용 형식\n- 첫 인용 시: 김철수와 이영희(2023)는 \"인공지능 기술이 사회에 미치는 영향은...\"이라고 주장했다.\n- 이후 인용 시: 김과 이(2023)는..."
            }
        ]
    },
    
    # 2.1 코딩 개념 이해 및 학습 예제
    "2.1": {
        "concept_explanation": [
            {
                "concept": "재귀 함수(Recursive Function)",
                "language": "Python",
                "level": "초급",
                "output_preview": "# 재귀 함수(Recursive Function) 이해하기\n\n## 정의\n재귀 함수란 **함수가 자기 자신을 호출하는 프로그래밍 기법**입니다. 복잡한 문제를 동일한 구조의 더 작은 문제로 나누어 해결하는 방식이죠..."
            }
        ],
        "code_debugging": [
            {
                "code": "def factorial(n):\n    if n == 0:\n        return 0\n    else:\n        return n * factorial(n-1)",
                "language": "Python",
                "error_description": "factorial(5)를 계산하려고 하는데 0을 반환합니다.",
                "output_preview": "# 팩토리얼 함수 디버깅\n\n## 문제 진단\n현재 코드에서는 `n == 0`일 때 0을 반환하고 있습니다. 그러나 팩토리얼의 정의에 따르면 0!은 1이어야 합니다..."
            }
        ]
    },
    
    # 3.1 연구 계획 및 설계 예제
    "3.1": {
        "research_design": [
            {
                "topic": "소셜 미디어 사용이 청소년 정신건강에 미치는 영향",
                "purpose": "소셜 미디어 사용 패턴과 청소년 불안/우울 증상 간의 상관관계 조사",
                "constraints": "대학 연구 프로젝트, 6개월 기간, 제한된 예산",
                "output_preview": "# 연구 계획: 소셜 미디어와 청소년 정신건강\n\n## 연구 질문\n1. 소셜 미디어 사용 시간과 청소년 불안/우울 증상 간에 상관관계가 있는가?\n2. 특정 유형의 소셜 미디어 활동이 정신건강에 차별적 영향을 미치는가?..."
            }
        ]
    },
    
    # 4.1 이력서 및 자기소개서 작성 예제
    "4.1": {
        "resume_writing": [
            {
                "field": "데이터 분석/데이터 사이언스",
                "experience_level": "신입/인턴",
                "skills": "Python, SQL, 통계 분석, 데이터 시각화",
                "output_preview": "# 데이터 분석 직무 이력서 작성 가이드\n\n## 효과적인 이력서 구조\n1. 인적사항 및 요약 정보\n2. 교육사항 (관련 전공/수업 강조)\n3. 프로젝트 경험..."
            }
        ],
        "cover_letter": [
            {
                "company": "네이버",
                "position": "UX/UI 디자이너",
                "background": "디자인 전공, 2년 프리랜서 경험",
                "output_preview": "# 네이버 UX/UI 디자이너 자기소개서 작성 가이드\n\n## 효과적인 자기소개서 구조\n1. 강렬한 시작 (디자인에 대한 열정, 비전 제시)\n2. 지원 동기 (네이버 제품/디자인 철학에 연결)..."
            }
        ]
    },
    
    # 5.1 역할 기반 프롬프팅 예제
    "5.1": {
        "role_prompting": [
            {
                "role": "경제학자",
                "role_description": "거시경제학을 전공한 20년 경력의 경제학 교수",
                "topic": "중앙은행의 금리 인상이 경제에 미치는 영향",
                "output_preview": "# 금리 인상의 경제적 영향: 경제학자 관점\n\n## 거시경제학적 효과\n금리 인상은 통화 정책의 주요 수단으로, 경제 활동을 냉각시키고 인플레이션을 억제하는 데 사용됩니다..."
            }
        ]
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

# 연구 방법론 목록
RESEARCH_METHODS = [
    "설문조사", "인터뷰", "실험", "사례 연구", "문헌 검토", "시뮬레이션", 
    "종단 연구", "횡단 연구", "현장 연구", "행동 관찰"
]

def get_examples(chapter_id: str, template_name: str, count: int = 1) -> List[Dict[str, Any]]:
    """
    특정 챕터와 템플릿의 예제 데이터 가져오기
    
    Args:
        chapter_id: 챕터 ID (예: 1.1, 2.3)
        template_name: 템플릿 이름
        count: 가져올 예제 수
        
    Returns:
        예제 데이터 목록
    """
    # 첫 두 자리만 추출 (예: 1.1.2 -> 1.1)
    main_chapter = '.'.join(chapter_id.split('.')[:2])
    
    # 해당 챕터의 예제가 있는지 확인
    chapter_data = CHAPTER_EXAMPLES.get(main_chapter, {})
    examples = chapter_data.get(template_name, [])
    
    # 요청한 수만큼 예제 반환 (없으면 빈 리스트)
    return examples[:count] if examples else []


def get_random_field() -> str:
    """랜덤 학문 분야 반환"""
    return random.choice(ACADEMIC_FIELDS)


def get_random_programming_language() -> str:
    """랜덤 프로그래밍 언어 반환"""
    return random.choice(PROGRAMMING_LANGUAGES)


def get_random_research_method() -> str:
    """랜덤 연구 방법론 반환"""
    return random.choice(RESEARCH_METHODS)


def get_sample_research_topics() -> List[str]:
    """샘플 연구 주제 목록 반환"""
    return [
        "인공지능이 노동 시장에 미치는 영향",
        "기후변화가 생태계에 미치는 장기적 영향",
        "소셜 미디어 사용과 청소년 정신건강의 상관관계",
        "도시 환경이 주민 건강에 미치는 영향",
        "원격 학습 환경의 효과성과 학습 성취도 관계",
        "블록체인 기술의 금융 시스템 적용 사례 분석",
        "인공지능 윤리와 사회적 책임에 관한 연구",
        "지속가능한 도시 개발을 위한 정책 방향",
        "현대 소비자의 친환경 제품 구매 행동 분석",
        "가상현실 기술의 교육적 활용과 학습 효과"
    ]


def get_sample_coding_problems() -> List[Dict[str, str]]:
    """샘플 코딩 문제 목록 반환"""
    return [
        {
            "title": "피보나치 수열 계산",
            "description": "주어진 n에 대해 n번째 피보나치 수를 계산하는 함수 작성",
            "difficulty": "쉬움"
        },
        {
            "title": "문자열 뒤집기",
            "description": "입력 문자열을 거꾸로 뒤집는 함수 작성",
            "difficulty": "쉬움"
        },
        {
            "title": "두 수의 최대공약수 찾기",
            "description": "유클리드 알고리즘을 사용하여 두 정수의 최대공약수를 찾는 함수 작성",
            "difficulty": "중간"
        },
        {
            "title": "이진 탐색 구현",
            "description": "정렬된 배열에서 특정 요소의 위치를 찾는 이진 탐색 알고리즘 구현",
            "difficulty": "중간"
        },
        {
            "title": "링크드 리스트 역순 변환",
            "description": "단일 연결 리스트를 역순으로 변환하는 함수 작성",
            "difficulty": "어려움"
        }
    ]


def load_custom_examples(category: str) -> Dict[str, Any]:
    """
    사용자 정의 예제 로드
    
    Args:
        category: 예제 카테고리 (academic, programming, research, career)
        
    Returns:
        사용자 정의 예제 데이터
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    examples_dir = os.path.join(base_dir, "examples")
    file_path = os.path.join(examples_dir, f"{category}_examples.json")
    
    # 파일이 존재하면 로드
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"예제 파일 로드 오류: {e}")
    
    # 없으면 빈 딕셔너리 반환
    return {}