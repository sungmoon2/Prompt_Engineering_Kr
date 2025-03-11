"""
유틸리티 패키지 초기화 모듈

이 모듈은 utils 패키지를 Python 패키지로 인식되게 하고,
공통적으로 사용되는 유틸리티 함수들을 가져오기 쉽게 합니다.
"""

# 편의를 위한 모듈 임포트
from .api_utils import generate_text, compare_responses
from .prompt_utils import (
    format_prompt, 
    create_role_prompt, 
    create_academic_prompt, 
    create_structured_prompt,
    create_chain_of_thought_prompt,
    create_few_shot_prompt
)
from .file_utils import (
    save_result,
    save_to_markdown,
    save_to_json,
    load_text_file,
    load_json_file,
    create_comparison_report
)

# 버전 정보
__version__ = '0.1.0'