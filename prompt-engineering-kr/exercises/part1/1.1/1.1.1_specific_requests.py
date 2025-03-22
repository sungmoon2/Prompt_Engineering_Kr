"""
구체적인 요청 작성하기 실습 모듈

Part 1 - 섹션 1.1.1 실습 코드: 명확하고 구체적인 요청을 통해 
정확한 응답을 얻는 방법을 학습합니다.
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
SPECIFIC_REQUEST_TOPICS = {
    "1": {
        "name": "데이터 분석 요약", 
        "topic": "월별 판매 데이터 분석 요약", 
        "output_format": "보고서"
    },
    "2": {
        "name": "코드 작성 요청", 
        "topic": "웹 스크래핑 스크립트 작성", 
        "output_format": "Python 코드"
    },
    "3": {
        "name": "문서 요약 요청", 
        "topic": "연구 논문 요약", 
        "output_format": "주요 포인트"
    },
    "4": {
        "name": "계획 수립 요청", 
        "topic": "개인 재무 계획", 
        "output_format": "단계별 가이드"
    },
    "5": {
        "name": "문제 해결 요청", 
        "topic": "온라인 학습 참여도 향상 방안", 
        "output_format": "해결책 목록"
    }
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["단순 질문이나 모호한 요청"],
    "enhanced": [
        "정확한 목표 명시: 무엇을 달성하려는지 명확하게 표현",
        "세부 조건 제시: 원하는 세부 조건을 구체적으로 명시",
        "예시 및 제한사항 추가: 예시와 제한사항을 통해 원하는 방향 명확화",
        "형식 및 길이 지정: 원하는 출력 형식과 길이를 명확하게 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "모호한 요청보다 구체적인 요청이 더 정확한 응답을 이끌어냅니다",
    "목표와 의도를 명확히 하면 AI가 맥락을 더 잘 이해합니다",
    "필요한 세부 사항과 제한사항을 명시하면 불필요한 정보가 줄어듭니다",
    "원하는 출력 형식과 길이를 지정하면 후속 처리가 용이해집니다",
    "구체적인 예시를 제공하면 원하는 스타일과 접근 방식이 더 잘 전달됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 정확한 목표 명시
    builder.add_context(
        f"저는 {purpose}을 위해 {topic}에 대한 정보가 필요합니다. "
        f"이 {output_format}은 전문가가 아닌 일반인도 이해할 수 있는 수준이어야 합니다."
    )
    
    # 세부 조건 제시
    if "데이터 분석" in topic:
        builder.add_instructions([
            "월별 추세와 계절적 패턴을 반드시 포함해주세요",
            "최소 3가지 이상의 핵심 인사이트를 도출해주세요",
            "데이터 기반 의사결정을 위한 제안을 2-3개 포함해주세요",
            "시각적 그래프나 차트를 설명하는 방식으로 표현해주세요",
            "전문 용어는 괄호 안에 간단한 설명을 추가해주세요"
        ])
    elif "코드 작성" in topic:
        builder.add_instructions([
            "Python 3.8 이상에서 동작하는 코드를 작성해주세요",
            "requests와 BeautifulSoup 라이브러리를 사용해주세요",
            "에러 처리와 재시도 로직을 포함해주세요",
            "결과를 CSV 파일로 저장하는 기능을 추가해주세요",
            "각 함수마다 docstring을 포함해 설명을 추가해주세요"
        ])
    elif "요약" in topic:
        builder.add_instructions([
            "논문의 연구 목적, 방법론, 주요 발견, 결론을 각각 구분해주세요",
            "전문 용어는 가능한 쉬운 말로 풀어서 설명해주세요",
            "연구의 한계점과 향후 연구 방향도 언급해주세요",
            "연구 결과가 실제 적용될 수 있는 분야를 2-3가지 제안해주세요",
            "500단어 이내로 요약해주세요"
        ])
    elif "계획" in topic:
        builder.add_instructions([
            "단기(3개월), 중기(1년), 장기(3-5년) 목표로 구분해주세요",
            "각 단계별로 구체적인 행동 계획을 포함해주세요",
            "재무 건전성을 평가할 수 있는 지표와 기준을 제시해주세요",
            "일반적인 함정이나 실수를 피하는 방법도 언급해주세요",
            "월별 예산 계획 템플릿도 추가해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 구체적이고 실행 가능한 방안을 제시해주세요",
            "각 방안의 장점과 단점을 함께 설명해주세요",
            "실제 적용 사례나 예시를 포함해주세요",
            "리소스나 비용 측면에서의 고려사항도 언급해주세요",
            "구현 난이도를 상/중/하로 표시해주세요"
        ])
    
    # 예시 및 제한사항 추가
    builder.add_context(
        "다음과 같은 형식으로 작성해주세요:\n"
        "1. 개요: 전체 내용의 요약\n"
        "2. 주요 내용: 핵심 정보 및 세부사항\n"
        "3. 적용 방안: 구체적인 활용 방법\n"
        "4. 참고사항: 추가 고려사항이나 조언\n\n"
        "너무 이론적이거나 학술적인 내용은 최소화하고, 실질적으로 활용할 수 있는 정보에 중점을 두어주세요."
    )
    
    # 형식 및 길이 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 마크다운을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"전체 길이는 800~1000단어 정도로, 너무 길지 않게 작성해주세요."
    )
    
    return builder.build()

def save_to_chapter_folder(content, filename, title=None, chapter_id=None, chapter_name=None):
    """
    결과를 챕터별 폴더에 저장하는 간단한 함수
    
    Args:
        content (str): 저장할 내용
        filename (str): 파일명
        title (str, optional): 문서 제목
        chapter_id (str, optional): 챕터 ID (없으면 경로에서 추출)
        chapter_name (str, optional): 챕터 이름 (없으면 파일명에서 추출)
    
    Returns:
        str: 저장된 파일 경로
    """
    # 프로젝트 루트 찾기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 챕터 ID가 제공되지 않은 경우 경로에서 추출
    if not chapter_id:
        # 경로에서 챕터 ID 추출 시도
        dir_path = current_dir.replace('\\', '/')
        
        # exercises/part1/1.1/ 형태에서 추출
        match = re.search(r'/exercises/part\d+/(\d+\.\d+)/', dir_path)
        if match:
            chapter_id = match.group(1)
        else:
            # 마지막 디렉토리가 숫자 형식인지 확인
            last_dir = os.path.basename(current_dir)
            if re.match(r'^\d+\.\d+$', last_dir):
                chapter_id = last_dir
            else:
                # 기본값
                chapter_id = "1.1.1"
    
    # 챕터 이름이 제공되지 않은 경우 기본값 사용
    if not chapter_name:
        chapter_name = "specific_requests"
    
    # 결과 디렉토리 경로 생성
    folder_name = f"{chapter_id}_{chapter_name}"
    results_dir = os.path.join(project_root, "results", folder_name)
    
    # 디렉토리가 없으면 생성
    os.makedirs(results_dir, exist_ok=True)
    
    # 파일 확장자 확인
    if not filename.endswith(('.md', '.txt', '.json', '.csv')):
        filename += '.md'
    
    # 파일 경로 생성
    file_path = os.path.join(results_dir, filename)
    
    # 내용에 제목 추가 (마크다운인 경우)
    if title and filename.endswith('.md'):
        content = f"# {title}\n\n{content}"
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"결과가 저장되었습니다: {file_path}")
    return file_path

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    result = run_exercise(
        title="구체적인 요청 작성하기",
        topic_options=SPECIFIC_REQUEST_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 직접 챕터 폴더를 생성하고 결과 저장
    if result:
        save_to_chapter_folder(
            content=result,
            filename="specific_requests_result.md",
            title="구체적인 요청 작성하기 실습 결과",
            chapter_id="1.1.1"
        )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")