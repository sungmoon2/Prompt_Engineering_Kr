"""
코드 생성 요청 실습 모듈

Part 5 - 섹션 5.2.1 실습 코드: 목적에 맞는 효과적인 코드 요청 방법을 학습합니다.
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
CODE_GENERATION_TOPICS = {
    "1": {"name": "데이터 처리 유틸리티", "topic": "파일 데이터 처리 유틸리티 함수 개발", "output_format": "코드 명세"},
    "2": {"name": "웹 컴포넌트", "topic": "인터랙티브 웹 UI 컴포넌트 개발", "output_format": "코드 및 설명"},
    "3": {"name": "API 클라이언트", "topic": "RESTful API 통합 클라이언트", "output_format": "코드 명세"},
    "4": {"name": "알고리즘 구현", "topic": "효율적인 알고리즘 구현", "output_format": "코드 및 설명"},
    "5": {"name": "디자인 패턴 적용", "topic": "디자인 패턴을 활용한 솔루션 구현", "output_format": "코드 명세"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["기본적인 코드 구현 요청"],
    "enhanced": [
        "명확한 요구사항: 정확한 기능, 입출력, 제약 조건 명시",
        "기술 스택 명세: 언어, 프레임워크, 라이브러리, 버전 명시",
        "품질 기준 제시: 코드 품질, 성능, 확장성 요구사항 명시",
        "예시와 맥락: 사용 사례, 테스트 케이스, 통합 방식 포함"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 코드 요청은 명확한 요구사항 정의와 구체적인 기술 스택 명세에서 시작합니다",
    "코드의 품질과 성능 기준을 미리 설정하여 기대에 맞는 결과를 얻을 수 있습니다",
    "예시 입출력과 사용 맥락을 제공하면 더 실용적이고 목적에 맞는 코드를 얻을 수 있습니다",
    "복잡한 코드는 기본 구현을 먼저 요청한 후 점진적으로 개선하는 접근법이 효과적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}을 구현하는 코드를 작성해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "소프트웨어 개발 전문가", 
        "사용자의 요구사항을 정확히 이해하고 고품질의 코드를 설계 및 구현하는 전문 개발자"
    )
    
    # 주제별 맞춤 지시사항 추가
    if "데이터 처리" in topic:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}을 개발하고 있습니다. CSV, JSON, XML 형식의 데이터 파일을 읽고, 변환하고, "
            f"분석하는 유틸리티 함수가 필요합니다. 이 유틸리티는 데이터 과학 프로젝트에서 "
            f"사용될 예정이며, 대용량 파일도 효율적으로 처리할 수 있어야 합니다."
        )
        
        builder.add_instructions([
            "다음 요구사항에 맞는 Python 3.9 데이터 처리 유틸리티를 개발해주세요:",
            
            "기능 요구사항:",
            "1. 다양한 형식(CSV, JSON, XML)의 파일 읽기 기능",
            "2. 형식 간 변환 기능(예: CSV → JSON)",
            "3. 기본 데이터 분석 기능(합계, 평균, 최대/최소값 등)",
            "4. 데이터 필터링 및 정렬 기능",
            "5. 처리 결과를 다양한 형식으로 저장 기능",
            
            "기술 요구사항:",
            "- Python 3.9와 표준 라이브러리 활용(pandas, numpy 선택적 사용)",
            "- 메모리 효율성(스트리밍 방식으로 대용량 파일 처리)",
            "- 적절한 예외 처리 및 오류 메시지",
            "- 모듈화된 구조와 확장 가능한 설계",
            
            "코드 품질 요구사항:",
            "- PEP 8 스타일 가이드 준수",
            "- 타입 힌팅 사용",
            "- 함수/클래스 단위 주석 및 문서화",
            "- 단위 테스트 포함",
            
            "다음과 같은 사용 예시를 지원해야 합니다:",
            "```python",
            "# CSV 파일 읽기 및 기본 통계",
            "stats = analyze_csv('data.csv', column='value')",
            "print(stats)  # {'mean': 23.5, 'max': 45, 'min': 10, ...}",
            "",
            "# CSV를 JSON으로 변환",
            "convert_file('data.csv', 'data.json', from_format='csv', to_format='json')",
            "",
            "# 데이터 필터링 및 저장",
            "filter_and_save('data.csv', 'filtered.csv', lambda row: float(row['value']) > 100)",
            "```"
        ])
        
    elif "웹 컴포넌트" in topic:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}을 개발하고 있습니다. 사용자 데이터를 표시하고 상호작용할 수 있는 "
            f"재사용 가능한 웹 컴포넌트가 필요합니다. 이 컴포넌트는 현대적인 웹 애플리케이션에 "
            f"통합될 예정이며, 반응형 디자인과 접근성을 갖추어야 합니다."
        )
        
        builder.add_instructions([
            "다음 요구사항에 맞는 React 컴포넌트를 TypeScript로 개발해주세요:",
            
            "기능 요구사항:",
            "1. 사용자 데이터 표시(이름, 이메일, 역할, 상태 등)",
            "2. 정렬 및 필터링 기능",
            "3. 페이지네이션 지원",
            "4. 항목 선택 및 일괄 작업 기능",
            "5. 항목별 상세 정보 표시/숨김 기능",
            
            "기술 요구사항:",
            "- React 18 및 TypeScript 4.x 사용",
            "- 상태 관리는 React Context API 또는 Redux 사용",
            "- 스타일링은 Styled Components 또는 Tailwind CSS 사용",
            "- RESTful API 연동(모킹 데이터 포함)",
            
            "코드 품질 요구사항:",
            "- 컴포넌트 분리 및 재사용성",
            "- TypeScript 타입 정의",
            "- 접근성(WCAG 2.1 AA) 준수",
            "- 성능 최적화(불필요한 리렌더링 방지)",
            "- 단위 테스트(Jest/React Testing Library)",
            
            "다음과 같은 인터페이스를 구현해야 합니다:",
            "```tsx",
            "interface User {",
            "  id: string;",
            "  name: string;",
            "  email: string;",
            "  role: string;",
            "  status: 'active' | 'inactive' | 'pending';",
            "  created_at: string;",
            "  // 기타 필요한 필드",
            "}",
            "",
            "interface UserListProps {",
            "  initialUsers?: User[];",
            "  onUserSelect?: (user: User) => void;",
            "  onBulkAction?: (action: string, userIds: string[]) => void;",
            "  loading?: boolean;",
            "  error?: string;",
            "  pageSize?: number;",
            "}",
            "```",
            
            "사용 예시:",
            "```tsx",
            "<UserList",
            "  initialUsers={users}",
            "  onUserSelect={handleUserSelect}",
            "  onBulkAction={handleBulkAction}",
            "  pageSize={10}",
            "/>"
            "```"
        ])
        
    elif "API 클라이언트" in topic:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}을 개발하고 있습니다. 외부 RESTful API와 통신하기 위한 "
            f"클라이언트 라이브러리가 필요합니다. 이 클라이언트는 인증, 요청 관리, "
            f"오류 처리 등을 처리할 수 있어야 하며, 다양한 프로젝트에서 재사용 가능해야 합니다."
        )
        
        builder.add_instructions([
            "다음 요구사항에 맞는 JavaScript/TypeScript API 클라이언트를 개발해주세요:",
            
            "기능 요구사항:",
            "1. RESTful API 엔드포인트 호출(GET, POST, PUT, DELETE)",
            "2. 인증 토큰 관리(Bearer 토큰)",
            "3. 요청/응답 인터셉터 지원",
            "4. 자동 재시도 및 오류 복구 기능",
            "5. 응답 캐싱 기능",
            "6. 요청 취소 기능",
            
            "기술 요구사항:",
            "- TypeScript 4.x 사용",
            "- Axios 라이브러리 기반(또는 fetch API)",
            "- Promise 및 async/await 지원",
            "- 모듈화된 구조",
            
            "코드 품질 요구사항:",
            "- 명확한 인터페이스 정의",
            "- 철저한 오류 처리",
            "- 단위 테스트 포함",
            "- 자세한 문서화(JSDoc)",
            
            "다음과 같은 사용 예시를 지원해야 합니다:",
            "```typescript",
            "// 클라이언트 초기화",
            "const api = new ApiClient({",
            "  baseURL: 'https://api.example.com',",
            "  headers: { 'Content-Type': 'application/json' },",
            "  auth: {",
            "    type: 'bearer',",
            "    token: 'your-token-here'",
            "  }",
            "});",
            "",
            "// GET 요청",
            "const users = await api.get('/users', { params: { limit: 10 } });",
            "",
            "// POST 요청",
            "const newUser = await api.post('/users', { name: 'John', email: 'john@example.com' });",
            "",
            "// 캐싱 및 재시도 옵션 설정",
            "const data = await api.get('/data', {",
            "  cache: true,",
            "  cacheTime: 60000,",
            "  retry: 3,",
            "  retryDelay: 1000",
            "});",
            "```"
        ])
        
    elif "알고리즘" in topic:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}에 관심이 있습니다. 데이터 처리 애플리케이션에서 사용할 "
            f"효율적인 알고리즘이 필요합니다. 구체적으로는 대용량 데이터 세트에서 "
            f"특정 패턴을 찾고 분석하는 알고리즘이 필요합니다."
        )
        
        builder.add_instructions([
            "다음 요구사항에 맞는 Python 알고리즘을 개발해주세요:",
            
            "기능 요구사항:",
            "1. 텍스트 문서에서 특정 패턴(정규식 포함) 검색",
            "2. 검색 결과의 컨텍스트(주변 텍스트) 추출",
            "3. 패턴 출현 빈도 및 분포 분석",
            "4. 검색 결과 관련성 점수 계산",
            "5. 결과 요약 및 리포트 생성",
            
            "기술 요구사항:",
            "- Python 3.8 이상",
            "- 표준 라이브러리만 사용(외부 의존성 최소화)",
            "- 대용량 파일 처리 지원(메모리 효율성)",
            "- 멀티스레딩 또는 멀티프로세싱 활용",
            
            "성능 요구사항:",
            "- 1GB 텍스트 파일 처리 시간 5분 이내",
            "- 메모리 사용량 최대 500MB 이내",
            "- CPU 사용률 최적화",
            
            "코드 품질 요구사항:",
            "- 모듈화된 설계",
            "- 타입 힌팅 적용",
            "- 단위 테스트 포함",
            "- 성능 측정 코드 포함",
            
            "알고리즘은 다음과 같은 인터페이스를 가져야 합니다:",
            "```python",
            "def search_patterns(file_path: str, patterns: List[str], options: Dict = None) -> Dict[str, Any]:",
            "    \"\"\"",
            "    텍스트 파일에서 패턴을 검색하고 분석합니다.",
            "    ",
            "    Args:",
            "        file_path: 검색할 텍스트 파일 경로",
            "        patterns: 검색할 패턴 목록 (정규식 지원)",
            "        options: 검색 옵션 (컨텍스트 크기, 대소문자 구분 등)",
            "        ",
            "    Returns:",
            "        검색 결과 및 분석 데이터를 포함하는 딕셔너리",
            "    \"\"\"",
            "    # 구현...",
            "```",
            
            "구체적인 사용 예시:",
            "```python",
            "results = search_patterns(",
            "    'large_document.txt',",
            "    ['error\\s+\\d+', 'warning', 'critical'],",
            "    {",
            "        'case_sensitive': False,",
            "        'context_size': 50,  # 패턴 전후 50자",
            "        'max_results': 1000,",
            "        'use_multiprocessing': True",
            "    }",
            ")",
            "",
            "print(f\"Found {results['total_matches']} matches\")",
            "print(f\"Most frequent pattern: {results['most_frequent']}\")",
            "",
            "# 결과 반복",
            "for match in results['matches'][:10]:  # 처음 10개만",
            "    print(f\"Pattern: {match['pattern']}\")",
            "    print(f\"Context: {match['context']}\")",
            "    print(f\"Relevance: {match['relevance_score']}\")",
            "```"
        ])
        
    elif "디자인 패턴" in topic:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}에 관심이 있습니다. 확장 가능하고 유지보수가 용이한 "
            f"소프트웨어를 개발하기 위해 적절한 디자인 패턴을 적용한 코드가 필요합니다. "
            f"실제 프로젝트에 적용할 수 있는 구체적인 예제를 통해 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "다음 요구사항에 맞는 Java 기반 디자인 패턴 구현 예제를 개발해주세요:",
            
            "구현할 시스템:",
            "간단한 문서 처리 시스템으로, 다양한 형식(텍스트, HTML, PDF 등)의 문서를 로드, 처리, 변환, 저장할 수 있어야 합니다.",
            
            "적용할 디자인 패턴:",
            "1. 팩토리 패턴: 다양한 문서 형식 객체 생성",
            "2. 전략 패턴: 문서 처리 알고리즘 교체 가능",
            "3. 데코레이터 패턴: 문서 처리에 추가 기능 동적 부여",
            "4. 옵저버 패턴: 문서 변경 이벤트 처리",
            "5. 싱글톤 패턴: 설정 관리자 구현",
            
            "기능 요구사항:",
            "- 다양한 형식의 문서 로드 및 저장",
            "- 문서 내용 검색 및 수정",
            "- 문서 형식 간 변환",
            "- 문서 처리 과정 로깅",
            "- 확장 가능한 플러그인 구조",
            
            "기술 요구사항:",
            "- Java 11 이상",
            "- 외부 라이브러리 최소화",
            "- 인터페이스 기반 설계",
            "- SOLID 원칙 준수",
            
            "코드 품질 요구사항:",
            "- 명확한 패키지 구조",
            "- 상세한 JavaDoc 주석",
            "- 단위 테스트(JUnit 5)",
            "- 디자인 패턴 적용 목적과 이점 설명",
            
            "다음과 같은 코드 구조가 필요합니다:",
            "```java",
            "// 문서 인터페이스",
            "public interface Document {",
            "    String getContent();",
            "    void setContent(String content);",
            "    DocumentType getType();",
            "    // 기타 메서드...",
            "}",
            "",
            "// 문서 처리 전략 인터페이스",
            "public interface ProcessingStrategy {",
            "    void process(Document document);",
            "}",
            "",
            "// 문서 팩토리",
            "public interface DocumentFactory {",
            "    Document createDocument(String path);",
            "    Document createNewDocument(DocumentType type);",
            "}",
            "",
            "// 문서 관리자",
            "public class DocumentManager {",
            "    // 싱글톤 구현",
            "    // 팩토리 사용",
            "    // 전략 패턴 적용",
            "    // 데코레이터 패턴 적용",
            "    // 옵저버 패턴 적용",
            "}",
            "```",
            
            "사용 예시:",
            "```java",
            "// 문서 관리자 인스턴스 가져오기",
            "DocumentManager manager = DocumentManager.getInstance();",
            "",
            "// 문서 로드",
            "Document doc = manager.loadDocument(\"sample.txt\");",
            "",
            "// 처리 전략 설정",
            "manager.setProcessingStrategy(new SpellCheckStrategy());",
            "",
            "// 문서 처리",
            "manager.processDocument(doc);",
            "",
            "// 문서 변환",
            "Document htmlDoc = manager.convertDocument(doc, DocumentType.HTML);",
            "",
            "// 문서 저장",
            "manager.saveDocument(htmlDoc, \"sample.html\");",
            "```",
            
            "각 디자인 패턴의 구현 목적과 이점, 적용 방법을 상세히 설명해주세요."
        ])
        
    else:
        # 맥락 정보 추가
        builder.add_context(
            f"{topic}을 개발하고 있습니다. 명확한 요구사항과 구체적인 기술 스택을 "
            f"바탕으로 고품질의 코드가 필요합니다. 실제 프로젝트에 바로 적용할 수 있는 "
            f"실용적인 구현이 필요합니다."
        )
        
        builder.add_instructions([
            f"{topic}에 대한 코드를 작성해주세요. 다음 요소를 포함해주세요:",
            
            "기능 요구사항:",
            "- 구현해야 할 핵심 기능 명세",
            "- 입력 및 출력 데이터 형식",
            "- 처리해야 할 비즈니스 로직",
            "- 필요한 사용자 인터페이스",
            
            "기술 요구사항:",
            "- 사용할 프로그래밍 언어 및 버전",
            "- 필요한 프레임워크 및 라이브러리",
            "- 개발 환경 및 제약 조건",
            "- 성능 및 확장성 요구사항",
            
            "코드 품질 요구사항:",
            "- 코드 스타일 및 포맷팅 기준",
            "- 테스트 요구사항",
            "- 문서화 요구사항",
            "- 오류 처리 방식",
            
            "구체적인 사용 예시 및 테스트 케이스를 포함해주세요."
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. 다음 섹션들을 포함해주세요:\n\n"
        f"1. 요구사항 분석: 제시된 요구사항 분석 및 구현 계획\n"
        f"2. 기술 스택 및 아키텍처: 사용할 기술과 아키텍처 설명\n"
        f"3. 코드 구현: 요구사항에 맞는 전체 코드 구현\n"
        f"4. 사용 예시: 코드 사용법 및 예시\n"
        f"5. 테스트 및 검증: 코드 테스트 방법\n\n"
        f"코드는 마크다운 형식의 코드 블록으로 제공하고, 각 부분에 대한 설명을 포함해주세요. "
        f"주요 결정 사항과 디자인 선택에 대한 근거도 제시해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="목적에 맞는 코드 요청",
        topic_options=CODE_GENERATION_TOPICS,
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