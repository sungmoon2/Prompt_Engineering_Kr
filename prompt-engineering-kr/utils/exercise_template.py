"""
실습 템플릿 모듈

실습 코드의 공통 구조를 제공하여 중복을 줄이고 일관성을 높입니다.
"""

import os
import sys
import inspect
from typing import Dict, List, Any, Optional, Callable, Tuple

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.ui_helpers import (
    print_header, print_step, get_user_input, 
    display_results_comparison, print_prompt_summary,
    print_learning_points
)
from utils.example_data import get_examples_by_category
from utils.chapter_utils import get_chapter_save_path

def run_exercise(
    title: str,
    topic_options: Dict[str, Any],
    get_basic_prompt: Callable[[str], str],
    get_enhanced_prompt: Callable[[str, Optional[str], Optional[str]], str],
    prompt_summary: Dict[str, List[str]],
    learning_points: List[str]
) -> None:
    """
    표준 실습 실행 함수
    
    Args:
        title: 실습 제목
        topic_options: 주제 선택 옵션
        get_basic_prompt: 기본 프롬프트 생성 함수
        get_enhanced_prompt: 향상된 프롬프트 생성 함수
        prompt_summary: 프롬프트 요약 정보
        learning_points: 학습 포인트 목록
    """
    # 디버그 정보 출력
    frame = inspect.stack()[1]
    calling_file = frame.filename
    print(f"실행 파일: {calling_file}")
    print(f"파일 이름: {os.path.basename(calling_file)}")
    
    print_header(title)
    
    # 1. 주제 선택 단계
    print_step(1, "주제 선택")
    
    # 옵션 표시
    print("\n주제 옵션:")
    for key, value in topic_options.items():
        if isinstance(value, dict):
            print(f"  {key}. {value.get('name', '')}")
        else:
            print(f"  {key}. {value}")
    print("  0. 직접 주제 입력하기")
    
    # 주제 선택 및 관련 정보 처리
    topic, purpose, output_format = select_topic(topic_options)
    
    # 2. 기본 프롬프트 실행 단계
    print_step(2, "기본 프롬프트로 요청하기")
    
    # 기본 프롬프트 생성
    basic_prompt = get_basic_prompt(topic)
    
    print("\n기본 프롬프트:")
    print(f"'{basic_prompt}'")
    
    # AI 응답 요청
    print("\n응답 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n✅ 기본 프롬프트 응답이 생성되었습니다.")
    
    # 3. 향상된 프롬프트 실행 단계
    print_step(3, "향상된 프롬프트로 요청하기")
    
    # 향상된 프롬프트 생성
    enhanced_prompt = get_enhanced_prompt(topic, purpose, output_format)
    
    # 프롬프트 요약 정보 출력
    print_prompt_summary("향상된", prompt_summary.get("enhanced", []))
    
    # AI 응답 요청
    print("\n응답 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n✅ 향상된 프롬프트 응답이 생성되었습니다.")
    
    # 4. 결과 비교 및 저장 단계
    print_step(4, "결과 비교 및 저장")
    
    # 결과 비교 표시
    display_results_comparison(basic_result, enhanced_result, 300)
    
    # 결과 저장
    save_option = get_user_input("\n결과를 파일로 저장하시겠습니까? (y/n)", "y")
    if save_option.lower() in ['y', 'yes']:
        save_results(topic, basic_prompt, basic_result, enhanced_prompt, enhanced_result, calling_file)
    
    # 5. 학습 내용 정리 단계
    print_step(5, "학습 내용 정리")
    
    # 학습 포인트 출력
    print_learning_points(learning_points)

def select_topic(topic_options: Dict[str, Any]) -> Tuple[str, str, str]:
    """
    주제 선택 처리
    
    Args:
        topic_options: 주제 선택 옵션
        
    Returns:
        주제, 목적, 출력 형식 튜플
    """
    choice = get_user_input("\n선택하세요", "1")
    
    if choice == "0":
        topic = get_user_input("주제를 입력하세요", "여름 휴가 계획")
        purpose = get_user_input("이 정보를 사용할 목적을 입력하세요", "휴가 계획 수립")
        output_format = get_user_input("원하는 출력 형식을 입력하세요", "일정표")
    else:
        selected = topic_options.get(choice, topic_options["1"])
        if isinstance(selected, dict):
            topic = selected.get("topic", "")
            purpose = selected.get("name", "") + " 작성"
            output_format = selected.get("output_format", "")
        else:
            topic = selected
            purpose = "정보 수집"
            output_format = "구조화된 형식"
    
    print(f"\n선택한 주제: {topic}")
    print(f"사용 목적: {purpose}")
    print(f"출력 형식: {output_format}")
    
    return topic, purpose, output_format

def save_comparison(basic_prompt, basic_result, enhanced_prompt, enhanced_result, topic, filename=None, calling_file=None):
    """
    기본 프롬프트와 향상된 프롬프트의 비교 결과를 저장합니다.
    
    Args:
        basic_prompt: 기본 프롬프트
        basic_result: 기본 프롬프트 결과
        enhanced_prompt: 향상된 프롬프트
        enhanced_result: 향상된 프롬프트 결과
        topic: 주제
        filename: 파일 이름 (없으면 자동 생성)
        calling_file: 호출 파일 경로 (없으면 호출 스택에서 추출)
        
    Returns:
        저장된 파일의 절대 경로
    """
    # 호출 파일이 제공되지 않으면 호출 스택에서 추출
    if calling_file is None:
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    # 파일 이름이 제공되지 않으면 주제에서 생성
    if filename is None:
        safe_topic = topic.replace(' ', '_').lower()
        filename = f"comparison_{safe_topic}.md"
    
    # 비교 내용 생성
    comparison_content = f"""# {topic} 프롬프트 비교

## 기본 프롬프트
```
{basic_prompt}
```

## 향상된 프롬프트
```
{enhanced_prompt}
```

## 기본 프롬프트 결과
{basic_result}

## 향상된 프롬프트 결과
{enhanced_result}

## 주요 개선점
1. **맥락 제공**: 목적과 활용 방법 명시
2. **구체적 지시사항**: 세부 요청 추가
3. **출력 형식 지정**: 원하는 형식과 구조 요청

## 효과
향상된 프롬프트는 더 구체적이고 맥락에 맞는 응답을 생성합니다.
기본 프롬프트는 일반적인 정보를 제공하는 반면, 향상된 프롬프트는
실제 사용 목적에 맞는 구조화된 정보를 제공합니다.
"""
    
    # 결과 저장 - calling_file 전달
    save_path = get_chapter_save_path(calling_file)
    
    # 전체 파일 경로
    file_path = os.path.join(save_path, filename)
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(comparison_content)
    
    print(f"결과가 저장되었습니다: {file_path}")
    return file_path

def save_results(
    topic: str,
    basic_prompt: str,
    basic_result: str,
    enhanced_prompt: str,
    enhanced_result: str,
    calling_file: str = None
) -> str:
    """
    결과 저장 처리
    
    Args:
        topic: 주제
        basic_prompt: 기본 프롬프트
        basic_result: 기본 결과
        enhanced_prompt: 향상된 프롬프트
        enhanced_result: 향상된 결과
        calling_file: 호출 파일 경로 (없으면 호출 스택에서 추출)
        
    Returns:
        결과 메시지
    """
    # 호출 파일이 제공되지 않으면 호출 스택에서 추출
    if calling_file is None:
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    # 파일명 생성
    safe_topic = topic.replace(' ', '_').lower()
    
    # 저장 경로 가져오기
    chapter_dir = get_chapter_save_path(calling_file)
    
    print(f"\n결과를 {os.path.relpath(chapter_dir, os.path.dirname(os.path.dirname(calling_file)))} 폴더에 저장합니다...")
    
    # 기본 응답 저장
    basic_filename = f"basic_{safe_topic}.md"
    basic_path = os.path.join(chapter_dir, basic_filename)
    with open(basic_path, 'w', encoding='utf-8') as f:
        f.write(f"# {topic} - 기본 프롬프트 결과\n\n{basic_result}")
    print(f"기본 응답이 저장되었습니다.")
    
    # 향상된 응답 저장
    enhanced_filename = f"enhanced_{safe_topic}.md"
    enhanced_path = os.path.join(chapter_dir, enhanced_filename)
    with open(enhanced_path, 'w', encoding='utf-8') as f:
        f.write(f"# {topic} - 향상된 프롬프트 결과\n\n{enhanced_result}")
    print(f"향상된 응답이 저장되었습니다.")
    
    # 비교 내용 저장 - calling_file 전달
    comparison_filename = f"comparison_{safe_topic}.md"
    save_comparison(
        basic_prompt, 
        basic_result, 
        enhanced_prompt, 
        enhanced_result, 
        topic, 
        comparison_filename,
        calling_file
    )
    print(f"프롬프트 비교가 저장되었습니다.")
    
    return f"{topic} 관련 결과가 {chapter_dir} 디렉토리에 저장되었습니다."