"""
파일 입출력 모듈

다양한 형식의 파일 읽기, 쓰기 및 변환 기능을 제공합니다.
"""

import os
import json
import csv
from typing import Dict, List, Any, Union, Optional

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


def save_markdown(content: Union[str, Dict[str, str]], 
                 file_path: str,
                 title: Optional[str] = None,
                 encoding: str = 'utf-8') -> None:
    """
    마크다운 형식으로 저장하는 함수
    
    Args:
        content: 저장할 내용 (문자열 또는 섹션별 내용)
        file_path: 저장할 파일 경로
        title: 문서 제목 (선택사항)
        encoding: 파일 인코딩
    """
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
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
    
    # 파일에 저장
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(markdown_content)


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