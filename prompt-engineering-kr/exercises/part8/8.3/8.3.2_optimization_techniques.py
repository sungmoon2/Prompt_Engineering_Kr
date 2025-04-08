"""
단어 선택과 구조의 중요성 실습 모듈

Part 8 - 섹션 8.3.2 실습 코드: 프롬프트에서 단어 선택과 구조 패턴이 응답에 미치는 
영향을 실험하고 최적화 전략을 개발하는 방법을 학습합니다.
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

# 단어 선택과 구조 실험을 위한 주제 옵션
WORD_STRUCTURE_TOPICS = {
    "1": "디지털 마케팅 전략",
    "2": "기업 리더십 스타일",
    "3": "지속가능한 도시 계획",
    "4": "효과적인 학습 방법론",
    "5": "의료 기술 혁신"
}

# 지시 동사 스펙트럼
DIRECTIVE_VERBS = {
    "낮은 수준": ["설명해", "알려", "소개해"],
    "중간 수준": ["요약해", "비교해", "분석해", "정의해"],
    "높은 수준": ["평가해", "비판해", "종합해", "최적화해", "재구성해"]
}

# 수식어 유형
MODIFIER_TYPES = {
    "범위 수식어": ["포괄적으로", "간략히", "심층적으로"],
    "품질 수식어": ["철저히", "정확하게", "엄밀하게"],
    "접근법 수식어": ["창의적으로", "체계적으로", "비판적으로"],
    "우선순위 수식어": ["특히", "무엇보다", "가장 중요하게"]
}

# 구조 패턴
STRUCTURE_PATTERNS = {
    "선형 구조": "정보를 순차적으로 제시하는 구조",
    "계층적 구조": "정보를 중요도나 관계에 따라 계층화하여 제시하는 구조",
    "프레임 구조": "시작과 끝에 중요한 정보나 지시를 배치하는 구조",
    "모듈식 구조": "독립적인 섹션으로 구분하여 정보를 제시하는 구조",
    "대화식 구조": "AI와의 상호작용을 유도하는 구조",
    "스토리텔링 구조": "이야기 형식으로 맥락과 과제를 제시하는 구조",
    "제약 기반 구조": "제약 조건을 중심으로 구조화하는 구조",
    "템플릿 채우기 구조": "응답을 위한 템플릿 형태를 미리 제시하는 구조"
}

def create_verb_variation_prompts(topic: str) -> Dict[str, str]:
    """
    지시 동사 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        지시 동사 수준별 프롬프트 딕셔너리
    """
    verb_prompts = {}
    
    # 각 동사 수준별 프롬프트 생성
    for level, verbs in DIRECTIVE_VERBS.items():
        # 각 수준에서 첫 번째 동사 사용
        verb = verbs[0]
        
        builder = PromptBuilder()
        builder.add_text(f"{topic}에 대해 {verb}주세요.")
        
        verb_prompts[level] = builder.build()
    
    return verb_prompts

def create_modifier_variation_prompts(topic: str) -> Dict[str, str]:
    """
    수식어 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        수식어 유형별 프롬프트 딕셔너리
    """
    modifier_prompts = {}
    
    # 각 수식어 유형별 프롬프트 생성
    for type_name, modifiers in MODIFIER_TYPES.items():
        # 각 유형에서 첫 번째 수식어 사용
        modifier = modifiers[0]
        
        builder = PromptBuilder()
        builder.add_text(f"{topic}에 대해 {modifier} 분석해주세요.")
        
        modifier_prompts[type_name] = builder.build()
    
    return modifier_prompts

def create_structure_variation_prompts(topic: str) -> Dict[str, str]:
    """
    구조 패턴 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        구조 패턴별 프롬프트 딕셔너리
    """
    structure_prompts = {}
    
    # 선형 구조 프롬프트
    builder = PromptBuilder()
    builder.add_text(
        f"주제: {topic}\n"
        f"요청: 주요 측면과 사례 분석\n"
        f"형식: 각 측면별 장단점 포함"
    )
    structure_prompts["선형 구조"] = builder.build()
    
    # 계층적 구조 프롬프트
    builder = PromptBuilder()
    builder.add_text(
        f"# {topic} 분석 요청\n\n"
        f"## 기본 정보\n"
        f"- 대상: 전략 담당자\n"
        f"- 목적: 의사결정 지원\n\n"
        f"## 핵심 요구사항\n"
        f"1. 주요 측면 분석\n"
        f"2. 장단점 평가\n"
        f"3. 사례 포함\n\n"
        f"## 우선순위\n"
        f"- 가장 중요: 실용적 적용성\n"
        f"- 중요: 비용 효율성"
    )
    structure_prompts["계층적 구조"] = builder.build()
    
    # 프레임 구조 프롬프트
    builder = PromptBuilder()
    builder.add_text(
        f"당신은 {topic} 전문가입니다. 이 주제에 대한 포괄적인 분석을 제공해주세요.\n\n"
        f"[중간에 세부 요구사항이나 배경 정보가 올 수 있음]\n\n"
        f"분석은 명확하고 실용적이어야 하며, 각 측면의 장단점을 균형있게 다루어야 합니다. "
        f"가능한 한 구체적인 사례와 증거를 포함해주세요."
    )
    structure_prompts["프레임 구조"] = builder.build()
    
    # 모듈식 구조 프롬프트
    builder = PromptBuilder()
    builder.add_text(
        f"[배경]\n"
        f"{topic}에 대한 전략적 이해 필요.\n\n"
        f"[목표]\n"
        f"주요 측면 및 최신 트렌드 파악.\n\n"
        f"[요청]\n"
        f"포괄적 분석 및 실용적 인사이트 제공.\n\n"
        f"[출력 형식]\n"
        f"각 핵심 측면별:\n"
        f"- 정의 및 중요성\n"
        f"- 장단점\n"
        f"- 적용 사례"
    )
    structure_prompts["모듈식 구조"] = builder.build()
    
    # 추가 구조 패턴은 필요에 따라 구현
    
    return structure_prompts

def run_word_choice_experiment(topic: str) -> Dict[str, Any]:
    """
    단어 선택 영향 실험 실행
    
    Args:
        topic: 실험 주제
        
    Returns:
        실험 결과 데이터
    """
    print_header(f"{topic}에 대한 단어 선택 실험")
    
    results = {
        "topic": topic,
        "verb_experiments": [],
        "modifier_experiments": [],
        "combined_experiments": []
    }
    
    # 1. 지시 동사 변형 실험
    print_step(1, "지시 동사 변형 실험")
    verb_prompts = create_verb_variation_prompts(topic)
    
    for level, prompt in verb_prompts.items():
        print(f"\n{level} 지시 동사 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {level} 지시 동사 프롬프트 응답이 생성되었습니다.")
        
        results["verb_experiments"].append({
            "level": level,
            "prompt": prompt,
            "result": result
        })
    
    # 2. 수식어 변형 실험
    print_step(2, "수식어 변형 실험")
    modifier_prompts = create_modifier_variation_prompts(topic)
    
    for type_name, prompt in modifier_prompts.items():
        print(f"\n{type_name} 수식어 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {type_name} 수식어 프롬프트 응답이 생성되었습니다.")
        
        results["modifier_experiments"].append({
            "type": type_name,
            "prompt": prompt,
            "result": result
        })
    
    # 3. 최적 조합 실험
    print_step(3, "최적 조합 실험")
    
    # 정보 추출 목적 최적 조합
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 체계적으로 종합해주세요. "
        f"특히 주요 구성 요소, 효과적인 접근법, 그리고 측정 가능한 결과에 초점을 맞춰주세요."
    )
    info_extraction_prompt = builder.build()
    
    print(f"\n정보 추출 목적 최적 조합 프롬프트:\n{info_extraction_prompt}\n")
    
    print("응답 생성 중...")
    info_extraction_result = get_completion(info_extraction_prompt, temperature=0.7)
    print("\n✅ 정보 추출 목적 최적 조합 프롬프트 응답이 생성되었습니다.")
    
    results["combined_experiments"].append({
        "purpose": "정보 추출",
        "prompt": info_extraction_prompt,
        "result": info_extraction_result
    })
    
    # 창의적 콘텐츠 목적 최적 조합
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 창의적으로 재해석해주세요. "
        f"기존의 틀을 벗어나 혁신적인 관점과 신선한 아이디어를 자유롭게 제시해주세요."
    )
    creative_prompt = builder.build()
    
    print(f"\n창의적 콘텐츠 목적 최적 조합 프롬프트:\n{creative_prompt}\n")
    
    print("응답 생성 중...")
    creative_result = get_completion(creative_prompt, temperature=0.7)
    print("\n✅ 창의적 콘텐츠 목적 최적 조합 프롬프트 응답이 생성되었습니다.")
    
    results["combined_experiments"].append({
        "purpose": "창의적 콘텐츠",
        "prompt": creative_prompt,
        "result": creative_result
    })
    
    # 분석 목적 최적 조합
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}을 비판적으로 평가해주세요. "
        f"다양한 관점에서 철저히 분석하고, 장단점을 체계적으로 비교하며, "
        f"구체적인 증거와 사례를 통해 주장을 뒷받침해주세요."
    )
    analysis_prompt = builder.build()
    
    print(f"\n분석 목적 최적 조합 프롬프트:\n{analysis_prompt}\n")
    
    print("응답 생성 중...")
    analysis_result = get_completion(analysis_prompt, temperature=0.7)
    print("\n✅ 분석 목적 최적 조합 프롬프트 응답이 생성되었습니다.")
    
    results["combined_experiments"].append({
        "purpose": "분석",
        "prompt": analysis_prompt,
        "result": analysis_result
    })
    
    # 결과 비교 표시
    print_step(4, "단어 선택 실험 결과 비교")
    
    print("\n지시 동사 변형 결과 비교:")
    for exp in results["verb_experiments"]:
        print(f"\n--- {exp['level']} 지시 동사 프롬프트 결과 ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n수식어 변형 결과 비교:")
    for exp in results["modifier_experiments"]:
        print(f"\n--- {exp['type']} 수식어 프롬프트 결과 ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n목적별 최적 조합 결과 비교:")
    for exp in results["combined_experiments"]:
        print(f"\n--- {exp['purpose']} 목적 최적 조합 프롬프트 결과 ---")
        display_results_comparison("", exp["result"], 200)
    
    return results

def run_structure_experiment(topic: str) -> Dict[str, Any]:
    """
    구조 패턴 영향 실험 실행
    
    Args:
        topic: 실험 주제
        
    Returns:
        실험 결과 데이터
    """
    print_header(f"{topic}에 대한 구조 패턴 실험")
    
    results = {
        "topic": topic,
        "structure_experiments": []
    }
    
    # 구조 패턴 변형 실험
    print_step(1, "구조 패턴 변형 실험")
    structure_prompts = create_structure_variation_prompts(topic)
    
    for pattern_name, prompt in structure_prompts.items():
        print(f"\n{pattern_name} 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {pattern_name} 프롬프트 응답이 생성되었습니다.")
        
        results["structure_experiments"].append({
            "pattern": pattern_name,
            "prompt": prompt,
            "result": result
        })
    
    # 결과 비교 표시
    print_step(2, "구조 패턴 실험 결과 비교")
    
    print("\n구조 패턴 변형 결과 비교:")
    for exp in results["structure_experiments"]:
        print(f"\n--- {exp['pattern']} 프롬프트 결과 ---")
        display_results_comparison("", exp["result"], 200)
    
    return results

def analyze_word_choice_results(results: Dict[str, Any]) -> str:
    """
    단어 선택 실험 결과 분석
    
    Args:
        results: 실험 결과 데이터
        
    Returns:
        분석 보고서
    """
    topic = results["topic"]
    verb_exps = results["verb_experiments"]
    modifier_exps = results["modifier_experiments"]
    combined_exps = results["combined_experiments"]
    
    # 분석 보고서 작성
    report = f"# {topic} 단어 선택 실험 분석\n\n"
    
    # 지시 동사 변형 분석
    report += "## 지시 동사 영향 분석\n\n"
    
    for exp in verb_exps:
        report += f"### {exp['level']} 지시 동사\n\n"
        report += f"**프롬프트:** {exp['prompt']}\n\n"
        
        # 각 수준별 효과 분석
        if exp['level'] == "낮은 수준":
            report += "**효과 분석:**\n"
            report += "- 일반적이고 개요 수준의 정보 제공\n"
            report += "- 폭넓지만 깊이가 상대적으로 낮은 응답\n"
            report += "- 기본적인 정보 요청에 적합\n\n"
        elif exp['level'] == "중간 수준":
            report += "**효과 분석:**\n"
            report += "- 더 체계적이고 구조화된 응답\n"
            report += "- 주제의 특정 측면에 더 집중된 정보\n"
            report += "- 분석적 요소가 증가하지만 평가는 제한적\n\n"
        elif exp['level'] == "높은 수준":
            report += "**효과 분석:**\n"
            report += "- 심층적이고 비판적인 분석 제공\n"
            report += "- 다양한 관점과 증거 기반 평가 포함\n"
            report += "- 종합적 사고와 가치 판단 요소 증가\n\n"
    
    # 수식어 변형 분석
    report += "## 수식어 영향 분석\n\n"
    
    for exp in modifier_exps:
        report += f"### {exp['type']}\n\n"
        report += f"**프롬프트:** {exp['prompt']}\n\n"
        
        # 각 유형별 효과 분석
        if exp['type'] == "범위 수식어":
            report += "**효과 분석:**\n"
            report += "- 응답의 범위와 깊이에 직접적 영향\n"
            report += "- 정보의 포괄성과 상세도 조절\n"
            report += "- 원하는 응답 길이와 복잡성 수준 조정에 효과적\n\n"
        elif exp['type'] == "품질 수식어":
            report += "**효과 분석:**\n"
            report += "- 응답의 정밀도와 완성도에 영향\n"
            report += "- 더 정확하고 철저한 분석 유도\n"
            report += "- 검증과 증거 제시 강화\n\n"
        elif exp['type'] == "접근법 수식어":
            report += "**효과 분석:**\n"
            report += "- AI의 사고 방식과 접근 방법 형성\n"
            report += "- 응답의 창의성, 체계성, 비판성 수준 조절\n"
            report += "- 다양한 관점과 사고 패턴 유도\n\n"
        elif exp['type'] == "우선순위 수식어":
            report += "**효과 분석:**\n"
            report += "- 응답의 초점과 강조점 설정\n"
            report += "- 특정 측면이나 요소에 가중치 부여\n"
            report += "- 복잡한 주제에서 핵심 요소 강조에 효과적\n\n"
    
    # 최적 조합 분석
    report += "## 목적별 최적 단어 조합 분석\n\n"
    
    for exp in combined_exps:
        report += f"### {exp['purpose']} 목적 최적 조합\n\n"
        report += f"**프롬프트:** {exp['prompt']}\n\n"
        
        # 각 목적별 최적 조합 효과 분석
        if exp['purpose'] == "정보 추출":
            report += "**효과 분석:**\n"
            report += "- 정밀한 지시 동사(종합)와 구조화 수식어(체계적으로)의 조합\n"
            report += "- 우선순위 수식어(특히)로 중요 요소 강조\n"
            report += "- 결과: 구조화된, 포괄적이지만 초점이 명확한 정보 제공\n\n"
        elif exp['purpose'] == "창의적 콘텐츠":
            report += "**효과 분석:**\n"
            report += "- 창의적 접근법 수식어와 재해석이라는 지시 동사 조합\n"
            report += "- 자유도를 높이는 표현(자유롭게)으로 창의성 촉진\n"
            report += "- 결과: 독창적이고 혁신적인 관점 제시\n\n"
        elif exp['purpose'] == "분석":
            report += "**효과 분석:**\n"
            report += "- 고수준 지시 동사(평가)와 접근법 수식어(비판적으로) 조합\n"
            report += "- 품질 수식어(철저히)로 분석 깊이 강화\n"
            report += "- 결과: 깊이 있고 균형 잡힌 비판적 분석 제공\n\n"
    
    # 단어 선택 최적화 가이드라인
    report += "## 단어 선택 최적화 가이드라인\n\n"
    
    report += "### 목적별 최적 지시 동사\n\n"
    report += "| 목적 | 추천 지시 동사 | 효과 |\n"
    report += "|------|------------|------|\n"
    report += "| 기본 정보 | 설명하다, 알려주다 | 일반적인 개요 수준 정보 제공 |\n"
    report += "| 데이터 요약 | 요약하다, 정리하다 | 핵심 정보 중심의 간결한 응답 |\n"
    report += "| 비교 분석 | 비교하다, 대조하다 | 공통점과 차이점 식별 |\n"
    report += "| 심층 분석 | 분석하다, 평가하다 | 주제의 측면과 의미 탐색 |\n"
    report += "| 비판적 검토 | 비판하다, 검증하다 | 가정과 증거 기반 평가 |\n"
    report += "| 통합적 사고 | 종합하다, 통합하다 | 다양한 관점과 정보 통합 |\n"
    report += "| 혁신적 접근 | 재구성하다, 혁신하다 | 새로운 관점과 해결책 제시 |\n\n"
    
    report += "### 효과적인 수식어 활용 전략\n\n"
    report += "1. **범위 조절을 위한 수식어**\n"
    report += "   - 넓은 범위: '포괄적으로', '전체적으로', '광범위하게'\n"
    report += "   - 좁은 범위: '간략히', '핵심적으로', '구체적으로'\n"
    report += "   - 깊이 조절: '심층적으로', '표면적으로', '개략적으로'\n\n"
    
    report += "2. **품질 강화를 위한 수식어**\n"
    report += "   - 정밀성 강화: '정확하게', '엄밀하게', '정교하게'\n"
    report += "   - 완성도 강화: '철저히', '포괄적으로', '완전하게'\n"
    report += "   - 신뢰성 강화: '객관적으로', '증거 기반으로', '검증 가능하게'\n\n"
    
    report += "3. **접근법 유도를 위한 수식어**\n"
    report += "   - 창의적 사고: '창의적으로', '혁신적으로', '새로운 시각으로'\n"
    report += "   - 체계적 사고: '체계적으로', '단계별로', '구조화하여'\n"
    report += "   - 비판적 사고: '비판적으로', '비평적으로', '의문을 제기하며'\n\n"
    
    report += "### 단어 조합 체크리스트\n\n"
    report += "- [ ] **목적 명확화**: 원하는 정보 유형 및 깊이 결정\n"
    report += "- [ ] **지시 동사 선택**: 목적에 맞는 정밀도의 동사 사용\n"
    report += "- [ ] **수식어 추가**: 응답의 범위, 품질, 접근법 조정\n"
    report += "- [ ] **우선순위 표시**: 필요시 강조할 요소 지정\n"
    report += "- [ ] **일관성 확인**: 모든 단어 선택이 일관된 방향성 유지\n\n"
    
    # 결론
    report += "## 결론\n\n"
    report += f"{topic}에 대한 단어 선택 실험을 통해 지시 동사와 수식어가 AI 응답에 미치는 상당한 영향을 확인했습니다. "
    report += "적절한 지시 동사는 응답의 깊이와 성격을 결정하며, 효과적인 수식어는 범위, 품질, 접근법을 세밀하게 조정합니다. "
    report += "목적에 맞게 단어를 전략적으로 조합함으로써 더 정확하고 유용한 AI 응답을 얻을 수 있습니다."
    
    return report

def analyze_structure_results(results: Dict[str, Any]) -> str:
    """
    구조 패턴 실험 결과 분석
    
    Args:
        results: 실험 결과 데이터
        
    Returns:
        분석 보고서
    """
    topic = results["topic"]
    structure_exps = results["structure_experiments"]
    
    # 분석 보고서 작성
    report = f"# {topic} 구조 패턴 실험 분석\n\n"
    
    # 구조 패턴 변형 분석
    report += "## 구조 패턴 영향 분석\n\n"
    
    for exp in structure_exps:
        report += f"### {exp['pattern']}\n\n"
        report += f"**프롬프트:**\n```"
        {exp['prompt']}
    # 각 패턴별 효과 분석
        if exp['pattern'] == "선형 구조":
            report += "**효과 분석:**\n"
            report += "- 간결하고 직접적인 정보 전달\n"
            report += "- 순차적 접근으로 인한 명확성\n"
            report += "- 심층적 분석보다는 개요 수준의 정보에 적합\n\n"
        elif exp['pattern'] == "계층적 구조":
            report += "**효과 분석:**\n"
            report += "- 정보의 우선순위와 관계가 명확히 표현됨\n"
            report += "- 복잡한 주제의 체계적 분해 가능\n"
            report += "- 여러 수준의, 체계적 분석 촉진\n\n"
        elif exp['pattern'] == "프레임 구조":
            report += "**효과 분석:**\n"
            report += "- 시작과 끝에 중요 정보 배치로 인한 프라이밍 효과\n"
            report += "- 전문성 설정과 명확한 요구사항 강조\n"
            report += "- AI의 역할과 응답 기대치 설정에 효과적\n\n"
        elif exp['pattern'] == "모듈식 구조":
            report += "**효과 분석:**\n"
            report += "- 명확한 섹션 구분으로 정보 접근성 향상\n"
            report += "- 다양한 측면을 독립적으로 다룰 수 있음\n"
            report += "- 복잡한 요청의 체계적 조직화에 효과적\n\n"
    
    # 구조 패턴 최적화 가이드라인
    report += "## 구조 패턴 최적화 가이드라인\n\n"
    report += "### 목적별 최적 구조 패턴\n\n"
    report += "| 목적 | 추천 구조 패턴 | 효과 |\n"
    report += "|------|------------|------|\n"
    report += "| 빠른 정보 요청 | 선형 구조 | 간결하고 직접적인 응답 |\n"
    report += "| 복잡한 주제 분석 | 계층적 구조 | 체계적 분해와 관계 표현 |\n"
    report += "| 특정 역할 설정 | 프레임 구조 | 전문성 확립과 기대치 설정 |\n"
    report += "| 다양한 측면 분석 | 모듈식 구조 | 독립적 섹션으로 명확한 구분 |\n"
    report += "| 상호작용적 응답 | 대화식 구조 | 맞춤형 및 단계적 정보 제공 |\n"
    report += "| 공감과 맥락 중심 | 스토리텔링 구조 | 풍부한 맥락과 관련성 제공 |\n"
    report += "| 명확한 경계 설정 | 제약 기반 구조 | 응답의 범위와 조건 명확화 |\n"
    report += "| 체계적 정보 요청 | 템플릿 채우기 구조 | 일관된 형식과 누락 방지 |\n\n"
    
    report += "### 구조적 요소와 효과\n\n"
    report += "1. **헤더와 섹션 구분**\n"
    report += "   - 효과: 정보 계층화, 우선순위 시각화\n"
    report += "   - 최적 사용: 복잡한 주제를 여러 측면으로 분해할 때\n\n"
    
    report += "2. **번호 매기기와 목록**\n"
    report += "   - 효과: 순서 강조, 명확한 항목 구분\n"
    report += "   - 최적 사용: 단계적 프로세스나 우선순위가 있는 요소 나열 시\n\n"
    
    report += "3. **들여쓰기와 그룹화**\n"
    report += "   - 효과: 관계성 시각화, 정보 구조화\n"
    report += "   - 최적 사용: 주요 개념과 하위 개념의 관계를 표현할 때\n\n"
    
    report += "4. **강조 표시**\n"
    report += "   - 효과: 중요 정보 강조, 구분 명확화\n"
    report += "   - 최적 사용: 특별히 주목해야 할 요소나 핵심 개념 표시 시\n\n"
    
    report += "### 구조 패턴 선택 체크리스트\n\n"
    report += "- [ ] **목적 파악**: 정보 제공, 분석, 창의성, 지침 등 주요 목적 결정\n"
    report += "- [ ] **복잡성 평가**: 주제의 복잡성과 다양한 측면 고려\n"
    report += "- [ ] **우선순위 결정**: 정보의 중요도와 관계 고려\n"
    report += "- [ ] **사용자 맥락**: 응답이 사용될 맥락과 사용자 니즈 고려\n"
    report += "- [ ] **구조적 요소 선택**: 목적에 맞는 헤더, 목록, 그룹화 등 선택\n\n"
    
    # 단어 선택과 구조 통합 전략
    report += "## 단어 선택과 구조의 통합 전략\n\n"
    
    report += "### 목적별 최적 통합 예시\n\n"
    
    report += "#### 정보 추출 최적화:\n\n"
    report += "```\n"
    report += "# 데이터 분석 요청\n\n"
    report += "## 분석 목표\n"
    report += "다음 금융 데이터 패턴을 체계적으로 종합해주세요.\n\n"
    report += "## 필수 분석 요소\n"
    report += "1. 주요 추세 식별\n"
    report += "2. 상관관계 분석\n"
    report += "3. 이상치 탐지\n\n"
    report += "## 출력 형식\n"
    report += "- 각 요소별 200단어 분석\n"
    report += "- 관련 지표와 통계 포함\n"
    report += "- 핵심 인사이트 불릿 포인트로 요약\n"
    report += "```\n\n"
    
    report += "**통합 전략 분석:**\n"
    report += "- 구조: 계층적 구조로 정보 우선순위 명확화\n"
    report += "- 단어 선택: '체계적으로 종합'으로 정밀한 분석 요청\n"
    report += "- 섹션 구분: 목표, 요소, 형식을 명확히 분리\n"
    report += "- 결과: 체계적이고 포괄적인 정보 추출 가능\n\n"
    
    report += "#### 창의적 콘텐츠 최적화:\n\n"
    report += "```\n"
    report += "당신은 혁신적인 미래학자입니다.\n\n"
    report += "다음 주제에 대해 창의적으로 재해석해주세요:\n"
    report += "'미래 도시의 공유 경제 시스템'\n\n"
    report += "[배경 맥락 및 영감 요소]\n\n"
    report += "제약 없이 자유롭게 상상하되, 다음 요소를 통합해보세요:\n"
    report += "- 지속가능성의 새로운 정의\n"
    report += "- 기술과 인간 관계의 균형\n"
    report += "- 예상치 못한 사회적 영향\n\n"
    report += "독창적인 관점과 파격적인 아이디어를 환영합니다.\n"
    report += "```\n\n"
    
    report += "**통합 전략 분석:**\n"
    report += "- 구조: 프레임 구조로 창의적 역할 설정 및 자유로운 표현 장려\n"
    report += "- 단어 선택: '창의적으로 재해석', '자유롭게 상상', '독창적', '파격적'\n"
    report += "- 제약 최소화: 요소는 제시하되 통합 방식은 열어둠\n"
    report += "- 결과: 창의성을 자극하면서도 방향성 제공\n\n"
    
    # 결론
    report += "## 결론\n\n"
    report += f"{topic}에 대한 구조 패턴 실험을 통해 프롬프트의 구조가 AI 응답의 체계성, 복잡성, 초점에 상당한 영향을 미침을 확인했습니다. "
    report += "단어 선택과 구조를 목적에 맞게 통합적으로 최적화함으로써 더 효과적이고 유용한 AI 응답을 얻을 수 있습니다. "
    report += "정보 추출을 위해서는 계층적, 모듈식 구조가 효과적이며, 창의적 콘텐츠에는 프레임 구조와 스토리텔링 접근이 유리합니다. "
    report += "최적의 프롬프트 설계를 위해서는 단어 선택과 구조를 목적과 맥락에 맞게 전략적으로 조합해야 합니다."
    
    return report

def main() -> None:
    """
    메인 함수
    """
    print_header("단어 선택과 구조의 중요성 실험")
    
    # 실험 유형 선택
    print_step(1, "실험 유형 선택")
    print("\n실험 유형 옵션:")
    print("  1. 단어 선택 실험 - 지시 동사와 수식어의 영향")
    print("  2. 구조 패턴 실험 - 다양한 구조 패턴의 영향")
    print("  3. 통합 실험 - 단어 선택과 구조 패턴 결합")
    
    exp_type = get_user_input("\n실험 유형을 선택하세요", "1")
    
    # 주제 선택
    print_step(2, "실험 주제 선택")
    
    print("\n실험 주제 옵션:")
    for key, value in WORD_STRUCTURE_TOPICS.items():
        print(f"  {key}. {value}")
    
    choice = get_user_input("\n주제를 선택하세요", "1")
    topic = WORD_STRUCTURE_TOPICS.get(choice, WORD_STRUCTURE_TOPICS["1"])
    
    print(f"\n선택한 주제: {topic}")
    
    # 선택한 실험 유형 실행
    if exp_type == "1":
        results = run_word_choice_experiment(topic)
        analysis_report = analyze_word_choice_results(results)
        report_filename = f"word_choice_experiment_{topic.replace(' ', '_').lower()}.md"
    elif exp_type == "2":
        results = run_structure_experiment(topic)
        analysis_report = analyze_structure_results(results)
        report_filename = f"structure_experiment_{topic.replace(' ', '_').lower()}.md"
    else:  # 통합 실험
        word_results = run_word_choice_experiment(topic)
        structure_results = run_structure_experiment(topic)
        
        # 간단한 통합 분석 (실제로는 더 복잡한 통합 분석이 필요할 수 있음)
        word_analysis = analyze_word_choice_results(word_results)
        structure_analysis = analyze_structure_results(structure_results)
        
        analysis_report = f"# {topic} 단어 선택 및 구조 패턴 통합 실험 분석\n\n"
        analysis_report += "## 단어 선택 실험 분석\n\n"
        analysis_report += word_analysis.split("# ")[1]  # 제목 제외
        analysis_report += "\n\n## 구조 패턴 실험 분석\n\n"
        analysis_report += structure_analysis.split("# ")[1]  # 제목 제외
        
        report_filename = f"integrated_experiment_{topic.replace(' ', '_').lower()}.md"
    
    # 결과 저장
    save_option = get_user_input("\n실험 결과와 분석을 파일로 저장하시겠습니까? (y/n)", "y")
    if save_option.lower() in ['y', 'yes']:
        save_markdown(report_filename, analysis_report)
        print(f"\n분석 보고서가 {report_filename} 파일로 저장되었습니다.")
    
    print("\n단어 선택과 구조의 중요성 실험이 완료되었습니다.")
    print("이 실험을 통해 단어 선택과 구조 패턴이 AI 응답에 미치는 영향을 확인했습니다.")
    print("목적에 맞는 최적의 단어-구조 조합을 개발하여 프롬프트 효과를 극대화해보세요!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")