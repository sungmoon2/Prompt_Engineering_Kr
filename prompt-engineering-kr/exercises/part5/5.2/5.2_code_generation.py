"""
코드 생성과 최적화 실습 모듈

Part 5 - 섹션 5.2 실습 코드: 목적에 맞는 코드 요청과 코드 품질 향상을 위한 전략을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
CODE_TOPICS = {
    "1": {"name": "데이터 처리 함수", "topic": "CSV 데이터 처리 유틸리티 함수", "output_format": "코드 설계"},
    "2": {"name": "웹 API 클라이언트", "topic": "RESTful API 클라이언트 라이브러리", "output_format": "코드 명세"},
    "3": {"name": "데이터 구조 구현", "topic": "효율적인 사용자 정의 데이터 구조", "output_format": "코드 예제"},
    "4": {"name": "알고리즘 최적화", "topic": "텍스트 처리 알고리즘 최적화", "output_format": "코드 예제"},
    "5": {"name": "디자인 패턴 구현", "topic": "실용적인 디자인 패턴 구현", "output_format": "코드 설계"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["기본적인 코드 요청"],
    "enhanced": [
        "요구사항 명세: 구체적인 기능, 입출력, 제약조건 명시",
        "기술 스택: 언어, 프레임워크, 라이브러리 명시",
        "품질 기준: 성능, 가독성, 확장성 등 기준 명시",
        "맥락 제공: 사용 사례, 통합 방식, 테스트 케이스 포함"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 코드 생성 요청은 명확한 요구사항 명세에서 시작합니다",
    "기술 스택과 환경을 구체적으로 지정하면 더 적합한 코드를 얻을 수 있습니다",
    "코드 품질 기준을 미리 설정하면 기대에 맞는 결과물을 얻을 수 있습니다",
    "복잡한 코드는 기본 구현부터 시작하여 점진적으로 개선하는 접근법이 효과적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}를 구현하는 코드를 작성해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "소프트웨어 개발 전문가", 
        "고품질의 코드를 설계하고 구현하는 전문 개발자로, 사용자의 요구사항을 정확히 이해하고 최적의 솔루션을 제공합니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"{topic}을 개발하고 있습니다. 이 코드는 {purpose}에 사용될 예정이며, "
        f"고품질의 실용적인 구현이 필요합니다. 구체적인 요구사항과 기술 스택 기반으로 "
        f"확장 가능하고 유지보수가 용이한 코드를 작성해주세요."
    )
    
    # 주제별 맞춤 지시사항 추가
    if "데이터 처리" in topic:
        builder.add_instructions([
            "다음 요구사항에 맞는 Python 데이터 처리 유틸리티 함수를 구현해주세요:",
            
            "기능 요구사항:",
            "- CSV 파일 읽기 및 파싱 기능",
            "- 데이터 필터링 및 변환 기능",
            "- 기본 통계 계산 기능 (평균, 합계, 최대/최소 등)",
            "- 결과를 다양한 형식으로 저장하는 기능",
            
            "기술 요구사항:",
            "- Python 3.8 이상",
            "- pandas 라이브러리 사용 가능",
            "- 메모리 효율성 고려 (대용량 파일 처리)",
            "- 적절한 예외 처리",
            
            "코드 품질 요구사항:",
            "- PEP 8 스타일 가이드 준수",
            "- 함수 및 매개변수에 타입 힌팅 적용",
            "- 명확한 문서화 및 주석",
            "- 단위 테스트 포함",
            
            "예시 사용법:",
            "```python",
            "# CSV 파일에서 특정 조건의 데이터 필터링",
            "filtered_data = process_csv('data.csv', lambda row: float(row['value']) > 100)",
            "",
            "# 데이터 통계 계산",
            "stats = calculate_statistics(filtered_data, columns=['price', 'quantity'])",
            "",
            "# 결과 저장",
            "save_data(filtered_data, 'results.json', format='json')",
            "```"
        ])
    elif "API 클라이언트" in topic:
        builder.add_instructions([
            "다음 요구사항에 맞는 RESTful API 클라이언트 라이브러리를 구현해주세요:",
            
            "기능 요구사항:",
            "- HTTP 메서드 지원 (GET, POST, PUT, DELETE)",
            "- 인증 처리 (API 키, OAuth 등)",
            "- 요청/응답 직렬화 및 역직렬화",
            "- 오류 처리 및 재시도 메커니즘",
            "- 비동기 요청 지원",
            
            "기술 요구사항:",
            "- JavaScript/TypeScript 사용",
            "- Axios 또는 Fetch API 기반",
            "- Promise 및 async/await 지원",
            "- 브라우저 및 Node.js 환경 모두 지원",
            
            "코드 품질 요구사항:",
            "- TypeScript 인터페이스 정의",
            "- 모듈화된 구조",
            "- 단위 테스트 (Jest)",
            "- JSDoc 문서화",
            
            "예시 사용법:",
            "```typescript",
            "// 클라이언트 초기화",
            "const api = new ApiClient({",
            "  baseUrl: 'https://api.example.com',",
            "  apiKey: 'your-api-key'",
            "});",
            "",
            "// GET 요청",
            "const data = await api.get('/users', { params: { limit: 10 } });",
            "",
            "// POST 요청",
            "const newUser = await api.post('/users', { name: 'John', email: 'john@example.com' });",
            "```"
        ])
    elif "데이터 구조" in topic:
        builder.add_instructions([
            "다음 요구사항에 맞는 사용자 정의 데이터 구조를 구현해주세요:",
            
            "기능 요구사항:",
            "- 키-값 쌍 저장 기능",
            "- 효율적인 조회, 삽입, 삭제 연산",
            "- 키 기반 정렬 및 반복 지원",
            "- 메모리 사용 최적화",
            
            "기술 요구사항:",
            "- Java 또는 Python으로 구현",
            "- 표준 라이브러리만 사용 (외부 의존성 없음)",
            "- 제네릭 타입 지원 (Java의 경우)",
            
            "성능 요구사항:",
            "- 조회 연산: O(1) 평균 시간 복잡도",
            "- 삽입/삭제 연산: O(1) 평균 시간 복잡도",
            "- 정렬된 반복: O(n log n) 시간 복잡도",
            
            "코드 품질 요구사항:",
            "- 완전한 클래스 구현",
            "- 적절한 인터페이스 정의",
            "- 단위 테스트 포함",
            "- 상세한 문서화",
            
            "예시 사용법:",
            "```java",
            "// Java 예시",
            "CustomMap<String, Integer> map = new CustomMap<>();",
            "map.put(\"apple\", 10);",
            "map.put(\"banana\", 5);",
            "Integer count = map.get(\"apple\");  // 10 반환",
            "```",
            "또는",
            "```python",
            "# Python 예시",
            "custom_map = CustomMap()",
            "custom_map.put(\"apple\", 10)",
            "custom_map.put(\"banana\", 5)",
            "count = custom_map.get(\"apple\")  # 10 반환",
            "```"
        ])
    elif "알고리즘 최적화" in topic:
        builder.add_instructions([
            "다음 요구사항에 맞는 텍스트 처리 알고리즘을 구현하고 최적화해주세요:",
            
            "기능 요구사항:",
            "- 대용량 텍스트에서 패턴 검색",
            "- 단어 빈도 계산",
            "- 텍스트 유사도 측정",
            "- 결과 요약 및 리포트 생성",
            
            "기술 요구사항:",
            "- Python 3.8 이상",
            "- 최소한의 외부 라이브러리 사용",
            "- 메모리 효율성 고려",
            "- 멀티스레딩/멀티프로세싱 활용 (선택적)",
            
            "성능 요구사항:",
            "- 1GB 텍스트 파일 처리 시간 < 2분",
            "- 메모리 사용량 < 500MB",
            
            "코드 품질 요구사항:",
            "- 알고리즘 복잡도 분석 포함",
            "- 단위 테스트 및 성능 테스트",
            "- 코드 최적화 과정 및 근거 설명",
            
            "최적화 전/후 비교를 포함하고, 다양한 입력 크기에 대한 성능 분석도 제공해주세요."
        ])
    elif "디자인 패턴" in topic:
        builder.add_instructions([
            "다음 요구사항에 맞는 디자인 패턴 구현 예제를 작성해주세요:",
            
            "구현할 시나리오:",
            "- 다양한 결제 방식을 지원하는 결제 처리 시스템",
            
            "적용할 디자인 패턴:",
            "- 전략 패턴 (결제 방식별 처리 전략)",
            "- 팩토리 패턴 (결제 프로세서 생성)",
            "- 데코레이터 패턴 (부가 기능 추가: 로깅, 알림 등)",
            "- 싱글톤 패턴 (결제 관리자)",
            
            "기술 요구사항:",
            "- Java 또는 C#으로 구현",
            "- 객체지향 원칙 준수",
            "- 인터페이스 기반 설계",
            
            "코드 품질 요구사항:",
            "- SOLID 원칙 준수",
            "- 패턴 적용 목적 및 이점 설명",
            "- 확장 가능한 구조",
            "- 단위 테스트",
            
            "각 디자인 패턴의 적용 방법과 이점, 그리고 패턴들이 어떻게 함께 작동하는지 상세히 설명해주세요."
        ])
    else:
        builder.add_instructions([
            f"{topic}을 구현하는 코드를 작성해주세요. 다음 요소를 포함해주세요:",
            
            "기능 요구사항:",
            "- 구현해야 할 핵심 기능",
            "- 입력 및 출력 형식",
            "- 처리해야 할 비즈니스 로직",
            
            "기술 요구사항:",
            "- 사용할 프로그래밍 언어 및 버전",
            "- 필요한 라이브러리 및 프레임워크",
            "- 개발 환경 및 제약 조건",
            
            "코드 품질 요구사항:",
            "- 코드 스타일 및 구조",
            "- 필요한 테스트",
            "- 문서화 요구사항",
            
            "구체적인 사용 예시와 테스트 케이스도 포함해주세요."
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. 다음 섹션들을 포함해주세요:\n\n"
        f"1. 요구사항 분석: 기능 및 기술 요구사항 분석\n"
        f"2. 설계 접근법: 코드 구조 및 아키텍처 설계\n"
        f"3. 구현: 요구사항에 맞는 코드 구현\n"
        f"4. 사용 예시: 구체적인 사용 방법\n"
        f"5. 테스트 및 검증: 코드 품질 보장 방법\n\n"
        f"코드는 명확한 주석과 문서화를 포함하고, 설계 결정에 대한 근거도 제시해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="코드 생성과 최적화",
        topic_options=CODE_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")