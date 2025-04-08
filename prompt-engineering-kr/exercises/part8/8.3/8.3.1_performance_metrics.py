"""
명확성, 구체성, 맥락 균형 맞추기 실습 모듈

Part 8 - 섹션 8.3.1 실습 코드: 프롬프트의 세 가지 핵심 요소(명확성, 구체성, 맥락)의 
균형을 조정하고 다양한 목적에 맞는 최적의 균형점을 찾는 방법을 실습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.ai_client import get_completion
from utils.file_handler import save_markdown
from utils.ui_helpers import (
    print_header, print_step, get_user_input, 
    display_results_comparison, print_prompt_summary
)

# 프롬프트 균형 조정 실험을 위한 주제 옵션
BALANCE_EXPERIMENT_TOPICS = {
    "1": "기후 변화 대응 전략",
    "2": "인공지능 윤리",
    "3": "원격 근무의 장단점",
    "4": "미래 교육 시스템",
    "5": "디지털 프라이버시"
}

# 균형 레벨 정의
BALANCE_LEVELS = {
    "명확성": ["낮음", "중간", "높음"],
    "구체성": ["낮음", "중간", "높음"],
    "맥락": ["낮음", "중간", "높음"]
}

# 목적별 최적 균형 프로필
PURPOSE_BALANCE_PROFILES = {
    "정보 추출": {"명확성": "높음", "구체성": "높음", "맥락": "중간"},
    "창의적 콘텐츠": {"명확성": "중간", "구체성": "낮음", "맥락": "높음"},
    "분석 및 의사결정": {"명확성": "높음", "구체성": "높음", "맥락": "높음"},
    "교육 콘텐츠": {"명확성": "높음", "구체성": "높음", "맥락": "높음"}
}

def create_balanced_prompt(
    topic: str, 
    clarity_level: str = "중간", 
    specificity_level: str = "중간", 
    context_level: str = "중간"
) -> str:
    """
    명확성, 구체성, 맥락 수준을 조정한 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        clarity_level: 명확성 수준 (낮음, 중간, 높음)
        specificity_level: 구체성 수준 (낮음, 중간, 높음)
        context_level: 맥락 수준 (낮음, 중간, 높음)
        
    Returns:
        균형 조정된 프롬프트
    """
    builder = PromptBuilder()
    
    # 명확성 요소 추가
    if clarity_level == "높음":
        if "기후 변화" in topic:
            builder.add_text(
                f"{topic}에 대해 다음 네 가지 측면에서 분석해주세요:\n"
                f"1. 현재 주요 과제 및 위험 요소\n"
                f"2. 정부 차원의 정책 방안\n"
                f"3. 기업 차원의 대응 전략\n"
                f"4. 개인 차원의 실천 방법"
            )
        elif "인공지능 윤리" in topic:
            builder.add_text(
                f"{topic}에 대해 다음 측면에서 체계적으로 설명해주세요:\n"
                f"1. 주요 윤리적 쟁점 정의\n"
                f"2. 현재 규제 프레임워크 현황\n"
                f"3. 이해관계자별 책임과 역할\n"
                f"4. 향후 발전 방향"
            )
        elif "원격 근무" in topic:
            builder.add_text(
                f"{topic}에 대해 다음 기준에 따라 비교 분석해주세요:\n"
                f"1. 생산성 영향\n"
                f"2. 직원 웰빙 및 만족도\n"
                f"3. 팀 협업 및 의사소통\n"
                f"4. 비용 구조 변화"
            )
        else:
            builder.add_text(
                f"{topic}에 대해 다음 네 가지 핵심 측면을 체계적으로 분석해주세요:\n"
                f"1. 현재 상황 및 주요 도전 과제\n"
                f"2. 다양한 접근법 및 해결 방안\n"
                f"3. 잠재적 영향 및 효과\n"
                f"4. 미래 전망 및 권장 사항"
            )
    elif clarity_level == "중간":
        builder.add_text(f"{topic}에 대해 주요 측면을 분석하고 핵심 요점을 설명해주세요.")
    else:  # 낮음
        builder.add_text(f"{topic}에 대해 알려주세요.")
    
    # 구체성 요소 추가
    if specificity_level == "높음":
        builder.add_text(
            f"\n출력 형식은 다음과 같이 구성해주세요:\n"
            f"- 각 섹션별 소제목과 300-400단어 분량의 설명\n"
            f"- 최소 2개의 구체적 사례나 데이터 포함\n"
            f"- 각 섹션 마지막에 핵심 요점 3-5개 불릿 포인트로 요약\n"
            f"- 전체 내용을 종합하는 150단어 이내의 결론\n"
            f"- 추가 참고를 위한 5개의 질문"
        )
    elif specificity_level == "중간":
        builder.add_text(
            f"\n응답은 주요 섹션으로 구분하고, 구체적인 예시나 데이터를 포함해주세요. "
            f"핵심 요점을 잘 요약해주세요."
        )
    # 낮음일 경우 추가 구체성 지시 없음
    
    # 맥락 요소 추가
    if context_level == "높음":
        if "기후 변화" in topic:
            builder.add_text(
                f"\n저는 환경 정책을 연구하는 대학원생으로, 기후 변화 대응책에 관한 "
                f"논문을 준비하고 있습니다. 특히 선진국과 개발도상국 간의 책임 분담과 "
                f"국제 협력 측면에 관심이 있으며, 다양한 이해관계자의 관점을 포괄하는 "
                f"균형 잡힌 분석이 필요합니다. 이 정보는 정책 제안서의 배경 자료로 "
                f"활용될 예정이며, 학술적 정확성과 최신 데이터에 기반한 분석이 중요합니다."
            )
        elif "인공지능 윤리" in topic:
            builder.add_text(
                f"\n저는 기술 기업의 정책 담당자로, 우리 회사의 AI 윤리 가이드라인을 "
                f"개발하고 있습니다. 실용적이면서도 윤리적 고려사항을 포괄하는 균형 잡힌 "
                f"접근이 필요하며, 규제 준수와 혁신 촉진 사이의 균형을 찾고자 합니다. "
                f"다양한 이해관계자(개발자, 사용자, 규제 기관 등)의 관점을 고려한 "
                f"분석이 필요합니다."
            )
        elif "원격 근무" in topic:
            builder.add_text(
                f"\n저는 중견 기업의 인사 담당자로, 코로나19 이후 하이브리드 근무 정책을 "
                f"수립하고 있습니다. 직원 300명 규모의 소프트웨어 회사로, 현재는 주 2일 "
                f"출근 정책을 시행 중입니다. 직원 만족도와 생산성을 모두 고려한 최적의 "
                f"정책을 개발하려고 하며, 특히 팀 협업과 회사 문화 유지에 관심이 있습니다. "
                f"경영진에게 제안할 정책 보고서 작성에 이 정보를 활용할 예정입니다."
            )
        else:
            builder.add_text(
                f"\n저는 이 주제에 대한 전문 지식이 필요한 실무자입니다. 이 정보는 "
                f"중요한 의사결정과 전략 수립에 활용될 예정이며, 정확하고 균형 잡힌 "
                f"관점이 필요합니다. 특히 실무적 적용과 장기적 영향에 관심이 있으며, "
                f"다양한 이해관계자의 관점을 고려한 분석이 도움이 될 것입니다."
            )
    elif context_level == "중간":
        builder.add_text(
            f"\n이 정보는 전문적인 이해를 위해 필요하며, 현실적인 적용 방안에 "
            f"관심이 있습니다. 균형 잡힌 관점의 분석이 도움이 될 것입니다."
        )
    # 낮음일 경우 추가 맥락 정보 없음
    
    return builder.build()

def run_balance_experiment(topic: str) -> Dict[str, Any]:
    """
    선택한 주제에 대해 다양한 균형 조합 실험 실행
    
    Args:
        topic: 실험 주제
        
    Returns:
        실험 결과 데이터
    """
    print_header(f"{topic}에 대한 균형 조정 실험")
    
    results = {
        "topic": topic,
        "experiments": [],
        "purpose_experiments": []
    }
    
    # 1. 기본 프롬프트 (모든 요소 중간 수준)
    print_step(1, "기본 균형 프롬프트 테스트 (모든 요소 중간 수준)")
    base_prompt = create_balanced_prompt(topic, "중간", "중간", "중간")
    print(f"\n기본 프롬프트:\n{base_prompt}\n")
    
    print("응답 생성 중...")
    base_result = get_completion(base_prompt, temperature=0.7)
    print("\n✅ 기본 프롬프트 응답이 생성되었습니다.")
    
    results["experiments"].append({
        "name": "기본 균형",
        "clarity": "중간",
        "specificity": "중간",
        "context": "중간",
        "prompt": base_prompt,
        "result": base_result
    })
    
    # 2. 명확성 강화 프롬프트
    print_step(2, "명확성 강화 프롬프트 테스트")
    clarity_prompt = create_balanced_prompt(topic, "높음", "중간", "중간")
    print(f"\n명확성 강화 프롬프트:\n{clarity_prompt}\n")
    
    print("응답 생성 중...")
    clarity_result = get_completion(clarity_prompt, temperature=0.7)
    print("\n✅ 명확성 강화 프롬프트 응답이 생성되었습니다.")
    
    results["experiments"].append({
        "name": "명확성 강화",
        "clarity": "높음",
        "specificity": "중간",
        "context": "중간",
        "prompt": clarity_prompt,
        "result": clarity_result
    })
    
    # 3. 구체성 강화 프롬프트
    print_step(3, "구체성 강화 프롬프트 테스트")
    specificity_prompt = create_balanced_prompt(topic, "중간", "높음", "중간")
    print(f"\n구체성 강화 프롬프트:\n{specificity_prompt}\n")
    
    print("응답 생성 중...")
    specificity_result = get_completion(specificity_prompt, temperature=0.7)
    print("\n✅ 구체성 강화 프롬프트 응답이 생성되었습니다.")
    
    results["experiments"].append({
        "name": "구체성 강화",
        "clarity": "중간",
        "specificity": "높음",
        "context": "중간",
        "prompt": specificity_prompt,
        "result": specificity_result
    })
    
    # 4. 맥락 강화 프롬프트
    print_step(4, "맥락 강화 프롬프트 테스트")
    context_prompt = create_balanced_prompt(topic, "중간", "중간", "높음")
    print(f"\n맥락 강화 프롬프트:\n{context_prompt}\n")
    
    print("응답 생성 중...")
    context_result = get_completion(context_prompt, temperature=0.7)
    print("\n✅ 맥락 강화 프롬프트 응답이 생성되었습니다.")
    
    results["experiments"].append({
        "name": "맥락 강화",
        "clarity": "중간",
        "specificity": "중간",
        "context": "높음",
        "prompt": context_prompt,
        "result": context_result
    })
    
    # 5. 목적별 최적 균형 테스트
    print_step(5, "목적별 최적 균형 테스트")
    
    for purpose, profile in PURPOSE_BALANCE_PROFILES.items():
        print(f"\n{purpose} 목적을 위한 최적 균형 테스트:")
        
        purpose_prompt = create_balanced_prompt(
            topic, 
            profile["명확성"], 
            profile["구체성"], 
            profile["맥락"]
        )
        
        print(f"- 명확성: {profile['명확성']}")
        print(f"- 구체성: {profile['구체성']}")
        print(f"- 맥락: {profile['맥락']}")
        
        print("\n응답 생성 중...")
        purpose_result = get_completion(purpose_prompt, temperature=0.7)
        print(f"\n✅ {purpose} 목적 프롬프트 응답이 생성되었습니다.")
        
        results["purpose_experiments"].append({
            "purpose": purpose,
            "profile": profile,
            "prompt": purpose_prompt,
            "result": purpose_result
        })
    
    # 결과 비교 표시
    print_step(6, "실험 결과 비교")
    
    print("\n요소별 강화 프롬프트 결과 비교:")
    for exp in results["experiments"]:
        print(f"\n--- {exp['name']} 프롬프트 결과 ---")
        print(f"[명확성: {exp['clarity']}, 구체성: {exp['specificity']}, 맥락: {exp['context']}]")
        display_results_comparison("", exp["result"], 200)
    
    print("\n목적별 최적 균형 프롬프트 결과:")
    for purpose_exp in results["purpose_experiments"]:
        print(f"\n--- {purpose_exp['purpose']} 목적 프롬프트 결과 ---")
        profile = purpose_exp["profile"]
        print(f"[명확성: {profile['명확성']}, 구체성: {profile['구체성']}, 맥락: {profile['맥락']}]")
        display_results_comparison("", purpose_exp["result"], 200)
    
    return results

def analyze_balance_experiment_results(results: Dict[str, Any]) -> str:
    """
    균형 조정 실험 결과 분석
    
    Args:
        results: 실험 결과 데이터
        
    Returns:
        분석 보고서
    """
    topic = results["topic"]
    experiments = results["experiments"]
    purpose_experiments = results["purpose_experiments"]
    
    # 분석 보고서 작성
    report = f"# {topic} 프롬프트 균형 조정 실험 분석\n\n"
    
    # 요소별 강화 실험 분석
    report += "## 요소별 강화 프롬프트 분석\n\n"
    
    for exp in experiments:
        report += f"### {exp['name']} 프롬프트\n\n"
        report += f"**균형 설정:** 명확성 {exp['clarity']}, 구체성 {exp['specificity']}, 맥락 {exp['context']}\n\n"
        report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
        report += f"**효과 분석:**\n"
        
        # 각 실험별 효과 분석
        if exp['name'] == "기본 균형":
            report += "- 기준점으로 사용된 균형 잡힌 프롬프트\n"
            report += "- 모든 요소가 중간 수준으로 설정된 상태\n\n"
        elif exp['name'] == "명확성 강화":
            report += "- 구조화된 요청과 명확한 지시로 인해 응답의 체계성이 향상됨\n"
            report += "- 특정 측면에 대한 분석이 더 직접적이고 포괄적임\n\n"
        elif exp['name'] == "구체성 강화":
            report += "- 출력 형식 지정으로 응답의 구조와 상세도가 개선됨\n"
            report += "- 예시, 데이터, 요약 등이 더 체계적으로 제공됨\n\n"
        elif exp['name'] == "맥락 강화":
            report += "- 풍부한 배경 정보로 인해 응답의 관련성과 타겟팅이 향상됨\n"
            report += "- 특정 상황과 목적에 맞춘 맞춤형 분석 제공\n\n"
    
    # 목적별 최적 균형 실험 분석
    report += "## 목적별 최적 균형 프롬프트 분석\n\n"
    
    for purpose_exp in purpose_experiments:
        purpose = purpose_exp["purpose"]
        profile = purpose_exp["profile"]
        
        report += f"### {purpose} 목적 프롬프트\n\n"
        report += f"**균형 설정:** 명확성 {profile['명확성']}, 구체성 {profile['구체성']}, 맥락 {profile['맥락']}\n\n"
        report += f"**프롬프트:**\n```\n{purpose_exp['prompt']}\n```\n\n"
        report += f"**효과 분석:**\n"
        
        # 각 목적별 최적 균형 효과 분석
        if purpose == "정보 추출":
            report += "- 높은 명확성과 구체성으로 정확하고 관련성 높은 정보 제공\n"
            report += "- 구조화된 형식으로 정보 접근성과 명확성 향상\n\n"
        elif purpose == "창의적 콘텐츠":
            report += "- 중간 명확성과 낮은 구체성으로 창의적 자유도 확보\n"
            report += "- 풍부한 맥락이 독창적인 발상과 연결성 촉진\n\n"
        elif purpose == "분석 및 의사결정":
            report += "- 모든 요소의 높은 수준으로 종합적이고 깊이 있는 분석 제공\n"
            report += "- 다면적 접근과 균형 잡힌 관점 제시\n\n"
        elif purpose == "교육 콘텐츠":
            report += "- 명확한 구조와 구체적인 예시로 학습 효과 최적화\n"
            report += "- 풍부한 맥락이 이해도와 적용 능력 향상\n\n"
    
    # 종합 인사이트 및 권장 사항
    report += "## 종합 인사이트 및 권장 사항\n\n"
    
    report += "### 핵심 발견사항\n\n"
    report += "1. **명확성의 영향**: 높은 명확성은 응답의 구조화와 체계성을 크게 향상시킴\n"
    report += "2. **구체성의 영향**: 높은 구체성은 상세도와 예시의 품질을 개선함\n"
    report += "3. **맥락의 영향**: 풍부한 맥락은 응답의 관련성과 맞춤화 수준을 높임\n"
    report += "4. **균형의 중요성**: 목적에 따라 세 요소의 최적 균형점이 다름\n\n"
    
    report += "### 균형 조정 체크리스트\n\n"
    report += "- [ ] **목적 명확화**: 프롬프트의 주요 목적 정의 (정보 추출, 창의성, 분석, 교육 등)\n"
    report += "- [ ] **균형 진단**: 현재 프롬프트의 명확성, 구체성, 맥락 수준 평가\n"
    report += "- [ ] **목적별 조정**: 목적에 맞는 이상적 균형 프로필 참조\n"
    report += "- [ ] **요소별 최적화**: 부족한 요소 보강 및 과잉 요소 조정\n"
    report += "- [ ] **통합 및 일관성**: 모든 요소가 유기적으로 연결되도록 확인\n\n"
    
    report += "### 상황별 균형 조정 권장사항\n\n"
    report += "| 상황 | 명확성 | 구체성 | 맥락 | 비고 |\n"
    report += "|------|--------|--------|------|------|\n"
    report += "| 빠른 사실 확인 | 높음 | 중간 | 낮음 | 직접적이고 간결한 응답을 위해 |\n"
    report += "| 종합적 보고서 | 높음 | 높음 | 높음 | 완전하고 심층적인 분석을 위해 |\n"
    report += "| 아이디어 브레인스토밍 | 중간 | 낮음 | 높음 | 창의적 발상과 다양성을 위해 |\n"
    report += "| 튜토리얼/가이드 | 높음 | 높음 | 중간 | 명확한 지침과 예시를 위해 |\n"
    report += "| 개인화된 조언 | 중간 | 중간 | 높음 | 상황에 맞는 맞춤형 조언을 위해 |\n\n"
    
    report += f"## 결론\n\n"
    report += f"{topic}에 대한 이 실험을 통해 프롬프트의 세 가지 핵심 요소(명확성, 구체성, 맥락)가 "
    report += f"AI 응답에 미치는 영향을 확인할 수 있었습니다. 각 요소는 독특한 방식으로 응답의 품질에 기여하며, "
    report += f"목적에 따라 이상적인 균형점이 달라집니다. 효과적인 프롬프트 설계를 위해서는 목적을 명확히 하고, "
    report += f"그에 맞는 균형 조정 전략을 적용하는 것이 중요합니다."
    
    return report

def main() -> None:
    """
    메인 함수
    """
    print_header("프롬프트 균형 조정 실험")
    
    # 주제 선택
    print_step(1, "실험 주제 선택")
    
    print("\n실험 주제 옵션:")
    for key, value in BALANCE_EXPERIMENT_TOPICS.items():
        print(f"  {key}. {value}")
    
    choice = get_user_input("\n주제를 선택하세요", "1")
    topic = BALANCE_EXPERIMENT_TOPICS.get(choice, BALANCE_EXPERIMENT_TOPICS["1"])
    
    print(f"\n선택한 주제: {topic}")
    
    # 균형 조정 실험 실행
    results = run_balance_experiment(topic)
    
    # 실험 결과 분석
    analysis_report = analyze_balance_experiment_results(results)
    
    # 결과 저장
    save_option = get_user_input("\n실험 결과와 분석을 파일로 저장하시겠습니까? (y/n)", "y")
    if save_option.lower() in ['y', 'yes']:
        # 파일명 생성
        safe_topic = topic.replace(' ', '_').lower()
        filename = f"balance_experiment_{safe_topic}.md"
        
        # 분석 보고서 저장
        save_markdown(filename, analysis_report)
        print(f"\n분석 보고서가 {filename} 파일로 저장되었습니다.")
    
    print("\n프롬프트 균형 조정 실험이 완료되었습니다.")
    print("이 실험을 통해 명확성, 구체성, 맥락의 균형이 AI 응답에 미치는 영향을 확인했습니다.")
    print("다양한 목적과 상황에 맞는 최적의 균형 조정 전략을 개발해보세요!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")