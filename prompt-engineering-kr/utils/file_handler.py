"""
파일 입출력 모듈

다양한 형식의 파일 읽기, 쓰기 및 변환 기능을 제공합니다.
"""

import os
import json
import csv
import inspect
import re
from typing import Dict, List, Any, Union, Optional, Tuple

def read_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    파일 읽기 함수
    
    Args:
        file_path: 파일 경로
        encoding: 파일 인코딩
        
    Returns:
        파일 내용
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()


def write_file(content: str, file_path: str, encoding: str = 'utf-8') -> None:
    """
    파일 쓰기 함수
    
    Args:
        content: 저장할 내용
        file_path: 저장할 파일 경로
        encoding: 파일 인코딩
    """
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(content)


def read_json(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    JSON 파일 읽기 함수
    
    Args:
        file_path: 파일 경로
        encoding: 파일 인코딩
        
    Returns:
        JSON 객체
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)


def write_json(data: Dict[str, Any], file_path: str, 
              encoding: str = 'utf-8', indent: int = 2) -> None:
    """
    JSON 파일 쓰기 함수
    
    Args:
        data: 저장할 데이터
        file_path: 저장할 파일 경로
        encoding: 파일 인코딩
        indent: JSON 들여쓰기
    """
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def read_csv(file_path: str, encoding: str = 'utf-8') -> List[Dict[str, str]]:
    """
    CSV 파일 읽기 함수
    
    Args:
        file_path: 파일 경로
        encoding: 파일 인코딩
        
    Returns:
        CSV 데이터 (행 기준 딕셔너리 목록)
    """
    data = []
    with open(file_path, 'r', encoding=encoding, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(dict(row))
    return data


def write_csv(data: List[Dict[str, Any]], file_path: str, 
             encoding: str = 'utf-8') -> None:
    """
    CSV 파일 쓰기 함수
    
    Args:
        data: 저장할 데이터 (행 기준 딕셔너리 목록)
        file_path: 저장할 파일 경로
        encoding: 파일 인코딩
    """
    if not data:
        raise ValueError("데이터가 비어 있습니다.")
    
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    fieldnames = data[0].keys()
    with open(file_path, 'w', encoding=encoding, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def get_chapter_info(calling_file: str = None) -> Tuple[Optional[str], str, str]:
    """
    실행 중인 파일의 챕터 정보를 추출합니다.
    
    Args:
        calling_file: 호출 파일 경로 (기본값은 호출 스택에서 추출)
        
    Returns:
        튜플 (챕터 ID, 챕터 이름, 프로젝트 루트 경로)
    """
    # 호출 파일이 제공되지 않으면 스택에서 추출
    if calling_file is None:
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    # 파일 경로 정규화
    file_path = os.path.abspath(calling_file)
    file_basename = os.path.basename(file_path)
    
    # 기본값 설정
    chapter_id = None
    chapter_name = "unknown"
    
    # 프로젝트 루트 찾기
    project_root = os.path.dirname(file_path)
    while project_root and os.path.basename(project_root).lower() != 'prompt-engineering-kr':
        parent = os.path.dirname(project_root)
        if parent == project_root:  # 루트에 도달
            break
        project_root = parent
    
    # 파일 이름 패턴에서 챕터 ID와 이름 추출
    # 패턴 1: 1.1_clear_instructions.py
    match = re.match(r'^(\d+\.\d+)_(.+?)\.py$', file_basename)
    if match:
        chapter_id = match.group(1)
        chapter_name = match.group(2)
    # 패턴 2: 1.1.1_specific_requests.py
    elif re.match(r'^(\d+\.\d+\.\d+)_(.+?)\.py$', file_basename):
        match = re.match(r'^(\d+\.\d+\.\d+)_(.+?)\.py$', file_basename)
        chapter_id = match.group(1)
        chapter_name = match.group(2)
    # 패턴 3: 경로에서 추출 (예: /exercises/part1/1.1/)
    elif not chapter_id:
        normalized_path = file_path.replace('\\', '/')
        match = re.search(r'/exercises/part\d+/(\d+\.\d+)/', normalized_path)
        if match:
            chapter_id = match.group(1)
            # 챕터 이름은 파일명에서 가져옴
            chapter_name = os.path.splitext(file_basename)[0]
    
    return (chapter_id, chapter_name, project_root)

def get_chapter_results_dir(calling_file: str = None) -> str:
    """
    실행 중인 파일의 챕터 기반 결과 디렉토리 경로를 생성합니다.
    
    Args:
        calling_file: 호출 파일 경로 (기본값은 호출 스택에서 추출)
        
    Returns:
        챕터 기반 결과 디렉토리 경로
    """
    from utils.chapter_utils import get_chapter_save_path
    
    # 호출 파일이 제공되지 않으면 스택에서 추출
    if calling_file is None:
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    # 새로운 chapter_utils 모듈의 함수 사용
    return get_chapter_save_path(calling_file)

def ensure_chapter_results_path(calling_file: str = None) -> str:
    """
    파일 경로에서 챕터 정보를 추출하고, 해당 챕터에 맞는 results 폴더 경로를 반환합니다.
    get_chapter_results_dir의 별칭입니다.
    
    Args:
        calling_file: 호출 파일 경로 (기본값은 호출 스택에서 추출)
        
    Returns:
        결과를 저장할 절대 경로
    """
    return get_chapter_results_dir(calling_file)

def get_templates_path() -> str:
    """
    템플릿 디렉토리 경로 반환
    
    Returns:
        템플릿 디렉토리 절대 경로
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'templates')


def load_template(template_name: str, encoding: str = 'utf-8') -> str:
    """
    템플릿 파일 로드 함수
    
    Args:
        template_name: 템플릿 이름
        encoding: 파일 인코딩
        
    Returns:
        템플릿 내용
    """
    template_path = os.path.join(get_templates_path(), f"{template_name}.txt")
    
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"템플릿 '{template_name}'을 찾을 수 없습니다.")
    
    return read_file(template_path, encoding)


def save_markdown(content: Union[str, Dict[str, str]], 
                 file_path: str,
                 title: Optional[str] = None,
                 encoding: str = 'utf-8',
                 use_chapter_path: bool = True) -> str:
    """
    마크다운 형식으로 저장하는 함수
    
    Args:
        content: 저장할 내용 (문자열 또는 섹션별 내용)
        file_path: 저장할 파일 경로 (절대 경로 또는 파일명)
        title: 문서 제목 (선택사항)
        encoding: 파일 인코딩
        use_chapter_path: 챕터 기반 경로 사용 여부 (기본값: True)
        
    Returns:
        저장된 파일의 절대 경로
    """
    from utils.chapter_utils import get_chapter_save_path
    
    # 문자열인 경우 그대로 저장
    if isinstance(content, str):
        markdown_content = content
        if title:
            markdown_content = f"# {title}\n\n{content}"
    
    # 딕셔너리인 경우 섹션별로 변환
    else:
        sections = []
        
        # 제목이 있으면 추가
        if title:
            sections.append(f"# {title}\n")
        
        # 각 섹션 추가
        for section_title, section_content in content.items():
            sections.append(f"## {section_title}\n\n{section_content}\n")
        
        markdown_content = "\n".join(sections)
    
    # 파일 경로 처리
    if use_chapter_path:
        # 호출자 스택에서 호출 파일 가져오기
        frame = inspect.stack()[1]
        caller_file = frame.filename
        
        # 챕터 기반 결과 경로 가져오기
        chapter_results_dir = get_chapter_save_path(caller_file)
        
        # 파일명만 있는 경우 챕터 경로에 추가
        if not os.path.isabs(file_path) and '/' not in file_path and '\\' not in file_path:
            full_path = os.path.join(chapter_results_dir, file_path)
        else:
            # 이미 경로가 포함된 경우는 그대로 사용
            full_path = file_path
    else:
        # 챕터 경로를 사용하지 않는 경우
        if not os.path.isabs(file_path):
            # 상대 경로인 경우 프로젝트 루트의 results 디렉토리에 저장
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(base_dir, "results", file_path)
        else:
            # 절대 경로인 경우 그대로 사용
            full_path = file_path
    
    # 파일 확장자 확인
    if not full_path.lower().endswith('.md'):
        full_path += '.md'
    
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(full_path)), exist_ok=True)
    
    # 파일에 저장
    with open(full_path, 'w', encoding=encoding) as f:
        f.write(markdown_content)
    
    print(f"파일이 저장되었습니다: {os.path.abspath(full_path)}")
    return os.path.abspath(full_path)