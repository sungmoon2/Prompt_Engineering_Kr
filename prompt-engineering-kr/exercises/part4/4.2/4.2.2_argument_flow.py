def demonstrate_logical_flow_analysis():
    """논리적 흐름 분석 기능의 데모 함수"""
    
    print("\n===== 논리적 흐름 분석 도구 데모 =====\n")
    
    # 샘플 텍스트 - 좋은 논리적 흐름을 가진 예시
    good_sample = """소셜 미디어는 현대 청소년의 정신 건강에 복합적인 영향을 미치고 있다. 최근 연구에 따르면, 청소년들은 하루 평균 3시간 이상을 소셜 미디어 플랫폼에서 보내며, 이는 10년 전에 비해 두 배 이상 증가한 수치이다. 이러한 증가세는 스마트폰의 보급과 함께 가속화되었으며, 코로나19 팬데믹 기간 동안 더욱 급격히 상승했다. 연구자들은 이러한 현상이 청소년 발달에 중요한 시기에 어떤 영향을 미치는지 주목하고 있다.

소셜 미디어의 부정적 영향 중 가장 우려되는 측면은 정신 건강 문제와의 연관성이다. 특히, 과도한, 소셜 미디어 사용은 불안, 우울증, 낮은 자존감과 같은 증상과 상관관계가 있는 것으로 나타났다. 예를 들어, 펜실베니아 대학의 한 연구에서는 소셜 미디어 사용을 2주간 제한한 그룹이 통제 그룹에 비해 외로움과 우울 증상이 유의미하게 감소함을 발견했다. 이러한 결과는 소셜 미디어가 청소년의 정신 건강에 직접적인 영향을 미칠 수 있음을 시사한다.

그러나 모든 소셜 미디어 활동이 동일한 영향을 미치는 것은 아니다. 연구에 따르면, 소셜 미디어 사용의 방식과 목적이 중요한 차이를 만들어낸다. 적극적인 소셜 미디어 참여(예: 콘텐츠 생성, 의미 있는 대화)는 사회적 연결과 지원을 강화할 수 있는 반면, 수동적 소비(예: 무한 스크롤링, 타인의 삶 관찰)는 사회적 비교와 부정적 감정을 촉발할 가능성이 더 높다. 따라서 단순히 사용 시간을 줄이는 것보다 어떻게 사용하는지가 더 중요한 요소일 수 있다.

이러한 연구 결과를 고려할 때, 교육자와 부모는 청소년의 소셜 미디어 사용에 대한 균형 잡힌 접근법을 개발할 필요가 있다. 완전한 금지보다는 비판적 미디어 리터러시 교육과 건강한 사용 습관 형성이 더 효과적인 전략일 수 있다. 결과적으로, 소셜 미디어의 잠재적 이점을 활용하면서 위험을 최소화하는 방향으로 청소년을 안내하는 것이 중요하다."""
    
    # 샘플 텍스트 - 논리적 흐름에 문제가 있는 예시
    bad_sample = """소셜 미디어는 청소년에게 영향을 미친다. 청소년들은 하루에 많은 시간을 소셜 미디어에 소비한다. 불안과 우울증이 증가하고 있다. 일부 연구에서는 긍정적 효과도 보고된다. 또래 압박이 온라인으로 확장되었다. 사회적 비교도 문제가 된다.

소셜 미디어 사용 시간을 제한해야 한다. 하지만 요즘 청소년들은 스마트폰 없이는 살 수 없다. 사실 어른들도 소셜 미디어를 많이 사용한다. 누구나 인스타그램과 틱톡"""
논리적 흐름과 일관성 확보 실습 모듈

Part 4 - 섹션 4.2.2 실습 코드: 에세이/보고서의 논리적 흐름과 
일관성을 향상시키는 다양한 전략과 기법을 실습합니다.
"""

import os
import sys
import re
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
LOGICAL_FLOW_TOPICS = {
    "1": {"name": "구조 패턴 분석", "topic": "학술 에세이의 다양한 논리적 구조 패턴 분석 및 적용", "output_format": "구조 가이드"},
    "2": {"name": "단락 구성 최적화", "topic": "MEAL/PEEL 구조를 활용한 효과적인 단락 구성 전략", "output_format": "작성 템플릿"},
    "3": {"name": "전환구 강화", "topic": "단락 및 섹션 간 자연스러운 전환을 위한 효과적인 전략", "output_format": "전환구 도구모음"},
    "4": {"name": "논리적 흐름 평가", "topic": "에세이/보고서의 논리적 흐름과 일관성을 체계적으로 평가하는 방법", "output_format": "평가 체크리스트"},
    "5": {"name": "흐름 개선 사례", "topic": "논리적 흐름과 일관성 문제를 성공적으로 개선한 실제 사례 분석", "output_format": "사례 분석"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "역할 설정: 학술 글쓰기 전문가",
        "맥락 제공: 학생의 목표와 어려움 명시",
        "구체적 요청: 체계적인 접근법과 실용적 도구 요청",
        "형식 지정: 단계별 가이드와 실제 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "논리적 흐름과 일관성은 독자가 작성자의 주장과 논증을 따라가는 데 필수적인 요소입니다",
    "효과적인, 단락 구성(MEAL/PEEL 구조)은 명확한 주제문, 증거, 분석, 연결을 포함합니다",
    "다양한 전환 기법(키워드 반복, 개념 연결, 전환어 사용 등)이 단락과 섹션 간 연결성을 강화합니다",
    "논리적 흐름은 거시적(전체 구조)과 미시적(단락 수준) 두 차원에서 모두 확보되어야 합니다",
    "일관된 용어, 시제, 스타일 사용은 내용의 명확성과 전문성을 높입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학술 글쓰기 전문가", 
        "학술적 글쓰기의 논리적 흐름과 일관성을 향상시키는 기법을 지도하는 전문가로, 학생들이 설득력 있고 명확한 학술 에세이와 보고서를 작성할 수 있도록 돕습니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"현재 학술 에세이/보고서를 작성하고 있으며, 제 글의 논리적 흐름과 일관성을 "
        f"향상시키는 데 어려움을 겪고 있습니다. 독자가 제 논점을 쉽게 따라갈 수 있고 "
        f"설득력 있는 글을 작성하기 위한 실용적인 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "구조 패턴 분석" in topic:
        builder.add_instructions([
            "학술 에세이/보고서에 적용할 수 있는 다양한 논리적 구조 패턴(선형적, 비교/대조, 문제/해결 등)을 상세히 설명해주세요",
            "각 구조 패턴의 특징, 장단점, 적합한 상황을 비교해주세요",
            "여러 학문 분야(인문학, 사회과학, 자연과학)에서 각 구조 패턴의 적용 방법 차이를 설명해주세요",
            "특정 주제에 가장 적합한 구조 패턴을 선택하는 기준과 고려사항을 제시해주세요",
            "선택한 구조 패턴을 효과적으로 적용하기 위한 단계별 접근법을 안내해주세요"
        ])
    elif "단락 구성 최적화" in topic:
        builder.add_instructions([
            "MEAL 구조(Main idea, Evidence, Analysis, Link)와 PEEL 구조(Point, Evidence, Explanation, Link)의 원리와 차이점을 상세히 설명해주세요",
            "효과적인 주제문 작성법과 주제문이 전체 논증에 기여하는 방식을 설명해주세요",
            "다양한 증거 유형(통계, 인용, 사례 등)과 이를 효과적으로 제시하는 방법을 안내해주세요",
            "증거에 대한 분석과 해석을 발전시키는 구체적인 전략을 제공해주세요",
            "단락을 전체 논증과 연결하는 다양한 방법과 다음 단락으로의 자연스러운 전환 기법을 제안해주세요"
        ])
    elif "전환구 강화" in topic:
        builder.add_instructions([
            "단락 및 섹션 간 효과적인 전환의 중요성과 역할을 설명해주세요",
            "다양한 유형의 전환(추가, 대조, 인과, 시간, 예시 등)과 각 유형에 적합한 표현을 제시해주세요",
            "전환을 위한 다양한 기법(키워드 반복, 개념 연결, 전환어 사용, 질문 활용 등)을 구체적인 예시와 함께 설명해주세요",
            "서로 다른 관계(유사성, 대조, 인과, 확장 등)를 가진 단락/섹션 간 전환 전략을 제안해주세요",
            "일반적인 전환 실수와 이를 개선하는 방법을 포함해주세요"
        ])
    elif "논리적 흐름 평가" in topic:
        builder.add_instructions([
            "에세이/보고서의 논리적 흐름과 일관성을 평가하기 위한 체계적인 방법을 설명해주세요",
            "거시적 수준(전체 구조)과 미시적 수준(단락 구성)의 논리적 흐름을 평가하는 구체적인 체크리스트를 제공해주세요",
            "논리적 비약, 주제 이탈, 모순적 주장, 구조적 불균형 등의 일반적인 문제를 식별하는 방법을 안내해주세요",
            "자가 평가, 피어 리뷰, AI 도구 활용 등 다양한 평가 접근법의 장단점을 비교해주세요",
            "평가 결과를 바탕으로 논리적 흐름과 일관성을 개선하는 단계별 전략을 제시해주세요"
        ])
    elif "흐름 개선 사례" in topic:
        builder.add_instructions([
            "논리적 흐름과 일관성 문제를 성공적으로 개선한 다양한 학문 분야의 실제 사례를 분석해주세요",
            "각 사례에서 초기에 존재했던 문제점을 명확히 식별하고 설명해주세요",
            "적용된 개선 전략과 기법을 단계별로 상세히 설명해주세요",
            "개선 전후를 비교하는 구체적인 예시를 포함하여 변화의 효과를 보여주세요",
            "각 사례에서 배울 수 있는 핵심 교훈과 다른 상황에 적용할 수 있는 일반적 원칙을 도출해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "이론적 배경과 주요 개념을 명확히 설명해주세요",
            "단계별 프로세스와 구체적인 적용 방법을 제시해주세요",
            "학생이 직접 적용할 수 있는 실용적인 전략과 도구를 포함해주세요",
            "다양한 학문적 맥락에 맞게 조정할 수 있는 유연한 접근법을 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 템플릿, 체크리스트, 워크시트 등의 실용적 도구를 포함해주세요. "
        f"개념 설명뿐만 아니라 다양한 학문 분야에서의 구체적인 예시를 포함해주세요. "
        f"모든 내용은 대학생이 직접 적용할 수 있도록 실용적이고 단계별로 작성해주세요."
    )
    
    return builder.build()

def get_potential_issues(text: str, transition_density: float) -> List[str]:
    """
    텍스트의 논리적 흐름에서 잠재적 문제를 식별하는 함수
    
    Args:
        text: 분석할 텍스트
        transition_density: 전환어 밀도
        
    Returns:
        잠재적 문제점 목록
    """
    issues = []
    
    # 전환어 밀도 기반 문제 식별
    if transition_density < 0.15:
        issues.append("전환어 사용 빈도가 낮아 단락 간 연결이 약할 수 있습니다.")
    
    # 단락 길이 기반 문제 식별
    paragraphs = text.split('\n\n')
    for i, para in enumerate(paragraphs):
        words = para.split()
        if len(words) > 200:
            issues.append(f"단락 {i+1}이 너무 길어 초점이 흐려질 수 있습니다.")
        elif len(words) < 30 and len(words) > 0:
            issues.append(f"단락 {i+1}이 너무 짧아 충분한 발전이 부족할 수 있습니다.")
    
    # 단락 시작 다양성 검사
    para_starts = [p.strip().split()[0].lower() if p.strip() and p.strip().split() else "" for p in paragraphs]
    start_counts = {}
    for start in para_starts:
        if start:
            start_counts[start] = start_counts.get(start, 0) + 1
    
    for word, count in start_counts.items():
        if count > 2 and word not in ["the", "a", "an"]:
            issues.append(f"'{word}'(으)로 시작하는 단락이 {count}개로, 시작 표현의 다양성을 높이는 것이 좋습니다.")
    
    return issues

def analyze_logical_flow(text: str) -> Dict[str, Any]:
    """
    텍스트의 논리적 흐름을 분석하는 함수
    
    Args:
        text: 분석할 텍스트
    
    Returns:
        분석 결과 딕셔너리
    """
    # 이 함수는 실제 분석을 위한 placeholder로,
    # AI 활용 없이 기본적인 지표만 계산합니다.
    
    paragraphs = text.split('\n\n')
    sentences = text.split('.')
    
    # 기본적인 지표 계산
    avg_paragraph_length = sum(len(p.split('.')) for p in paragraphs) / len(paragraphs) if paragraphs else 0
    
    # 전환어 목록
    transition_words = [
        "furthermore", "moreover", "in addition", "additionally", 
        "however", "nevertheless", "on the other hand", "in contrast",
        "for example", "for instance", "specifically", "particularly",
        "as a result", "therefore", "consequently", "thus",
        "first", "second", "finally", "subsequently",
        "in conclusion", "to summarize", "in summary", "to synthesize"
    ]
    
    # 전환어 사용 빈도 계산
    transition_count = sum(1 for word in transition_words if word.lower() in text.lower())
    transition_density = transition_count / len(sentences) if sentences else 0
    
    # 분석 결과 반환
    return {
        "paragraph_count": len(paragraphs),
        "sentence_count": len(sentences),
        "avg_paragraph_length": round(avg_paragraph_length, 2),
        "avg_sentence_length": round(avg_sentence_length, 2),
        "transition_count": transition_count,
        "transition_density": round(transition_density, 2),
        "potential_issues": self.get_potential_issues(text, transition_density, paragraphs)
    }

def demonstrate_logical_flow_analysis():
    """논리적 흐름 분석 기능의 데모 함수"""
    
    print("\n===== 논리적 흐름 분석 도구 데모 =====\n")
    
    # 샘플 텍스트 - 좋은 논리적 흐름을 가진 예시
    good_sample = """소셜 미디어는 현대 청소년의 정신 건강에 복합적인 영향을 미치고 있다. 최근 연구에 따르면, 청소년들은 하루 평균 3시간 이상을 소셜 미디어 플랫폼에서 보내며, 이는 10년 전에 비해 두 배 이상 증가한 수치이다. 이러한 증가세는 스마트폰의 보급과 함께 가속화되었으며, 코로나19 팬데믹 기간 동안 더욱 급격히 상승했다. 연구자들은 이러한 현상이 청소년 발달에 중요한 시기에 어떤 영향을 미치는지 주목하고 있다.

소셜 미디어의 부정적 영향 중 가장 우려되는 측면은 정신 건강 문제와의 연관성이다. 특히, 과도한, 소셜 미디어 사용은 불안, 우울증, 낮은 자존감과 같은 증상과 상관관계가 있는 것으로 나타났다. 예를 들어, 펜실베니아 대학의 한 연구에서는 소셜 미디어 사용을 2주간 제한한 그룹이 통제 그룹에 비해 외로움과 우울 증상이 유의미하게 감소함을 발견했다. 이러한 결과는 소셜 미디어가 청소년의 정신 건강에 직접적인 영향을 미칠 수 있음을 시사한다.

그러나 모든 소셜 미디어 활동이 동일한 영향을 미치는 것은 아니다. 연구에 따르면, 소셜 미디어 사용의 방식과 목적이 중요한 차이를 만들어낸다. 적극적인 소셜 미디어 참여(예: 콘텐츠 생성, 의미 있는 대화)는 사회적 연결과 지원을 강화할 수 있는 반면, 수동적 소비(예: 무한 스크롤링, 타인의 삶 관찰)는 사회적 비교와 부정적 감정을 촉발할 가능성이 더 높다. 따라서 단순히 사용 시간을 줄이는 것보다 어떻게 사용하는지가 더 중요한 요소일 수 있다.

이러한 연구 결과를 고려할 때, 교육자와 부모는 청소년의 소셜 미디어 사용에 대한 균형 잡힌 접근법을 개발할 필요가 있다. 완전한 금지보다는 비판적 미디어 리터러시 교육과 건강한 사용 습관 형성이 더 효과적인 전략일 수 있다. 결과적으로, 소셜 미디어의 잠재적 이점을 활용하면서 위험을 최소화하는 방향으로 청소년을 안내하는 것이 중요하다."""
    
    # 샘플 텍스트 - 논리적 흐름에 문제가 있는 예시
    bad_sample = """소셜 미디어는 청소년에게 영향을 미친다. 청소년들은 하루에 많은 시간을 소셜 미디어에 소비한다. 불안과 우울증이 증가하고 있다. 일부 연구에서는 긍정적 효과도 보고된다. 또래 압박이 온라인으로 확장되었다. 사회적 비교도 문제가 된다.

소셜 미디어 사용 시간을 제한해야 한다. 하지만 요즘 청소년들은 스마트폰 없이는 살 수 없다. 사실 어른들도 소셜 미디어를 많이 사용한다. 누구나 인스타그램과 틱톡을 사용한다. 이것은 학교 성적에도 영향을 준다. 스트레스도 증가한다."""
    
    # 논리적 흐름 분석기 인스턴스 생성
    analyzer = LogicalFlowAnalyzer()
    
    # 좋은 예시 분석
    print("==== 논리적 흐름이 좋은 텍스트 분석 ====")
    good_analysis = analyzer.analyze_text(good_sample)
    
    print("\n[전체 텍스트 분석]")
    print(f"- 단락 수: {good_analysis['overall_analysis']['paragraph_count']}")
    print(f"- 문장 수: {good_analysis['overall_analysis']['sentence_count']}")
    print(f"- 평균 단락 길이: {good_analysis['overall_analysis']['avg_paragraph_length']} 단어")
    print(f"- 평균 문장 길이: {good_analysis['overall_analysis']['avg_sentence_length']} 단어")
    print(f"- 전환어 수: {good_analysis['overall_analysis']['transition_count']}")
    print(f"- 전환어 밀도: {good_analysis['overall_analysis']['transition_density']}")
    
    print("\n[잠재적 문제점]")
    if good_analysis['overall_analysis']['potential_issues']:
        for issue in good_analysis['overall_analysis']['potential_issues']:
            print(f"- {issue}")
    else:
        print("- 특별한 문제점이 발견되지 않았습니다.")
    
    print("\n[단락 구조 분석]")
    for para_analysis in good_analysis['paragraph_analyses']:
        print(f"\n단락 {para_analysis['paragraph_number']}:")
        print(f"- 내용: {para_analysis['content']}")
        print(f"- MEAL 구조 점수: {para_analysis['meal_structure']['structure_score']}/4")
        
        meal_components = []
        if para_analysis['meal_structure']['has_main_idea']:
            meal_components.append("주제문(M)")
        if para_analysis['meal_structure']['has_evidence']:
            meal_components.append("증거(E)")
        if para_analysis['meal_structure']['has_analysis']:
            meal_components.append("분석(A)")
        if para_analysis['meal_structure']['has_link']:
            meal_components.append("연결(L)")
        
        print(f"- 포함된 요소: {', '.join(meal_components)}")
        print("- 개선 제안:")
        for suggestion in para_analysis['meal_structure']['improvement_suggestions']:
            print(f"  * {suggestion}")
    
    # 나쁜 예시 분석 (간략히)
    print("\n\n==== 논리적 흐름에 문제가 있는 텍스트 분석 ====")
    bad_analysis = analyzer.analyze_text(bad_sample)
    
    print("\n[전체 텍스트 분석]")
    print(f"- 단락 수: {bad_analysis['overall_analysis']['paragraph_count']}")
    print(f"- 평균 단락 길이: {bad_analysis['overall_analysis']['avg_paragraph_length']} 단어")
    print(f"- 전환어 밀도: {bad_analysis['overall_analysis']['transition_density']}")
    
    print("\n[잠재적 문제점]")
    for issue in bad_analysis['overall_analysis']['potential_issues']:
        print(f"- {issue}")
    
    print("\n[비교 결과]")
    print(f"좋은 예시 전환어 밀도: {good_analysis['overall_analysis']['transition_density']}")
    print(f"나쁜 예시 전환어 밀도: {bad_analysis['overall_analysis']['transition_density']}")
    print(f"좋은 예시 평균 MEAL 구조 점수: {sum(p['meal_structure']['structure_score'] for p in good_analysis['paragraph_analyses']) / len(good_analysis['paragraph_analyses']):.2f}/4")
    print(f"나쁜 예시 평균 MEAL 구조 점수: {sum(p['meal_structure']['structure_score'] for p in bad_analysis['paragraph_analyses']) / len(bad_analysis['paragraph_analyses']):.2f}/4")

def interactive_logical_flow_analysis():
    """사용자 입력 텍스트의 논리적 흐름을 분석하는 대화형 함수"""
    
    print("\n===== 논리적 흐름 분석 도구 =====\n")
    print("이 도구는 에세이/보고서의 논리적 흐름과 일관성을 분석하고 개선 제안을 제공합니다.")
    print("분석하려는 텍스트를 입력하세요. 텍스트 입력이 완료되면 빈 줄 입력 후 Ctrl+D(Unix) 또는 Ctrl+Z(Windows)를 누르세요.\n")
    
    # 사용자 입력 수집
    print("텍스트 입력 (종료: 빈 줄 + Ctrl+D/Z):")
    lines = []
    try:
        while True:
            line = input()
            if not line and not lines:  # 첫 번째 줄이 비어있는 경우 예시 사용
                use_example = input("텍스트를 입력하지 않았습니다. 예시 텍스트를 사용하시겠습니까? (y/n): ").lower()
                if use_example == 'y':
                    lines = [
                        "소셜 미디어는 청소년의 정신 건강에 영향을 미친다. 최근 연구에 따르면 청소년들은 하루 평균 3시간 이상을 소셜 미디어에 소비한다.",
                        "소셜 미디어 사용이 증가하면서 청소년의 불안과 우울증 사례도 증가했다. 그러나 모든 소셜 미디어 활동이 부정적인 것은 아니다.",
                        "적극적인 소셜 미디어 참여는 사회적 연결을 강화할 수 있다. 반면, 수동적 소비는 부정적 영향을 미칠 수 있다."
                    ]
                    break
                else:
                    print("프로그램을 종료합니다.")
                    return
            lines.append(line)
            if not line and lines:  # 빈 줄 입력으로 종료
                break
    except EOFError:
        pass
    
    text = "\n".join(lines)
    if not text.strip():
        print("유효한 텍스트가 입력되지 않았습니다. 프로그램을 종료합니다.")
        return
    
    # 논리적 흐름 분석
    analyzer = LogicalFlowAnalyzer()
    analysis = analyzer.analyze_text(text)
    
    # 결과 출력
    print("\n===== 논리적 흐름 분석 결과 =====\n")
    
    print("[기본 정보]")
    print(f"- 단락 수: {analysis['overall_analysis']['paragraph_count']}")
    print(f"- 문장 수: {analysis['overall_analysis']['sentence_count']}")
    print(f"- 평균 단락 길이: {analysis['overall_analysis']['avg_paragraph_length']} 단어")
    print(f"- 평균 문장 길이: {analysis['overall_analysis']['avg_sentence_length']} 단어")
    
    print("\n[논리적 흐름 지표]")
    transition_density = analysis['overall_analysis']['transition_density']
    print(f"- 전환어 수: {analysis['overall_analysis']['transition_count']}")
    print(f"- 전환어 밀도: {transition_density:.2f}")
    
    # 전환어 밀도 평가
    if transition_density < 0.1:
        print("  * 전환어 밀도가 매우 낮습니다. 단락/문장 간 연결을 강화하세요.")
    elif transition_density < 0.2:
        print("  * 전환어 밀도가 다소 낮습니다. 더 다양한 전환어를 고려하세요.")
    elif transition_density > 0.4:
        print("  * 전환어 밀도가 다소 높습니다. 과도한 전환어 사용을 점검하세요.")
    else:
        print("  * 전환어 밀도가 적절합니다.")
    
    print("\n[잠재적 문제점]")
    if analysis['overall_analysis']['potential_issues']:
        for issue in analysis['overall_analysis']['potential_issues']:
            print(f"- {issue}")
    else:
        print("- 특별한 문제점이 발견되지 않았습니다.")
    
    print("\n[단락 구조 분석]")
    for para_analysis in analysis['paragraph_analyses']:
        print(f"\n단락 {para_analysis['paragraph_number']}:")
        print(f"- 내용: {para_analysis['content']}")
        print(f"- MEAL 구조 점수: {para_analysis['meal_structure']['structure_score']}/4")
        
        meal_components = []
        if para_analysis['meal_structure']['has_main_idea']:
            meal_components.append("주제문(M)")
        if para_analysis['meal_structure']['has_evidence']:
            meal_components.append("증거(E)")
        if para_analysis['meal_structure']['has_analysis']:
            meal_components.append("분석(A)")
        if para_analysis['meal_structure']['has_link']:
            meal_components.append("연결(L)")
        
        if meal_components:
            print(f"- 포함된 요소: {', '.join(meal_components)}")
        else:
            print("- 포함된 MEAL 요소 없음")
        
        print("- 개선 제안:")
        for suggestion in para_analysis['meal_structure']['improvement_suggestions']:
            print(f"  * {suggestion}")
    
    if len(analysis['transition_analyses']) > 0:
        print("\n[단락 간 전환 분석]")
        for trans_analysis in analysis['transition_analyses']:
            print(f"\n단락 {trans_analysis['from_paragraph']}에서 단락 {trans_analysis['to_paragraph']}로의 전환:")
            print("- 추천 전환구:")
            for i, suggestion in enumerate(trans_analysis['transition_suggestions'][:3], 1):
                print(f"  {i}. {suggestion}")
    
    print("\n===== 논리적 흐름 개선을 위한 종합 제안 =====\n")
    
    # 종합 점수 계산 (0-10)
    meal_avg_score = sum(p['meal_structure']['structure_score'] for p in analysis['paragraph_analyses']) / len(analysis['paragraph_analyses']) if analysis['paragraph_analyses'] else 0
    normalized_meal_score = (meal_avg_score / 4) * 5  # 0-5점 변환
    
    transition_score = min(5, max(0, transition_density * 10))  # 0-5점 변환 (0.5가 최적)
    if transition_density > 0.5:
        transition_score = 5 - min(5, (transition_density - 0.5) * 10)
    
    total_score = normalized_meal_score + transition_score
    
    print(f"논리적 흐름 종합 점수: {total_score:.1f}/10")
    
    # 점수 기반 종합 평가
    if total_score >= 8:
        print("전반적으로 논리적 흐름이 좋습니다. 제안된 개선사항을 적용하면 더욱 향상될 것입니다.")
    elif total_score >= 6:
        print("논리적 흐름이 양호하지만 개선의 여지가 있습니다. 위에 제시된 제안사항에 주목하세요.")
    elif total_score >= 4:
        print("논리적 흐름에 다소 문제가 있습니다. 단락 구조와 전환을 중점적으로 개선하세요.")
    else:
        print("논리적 흐름에 상당한 문제가 있습니다. 글의 구조와 연결성을 전체적으로 재검토하세요.")
    
    # 우선 개선 영역 제안
    print("\n[우선 개선 영역]")
    
    if meal_avg_score < 2:
        print("1. 단락 구조: MEAL 구조를 따르도록 각 단락을 재구성하세요.")
        print("   - 명확한 주제문으로 시작")
        print("   - 구체적인 증거/예시 추가")
        print("   - 증거에 대한 분석 포함")
        print("   - 전체 논점과의 연결 강화")
    
    if transition_density < 0.15:
        print("2. 전환어 활용: 문장과 단락 간 연결을 강화하기 위해 더 많은 전환어를 활용하세요.")
        print("   - 추가 관계: '또한', '더욱이', '이에 더해'")
        print("   - 대조 관계: '그러나', '반면에', '그럼에도 불구하고'")
        print("   - 인과 관계: '따라서', '그 결과', '이로 인해'")
        print("   - 예시 관계: '예를 들어', '구체적으로', '특히'")
    
    if analysis['overall_analysis']['potential_issues']:
        issue_count = len(analysis['overall_analysis']['potential_issues'])
        print(f"3. 식별된 문제점({issue_count}개): 위에 나열된 잠재적 문제점을 해결하세요.")
    
    print("\n이 분석은 기본적인 텍스트 특성에 기반한 것입니다.")
    print("더 깊이 있는 분석과 맞춤형 피드백을 위해 AI를 활용한 프롬프트를 고려하세요.")

def custom_get_enhanced_prompt(topic: str) -> str:
    """
    논리적 흐름 분석을 위한 맞춤형 향상된 프롬프트 생성
    
    Args:
        topic: 텍스트 주제/내용
        
    Returns:
        AI 분석을 위한 프롬프트
    """
    builder = PromptBuilder()
    
    builder.add_role(
        "논리적 흐름 분석 전문가", 
        "학술적 글쓰기의 논리적 흐름과 일관성을 분석하고 개선하는 전문가로, 효과적인 에세이와 보고서 작성을 위한 실용적인 피드백을 제공합니다."
    )
    
    builder.add_context(
        f"다음 텍스트의 논리적 흐름과 일관성을 분석하고 개선점을 제안해주세요:\n\n{topic}"
    )
    
    builder.add_instructions([
        "텍스트의 전체적인 논리적 구조와 흐름을 분석해주세요",
        "단락 내부 구조 (MEAL/PEEL 구조 적용 여부)를 평가해주세요",
        "단락 간 전환의 효과성과 자연스러움을 분석해주세요",
        "논리적 비약, 모순, 불필요한 반복 등의 문제를 식별해주세요",
        "언어적 일관성(용어, 시제, 어조 등)을 평가해주세요",
        "논리적 흐름과 일관성을 향상시키기 위한 구체적인 개선 제안을 제공해주세요"
    ])
    
    builder.add_format_instructions(
        "다음 섹션을 포함하여 체계적인 분석을 제공해주세요:\n\n"
        "1. 전체 구조 분석: 전반적인 논리적 구조와 흐름 평가\n"
        "2. 단락 수준 분석: 각 단락의 내부 구조와 기능 평가\n"
        "3. 전환 분석: 단락/섹션 간 전환의 효과성 평가\n"
        "4. 문제점 식별: 논리적 흐름을 방해하는 요소들\n"
        "5. 개선 제안: 구체적이고 실행 가능한 개선 방안\n\n"
        "평가는 객관적이고 건설적이며, 개선 제안은 구체적이고 실용적이어야 합니다."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="논리적 흐름과 일관성 확보 방법",
        topic_options=LOGICAL_FLOW_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 추가 옵션: 대화형 분석 도구 실행
    print("\n===== 추가 옵션 =====")
    print("1. 데모 실행: 샘플 텍스트의 논리적 흐름 분석")
    print("2. 대화형 분석: 사용자 입력 텍스트 분석")
    print("3. 끝내기")
    
    choice = input("\n선택 (1-3): ").strip()
    
    if choice == '1':
        demonstrate_logical_flow_analysis()
    elif choice == '2':
        interactive_logical_flow_analysis()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")
