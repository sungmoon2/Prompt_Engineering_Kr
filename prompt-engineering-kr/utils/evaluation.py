"""
프롬프트 결과 평가 모듈

AI 응답 품질 평가 및 프롬프트 개선을 위한 유틸리티 함수를 제공합니다.
"""

from typing import Dict, List, Any, Optional, Union
from .ai_client import get_completion

def evaluate_response(prompt: str, response: str, criteria: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    AI 응답 품질 평가
    
    Args:
        prompt: 원본 프롬프트
        response: AI 응답
        criteria: 평가 기준 목록 (없으면 기본 기준 사용)
        
    Returns:
        평가 결과 (기준별 점수와 코멘트)
    """
    if not criteria:
        criteria = [
            "관련성 (Relevance)", 
            "정확성 (Accuracy)", 
            "완전성 (Completeness)", 
            "유용성 (Usefulness)", 
            "명확성 (Clarity)"
        ]
    
    criteria_str = "\n".join([f"- {c}" for c in criteria])
    
    evaluation_prompt = f"""
당신은 AI 응답을 평가하는 전문가입니다. 다음 기준에 따라 AI의 응답을 평가해주세요:

{criteria_str}

각 기준에 대해 1-10점 척도로 점수를 매기고, 간략한 코멘트를 제공해주세요.

원본 프롬프트:
```
{prompt}
```

AI 응답:
```
{response}
```

다음 JSON 형식으로 평가 결과를 제공해주세요:
{{
  "scores": {{
    "기준1": 점수,
    "기준2": 점수,
    ...
  }},
  "comments": {{
    "기준1": "코멘트",
    "기준2": "코멘트",
    ...
  }},
  "overall_score": 종합점수,
  "strengths": ["강점1", "강점2", ...],
  "areas_for_improvement": ["개선점1", "개선점2", ...],
  "suggestions": "프롬프트 개선 제안"
}}
"""
    
    # 평가 요청
    evaluation_result = get_completion(evaluation_prompt, temperature=0.3)
    
    # JSON 형식으로 파싱
    import json
    from .response_formatter import extract_json
    
    try:
        result = extract_json(evaluation_result)
        return result
    except Exception as e:
        print(f"평가 결과 파싱 오류: {e}")
        return {
            "error": "평가 결과를 파싱할 수 없습니다.",
            "raw_response": evaluation_result
        }


def compare_prompts(prompts: List[str], task: str, 
                   criteria: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    여러 프롬프트 성능 비교
    
    Args:
        prompts: 비교할 프롬프트 목록
        task: 프롬프트 목적/태스크 설명
        criteria: 평가 기준 목록 (없으면 기본 기준 사용)
        
    Returns:
        프롬프트별 평가 및 순위
    """
    if not criteria:
        criteria = [
            "명확성 (Clarity)",
            "효율성 (Efficiency)",
            "구체성 (Specificity)",
            "맥락 제공 (Context)",
            "효과적 제약 (Constraints)"
        ]
    
    criteria_str = "\n".join([f"- {c}" for c in criteria])
    prompt_list = "\n\n".join([f"프롬프트 {i+1}:\n```\n{p}\n```" for i, p in enumerate(prompts)])
    
    comparison_prompt = f"""
당신은 프롬프트 엔지니어링 전문가입니다. 다음 프롬프트들을 비교 평가해주세요:

{prompt_list}

태스크/목적: {task}

다음 기준에 따라 각 프롬프트를 평가해주세요:
{criteria_str}

각 기준에 대해 1-10점 척도로 점수를 매기고, 각 프롬프트의 장단점을 분석해주세요.
프롬프트 간 비교 평가와 종합 순위도 제공해주세요.

다음 JSON 형식으로 평가 결과를 제공해주세요:
{{
  "prompt_evaluations": [
    {{
      "prompt_number": 1,
      "scores": {{ ... }},
      "strengths": ["강점1", ...],
      "weaknesses": ["약점1", ...],
      "overall_score": 종합점수
    }},
    ...
  ],
  "comparative_analysis": "프롬프트 간 비교 분석",
  "rankings": [1, 3, 2, ...],
  "best_prompt": 프롬프트번호,
  "improvement_suggestions": "개선 제안"
}}
"""
    
    # 비교 평가 요청
    comparison_result = get_completion(comparison_prompt, temperature=0.3)
    
    # JSON 형식으로 파싱
    from .response_formatter import extract_json
    
    try:
        result = extract_json(comparison_result)
        return result
    except Exception as e:
        print(f"비교 평가 결과 파싱 오류: {e}")
        return {
            "error": "비교 평가 결과를 파싱할 수 없습니다.",
            "raw_response": comparison_result
        }


def suggest_improvements(prompt: str, response: str, issues: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    프롬프트 개선 제안
    
    Args:
        prompt: 원본 프롬프트
        response: AI 응답
        issues: 개선이 필요한 문제점 목록 (선택사항)
        
    Returns:
        개선된 프롬프트 및 설명
    """
    issues_str = ""
    if issues:
        issues_str = "특히 다음 문제점들을 해결하는 데 중점을 두어주세요:\n" + "\n".join([f"- {i}" for i in issues])
    
    improvement_prompt = f"""
당신은 프롬프트 엔지니어링 전문가입니다. 다음 프롬프트와 그에 대한 응답을 분석하고, 
프롬프트를 개선할 방법을 제안해주세요.

원본 프롬프트:
```
{prompt}
```

받은 응답:
```
{response}
```

{issues_str}

다음 요소를 고려하여 프롬프트를 개선해주세요:
1. 명확성 및 구체성
2. 역할 지정 및 맥락 제공
3. 예시 활용 (few-shot learning)
4. 단계적 사고 유도
5. 출력 형식 지정
6. 제약 조건 명시

다음 JSON 형식으로 응답해주세요:
{{
  "analysis": "현재 프롬프트 분석",
  "issues": ["문제점1", "문제점2", ...],
  "improved_prompt": "개선된 프롬프트",
  "explanation": "개선 사항 설명",
  "expected_benefits": ["기대 효과1", "기대 효과2", ...]
}}
"""
    
    # 개선 제안 요청
    improvement_result = get_completion(improvement_prompt, temperature=0.3)
    
    # JSON 형식으로 파싱
    from .response_formatter import extract_json
    
    try:
        result = extract_json(improvement_result)
        return result
    except Exception as e:
        print(f"개선 제안 결과 파싱 오류: {e}")
        return {
            "error": "개선 제안 결과를 파싱할 수 없습니다.",
            "raw_response": improvement_result
        }


def analyze_prompt_components(prompt: str) -> Dict[str, Any]:
    """
    프롬프트 구성 요소 분석
    
    Args:
        prompt: 분석할 프롬프트
        
    Returns:
        프롬프트 구성 요소 분석 결과
    """
    analysis_prompt = f"""
당신은 프롬프트 엔지니어링 분석 전문가입니다. 다음 프롬프트의 구성 요소를 분석해주세요:

```
{prompt}
```

다음 구성 요소들을 식별하고 분석해주세요:
1. 역할 지정 (Role prompting)
2. 맥락 제공 (Context setting)
3. 작업 지시 (Task instructions)
4. 예시 (Examples)
5. 제약 조건 (Constraints)
6. 출력 형식 (Output formatting)
7. 단계적 사고 유도 (Chain of thought)
8. 기타 패턴

다음 JSON 형식으로 응답해주세요:
{{
  "identified_components": ["역할 지정", ...],
  "component_analysis": {{
    "역할 지정": {{
      "present": true/false,
      "content": "구체적 내용",
      "effectiveness": "효과 분석"
    }},
    ...
  }},
  "patterns_used": ["패턴1", ...],
  "missing_components": ["컴포넌트1", ...],
  "overall_analysis": "전반적 분석"
}}
"""
    
    # 구성 요소 분석 요청
    analysis_result = get_completion(analysis_prompt, temperature=0.3)
    
    # JSON 형식으로 파싱
    from .response_formatter import extract_json
    
    try:
        result = extract_json(analysis_result)
        return result
    except Exception as e:
        print(f"프롬프트 분석 결과 파싱 오류: {e}")
        return {
            "error": "프롬프트 분석 결과를 파싱할 수 없습니다.",
            "raw_response": analysis_result
        }