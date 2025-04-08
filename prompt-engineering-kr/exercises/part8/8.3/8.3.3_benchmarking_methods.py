"""
미묘한 뉘앙스 조정하기 실습 모듈

Part 8 - 섹션 8.3.3 실습 코드: 프롬프트의 미묘한 뉘앙스가 AI 응답에 미치는 영향을 
실험하고 섬세한 표현 차이를 활용하여 결과를 정교하게 조정하는 방법을 학습합니다.
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

# 뉘앙스 조정 실험을 위한 주제 옵션
NUANCE_EXPERIMENT_TOPICS = {
    "1": "인공지능의 사회적 영향",
    "2": "원격 근무의 미래",
    "3": "지속가능한 식품 시스템",
    "4": "디지털 프라이버시와 보안",
    "5": "교육의 디지털 전환"
}

# 어조 스펙트럼
TONE_SPECTRUM = {
    "격식성": ["고격식", "중간 격식", "비격식"],
    "전문성": ["전문가", "교육자", "일반인"],
    "감정": ["중립적", "열정적", "공감적"]
}

# 관점 프레이밍 유형
PERSPECTIVE_FRAMING = {
    "관점 범위": ["단일 관점", "대립 관점", "다중 관점"],
    "시간적 관점": ["과거", "현재", "미래", "통합적"],
    "문화적 관점": ["서구적", "동양적", "글로벌", "지역적"]
}

# 제약 조건과 자유도 수준
CONSTRAINT_FREEDOM_LEVELS = {
    "형식적 제약": ["높음", "중간", "낮음"],
    "내용적 제약": ["높음", "중간", "낮음"],
    "창의적 자유도": ["높음", "중간", "낮음"]
}

# 언어적 장치
LINGUISTIC_DEVICES = {
    "가정/전제": ["강한 전제", "조건부 가정", "중립적 접근"],
    "헤징 표현": ["높은 확신", "중간 확신", "낮은 확신"],
    "절대/상대 표현": ["절대 표현", "상대 표현"]
}

def create_tone_variation_prompts(topic: str) -> Dict[str, str]:
    """
    어조 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        어조 유형별 프롬프트 딕셔너리
    """
    tone_prompts = {}
    
    # 격식성 변형
    builder = PromptBuilder()
    builder.add_text(
        f"귀하께서 요청하신 {topic}에 대한 분석을 제공해 드리고자 합니다. "
        f"해당 주제에 관한 객관적 평가와 학술적 고찰을 포함하여 체계적으로 "
        f"정리해 드리겠습니다."
    )
    tone_prompts["고격식"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 분석을 제공해 드리겠습니다. "
        f"이 주제의 주요 측면과 영향을 살펴보고 균형 잡힌 시각을 "
        f"제시하겠습니다."
    )
    tone_prompts["중간 격식"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 알아볼까요? "
        f"이 흥미로운 주제의 여러 측면을 함께 살펴보고 "
        f"어떤 의미가 있는지 이야기해 보겠습니다."
    )
    tone_prompts["비격식"] = builder.build()
    
    # 전문성 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}의 다차원적 함의를 분석하겠습니다. "
        f"이 분야의 주요 이론적 프레임워크와 최신 연구 동향을 바탕으로 "
        f"체계적인 평가를 제시하겠습니다."
    )
    tone_prompts["전문가"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 설명해 드리겠습니다. "
        f"복잡한 개념을 이해하기 쉽게 풀어서 설명하고, "
        f"실제 사례와 함께 핵심 원리를 알려드리겠습니다."
    )
    tone_prompts["교육자"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 쉽게 알려드릴게요. "
        f"일상에서 볼 수 있는 예시와 함께 이야기하면서 "
        f"누구나 이해할 수 있게 설명해 드릴게요."
    )
    tone_prompts["일반인"] = builder.build()
    
    # 감정 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 객관적 분석을 제공합니다. "
        f"다양한 측면을 데이터와 사실에 기반하여 균형 있게 검토하겠습니다."
    )
    tone_prompts["중립적"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 놀라운 가능성을 살펴보겠습니다! "
        f"이 혁신적인 분야가 어떻게 우리의 미래를 변화시킬지, "
        f"그 흥미롭고 영감을 주는 측면들을 함께 알아보겠습니다."
    )
    tone_prompts["열정적"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}이 많은 사람들의 삶에 미치는 영향을 이해합니다. "
        f"이러한 변화가 가져오는 도전과 기회, 그리고 개인적 경험에 "
        f"어떤 의미를 갖는지 함께 살펴보겠습니다."
    )
    tone_prompts["공감적"] = builder.build()
    
    return tone_prompts

def create_perspective_variation_prompts(topic: str) -> Dict[str, str]:
    """
    관점 프레이밍 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        관점 유형별 프롬프트 딕셔너리
    """
    perspective_prompts = {}
    
    # 관점 범위 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}을 기술 낙관주의 관점에서 분석해주세요. "
        f"기술 발전이 가져올 긍정적 변화와 혜택을 중심으로 설명해주세요."
    )
    perspective_prompts["단일 관점"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}을 기술 낙관주의자와 비관주의자 관점에서 비교 분석해주세요. "
        f"두 관점의 주요 주장과 근거를 대조하고, 각 입장의 강점과 약점을 평가해주세요."
    )
    perspective_prompts["대립 관점"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}을 기술 기업, 정부 규제 기관, 일반 사용자, 사회 활동가 등 "
        f"다양한 이해관계자 관점에서 종합적으로 분석해주세요. "
        f"각 집단의 관심사, 우려, 기대를 포함해주세요."
    )
    perspective_prompts["다중 관점"] = builder.build()
    
    # 시간적 관점 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}의 역사적 발전 과정을 분석해주세요. "
        f"어떻게 시작되었고, 중요한 변곡점은 무엇이었으며, "
        f"지금까지 어떻게 진화해왔는지 설명해주세요."
    )
    perspective_prompts["과거"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}의 현재 상황을 분석해주세요. "
        f"현재 직면한 주요 도전 과제, 기회, 트렌드를 설명하고, "
        f"현재 가장 중요한 이슈와 논쟁점을 평가해주세요."
    )
    perspective_prompts["현재"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}의 미래 전망을 분석해주세요. "
        f"향후 5-10년 동안 예상되는 주요 발전, 변화, 기회를 예측하고, "
        f"잠재적 시나리오와 영향을 설명해주세요."
    )
    perspective_prompts["미래"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}을 과거, 현재, 미래를 연결하는 통합적 관점에서 분석해주세요. "
        f"역사적 발전이 현재 상황을 어떻게 형성했으며, 현재 추세가 "
        f"어떻게 미래 방향을 시사하는지 설명해주세요."
    )
    perspective_prompts["통합적"] = builder.build()
    
    return perspective_prompts

def create_constraint_freedom_prompts(topic: str) -> Dict[str, str]:
    """
    제약 조건과 자유도 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        제약/자유도 수준별 프롬프트 딕셔너리
    """
    constraint_freedom_prompts = {}
    
    # 높은 제약, 낮은 자유도
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 정확히 500단어로 분석해주세요. "
        f"반드시 다음 구조를 따라야 합니다:\n"
        f"1. 정의 및 범위 (100단어)\n"
        f"2. 주요 구성 요소 (150단어)\n"
        f"3. 현재 동향 (150단어)\n"
        f"4. 미래 전망 (100단어)\n\n"
        f"각 섹션은 반드시 2-3개의 구체적 사례를 포함해야 하며, "
        f"기술적 측면에만 집중하고 사회적, 윤리적 측면은 제외해주세요. "
        f"학술적 문체로 작성하고, 1인칭 표현은 사용하지 마세요."
    )
    constraint_freedom_prompts["높은 제약"] = builder.build()
    
    # 중간 제약, 중간 자유도
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 약 500단어 내외로 분석해주세요. "
        f"다음 요소를 포함하는 것이 좋습니다:\n"
        f"- 정의 및 범위\n"
        f"- 주요 구성 요소\n"
        f"- 현재 동향\n"
        f"- 미래 전망\n\n"
        f"기술적 측면을 중심으로 하되, 관련 있다면 사회적 측면도 언급할 수 있습니다. "
        f"적절한 사례를 포함하면 좋겠습니다. 전문적인 어조를 유지해주세요."
    )
    constraint_freedom_prompts["중간 제약"] = builder.build()
    
    # 낮은 제약, 높은 자유도
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대해 자유롭게 분석해주세요. "
        f"접근 방식, 구조, 길이는 귀하가 가장 효과적이라고 판단하는 대로 결정하세요. "
        f"다양한 측면(기술적, 사회적, 윤리적, 경제적 등)을 자유롭게 탐색하고, "
        f"개인적 견해와 창의적 해석을 포함하셔도 좋습니다. "
        f"기존의 틀을 벗어난 새로운 관점도 환영합니다."
    )
    constraint_freedom_prompts["낮은 제약"] = builder.build()
    
    return constraint_freedom_prompts

def create_linguistic_device_prompts(topic: str) -> Dict[str, str]:
    """
    언어적 장치 변형 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        언어적 장치 유형별 프롬프트 딕셔너리
    """
    linguistic_prompts = {}
    
    # 가정/전제 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}이 현대 사회의 핵심 과제라는 점은 분명합니다. "
        f"이 근본적인 문제가 우리의 미래를 결정할 것입니다. "
        f"이 중대한 변화의 주요 측면을 분석해주세요."
    )
    linguistic_prompts["강한 전제"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"만약 {topic}이 앞으로 10년간 지속적으로 발전한다면, "
        f"어떤 변화와 영향이 예상될까요? 이러한 가정 하에 "
        f"주요 측면과 잠재적 결과를 분석해주세요."
    )
    linguistic_prompts["조건부 가정"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 다양한 관점이 존재합니다. "
        f"이 주제의 여러 측면과 가능한 영향을 객관적으로 분석해주세요."
    )
    linguistic_prompts["중립적 접근"] = builder.build()
    
    # 헤징 표현 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}은 분명히 미래 사회를 형성할 결정적 요소입니다. "
        f"의심할 여지 없이 중요한 이 주제의 주요 측면과 확실한 영향을 분석해주세요."
    )
    linguistic_prompts["높은 확신"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}은 대체로 미래 사회에 상당한 영향을 미칠 것으로 보입니다. "
        f"이 주제의 주요 측면과 가능성이 높은 영향에 대해 분석해주세요."
    )
    linguistic_prompts["중간 확신"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}은 미래 사회에 어떤 영향을 미칠 수도 있습니다. "
        f"이 주제의 잠재적 측면과 가능한 영향에 대해 탐색해주세요."
    )
    linguistic_prompts["낮은 확신"] = builder.build()
    
    # 절대/상대 표현 변형
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 최선의 접근 방식을 분석해주세요. "
        f"가장 효과적인 전략, 필수적인 요소, 그리고 유일한 해결책에 초점을 맞춰주세요."
    )
    linguistic_prompts["절대 표현"] = builder.build()
    
    builder = PromptBuilder()
    builder.add_text(
        f"{topic}에 대한 다양한 접근 방식을 분석해주세요. "
        f"상황에 따라 더 효과적일 수 있는 전략들, 중요한 고려사항들, "
        f"그리고 가능한 여러 해결책을 탐색해주세요."
    )
    linguistic_prompts["상대 표현"] = builder.build()
    
    return linguistic_prompts

def create_advanced_nuance_prompts(topic: str) -> Dict[str, str]:
    """
    고급 뉘앙스 조정 프롬프트 생성
    
    Args:
        topic: 프롬프트 주제
        
    Returns:
        고급 뉘앙스 예시 프롬프트 딕셔너리
    """
    advanced_prompts = {}
    
    # 정책 분석 예시
    builder = PromptBuilder()
    builder.add_text(
        f"{topic} 정책이 다양한 이해관계자에게 미치는 영향을 분석해주세요. "
        f"단기적 경제 부담과 장기적 사회적 혜택 사이의 균형을 고려하고, "
        f"서로 다른 사회경제적 상황에서 어떻게 다르게 적용될 수 있는지 살펴봐주세요. "
        f"분석에는 일반적으로 제기되는 우려와 이에 대한 가능한 대응 방안도 포함해주세요. "
        f"명확한 결론보다는 정책 설계 시 고려해야 할 뉘앙스와 상충관계(trade-offs)를 "
        f"강조해주세요."
    )
    advanced_prompts["정책 분석"] = builder.build()
    
    # 제품 설명 예시
    builder = PromptBuilder()
    builder.add_text(
        f"{topic} 관련 제품이 어떻게 사용자의 일상을 향상시킬 수 있는지, "
        f"특히 생산성과 삶의 질 측면에서 설명해주세요. "
        f"기술적 사양보다는 사용자 경험과 실질적 혜택에 초점을 맞추되, "
        f"잠재적 사용자가 가질 수 있는 우려(예: 비용, 학습 곡선)에도 솔직하게 "
        f"대응해주세요. 다양한 사용자 프로필(초보자부터 전문가까지)에 맞춘 "
        f"맞춤형 가치 제안을 포함하고, 열정적이면서도 과장되지 않은 톤으로 작성해주세요."
    )
    advanced_prompts["제품 설명"] = builder.build()
    
    return advanced_prompts

def run_nuance_experiment(topic: str) -> Dict[str, Any]:
    """
    선택한 주제에 대해 다양한 뉘앙스 조정 실험 실행
    
    Args:
        topic: 실험 주제
        
    Returns:
        실험 결과 데이터
    """
    print_header(f"{topic}에 대한 뉘앙스 조정 실험")
    
    results = {
        "topic": topic,
        "tone_experiments": [],
        "perspective_experiments": [],
        "constraint_freedom_experiments": [],
        "linguistic_experiments": [],
        "advanced_experiments": []
    }
    
    # 1. 어조 변형 실험
    print_step(1, "어조 변형 실험")
    
    # 어조 변형 프롬프트 생성
    tone_prompts = create_tone_variation_prompts(topic)
    
    # 실험할 어조 유형 선택
    print("\n어조 유형 옵션:")
    print("  1. 격식성 (고격식 vs. 비격식)")
    print("  2. 전문성 (전문가 vs. 일반인)")
    print("  3. 감정 (중립적 vs. 열정적 vs. 공감적)")
    
    tone_type = get_user_input("\n실험할 어조 유형을 선택하세요", "1")
    
    # 선택된 어조 유형에 따라 프롬프트 필터링
    if tone_type == "1":
        selected_tones = ["고격식", "비격식"]
    elif tone_type == "2":
        selected_tones = ["전문가", "일반인"]
    else:
        selected_tones = ["중립적", "열정적", "공감적"]
    
    # 선택된 어조 실험 실행
    for tone in selected_tones:
        prompt = tone_prompts[tone]
        
        print(f"\n{tone} 어조 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {tone} 어조 프롬프트 응답이 생성되었습니다.")
        
        results["tone_experiments"].append({
            "tone": tone,
            "prompt": prompt,
            "result": result
        })
    
    # 2. 관점 프레이밍 실험
    print_step(2, "관점 프레이밍 실험")
    
    # 관점 프레이밍 프롬프트 생성
    perspective_prompts = create_perspective_variation_prompts(topic)
    
    # 실험할 관점 유형 선택
    print("\n관점 유형 옵션:")
    print("  1. 관점 범위 (단일 vs. 대립 vs. 다중)")
    print("  2. 시간적 관점 (과거 vs. 현재 vs. 미래 vs. 통합적)")
    
    perspective_type = get_user_input("\n실험할 관점 유형을 선택하세요", "1")
    
    # 선택된 관점 유형에 따라 프롬프트 필터링
    if perspective_type == "1":
        selected_perspectives = ["단일 관점", "대립 관점", "다중 관점"]
    else:
        selected_perspectives = ["과거", "현재", "미래"]
    
    # 선택된 관점 실험 실행
    for perspective in selected_perspectives:
        prompt = perspective_prompts[perspective]
        
        print(f"\n{perspective} 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {perspective} 프롬프트 응답이 생성되었습니다.")
        
        results["perspective_experiments"].append({
            "perspective": perspective,
            "prompt": prompt,
            "result": result
        })
    
    # 3. 제약 조건과 자유도 실험
    print_step(3, "제약 조건과 자유도 실험")
    
    # 제약 조건과 자유도 프롬프트 생성
    constraint_freedom_prompts = create_constraint_freedom_prompts(topic)
    
    # 제약 수준 실험 실행
    for level, prompt in constraint_freedom_prompts.items():
        print(f"\n{level} 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {level} 프롬프트 응답이 생성되었습니다.")
        
        results["constraint_freedom_experiments"].append({
            "level": level,
            "prompt": prompt,
            "result": result
        })
    
    # 4. 언어적 장치 실험
    print_step(4, "언어적 장치 실험")
    
    # 언어적 장치 프롬프트 생성
    linguistic_prompts = create_linguistic_device_prompts(topic)
    
    # 실험할 언어적 장치 유형 선택
    print("\n언어적 장치 유형 옵션:")
    print("  1. 가정/전제 (강한 전제 vs. 조건부 가정 vs. 중립적 접근)")
    print("  2. 헤징 표현 (높은 확신 vs. 중간 확신 vs. 낮은 확신)")
    print("  3. 절대/상대 표현 (절대 표현 vs. 상대 표현)")
    
    linguistic_type = get_user_input("\n실험할 언어적 장치 유형을 선택하세요", "1")
    
    # 선택된 언어적 장치 유형에 따라 프롬프트 필터링
    if linguistic_type == "1":
        selected_devices = ["강한 전제", "조건부 가정", "중립적 접근"]
    elif linguistic_type == "2":
        selected_devices = ["높은 확신", "중간 확신", "낮은 확신"]
    else:
        selected_devices = ["절대 표현", "상대 표현"]
    
    # 선택된 언어적 장치 실험 실행
    for device in selected_devices:
        prompt = linguistic_prompts[device]
        
        print(f"\n{device} 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {device} 프롬프트 응답이 생성되었습니다.")
        
        results["linguistic_experiments"].append({
            "device": device,
            "prompt": prompt,
            "result": result
        })
    
    # 5. 고급 뉘앙스 조정 실험
    print_step(5, "고급 뉘앙스 조정 실험")
    
    # 고급 뉘앙스 조정 프롬프트 생성
    advanced_prompts = create_advanced_nuance_prompts(topic)
    
    # 고급 뉘앙스 조정 실험 실행
    for example_name, prompt in advanced_prompts.items():
        print(f"\n{example_name} 고급 뉘앙스 프롬프트:\n{prompt}\n")
        
        print("응답 생성 중...")
        result = get_completion(prompt, temperature=0.7)
        print(f"\n✅ {example_name} 고급 뉘앙스 프롬프트 응답이 생성되었습니다.")
        
        results["advanced_experiments"].append({
            "example": example_name,
            "prompt": prompt,
            "result": result
        })
    
    # 결과 비교 표시
    print_step(6, "실험 결과 비교")
    
    # 실험 결과 간략 비교
    print("\n=== 어조 변형 결과 비교 ===")
    for exp in results["tone_experiments"]:
        print(f"\n--- {exp['tone']} 어조 ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n=== 관점 프레이밍 결과 비교 ===")
    for exp in results["perspective_experiments"]:
        print(f"\n--- {exp['perspective']} ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n=== 제약 조건과 자유도 결과 비교 ===")
    for exp in results["constraint_freedom_experiments"]:
        print(f"\n--- {exp['level']} ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n=== 언어적 장치 결과 비교 ===")
    for exp in results["linguistic_experiments"]:
        print(f"\n--- {exp['device']} ---")
        display_results_comparison("", exp["result"], 200)
    
    print("\n=== 고급 뉘앙스 조정 결과 비교 ===")
    for exp in results["advanced_experiments"]:
        print(f"\n--- {exp['example']} ---")
        display_results_comparison("", exp["result"], 200)
    
    return results

def analyze_nuance_experiment_results(results: Dict[str, Any]) -> str:
    """
    뉘앙스 조정 실험 결과 분석
    
    Args:
        results: 실험 결과 데이터
        
    Returns:
        분석 보고서
    """
    topic = results["topic"]
    tone_exps = results["tone_experiments"]
    perspective_exps = results["perspective_experiments"]
    constraint_freedom_exps = results["constraint_freedom_experiments"]
    linguistic_exps = results["linguistic_experiments"]
    advanced_exps = results["advanced_experiments"]
    
    # 분석 보고서 작성
    report = f"# {topic} 뉘앙스 조정 실험 분석\n\n"
    
    # 어조 변형 분석
    if tone_exps:
        report += "## 어조 변형 분석\n\n"
        
        for exp in tone_exps:
            report += f"### {exp['tone']} 어조\n\n"
            report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
            
            # 각 어조별 효과 분석
            report += "**효과 분석:**\n"
            
            if exp['tone'] == "고격식":
                report += "- 공식적이고 학술적인 어조 형성\n"
                report += "- 더 체계적이고 객관적인 분석 유도\n"
                report += "- 전문성과 신뢰성 인상 강화\n"
                report += "- 감정적 반응보다 논리적 분석 촉진\n\n"
            elif exp['tone'] == "중간 격식":
                report += "- 전문성을 유지하면서 접근성 향상\n"
                report += "- 균형 잡힌 분석과 일반적 이해 용이성 사이 균형\n"
                report += "- 넓은 독자층에게 적합한 톤 형성\n\n"
            elif exp['tone'] == "비격식":
                report += "- 친근하고 대화적인 어조 형성\n"
                report += "- 접근성과 이해도 향상, 특히 초보자에게 적합\n"
                report += "- 몰입도와 관심도 증가 가능성\n"
                report += "- 복잡한 주제의 부담감 감소\n\n"
            elif exp['tone'] == "전문가":
                report += "- 깊이 있는 분석과 전문 용어 사용 증가\n"
                report += "- 복잡한 개념과 이론적 프레임워크 활용\n"
                report += "- 전문 독자를 위한 심층적 통찰 제공\n"
                report += "- 비전문가에게는 접근성 제한 가능성\n\n"
            elif exp['tone'] == "교육자":
                report += "- 개념 설명과 예시 활용 증가\n"
                report += "- 복잡한 내용을 단계적으로 소개\n"
                report += "- 학습자의 이해를 돕는 교육적 접근법\n"
                report += "- 전문 지식과 접근성 사이의 균형\n\n"
            elif exp['tone'] == "일반인":
                report += "- 일상적 언어와 비유 활용 증가\n"
                report += "- 복잡한 개념의 단순화와 실생활 연결\n"
                report += "- 최대한의 접근성과 친근감 조성\n"
                report += "- 깊이보다 폭넓은 이해에 초점\n\n"
            elif exp['tone'] == "중립적":
                report += "- 사실 중심적이고 균형 잡힌 분석 촉진\n"
                report += "- 개인적 의견이나 감정 표현 최소화\n"
                report += "- 객관적이고 분석적인 접근 강화\n"
                report += "- 논쟁적 주제에 적합한 중립성 유지\n\n"
            elif exp['tone'] == "열정적":
                report += "- 긍정적 에너지와 흥미 유발 효과\n"
                report += "- 주제의 흥미로운 측면과 가능성 강조\n"
                report += "- 독자의 관심과 몰입도 증가 가능성\n"
                report += "- 객관성보다 영감과 동기부여에 초점\n\n"
            elif exp['tone'] == "공감적":
                report += "- 인간적 측면과 개인 경험 강조\n"
                report += "- 독자와 감정적 연결 형성\n"
                report += "- 실제 영향과 의미에 대한 성찰 증가\n"
                report += "- 분석적 접근과 감정적 이해 결합\n\n"
    
    # 관점 프레이밍 분석
    if perspective_exps:
        report += "## 관점 프레이밍 분석\n\n"
        
        for exp in perspective_exps:
            report += f"### {exp['perspective']} 프레이밍\n\n"
            report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
            
            # 각 관점별 효과 분석
            report += "**효과 분석:**\n"
            
            if exp['perspective'] == "단일 관점":
                report += "- 특정 관점의 깊이 있는 탐색 유도\n"
                report += "- 일관된 논리와 전제 기반 분석 촉진\n"
                report += "- 선택된 관점의 강점과 통찰력 강조\n"
                report += "- 균형성 제한과 편향 가능성 증가\n\n"
            elif exp['perspective'] == "대립 관점":
                report += "- 대조되는 입장 간의 직접 비교 촉진\n"
                report += "- 각 관점의 강점과 약점 명확화\n"
                report += "- 주제의 복잡성과 논쟁점 부각\n"
                report += "- 비판적 사고와 분석적 평가 증진\n\n"
            elif exp['perspective'] == "다중 관점":
                report += "- 다양한 이해관계자와 입장 고려 유도\n"
                report += "- 주제의 복잡성과 다면성 인식 증진\n"
                report += "- 보다 포괄적이고 균형 잡힌 분석 촉진\n"
                report += "- 깊이보다 폭넓은 이해와 종합에 초점\n\n"
            elif exp['perspective'] == "과거":
                report += "- 역사적 맥락과 발전 과정 강조\n"
                report += "- 현재 상황의 기원과 진화 이해 촉진\n"
                report += "- 패턴, 교훈, 선례 식별 유도\n"
                report += "- 현재와 미래보다 과거 중심 접근\n\n"
            elif exp['perspective'] == "현재":
                report += "- 현 상황과 즉각적 과제에 초점\n"
                report += "- 실시간 트렌드와 이슈 분석 유도\n"
                report += "- 실용적이고 적용 가능한 인사이트 강조\n"
                report += "- 더 넓은 역사적/미래적 맥락 제한 가능성\n\n"
            elif exp['perspective'] == "미래":
                report += "- 예측, 전망, 잠재적 시나리오에 초점\n"
                report += "- 혁신적 사고와 가능성 탐색 촉진\n"
                report += "- 장기적 영향과 전략적 준비 강조\n"
                report += "- 현실적 제약보다 변화 가능성에 중점\n\n"
    
    # 제약 조건과 자유도 분석
    if constraint_freedom_exps:
        report += "## 제약 조건과 자유도 분석\n\n"
        
        for exp in constraint_freedom_exps:
            report += f"### {exp['level']}\n\n"
            report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
            
            # 각 제약/자유도별 효과 분석
            report += "**효과 분석:**\n"
            
            if exp['level'] == "높은 제약":
                report += "- 엄격한 구조와 형식 요구로 일관된 형식 보장\n"
                report += "- 명확한 경계 설정으로 초점과 방향성 제공\n"
                report += "- 예측 가능한 결과물과 완성도 향상\n"
                report += "- 창의성과 유연성 제한, 독창적 접근 억제\n\n"
            elif exp['level'] == "중간 제약":
                report += "- 방향성과 구조 제공하면서 유연성 허용\n"
                report += "- 균형 잡힌 형식과 창의적 자유 제공\n"
                report += "- 구조화된 응답이지만 상황별 조정 가능\n"
                report += "- 다양한 목적과 상황에 적응 가능한 균형\n\n"
            elif exp['level'] == "낮은 제약":
                report += "- 최대한의 창의적 자유와 유연성 제공\n"
                report += "- 다양하고 예상치 못한 접근법 장려\n"
                report += "- 아이디어 탐색과 혁신적 발상 촉진\n"
                report += "- 일관성과 예측가능성 감소, 결과 변동성 증가\n\n"
    
    # 언어적 장치 분석
    if linguistic_exps:
        report += "## 언어적 장치 분석\n\n"
        
        for exp in linguistic_exps:
            report += f"### {exp['device']}\n\n"
            report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
            
            # 각 언어적 장치별 효과 분석
            report += "**효과 분석:**\n"
            
            if exp['device'] == "강한 전제":
                report += "- 주제의 중요성과 확실성을 기정사실화\n"
                report += "- 특정 방향으로의 분석 프레이밍\n"
                report += "- 비판적 검토보다 수용에 기반한 분석 유도\n"
                report += "- 대안적 관점이나 의문 제기 범위 축소\n\n"
            elif exp['device'] == "조건부 가정":
                report += "- 특정 조건 하에서의 분석 장려\n"
                report += "- 가상 시나리오 기반 사고 실험 유도\n"
                report += "- 불확실성 인정하면서 탐색적 분석 가능\n"
                report += "- 더 광범위한 사고와 조건부 결론 도출\n\n"
            elif exp['device'] == "중립적 접근":
                report += "- 다양한 관점과 가능성에 열린 접근 장려\n"
                report += "- 균형 잡힌 분석과 객관적 평가 촉진\n"
                report += "- 결론보다 다면적 탐색 우선시\n"
                report += "- 방향성 부족으로 인한 초점 분산 가능성\n\n"
            elif exp['device'] == "높은 확신":
                report += "- 강한 확신과 단정적 표현으로 신뢰감 형성\n"
                report += "- 명확하고 직접적인 주장 강화\n"
                report += "- 불확실성보다 명확한 방향성 제공\n"
                report += "- 뉘앙스 손실과 복잡성 단순화 위험\n\n"
            elif exp['device'] == "중간 확신":
                report += "- 적절한 확신과 신중함의 균형\n"
                report += "- 주요 패턴 인정하면서 예외 가능성 수용\n"
                report += "- 전문성 유지하면서 유연성 확보\n"
                report += "- 대부분의 분석적 맥락에 적합한 균형\n\n"
            elif exp['device'] == "낮은 확신":
                report += "- 가능성과 탐색 중심의 접근 장려\n"
                report += "- 다양한 시나리오와 대안적 해석 고려\n"
                report += "- 불확실성과 복잡성에 대한 인식 증진\n"
                report += "- 명확한 지침보다는 질문과 고려사항 강조\n\n"
            elif exp['device'] == "절대 표현":
                report += "- 명확하고 강한 판단 제공\n"
                report += "- 최적해와 필수 요소 중심 접근\n"
                report += "- 의사결정을 위한 명확한 방향성 제시\n"
                report += "- 맥락별 차이와 대안 가능성 간과 위험\n\n"
            elif exp['device'] == "상대 표현":
                report += "- 상황과 맥락에 따른 유연한 접근 장려\n"
                report += "- 다양한 선택지와 맞춤형 해결책 고려\n"
                report += "- 복잡성과 뉘앙스에 대한 인식 강화\n"
                report += "- 명확한 의사결정보다 맥락별 조정 강조\n\n"
    
    # 고급 뉘앙스 조정 분석
    if advanced_exps:
        report += "## 고급 뉘앙스 조정 분석\n\n"
        
        for exp in advanced_exps:
            report += f"### {exp['example']}\n\n"
            report += f"**프롬프트:**\n```\n{exp['prompt']}\n```\n\n"
            
            # 각 고급 예시별 효과 분석
            report += "**효과 분석:**\n"
            
            if exp['example'] == "정책 분석":
                report += "- 다양한 이해관계자와 시간적 관점 통합\n"
                report += "- 단순한 장단점 나열이 아닌 상충관계(trade-offs) 탐색\n"
                report += "- 맥락과 조건에 따른 차별화된 효과 인식\n"
                report += "- 단정적 결론보다 균형 잡힌 뉘앙스 강조\n"
                report += "- 우려와 대응 방안의 균형으로 현실적 진단\n\n"
            elif exp['example'] == "제품 설명":
                report += "- 기술 사양보다 사용자 경험과 실질적 혜택 강조\n"
                report += "- 솔직한 한계 인정과 다양한 사용자 상황 고려\n"
                report += "- 열정과 객관성의 균형 잡힌 톤 설정\n"
                report += "- 맞춤형 가치 제안을 통한 다양한 니즈 충족\n"
                report += "- 과장되지 않은 현실적 기대 설정\n\n"
    
    # 뉘앙스 최적화 가이드라인
    report += "## 뉘앙스 최적화 가이드라인\n\n"
    
    report += "### 목적별 최적 뉘앙스 전략\n\n"
    report += "| 목적 | 권장 어조 | 관점 프레이밍 | 제약/자유도 | 언어적 장치 |\n"
    report += "|------|----------|--------------|-----------|------------|\n"
    report += "| 정보 전달 | 중간 격식, 교육자 | 다중 관점, 통합적 시간 | 중간 제약 | 중간 확신, 중립적 가정 |\n"
    report += "| 설득/주장 | 고격식, 전문가 | 대립 관점 | 중간~높은 제약 | 강한 전제, 높은 확신 |\n"
    report += "| 창의적 발상 | 비격식, 열정적 | 단일/다중 관점 | 낮은 제약 | 조건부 가정, 낮은 확신 |\n"
    report += "| 비판적 분석 | 고격식, 중립적 | 대립 관점 | 중간 제약 | 중립적 접근, 상대 표현 |\n"
    report += "| 공감/지원 | 비격식, 공감적 | 단일 관점 | 낮은 제약 | 중간 확신, 상대 표현 |\n\n"
    
    report += "### 뉘앙스 조정 체크리스트\n\n"
    report += "- [ ] **목적 명확화**: 의도한 응답 유형 및 톤 정의\n"
    report += "- [ ] **어조 선택**: 적절한 격식성, 전문성, 감정 수준 결정\n"
    report += "- [ ] **관점 설정**: 가장 효과적인 관점 범위와 시간적 프레임 선택\n"
    report += "- [ ] **제약/자유도 균형**: 목적에 맞는 구조와 창의적 자유도 조정\n"
    report += "- [ ] **언어적 장치 최적화**: 전제, 확신성, 절대/상대 표현 미세 조정\n"
    report += "- [ ] **통합적 일관성**: 모든 뉘앙스 요소가 서로 조화를 이루는지 확인\n\n"
    
    report += "### 뉘앙스 조정 워크플로우\n\n"
    report += "1. **목적과 맥락 명확화**\n"
    report += "   - 원하는 응답의 정확한 특성 정의\n"
    report += "   - 응답이 사용될 맥락과 대상 고려\n"
    report += "   - 가장 중요한 뉘앙스 요소 우선순위화\n\n"
    
    report += "2. **초기 프롬프트 작성**\n"
    report += "   - 기본 질문이나 요청 작성\n"
    report += "   - 핵심 제약 조건 및 요구사항 포함\n"
    report += "   - 명확한 구조 및 지시 설정\n\n"
    
    report += "3. **뉘앙스 요소 분석**\n"
    report += "   - 현재 프롬프트의 어조, 관점, 제약/자유도 분석\n"
    report += "   - 가정 및 전제 검토\n"
    report += "   - 언어적 패턴 및 표현 효과 평가\n\n"
    
    report += "4. **미세 조정 적용**\n"
    report += "   - 목적에 맞는 어조 및 관점 조정\n"
    report += "   - 제약과 자유도 균형 최적화\n"
    report += "   - 언어적 뉘앙스 정교화 (헤징, 대조, 전제 등)\n\n"
    
    report += "5. **테스트 및 반복**\n"
    report += "   - 조정된 프롬프트 테스트\n"
    report += "   - 응답 분석 및 목표 달성도 평가\n"
    report += "   - 필요에 따라 추가 미세 조정\n\n"
    
    # 고급 뉘앙스 조정 예시
    report += "### 고급 뉘앙스 조정 예시\n\n"
    
    report += "**기본 프롬프트:**\n"
    report += "```\n"
    report += f"{topic}에 대해 설명해주세요.\n"
    report += "```\n\n"
    
    report += "**정교화된 프롬프트:**\n"
    report += "```\n"
    report += f"{topic}이 다양한 이해관계자에게 미치는 영향을 분석해주세요. 단기적 비용과 \n"
    report += "장기적 혜택 사이의 균형을 고려하고, 서로 다른 상황과 맥락에 따라 어떻게 \n"
    report += "다르게 적용될 수 있는지 살펴봐주세요. 일반적으로 제기되는 우려에도 솔직하게 \n"
    report += "대응하되, 가능한 완화 전략도 함께 제시해주세요. 명확한 결론보다는 의사결정 시 \n"
    report += "고려해야 할 뉘앙스와 상충관계(trade-offs)를 강조해주세요.\n"
    report += "```\n\n"
    
    report += "**뉘앙스 요소 분석:**\n"
    report += "- **어조**: 중간 격식성, 전문가적 접근, 중립적 감정\n"
    report += "- **관점**: 다중 관점, 단기/장기 시간 프레임 통합\n"
    report += "- **제약/자유도**: 중간 수준의 구조화된 자유도\n"
    report += "- **언어적 장치**: 중립적 가정, 중간 확신, 상대적 표현\n"
    report += "- **효과**: 균형 잡히고 뉘앙스 있는 분석 유도, 복잡성 인정, 맥락 고려\n\n"
    
    # 결론
    report += "## 결론\n\n"
    report += f"{topic}에 대한 뉘앙스 조정 실험을 통해 미묘한 표현 차이가 AI 응답의 성격, 깊이, 유용성에 상당한 영향을 미침을 확인했습니다. "
    report += "어조, 관점, 제약/자유도, 언어적 장치와 같은 요소들을 목적에 맞게 정교하게 조정함으로써 AI 응답의 품질을 크게 향상시킬 수 있습니다. "
    report += "특히 복잡하고 미묘한 뉘앙스를 요구하는 주제일수록 이러한 요소들의 중요성이 더욱 커집니다. "
    report += "목적과 맥락에 맞는 최적의 뉘앙스 조정 전략을 개발하고 적용함으로써 AI와의 소통 효과를 극대화할 수 있습니다."
    
    return report

def main() -> None:
    """
    메인 함수
    """
    print_header("미묘한 뉘앙스 조정 실험")
    
    # 주제 선택
    print_step(1, "실험 주제 선택")
    
    print("\n실험 주제 옵션:")
    for key, value in NUANCE_EXPERIMENT_TOPICS.items():
        print(f"  {key}. {value}")
    
    choice = get_user_input("\n주제를 선택하세요", "1")
    topic = NUANCE_EXPERIMENT_TOPICS.get(choice, NUANCE_EXPERIMENT_TOPICS["1"])
    
    print(f"\n선택한 주제: {topic}")
    
    # 뉘앙스 조정 실험 실행
    results = run_nuance_experiment(topic)
    
    # 실험 결과 분석
    analysis_report = analyze_nuance_experiment_results(results)
    
    # 결과 저장
    save_option = get_user_input("\n실험 결과와 분석을 파일로 저장하시겠습니까? (y/n)", "y")
    if save_option.lower() in ['y', 'yes']:
        # 파일명 생성
        safe_topic = topic.replace(' ', '_').lower()
        filename = f"nuance_experiment_{safe_topic}.md"
        
        # 분석 보고서 저장
        save_markdown(filename, analysis_report)
        print(f"\n분석 보고서가 {filename} 파일로 저장되었습니다.")
    
    print("\n미묘한 뉘앙스 조정 실험이 완료되었습니다.")
    print("이 실험을 통해 미묘한 표현 차이가 AI 응답에 미치는 영향을 확인했습니다.")
    print("목적과 상황에 맞는 뉘앙스 조정 전략을 개발하여 더 정교한 프롬프트를 설계해보세요!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")