"""
실습 스크립트 생성 모듈

실습 챕터를 위한 파일 및 코드 템플릿을 생성하는 기능을 제공합니다.
"""

import os
import re
from typing import Dict, List, Any, Optional

def generate_script_template(chapter_id: str, title: str, description: str = "") -> str:
    """
    실습 스크립트 템플릿 생성
    
    Args:
        chapter_id: 챕터 ID (예: 1.1.1)
        title: 챕터 제목
        description: 챕터 설명 (선택사항)
        
    Returns:
        스크립트 템플릿 문자열
    """
    if not description:
        description = f"{title} 실습 코드"
    
    # 파일명에 사용할 스네이크 케이스 변환
    safe_title = title.lower()
    safe_title = re.sub(r'[^\w\s]', '', safe_title)  # 특수문자 제거
    safe_title = re.sub(r'\s+', '_', safe_title)     # 공백을 언더스코어로 변환
    
    # 챕터 ID에서 숫자만 추출하여 점으로 구분
    chapter_nums = re.findall(r'\d+', chapter_id)
    chapter_path = '.'.join(chapter_nums)
    
    template = f'''"""
{title} 실습 모듈

{description}
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import write_file, save_markdown
from utils.templates import get_template

def main():
    """
    실습 코드 메인 함수
    """
    print(f"===== {title} =====")
    print(f"{description}\\n")
    
    # 사용자 입력 받기
    topic = input("주제를 입력하세요: ")
    
    # 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role("전문 조언자")
    prompt_builder.add_context(f"주제: {topic}")
    prompt_builder.add_instructions([
        "주제를 분석하고 핵심 요소를 파악해주세요",
        "논리적인 구조를 제안해주세요",
        "효과적인 전개 방법을 제시해주세요"
    ])
    
    prompt = prompt_builder.build()
    
    # AI 응답 요청
    print("\\n분석 중...")
    response = get_completion(prompt)
    
    # 결과 출력
    print("\\n=== 분석 결과 ===")
    print(response)
    
    # 결과 저장
    save_path = f"results/chapter_{chapter_path}_{safe_title}.md"
    save_markdown(response, save_path, title=f"{title}: {topic}")
    print(f"\\n결과가 '{save_path}'에 저장되었습니다.")


if __name__ == "__main__":
    main()
'''
    
    return template


def create_chapter_script(chapter_id: str, title: str, description: str = "", base_dir: str = None) -> str:
    """
    챕터 실습 스크립트 파일 생성
    
    Args:
        chapter_id: 챕터 ID (예: 1.1.1)
        title: 챕터 제목
        description: 챕터 설명 (선택사항)
        base_dir: 기본 디렉토리 (없으면 현재 디렉토리)
        
    Returns:
        생성된 파일 경로
    """
    # 기본 디렉토리 설정
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 챕터 ID 분석하여 디렉토리 구조 생성
    parts = chapter_id.split('.')
    if len(parts) >= 1:
        chapter_dir = os.path.join(base_dir, f"chapter{parts[0]}")
        os.makedirs(chapter_dir, exist_ok=True)
    else:
        chapter_dir = base_dir
    
    # 파일명 생성
    safe_title = title.lower()
    safe_title = re.sub(r'[^\w\s]', '', safe_title)
    safe_title = re.sub(r'\s+', '_', safe_title)
    
    # 챕터 번호 포맷팅
    chapter_num = '_'.join(parts)
    file_name = f"{chapter_num}_{safe_title}.py"
    file_path = os.path.join(chapter_dir, file_name)
    
    # 템플릿 생성
    template = generate_script_template(chapter_id, title, description)
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return file_path


def create_project_structure(chapters_info: List[Dict[str, str]], base_dir: str = None) -> Dict[str, str]:
    """
    전체 프로젝트 구조 생성
    
    Args:
        chapters_info: 챕터 정보 목록 (chapter_id, title, description 키 포함)
        base_dir: 기본 디렉토리 (없으면 현재 디렉토리)
        
    Returns:
        생성된 파일 경로 딕셔너리
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 필요한 디렉토리 생성
    os.makedirs(os.path.join(base_dir, "results"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "examples"), exist_ok=True)
    
    # 각 챕터 스크립트 생성
    created_files = {}
    
    for chapter in chapters_info:
        chapter_id = chapter.get("chapter_id")
        title = chapter.get("title")
        description = chapter.get("description", "")
        
        if chapter_id and title:
            file_path = create_chapter_script(chapter_id, title, description, base_dir)
            created_files[chapter_id] = file_path
    
    return created_files