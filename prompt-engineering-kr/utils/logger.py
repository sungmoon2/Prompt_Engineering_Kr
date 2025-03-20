"""
로깅 모듈

프롬프트 및 응답 로깅을 위한 기능을 제공합니다.
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional

from .config import get_setting

# 로거 객체
_logger = None

def setup_logger() -> logging.Logger:
    """
    로거 설정
    
    Returns:
        설정된 로거 객체
    """
    global _logger
    
    # 이미 설정된 로거가 있으면 반환
    if _logger is not None:
        return _logger
    
    # 로깅 설정 로드
    enabled = get_setting('logging.enabled', True)
    log_level = get_setting('logging.log_level', 'INFO')
    log_file = get_setting('logging.log_file', 'prompt_engineering.log')
    
    # 로깅이 비활성화되어 있으면 NullHandler 사용
    if not enabled:
        _logger = logging.getLogger('prompt_engineering')
        _logger.addHandler(logging.NullHandler())
        return _logger
    
    # 로그 레벨 문자열을 상수로 변환
    level_map = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    level = level_map.get(log_level.upper(), logging.INFO)
    
    # 로그 파일 경로 설정
    if not os.path.isabs(log_file):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_file = os.path.join(base_dir, log_file)
    
    # 로그 디렉토리 생성
    os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)
    
    # 로거 설정
    _logger = logging.getLogger('prompt_engineering')
    _logger.setLevel(level)
    
    # 파일 핸들러 설정
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)
    
    # 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # 포맷터 설정
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 핸들러 추가
    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)
    
    return _logger


def get_logger() -> logging.Logger:
    """
    로거 객체 가져오기
    
    Returns:
        로거 객체
    """
    if _logger is None:
        return setup_logger()
    return _logger


def log_prompt(prompt: str, metadata: Optional[Dict[str, Any]] = None) -> str:
    """
    프롬프트 로깅
    
    Args:
        prompt: 프롬프트 텍스트
        metadata: 추가 메타데이터
        
    Returns:
        프롬프트 ID
    """
    logger = get_logger()
    
    # 프롬프트 ID 생성 (타임스탬프 기반)
    prompt_id = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # 메타데이터 준비
    if metadata is None:
        metadata = {}
    
    metadata.update({
        'prompt_id': prompt_id,
        'timestamp': datetime.now().isoformat(),
        'length': len(prompt)
    })
    
    # 로그 메시지 작성
    log_message = f"프롬프트 전송 [ID: {prompt_id}]: {prompt[:100]}..."
    logger.info(log_message)
    
    # 상세 로깅 (JSON 파일)
    if get_setting('logging.save_prompts', True):
        try:
            log_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                'logs', 'prompts'
            )
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, f"prompt_{prompt_id}.json")
            
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'prompt': prompt,
                    'metadata': metadata
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"프롬프트 로그 파일 저장 오류: {e}")
    
    return prompt_id


def log_response(prompt_id: str, response: str, metadata: Optional[Dict[str, Any]] = None) -> None:
    """
    응답 로깅
    
    Args:
        prompt_id: 프롬프트 ID
        response: 응답 텍스트
        metadata: 추가 메타데이터
    """
    logger = get_logger()
    
    # 메타데이터 준비
    if metadata is None:
        metadata = {}
    
    metadata.update({
        'prompt_id': prompt_id,
        'timestamp': datetime.now().isoformat(),
        'length': len(response)
    })
    
    # 로그 메시지 작성
    log_message = f"응답 수신 [프롬프트 ID: {prompt_id}]: {response[:100]}..."
    logger.info(log_message)
    
    # 상세 로깅 (JSON 파일)
    if get_setting('logging.save_responses', True):
        try:
            log_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                'logs', 'responses'
            )
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, f"response_{prompt_id}.json")
            
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'response': response,
                    'metadata': metadata
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"응답 로그 파일 저장 오류: {e}")


def log_error(message: str, error: Optional[Exception] = None, metadata: Optional[Dict[str, Any]] = None) -> None:
    """
    오류 로깅
    
    Args:
        message: 오류 메시지
        error: 예외 객체 (선택사항)
        metadata: 추가 메타데이터 (선택사항)
    """
    logger = get_logger()
    
    # 예외 정보 추가
    if error:
        message = f"{message}: {str(error)}"
    
    # 메타데이터 추가
    if metadata:
        message = f"{message} - {json.dumps(metadata, ensure_ascii=False)}"
    
    # 로그 기록
    logger.error(message)