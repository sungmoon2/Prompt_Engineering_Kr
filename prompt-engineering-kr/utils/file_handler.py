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
        # 호출 스택에서 호출자 파일 경로 가져오기 (프레임 1은 직접적인 호출자)
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    # 파일 경로 정규화
    file_path = os.path.abspath(calling_file)
    file_basename = os.path.basename(file_path)
    
    print(f"\n디버깅 - get_chapter_info:")
    print(f"분석 중인 파일: {file_path}")
    print(f"파일 이름: {file_basename}")
    
    # 기본값 설정
    chapter_id = None
    chapter_name = "unknown"
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        # 프로젝트 루트 찾기
        project_root_found = False
        root_path = os.path.dirname(file_path)
        while root_path and not project_root_found:
            if os.path.basename(root_path).lower() == 'prompt-engineering-kr':
                project_root = root_path
                project_root_found = True
                print(f"프로젝트 루트 찾음: {project_root}")
                break
            parent = os.path.dirname(root_path)
            if parent == root_path:  # 루트에 도달
                break
            root_path = parent
        
        if not project_root_found:
            print(f"프로젝트 루트를 찾지 못했습니다. 기본값 사용: {project_root}")
        
        # 1. 파일 이름 패턴 1: 1.1_clear_instructions.py
        pattern1 = r'^(\d+\.\d+)_(.+)\.py$'
        match1 = re.match(pattern1, file_basename)
        if match1:
            chapter_id = match1.group(1)
            chapter_name = match1.group(2)
            print(f"패턴 1 매치: chapter_id={chapter_id}, chapter_name={chapter_name}")
        
        # 2. 파일 이름 패턴 2: 1.1.1_specific_requests.py
        pattern2 = r'^(\d+\.\d+\.\d+)_(.+)\.py$'
        match2 = re.match(pattern2, file_basename)
        if match2:
            chapter_id = match2.group(1)
            chapter_name = match2.group(2)
            print(f"패턴 2 매치: chapter_id={chapter_id}, chapter_name={chapter_name}")
        
        # 3. 파일 경로에서 챕터 정보 추출
        if chapter_id is None:
            normalized_path = file_path.replace('\\', '/')
            print(f"정규화된 경로: {normalized_path}")
            
            # 패턴: exercises/part1/1.1/
            pattern3 = r'/exercises/part\d+/(\d+\.\d+)/'
            match3 = re.search(pattern3, normalized_path)
            if match3:
                chapter_id = match3.group(1)
                # 챕터 이름은 파일명에서 가져옴
                chapter_name = os.path.splitext(file_basename)[0]
                print(f"패턴 3 매치: chapter_id={chapter_id}, chapter_name={chapter_name}")
                
                # 챕터 이름에서 숫자 접두사 제거 (예: 1.1_clear_instructions -> clear_instructions)
                name_pattern = r'^\d+\.\d+(?:\.\d+)?_(.+)$'
                name_match = re.match(name_pattern, chapter_name)
                if name_match:
                    chapter_name = name_match.group(1)
                    print(f"이름 패턴 매치: chapter_name={chapter_name}")
        
        # 4. 디렉토리 이름에서 챕터 정보 추출
        if chapter_id is None:
            dir_name = os.path.basename(os.path.dirname(file_path))
            print(f"디렉토리 이름: {dir_name}")
            
            # 디렉토리 이름이 챕터 형식인지 확인 (예: 1.1)
            if re.match(r'^\d+\.\d+$', dir_name):
                chapter_id = dir_name
                print(f"디렉토리 이름 매치: chapter_id={chapter_id}")
                
                # 챕터 이름은 파일명에서 가져옴
                file_base = os.path.basename(file_path)
                base_name = os.path.splitext(file_base)[0]
                
                # 파일 이름에 챕터 ID가 포함된 경우 제거 (예: 1.1_clear_instructions.py)
                name_pattern = rf'^{chapter_id}_(.+)$'
                name_match = re.match(name_pattern, base_name)
                if name_match:
                    chapter_name = name_match.group(1)
                else:
                    chapter_name = base_name
                print(f"파일 이름에서 챕터 이름 추출: chapter_name={chapter_name}")
        
        # 5. 하드코딩된 매핑 사용 (최후의 수단)
        if chapter_id is None:
            # 알려진 파일 이름을 기반으로 매핑
            known_files = {
                "1.1_clear_instructions.py": ("1.1", "clear_instructions"),
                "1.1.1_specific_requests.py": ("1.1.1", "specific_requests"),
                "1.1.2_key_questions.py": ("1.1.2", "key_questions"),
                "1.1.3_concrete_terms.py": ("1.1.3", "concrete_terms"),
                # 필요한 만큼 추가
            }
            
            if file_basename in known_files:
                chapter_id, chapter_name = known_files[file_basename]
                print(f"하드코딩된 매핑 사용: chapter_id={chapter_id}, chapter_name={chapter_name}")
    
    except Exception as e:
        print(f"챕터 정보 추출 중 오류 발생: {e}")
    
    print(f"최종 결과: chapter_id={chapter_id}, chapter_name={chapter_name}, project_root={project_root}")
    return (chapter_id, chapter_name, project_root)

def get_chapter_results_dir(calling_file: str = None) -> str:
    """
    실행 중인 파일의 챕터 기반 결과 디렉토리 경로를 생성합니다.
    
    Args:
        calling_file: 호출 파일 경로 (기본값은 호출 스택에서 추출)
        
    Returns:
        챕터 기반 결과 디렉토리 경로
    """
    # 설정에서 챕터별 폴더 사용 여부 확인
    from utils.config import get_setting
    use_chapter_folders = get_setting('output.use_chapter_folders', True)
    
    # 호출 파일이 제공되지 않으면 스택에서 추출
    if calling_file is None:
        # 호출 스택에서 호출자 파일 경로 가져오기
        frame = inspect.stack()[1]
        calling_file = frame.filename
    
    print(f"\n디버깅 - get_chapter_results_dir:")
    print(f"호출 파일: {calling_file}")
    print(f"챕터별 폴더 사용: {use_chapter_folders}")
    
    # 챕터 정보 가져오기
    chapter_id, chapter_name, project_root = get_chapter_info(calling_file)
    
    # 결과 디렉토리 경로
    if use_chapter_folders and chapter_id:
        # 파일 이름에서 파트 번호 추출
        part_match = None
        if chapter_id and '.' in chapter_id:
            part_num = chapter_id.split('.')[0]
            part_match = part_num
            print(f"파트 번호 추출: {part_num}")
        
        # 새로운 폴더 구조: results/part{part_num}/{chapter_id}
        if part_match:
            part_path = f"part{part_match}"
            
            # 챕터 ID에 마침표 포함 (예: 1.1 또는 1.1.1)
            if '.' in chapter_id:
                # 챕터 ID 분석
                parts = chapter_id.split('.')
                
                if len(parts) == 2:  # 예: 1.1
                    # results/part1/1.1
                    results_dir = os.path.join(project_root, "results", part_path, chapter_id)
                    print(f"기본 챕터 경로: {results_dir}")
                elif len(parts) == 3:  # 예: 1.1.1
                    # 상위 챕터 경로: results/part1/1.1
                    parent_chapter = f"{parts[0]}.{parts[1]}"
                    # 전체 경로: results/part1/1.1/1.1.1
                    results_dir = os.path.join(project_root, "results", part_path, parent_chapter, chapter_id)
                    print(f"하위 챕터 경로: {results_dir}")
                else:
                    # 알 수 없는 형식: 기본 폴더 구조 사용
                    folder_name = f"{chapter_id}_{chapter_name}"
                    results_dir = os.path.join(project_root, "results", folder_name)
                    print(f"알 수 없는 챕터 형식, 기본 폴더 사용: {results_dir}")
            else:
                # 챕터 ID에 마침표가 없는 경우: 기본 폴더 구조 사용
                folder_name = f"{chapter_id}_{chapter_name}"
                results_dir = os.path.join(project_root, "results", folder_name)
                print(f"마침표 없는 챕터 ID, 기본 폴더 사용: {results_dir}")
        else:
            # 파트 번호 추출 실패: 기본 폴더 구조 사용
            folder_name = f"{chapter_id}_{chapter_name}"
            results_dir = os.path.join(project_root, "results", folder_name)
            print(f"파트 번호 추출 실패, 기본 폴더 사용: {results_dir}")
    else:
        # 챕터 정보가 없거나 챕터별 폴더 사용하지 않음: 기본 results 디렉토리 사용
        results_dir = os.path.join(project_root, "results")
        print(f"챕터 정보 없음 또는 챕터별 폴더 미사용, 기본 폴더 사용: {results_dir}")
    
    # 디렉토리가 없으면 생성
    os.makedirs(results_dir, exist_ok=True)
    
    print(f"최종 결과 디렉토리: {results_dir}")
    return results_dir

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
        chapter_results_dir = get_chapter_results_dir(caller_file)
        
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


def save_result(content: Union[str, Dict[str, str]], 
                filename: str,
                title: Optional[str] = None,
                encoding: str = 'utf-8',
                chapter_id: Optional[str] = None,
                chapter_name: Optional[str] = None) -> str:
    """
    결과 파일을 챕터별 폴더에 저장하는 간편 함수
    
    Args:
        content: 저장할 내용 (문자열 또는 섹션별 내용)
        filename: 저장할 파일 이름 (확장자 포함)
        title: 문서 제목 (선택사항)
        encoding: 파일 인코딩
        chapter_id: 챕터 ID (수동 지정 시)
        chapter_name: 챕터 이름 (수동 지정 시)
        
    Returns:
        저장된 파일의 절대 경로
    """
    # 호출자 스택에서 호출 파일 가져오기
    frame = inspect.stack()[1]
    caller_file = frame.filename
    
    # 챕터 정보가 수동으로 제공되었는지 확인
    if chapter_id and chapter_name:
        # 프로젝트 루트 경로 가져오기
        _, _, project_root = get_chapter_info(caller_file)
        
        # 결과 디렉토리 구성
        folder_name = f"{chapter_id}_{chapter_name}"
        results_dir = os.path.join(project_root, "results", folder_name)
    else:
        # 자동으로 챕터 기반 결과 경로 가져오기
        results_dir = get_chapter_results_dir(caller_file)
    
    # 파일 확장자 확인
    if not filename.endswith(('.md', '.txt', '.json', '.csv')):
        filename += '.md'  # 기본값으로 마크다운 확장자 추가
    
    # 전체 경로 구성
    full_path = os.path.join(results_dir, filename)
    
    # 내용 처리
    if isinstance(content, str):
        file_content = content
        if title and filename.endswith('.md'):
            file_content = f"# {title}\n\n{content}"
    else:
        # 딕셔너리인 경우 섹션별로 변환 (마크다운 형식)
        if filename.endswith('.md'):
            sections = []
            if title:
                sections.append(f"# {title}\n")
            for section_title, section_content in content.items():
                sections.append(f"## {section_title}\n\n{section_content}\n")
            file_content = "\n".join(sections)
        elif filename.endswith('.json'):
            import json
            file_content = json.dumps(content, ensure_ascii=False, indent=2)
        else:
            # 기본적으로 문자열로 변환
            file_content = str(content)
    
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(os.path.abspath(full_path)), exist_ok=True)
    
    # 파일에 저장
    with open(full_path, 'w', encoding=encoding) as f:
        f.write(file_content)
    
    print(f"파일이 저장되었습니다: {os.path.abspath(full_path)}")
    return os.path.abspath(full_path)