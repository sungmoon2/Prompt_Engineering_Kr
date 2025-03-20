"""
응답 포맷팅 모듈

AI 응답을 다양한 형식으로 변환하고 구조화하는 기능을 제공합니다.
"""

import re
import json
from typing import Dict, List, Any, Union, Optional, Tuple

def format_response(response: str, format_type: str = "markdown") -> str:
    """
    AI 응답을 지정된 형식으로 변환
    
    Args:
        response: AI 응답 텍스트
        format_type: 변환할 형식 (markdown, plain, html)
        
    Returns:
        변환된 응답 텍스트
    """
    # 마크다운 형식 - 일부 정리
    if format_type == "markdown":
        # 코드 블록이 제대로 닫히지 않은 경우 처리
        if response.count("```") % 2 == 1:
            response += "\n```"
        return response
    
    # 일반 텍스트 형식 - 마크다운 제거
    elif format_type == "plain":
        # 코드 블록 제거
        plain_text = re.sub(r'```.*?\n', '', response)
        plain_text = re.sub(r'```', '', plain_text)
        
        # 헤딩 기호 제거
        plain_text = re.sub(r'^\s*#{1,6}\s+', '', plain_text, flags=re.MULTILINE)
        
        # 굵게, 기울임 제거
        plain_text = re.sub(r'\*\*(.*?)\*\*', r'\1', plain_text)
        plain_text = re.sub(r'\*(.*?)\*', r'\1', plain_text)
        
        # 링크 텍스트만 남기기
        plain_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', plain_text)
        
        return plain_text
    
    # HTML 형식
    elif format_type == "html":
        import markdown
        return markdown.markdown(response)
    
    # 지원하지 않는 형식
    else:
        return response


def extract_sections(response: str) -> Dict[str, str]:
    """
    마크다운 응답에서 섹션 추출
    
    Args:
        response: 마크다운 형식의 응답
        
    Returns:
        섹션 제목과 내용의 딕셔너리
    """
    # 제목 패턴: # 제목, ## 제목 등
    section_pattern = r'^(#{1,6})\s+(.+?)\s*$'
    
    # 응답을 줄 단위로 분할
    lines = response.split('\n')
    
    sections = {}
    current_section = "intro"  # 첫 번째 섹션 이전의 내용을 위한 기본 키
    current_content = []
    
    for line in lines:
        # 섹션 제목 라인인지 확인
        match = re.match(section_pattern, line)
        
        if match:
            # 현재까지 수집된 내용을 이전 섹션에 저장
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
                current_content = []
            
            # 새 섹션 시작
            current_section = match.group(2)
        else:
            # 내용 라인 추가
            current_content.append(line)
    
    # 마지막 섹션 내용 저장
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def extract_code_blocks(response: str, language: Optional[str] = None) -> List[str]:
    """
    마크다운 응답에서 코드 블록 추출
    
    Args:
        response: 마크다운 형식의 응답
        language: 특정 언어 코드 블록만 추출 (선택사항)
        
    Returns:
        추출된 코드 블록 목록
    """
    if language:
        # 특정 언어 코드 블록 패턴
        pattern = rf'```{language}(.*?)```'
    else:
        # 모든 코드 블록 패턴
        pattern = r'```(?:\w+)?(.*?)```'
    
    # 코드 블록 추출
    matches = re.finditer(pattern, response, re.DOTALL)
    code_blocks = [match.group(1).strip() for match in matches]
    
    return code_blocks


def extract_json(response: str) -> Dict[str, Any]:
    """
    응답에서 JSON 데이터 추출
    
    Args:
        response: JSON 형식이 포함된 응답 텍스트
        
    Returns:
        추출된 JSON 데이터 (딕셔너리)
    """
    # JSON 코드 블록 패턴
    json_pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
    
    # JSON 블록 찾기
    match = re.search(json_pattern, response)
    if match:
        json_str = match.group(1).strip()
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"JSON 파싱 오류: {e}")
    
    # JSON 코드 블록이 없으면 전체 텍스트를 JSON으로 파싱 시도
    try:
        return json.loads(response.strip())
    except json.JSONDecodeError:
        # 실패하면 빈 딕셔너리 반환
        return {}


def extract_list_items(response: str) -> List[str]:
    """
    응답에서 목록 항목 추출
    
    Args:
        response: 목록이 포함된 응답 텍스트
        
    Returns:
        추출된 목록 항목
    """
    # 불릿 목록 또는 번호 목록 패턴
    list_pattern = r'^\s*(?:[-*+]|\d+\.)\s+(.*?)'
    
    items = []
    for line in response.split('\n'):
        match = re.match(list_pattern, line)
        if match:
            items.append(match.group(1).strip())
    
    return items


def extract_table(response: str) -> List[Dict[str, str]]:
    """
    마크다운 응답에서 테이블 추출
    
    Args:
        response: 마크다운 테이블이 포함된 응답 텍스트
        
    Returns:
        추출된 테이블 데이터 (행 기준 딕셔너리 목록)
    """
    # 테이블 패턴 (헤더 행, 구분 행, 데이터 행)
    table_pattern = r'\|(.+?)\|\s*\n\|(?:[-:]+\|)+\s*\n((?:\|.+?\|\s*\n)+)'
    
    match = re.search(table_pattern, response, re.DOTALL)
    if not match:
        return []
    
    # 헤더 추출 및 처리
    header_row = match.group(1)
    headers = [h.strip() for h in header_row.split('|') if h.strip()]
    
    # 데이터 행 추출 및 처리
    data_rows = match.group(2).strip().split('\n')
    
    result = []
    for row in data_rows:
        values = [v.strip() for v in row.split('|') if v.strip()]
        if len(values) == len(headers):
            row_dict = {headers[i]: values[i] for i in range(len(headers))}
            result.append(row_dict)
    
    return result


def format_as_table(data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
    """
    데이터를 마크다운 테이블 형식으로 변환
    
    Args:
        data: 행 기준 딕셔너리 목록
        headers: 테이블 헤더 목록 (없으면 첫 행 키 사용)
        
    Returns:
        마크다운 테이블 형식 문자열
    """
    if not data:
        return ""
    
    # 헤더가 지정되지 않으면 첫 행의 키 사용
    if not headers:
        headers = list(data[0].keys())
    
    # 테이블 헤더 행
    table = "| " + " | ".join(headers) + " |\n"
    
    # 구분 행
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    
    # 데이터 행
    for row in data:
        values = [str(row.get(h, "")) for h in headers]
        table += "| " + " | ".join(values) + " |\n"
    
    return table