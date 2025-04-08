"""
A/B 테스트 접근법 실습 모듈

Part 8 - 섹션 8.2.2 실습 코드: 프롬프트 개선을 위한 A/B 테스트 접근법을 학습하고 적용합니다.
"""

import os
import sys
import random
from typing import Dict, List, Any, Optional, Tuple

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.ai_client import get_completion
from utils.exercise_template import run_exercise

# 주제 옵션 정의
AB_TEST_TOPICS = {
    "1": {"name": "역할 지정 효과", "topic": "역할 지정 유무에 따른 프롬프트 효과성 비교", "output_format": "분석 리포트"},
    "2": {"name": "지시 방식 차이", "topic": "일반 지시와 단계별 지시 방식의 효과 비교", "output_format": "비교 분석"},
    "3": {"name": "예시 포함 효과", "topic": "예시 포함 여부에 따른 결과 차이 분석", "output_format": "테스트 보고서"},
    "4": {"name": "맥락 제공 효과", "topic": "배경 정보 제공 유무의 영향 평가", "output_format": "효과 분석"},
    "5": {"name": "길이 영향 분석", "topic": "간결한 프롬프트와 상세한 프롬프트의 효과성 비교", "output_format": "성능 비교"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["A/B 테스트에 대한 일반적 접근법 요청"],
    "enhanced": [
        "체계적 테스트 설계: 명확한 가설과 변수 설정",
        "다양한 A/B 테스트 유형 적용: 목적에 맞는 테스트 방법론 선택",
        "객관적 평가 기준: 정량적/정성적 분석을 위한 명확한 기준 제시"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "A/B 테스트는 프롬프트 개선을 위한 체계적이고 과학적인 접근법입니다",
    "단일 변수 원칙을 통해 어떤 요소가 성능에 영향을 미치는지 명확히 파악할 수 있습니다",
    "객관적 평가 기준과 충분한 반복은 신뢰할 수 있는 결과를 얻는 데 필수적입니다",
    "다양한 유형의 A/B 테스트를 통해 프롬프트의 다양한 측면을 최적화할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "A/B 테스트 전문가", 
        "프롬프트 엔지니어링에서 A/B 테스트를 설계하고 실행하여 최적의 결과를 도출하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심이 있는 프롬프트 엔지니어링 학습자입니다. "
        f"다양한 프롬프트 패턴과 구성요소의 효과를 객관적으로 평가하고 "
        f"최적의 방식을 찾기 위한 체계적인 A/B 테스트 접근법을 배우고 싶습니다. "
        f"이를 통해 더 효과적인 프롬프트를 개발하는 능력을 키우고자 합니다."
    )
    
    # 구체적인 지시사항 추가
    if "역할 지정" in topic:
        builder.add_instructions([
            "역할 지정의 효과를 테스트하기 위한 체계적인 A/B 테스트 설계 방법을 설명해주세요",
            "역할 지정이 있는 프롬프트(B)와 없는 프롬프트(A)를 비교하는 구체적인 실험 설계를 제안해주세요",
            "다양한 역할 유형(전문가, 교육자, 코치 등)의 효과 차이를 테스트하는 방법도 포함해주세요",
            "역할 지정 효과를 객관적으로 평가할 수 있는 명확한 지표와 평가 기준을 제시해주세요",
            "실제 A/B 테스트 예시와 함께 결과 분석 및 해석 방법을 설명해주세요"
        ])
    elif "지시 방식" in topic:
        builder.add_instructions([
            "일반 지시와 단계별 지시 방식의 효과를 비교하는 A/B 테스트 설계 방법을 설명해주세요",
            "동일한 과제에 대해 단순 지시(A)와 상세한 단계별 지시(B)를 비교하는 실험 설계를 제안해주세요",
            "다양한 복잡성 수준의 과제에서 지시 방식의 효과 차이를 테스트하는 방법을 포함해주세요",
            "지시 방식의 효과를 평가하기 위한 객관적인 지표와 평가 프레임워크를 제시해주세요",
            "실제 A/B 테스트 사례와 함께 결과 분석 및 최적의 지시 방식 도출 과정을 설명해주세요"
        ])
    elif "예시 포함" in topic:
        builder.add_instructions([
            "예시 포함 여부에 따른 프롬프트 효과 차이를 테스트하는 A/B 테스트 설계 방법을 설명해주세요",
            "예시가 없는 프롬프트(A)와 예시가 포함된 프롬프트(B)를 비교하는 실험 구조를 제안해주세요",
            "다양한 예시 유형(긍정/부정 예시, 단일/복수 예시 등)의 효과 차이를 테스트하는 방법도 포함해주세요",
            "예시 효과를 객관적으로 평가할 수 있는 지표와 평가 방법을 제시해주세요",
            "실제 예시가 포함된 A/B 테스트 케이스와 함께 결과 분석 및 최적의 예시 활용 전략을 설명해주세요"
        ])
    elif "맥락 제공" in topic:
        builder.add_instructions([
            "배경 정보 제공 유무에 따른 프롬프트 효과를 테스트하는 A/B 테스트 설계 방법을 설명해주세요",
            "맥락 없는 직접적 질문(A)과 배경 정보가 포함된 질문(B)을 비교하는 실험 구조를 제안해주세요",
            "다양한 맥락 유형(개인적 상황, 목적 설명, 제약 조건 등)의 효과 차이를 테스트하는 방법을 포함해주세요",
            "맥락 제공 효과를 객관적으로 평가할 수 있는 지표와 평가 프레임워크를 제시해주세요",
            "실제 맥락 제공 관련 A/B 테스트 사례와 함께 결과 분석 및 최적의 맥락 설계 전략을 설명해주세요"
        ])
    elif "길이 영향" in topic:
        builder.add_instructions([
            "프롬프트 길이가 결과에 미치는 영향을 테스트하는 A/B 테스트 설계 방법을 설명해주세요",
            "간결한 프롬프트(A)와 상세한 프롬프트(B)를 비교하는 체계적인 실험 구조를 제안해주세요",
            "다양한 복잡성 수준의 과제에서 프롬프트 길이의 효과 차이를 테스트하는 방법을 포함해주세요",
            "프롬프트 길이와 효과성 관계를 객관적으로 평가할 수 있는 지표와 방법론을 제시해주세요",
            "실제 프롬프트 길이 관련 A/B 테스트 사례와 함께 결과 분석 및 최적의 길이 설계 전략을 설명해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적인 A/B 테스트 접근법을 설명해주세요",
            "해당 유형의 A/B 테스트를 위한 구체적인 실험 설계와 변수 정의 방법을 제안해주세요",
            "테스트 결과를 객관적으로 평가할 수 있는 지표와 분석 프레임워크를 제시해주세요",
            "잠재적 편향이나 오류를 방지하기 위한 테스트 설계 전략을 포함해주세요",
            "실제 관련 A/B 테스트 사례와 함께 결과 해석 및 최적의 프롬프트 도출 방법을 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요: "
        f"1) A/B 테스트 설계: 가설, 변수, 측정 지표 정의 "
        f"2) 테스트 구현: 구체적인 프롬프트 예시와 실험 절차 "
        f"3) 결과 분석: 데이터 수집, 통계적 방법, 해석 가이드 "
        f"4) 최적화 전략: 테스트 결과를 바탕으로 한 개선 접근법 "
        f"5) 실제 사례 연구: 관련된 실제 A/B 테스트 예시와 교훈 "
        f"표, 다이어그램, 예시 프롬프트 쌍 등 시각적 요소를 활용하여 명확성을 높여주세요. "
        f"실제 프롬프트 엔지니어링에 바로 적용할 수 있는 실용적인 가이드를 제공해주세요."
    )
    
    return builder.build()

def run_ab_test(test_type: str) -> Tuple[List[Dict], Dict]:
    """A/B 테스트 실행 및 결과 반환

    Args:
        test_type: 테스트 유형 (역할 지정, 지시 방식, 예시 포함 등)

    Returns:
        Tuple[List[Dict], Dict]: 테스트 결과와 요약 정보
    """
    print_header(f"A/B 테스트 실행: {test_type}")
    
    # 테스트 유형에 따른 A/B 프롬프트 쌍 설정
    prompt_pairs = get_test_prompts(test_type)
    if not prompt_pairs:
        return [], {"error": "지원되지 않는 테스트 유형입니다."}
    
    # 테스트 설정
    repeats = 3  # 반복 횟수 (실제로는 더 많은 반복이 필요할 수 있음)
    test_results = []
    
    print(f"\n{test_type} 테스트를 {repeats}회 반복 실행합니다...\n")
    
    # 테스트 실행
    for i in range(repeats):
        pair = random.choice(prompt_pairs)  # 여러 쌍 중 무작위 선택
        prompt_a = pair["prompt_a"]
        prompt_b = pair["prompt_b"]
        question = pair["question"]
        
        print(f"반복 {i+1}/{repeats} - 질문: {question[:50]}...")
        
        # 무작위 순서로 A와 B 실행 (순서 편향 방지)
        if random.choice([True, False]):
            print("순서: A → B")
            result_a = run_single_test("A", prompt_a, question)
            result_b = run_single_test("B", prompt_b, question)
        else:
            print("순서: B → A")
            result_b = run_single_test("B", prompt_b, question)
            result_a = run_single_test("A", prompt_a, question)
        
        # 결과 비교 분석
        comparison = compare_results(result_a, result_b)
        
        # 결과 저장
        test_results.append({
            "question": question,
            "prompt_a": prompt_a,
            "prompt_b": prompt_b,
            "result_a": result_a,
            "result_b": result_b,
            "comparison": comparison
        })
        
        print(f"반복 {i+1} 완료: {comparison['winner']} 승리 (점수: {comparison['score_a']} vs {comparison['score_b']})\n")
    
    # 종합 결과 분석
    summary = analyze_results(test_results)
    print("\n===== 테스트 결과 요약 =====")
    print(f"총 테스트 횟수: {summary['total_tests']}")
    print(f"A 승리: {summary['a_wins']} ({summary['a_win_percent']}%)")
    print(f"B 승리: {summary['b_wins']} ({summary['b_win_percent']}%)")
    print(f"무승부: {summary['ties']} ({summary['tie_percent']}%)")
    print(f"평균 점수 - A: {summary['avg_score_a']:.2f}, B: {summary['avg_score_b']:.2f}")
    print(f"개선 효과: {summary['improvement_percent']}%")
    print(f"결론: {summary['conclusion']}")
    
    return test_results, summary

def print_header(title: str) -> None:
    """테스트 섹션 헤더 출력"""
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)

def get_test_prompts(test_type: str) -> List[Dict]:
    """테스트 유형에 따른 A/B 프롬프트 쌍 반환"""
    prompt_pairs = []
    
    if "역할 지정" in test_type:
        prompt_pairs = [
            {
                "question": "기후 변화의 주요 원인과 해결책을 설명해주세요.",
                "prompt_a": "기후 변화의 주요 원인과 해결책을 설명해주세요.",
                "prompt_b": "기후 과학자로서, 기후 변화의 주요 원인과 해결책을 설명해주세요."
            },
            {
                "question": "효과적인 학습 방법에 대해 알려주세요.",
                "prompt_a": "효과적인 학습 방법에 대해 알려주세요.",
                "prompt_b": "교육 심리학 전문가로서, 효과적인 학습 방법에 대해 알려주세요."
            }
        ]
    elif "지시 방식" in test_type:
        prompt_pairs = [
            {
                "question": "고객 만족도를 높이는 전략을 설명해주세요.",
                "prompt_a": "고객 만족도를 높이는 전략을 설명해주세요.",
                "prompt_b": "고객 만족도를 높이는 전략을 설명하되, 먼저 주요 문제점을 파악하고, 각 문제점에 대한 해결책을 제시한 후, 구현 방안을 설명해주세요."
            },
            {
                "question": "프레젠테이션 스킬 향상 방법에 대해 알려주세요.",
                "prompt_a": "프레젠테이션 스킬 향상 방법에 대해 알려주세요.",
                "prompt_b": "프레젠테이션 스킬 향상 방법에 대해 알려주되, 1) 준비 단계, 2) 내용 구성, 3) 발표 기술, 4) 시각 자료 활용, 5) 질의응답 대응으로 나누어 단계별로 설명해주세요."
            }
        ]
    elif "예시 포함" in test_type:
        prompt_pairs = [
            {
                "question": "설득력 있는 이메일을 작성하는 방법을 알려주세요.",
                "prompt_a": "설득력 있는 이메일을 작성하는 방법을 알려주세요.",
                "prompt_b": "설득력 있는 이메일을 작성하는 방법을 알려주세요. 예를 들어, '안녕하세요, 귀사의 제품에 큰 관심이 있어 연락드립니다...'와 같은 시작이 효과적일 수 있습니다."
            },
            {
                "question": "효과적인 목표 설정 방법에 대해 설명해주세요.",
                "prompt_a": "효과적인 목표 설정 방법에 대해 설명해주세요.",
                "prompt_b": "효과적인 목표 설정 방법에 대해 설명해주세요. 예를 들어, '6개월 내에 5kg 감량하기'는 '살을 빼기'보다 SMART 원칙에 부합하는 목표입니다."
            }
        ]
    elif "맥락 제공" in test_type:
        prompt_pairs = [
            {
                "question": "투자 포트폴리오 구성 전략을 설명해주세요.",
                "prompt_a": "투자 포트폴리오 구성 전략을 설명해주세요.",
                "prompt_b": "저는 30대 초반의 직장인으로, 은퇴를 위한 장기 투자를 시작하려고 합니다. 현재 적금과 주식에 소액 투자 중이며, 중간 정도의 위험을 감수할 수 있습니다. 이런 상황에서 투자 포트폴리오 구성 전략을 설명해주세요."
            },
            {
                "question": "영어 회화 실력을 향상시키는 방법을 알려주세요.",
                "prompt_a": "영어 회화 실력을 향상시키는 방법을 알려주세요.",
                "prompt_b": "저는 TOEIC 850점 정도의 영어 실력을 갖고 있지만, 실제 대화에서는 말문이 막히는 경우가 많습니다. 3개월 후 해외 출장이 예정되어 있어 비즈니스 상황에서 자연스럽게 의사소통할 수 있도록 영어 회화 실력을 향상시키는 방법을 알려주세요."
            }
        ]
    elif "길이 영향" in test_type:
        prompt_pairs = [
            {
                "question": "팀 협업을 개선하는 방법을 알려주세요.",
                "prompt_a": "팀 협업을 개선하는 방법을 알려주세요.",
                "prompt_b": "팀 협업을 개선하는 방법을 알려주세요. 현재 우리 팀은 소통 부재, 역할 불명확, 일정 지연 등의 문제가 있습니다. 팀원들은 각자 업무에만 집중하는 경향이 있으며, 회의는 비효율적으로 진행되고 있습니다. 원격 근무와 사무실 근무가 혼합된 하이브리드 환경에서 작업하고 있으며, 다양한 부서와의 협업도 필요합니다. 이러한 상황에서 팀워크를 강화하고, 의사소통을 개선하며, 프로젝트 효율성을 높일 수 있는 구체적인 전략과 방법을 알려주세요."
            },
            {
                "question": "시간 관리 기술을 향상시키는 방법을 알려주세요.",
                "prompt_a": "시간 관리 기술을 향상시키는 방법을 알려주세요.",
                "prompt_b": "시간 관리 기술을 향상시키는 방법을 알려주세요. 저는 일과 개인 생활의 균형을 맞추기 위해 노력하고 있는 직장인입니다. 매일 할 일이 너무 많아 우선순위를 정하기 어렵고, 자주 업무에 압도됨을 느낍니다. 특히 이메일 처리, 회의 참석, 예상치 못한 작업 등으로 계획된 일정이 자주 흐트러집니다. 또한 집중력 유지와 업무 중 방해 요소 관리에도 어려움을 겪고 있습니다. 이런 상황에서 일과 개인 생활의 균형을 유지하면서도 효과적으로 시간을 관리하고 생산성을 높일 수 있는 구체적인 기술과 전략을 알려주세요."
            }
        ]
    
    return prompt_pairs

def run_single_test(variant: str, prompt: str, question: str) -> Dict:
    """단일 테스트 실행"""
    print(f"  변형 {variant} 테스트 중...")
    
    # 프롬프트와 질문 결합
    full_prompt = prompt if question in prompt else prompt + "\n\n" + question
    
    # API 호출
    try:
        response = get_completion(full_prompt, temperature=0.7)
        
        # 간단한 응답 평가 (실제로는 더 복잡한 평가 필요)
        word_count = len(response.split())
        structure_score = evaluate_structure(response)
        relevance_score = evaluate_relevance(response, question)
        
        return {
            "variant": variant,
            "response": response[:300] + "...",  # 긴 응답은 잘라서 표시
            "full_response": response,
            "word_count": word_count,
            "structure_score": structure_score,
            "relevance_score": relevance_score
        }
    except Exception as e:
        print(f"  오류 발생: {e}")
        return {
            "variant": variant,
            "error": str(e),
            "word_count": 0,
            "structure_score": 0,
            "relevance_score": 0
        }

def evaluate_structure(text: str) -> int:
    """응답의 구조 평가 (1-10 점수)"""
    # 실제로는 더 복잡한 평가 로직이 필요함
    # 여기서는 마크다운 요소와 단락 구성을 기준으로 간단히 평가
    score = 5  # 기본 점수
    
    # 제목/소제목 사용
    if "#" in text:
        score += 1
    
    # 목록 사용
    if "- " in text or "* " in text or any(f"{i}. " in text for i in range(1, 10)):
        score += 1
    
    # 단락 구분
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    if len(paragraphs) >= 3:
        score += 1
    
    # 강조 사용
    if "**" in text or "*" in text:
        score += 1
    
    # 표/코드 블록 사용
    if "```" in text or "|" in text:
        score += 1
    
    return min(score, 10)  # 최대 10점

def evaluate_relevance(response: str, question: str) -> int:
    """응답의 관련성 평가 (1-10 점수)"""
    # 실제로는 더 복잡한 평가 로직이 필요함
    # 여기서는 간단한 키워드 매칭과 응답 길이를 기준으로 평가
    score = 5  # 기본 점수
    
    # 질문에서 핵심 키워드 추출 (실제로는 NLP 기술 활용 필요)
    keywords = [word.lower() for word in question.split() if len(word) > 3]
    
    # 키워드 매칭
    response_lower = response.lower()
    matched_keywords = sum(1 for keyword in keywords if keyword in response_lower)
    keyword_match_rate = matched_keywords / len(keywords) if keywords else 0
    
    # 키워드 매칭률에 따라 점수 조정
    if keyword_match_rate > 0.8:
        score += 3
    elif keyword_match_rate > 0.5:
        score += 2
    elif keyword_match_rate > 0.3:
        score += 1
    
    # 응답 길이 평가
    word_count = len(response.split())
    if 200 <= word_count <= 500:
        score += 1
    elif word_count > 500:
        score += 2
    
    return min(score, 10)  # 최대 10점

def compare_results(result_a: Dict, result_b: Dict) -> Dict:
    """A와 B 결과 비교 분석"""
    # 평가 요소별 가중치
    weights = {
        "structure": 0.4,
        "relevance": 0.6
    }
    
    # 각 평가 요소별 점수 계산
    score_a = (result_a["structure_score"] * weights["structure"] + 
               result_a["relevance_score"] * weights["relevance"])
    
    score_b = (result_b["structure_score"] * weights["structure"] + 
               result_b["relevance_score"] * weights["relevance"])
    
    # 승자 결정
    if score_a > score_b:
        winner = "A"
        diff = score_a - score_b
    elif score_b > score_a:
        winner = "B"
        diff = score_b - score_a
    else:
        winner = "무승부"
        diff = 0
    
    return {
        "score_a": score_a,
        "score_b": score_b,
        "winner": winner,
        "diff": diff,
        "percent_diff": (diff / ((score_a + score_b) / 2)) * 100 if (score_a + score_b) > 0 else 0
    }

def analyze_results(test_results: List[Dict]) -> Dict:
    """모든 테스트 결과 분석 및 요약"""
    total_tests = len(test_results)
    if total_tests == 0:
        return {"error": "테스트 결과가 없습니다."}
    
    # 승리 횟수 집계
    a_wins = sum(1 for test in test_results if test["comparison"]["winner"] == "A")
    b_wins = sum(1 for test in test_results if test["comparison"]["winner"] == "B")
    ties = sum(1 for test in test_results if test["comparison"]["winner"] == "무승부")
    
    # 평균 점수 계산
    avg_score_a = sum(test["comparison"]["score_a"] for test in test_results) / total_tests
    avg_score_b = sum(test["comparison"]["score_b"] for test in test_results) / total_tests
    
    # 개선율 계산
    improvement = avg_score_b - avg_score_a
    improvement_percent = (improvement / avg_score_a * 100) if avg_score_a > 0 else 0
    
    # 결론 도출
    if b_wins > a_wins:
        conclusion = "B 변형이 더 효과적입니다."
    elif a_wins > b_wins:
        conclusion = "A 변형이 더 효과적입니다."
    else:
        if avg_score_b > avg_score_a:
            conclusion = "B 변형이 약간 더 효과적이지만, 유의미한 차이는 아닙니다."
        elif avg_score_a > avg_score_b:
            conclusion = "A 변형이 약간 더 효과적이지만, 유의미한 차이는 아닙니다."
        else:
            conclusion = "두 변형 간에 유의미한 차이가 없습니다."
    
    return {
        "total_tests": total_tests,
        "a_wins": a_wins,
        "b_wins": b_wins,
        "ties": ties,
        "a_win_percent": round(a_wins / total_tests * 100, 1),
        "b_win_percent": round(b_wins / total_tests * 100, 1),
        "tie_percent": round(ties / total_tests * 100, 1),
        "avg_score_a": avg_score_a,
        "avg_score_b": avg_score_b,
        "improvement": improvement,
        "improvement_percent": round(improvement_percent, 1),
        "conclusion": conclusion
    }

def main():
    """메인 함수"""
    # 기본/향상된 프롬프트 접근법 비교 실습
    run_exercise(
        title="A/B 테스트 접근법",
        topic_options=AB_TEST_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 추가 실습: 실제 A/B 테스트 수행
    print("\n선택적 실습: 실제 A/B 테스트 수행")
    choice = input("실제 A/B 테스트를 수행하시겠습니까? (y/n): ")
    
    if choice.lower() in ['y', 'yes']:
        test_options = {
            "1": "역할 지정 효과",
            "2": "지시 방식 차이",
            "3": "예시 포함 효과",
            "4": "맥락 제공 효과",
            "5": "길이 영향 분석"
        }
        
        print("\n테스트 유형 선택:")
        for key, value in test_options.items():
            print(f"  {key}. {value}")
        
        test_choice = input("\n선택하세요 (1-5): ")
        if test_choice in test_options:
            test_type = test_options[test_choice]
            results, summary = run_ab_test(test_type)
            
            # 결과 저장 여부 확인
            save_choice = input("\n테스트 결과를 파일로 저장하시겠습니까? (y/n): ")
            if save_choice.lower() in ['y', 'yes']:
                try:
                    import json
                    from datetime import datetime
                    
                    # 저장 경로 설정
                    save_dir = os.path.join(project_root, "results", "part8", "8.2")
                    os.makedirs(save_dir, exist_ok=True)
                    
                    # 파일명 생성
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"ab_test_{test_type.replace(' ', '_')}_{timestamp}.json"
                    filepath = os.path.join(save_dir, filename)
                    
                    # 결과 저장
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump({
                            "test_type": test_type,
                            "timestamp": timestamp,
                            "summary": summary,
                            "detailed_results": [
                                {
                                    "question": result["question"],
                                    "prompt_a": result["prompt_a"],
                                    "prompt_b": result["prompt_b"],
                                    "result_a_summary": {
                                        "word_count": result["result_a"]["word_count"],
                                        "structure_score": result["result_a"]["structure_score"],
                                        "relevance_score": result["result_a"]["relevance_score"]
                                    },
                                    "result_b_summary": {
                                        "word_count": result["result_b"]["word_count"],
                                        "structure_score": result["result_b"]["structure_score"],
                                        "relevance_score": result["result_b"]["relevance_score"]
                                    },
                                    "comparison": result["comparison"]
                                }
                                for result in results
                            ]
                        }, f, indent=2)
                    
                    print(f"\n결과가 저장되었습니다: {filepath}")
                except Exception as e:
                    print(f"\n결과 저장 중 오류 발생: {e}")
        else:
            print("\n잘못된 선택입니다.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")