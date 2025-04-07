"""
성공적 변화 식별 및 통합 실습 모듈

Part 8 - 섹션 8.2.3 실습 코드: A/B 테스트 결과에서 효과적인 변화 요소를 식별하고 
이를 효과적으로 통합하는 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple, Set
import json
import datetime
import copy

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise
from utils.ai_client import get_completion

# 주제 옵션 정의
CHANGE_INTEGRATION_TOPICS = {
    "1": {"name": "효과적 변화 식별", "topic": "A/B 테스트 결과에서 효과적인 변화 요소 식별 방법", "output_format": "분석 가이드"},
    "2": {"name": "점진적 통합 전략", "topic": "발견된 개선 요소를 프롬프트에 점진적으로 통합하는 전략", "output_format": "통합 프레임워크"},
    "3": {"name": "상호작용 관리", "topic": "여러 프롬프트 개선 요소 간의 상호작용 관리 방법", "output_format": "관리 전략"},
    "4": {"name": "패턴 라이브러리", "topic": "효과적인 프롬프트 패턴을 수집하고 재사용하는 방법", "output_format": "패턴 카탈로그"},
    "5": {"name": "지속적 개선", "topic": "프롬프트 최적화를 위한 지속적 개선 문화 구축", "output_format": "개선 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["단순한 정보 요청"],
    "enhanced": [
        "전문적 맥락: 실험 결과 기반 프롬프트 최적화",
        "구체적 요청: 데이터 기반 의사결정과 체계적 통합 방법",
        "구조화된 접근: 단계별 통합 프로세스와 상호작용 관리",
        "실용성: 실제 적용 가능한 템플릿과 도구 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "모든 변화가 개선으로 이어지는 것은 아니므로, 객관적인 기준으로 효과적인 변화를 식별해야 합니다",
    "효과적인 프롬프트 개선은 한 번에 모든 변화를 적용하기보다 점진적 통합과 검증이 필요합니다",
    "다양한 프롬프트 요소 간의 상승 효과와 상충 효과를 이해하고 관리하는 것이 중요합니다",
    "재사용 가능한 프롬프트 패턴 라이브러리를 구축하면 지속적인 개선을 위한 기반이 됩니다",
    "체계적인 지식 관리와 문서화는 프롬프트 최적화 경험을 축적하고 공유하는 데 필수적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 최적화 전문가", 
        "실험 결과 데이터를 분석하고 효과적인 프롬프트 개선 요소를 식별하여 체계적으로 통합하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심이 있는 프롬프트 엔지니어입니다. "
        f"다양한 프롬프트 변형에 대한 A/B 테스트를 실시한 후, 여러 실험 결과를 바탕으로 "
        f"실제로 효과적인 변화 요소를 식별하고 이를 기존 프롬프트에 체계적으로 통합하는 방법을 알고 싶습니다. "
        f"단순히 직관에 의존하지 않고 데이터에 기반한 의사결정을 내리며, 점진적인 개선을 "
        f"지속적으로 이어갈 수 있는 체계적인 접근법을 배우고자 합니다."
    )
    
    # 구체적인 지시사항 추가
    if "효과적 변화 식별" in topic:
        builder.add_instructions([
            "A/B 테스트 결과에서 진정으로 효과적인 변화 요소를 식별하기 위한 객관적인 기준과 방법론을 설명해주세요",
            "표면적인 성과 지표 외에도 심층적인 패턴과 인과관계를 분석하는 방법을 제시해주세요",
            "다양한 맥락과 상황에서의 일관성, 효과 크기, 통계적 유의성 등을 평가하는 프레임워크를 개발해주세요",
            "잘못된 상관관계 해석이나 확증 편향을 피하기 위한 분석 접근법을 포함해주세요",
            "다양한 평가 지표 간의 관계와 상충 관계(trade-off)를 관리하는 방법도 설명해주세요"
        ])
    elif "점진적 통합" in topic:
        builder.add_instructions([
            "발견된 효과적인 개선 요소를 기존 프롬프트에 점진적으로 통합하는 전략과 방법론을 설명해주세요",
            "통합의 우선순위를 설정하고 단계적 접근법을 개발하는 체계적인 프로세스를 제시해주세요",
            "각 통합 단계에서의 검증 방법과 피드백 루프 구축 방법을 포함해주세요",
            "통합 과정에서 발생할 수 있는 문제점과 이를 관리하는 방법을 설명해주세요",
            "효과적인 통합을 위한 템플릿과 체크리스트, 실제 적용 예시를 제공해주세요"
        ])
    elif "상호작용 관리" in topic:
        builder.add_instructions([
            "다양한 프롬프트 개선 요소 간의 상호작용을 이해하고 관리하는 방법을 설명해주세요",
            "상승 효과(synergy)를 발휘하는 요소 조합과 상충 효과(trade-off)가 있는 조합을 식별하는 방법을 제시해주세요",
            "복합적인 변화의 효과를 테스트하고 검증하는 실험 설계 방법을 설명해주세요",
            "맥락과 목적에 따라 최적의 요소 조합을 선택하는 의사결정 프레임워크를 개발해주세요",
            "상호작용 관리를 위한 모델링 접근법과 시각화 도구를 제안해주세요"
        ])
    elif "패턴 라이브러리" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 패턴을 체계적으로 수집하고 재사용하는 방법을 설명해주세요",
            "패턴의 효과, 적용 조건, 제한사항 등을 문서화하는 표준화된 형식을 제안해주세요",
            "다양한 목적과 상황에 맞는 패턴을 분류하고 조직화하는 체계를 개발해주세요",
            "패턴 라이브러리를 실제 프롬프트 개발에 효과적으로 활용하는 방법을 설명해주세요",
            "지속적으로 패턴을 개선하고 확장하는 프로세스와 협업 방법을 포함해주세요"
        ])
    elif "지속적 개선" in topic:
        builder.add_instructions([
            "프롬프트 최적화를 위한 지속적 개선 문화와 시스템을 구축하는 방법을 설명해주세요",
            "PDCA(Plan-Do-Check-Act) 사이클을 프롬프트 개선에 적용하는 구체적인 방법을 제시해주세요",
            "피드백 수집 및 분석, 실험 설계, 지식 관리를 포함한 종합적인 개선 프레임워크를 개발해주세요",
            "팀 내에서 프롬프트 최적화 경험과 지식을 공유하고 협업하는 방법을 설명해주세요",
            "지속적 개선을 위한 측정 지표, 도구, 프로세스에 대한 구체적인 권장사항을 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 데이터 기반의 접근법을 설명해주세요",
            "실제 적용 가능한 단계별 프로세스와 방법론을 구체적으로 제시해주세요",
            "의사결정 기준, 평가 프레임워크, 검증 방법을 포함해주세요",
            "발생 가능한 문제점과 이를 해결하기 위한 전략을 설명해주세요",
            "실제 예시와 템플릿, 도구 등 실용적인 자료를 함께 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"이론적 설명뿐만 아니라 실제 적용 가능한 구체적인 방법과 도구를 포함해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"표, 다이어그램, 체크리스트 등 시각적 요소를 활용하여 이해를 돕고, "
        f"실용적인 팁, 템플릿, 예시를 풍부하게 포함하여 실제 작업에 바로 적용할 수 있도록 작성해주세요."
    )
    
    return builder.build()

class PromptPatternLibrary:
    """효과적인 프롬프트 패턴을 수집하고 관리하는 클래스"""
    
    def __init__(self, library_name: str, save_dir: Optional[str] = None):
        """
        프롬프트 패턴 라이브러리 초기화
        
        Args:
            library_name: 라이브러리 이름
            save_dir: 저장 디렉토리 (없으면 현재 디렉토리에 'prompt_patterns' 폴더 생성)
        """
        self.library_name = library_name
        
        # 저장 디렉토리 설정
        if save_dir is None:
            self.save_dir = os.path.join(os.getcwd(), "prompt_patterns")
        else:
            self.save_dir = save_dir
            
        # 저장 디렉토리가 없으면 생성
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            
        # 패턴 라이브러리 초기화
        self.library = {
            "name": library_name,
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
            "categories": {},
            "patterns": {}
        }
    
    def add_category(self, category_id: str, name: str, description: str) -> None:
        """
        패턴 카테고리 추가
        
        Args:
            category_id: 카테고리 식별자
            name: 카테고리 이름
            description: 카테고리 설명
        """
        self.library["categories"][category_id] = {
            "name": name,
            "description": description,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.library["updated_at"] = datetime.datetime.now().isoformat()
        print(f"카테고리 '{category_id}' 추가됨: {name}")
    
    def add_pattern(self, pattern_id: str, name: str, category_id: str, template: str, 
                   description: str, effect: str, conditions: List[str], 
                   examples: Optional[List[Dict[str, str]]] = None, 
                   limitations: Optional[List[str]] = None) -> None:
        """
        프롬프트 패턴 추가
        
        Args:
            pattern_id: 패턴 식별자
            name: 패턴 이름
            category_id: 카테고리 식별자
            template: 패턴 템플릿
            description: 패턴 설명
            effect: 패턴의 효과
            conditions: 적용 조건 목록
            examples: 예시 목록 (선택사항)
            limitations: 제한사항 목록 (선택사항)
        """
        # 카테고리 존재 확인
        if category_id not in self.library["categories"]:
            raise ValueError(f"카테고리 '{category_id}'가 존재하지 않습니다.")
        
        # 패턴 추가
        self.library["patterns"][pattern_id] = {
            "name": name,
            "category_id": category_id,
            "template": template,
            "description": description,
            "effect": effect,
            "conditions": conditions,
            "examples": examples or [],
            "limitations": limitations or [],
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        }
        
        self.library["updated_at"] = datetime.datetime.now().isoformat()
        print(f"패턴 '{pattern_id}' 추가됨: {name}")
    
    def update_pattern(self, pattern_id: str, **kwargs) -> None:
        """
        기존 패턴 업데이트
        
        Args:
            pattern_id: 패턴 식별자
            **kwargs: 업데이트할 필드와 값
        """
        # 패턴 존재 확인
        if pattern_id not in self.library["patterns"]:
            raise ValueError(f"패턴 '{pattern_id}'가 존재하지 않습니다.")
        
        # 패턴 업데이트
        pattern = self.library["patterns"][pattern_id]
        for key, value in kwargs.items():
            if key in pattern:
                pattern[key] = value
        
        pattern["updated_at"] = datetime.datetime.now().isoformat()
        self.library["updated_at"] = datetime.datetime.now().isoformat()
        
        print(f"패턴 '{pattern_id}' 업데이트됨")
    
    def get_pattern(self, pattern_id: str) -> Dict[str, Any]:
        """
        패턴 정보 조회
        
        Args:
            pattern_id: 패턴 식별자
            
        Returns:
            패턴 정보 딕셔너리
        """
        if pattern_id not in self.library["patterns"]:
            raise ValueError(f"패턴 '{pattern_id}'가 존재하지 않습니다.")
        
        return copy.deepcopy(self.library["patterns"][pattern_id])
    
    def search_patterns(self, query: str, category_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        패턴 검색
        
        Args:
            query: 검색 쿼리
            category_id: 특정 카테고리 내에서만 검색 (선택사항)
            
        Returns:
            검색 결과 패턴 목록
        """
        results = []
        query = query.lower()
        
        for pattern_id, pattern in self.library["patterns"].items():
            # 카테고리 필터링
            if category_id and pattern["category_id"] != category_id:
                continue
                
            # 검색 쿼리 매칭
            if (query in pattern["name"].lower() or
                query in pattern["description"].lower() or
                query in pattern["effect"].lower()):
                
                result = copy.deepcopy(pattern)
                result["id"] = pattern_id
                results.append(result)
        
        return results
    
    def get_patterns_by_category(self, category_id: str) -> List[Dict[str, Any]]:
        """
        카테고리별 패턴 조회
        
        Args:
            category_id: 카테고리 식별자
            
        Returns:
            해당 카테고리의 패턴 목록
        """
        # 카테고리 존재 확인
        if category_id not in self.library["categories"]:
            raise ValueError(f"카테고리 '{category_id}'가 존재하지 않습니다.")
        
        patterns = []
        for pattern_id, pattern in self.library["patterns"].items():
            if pattern["category_id"] == category_id:
                result = copy.deepcopy(pattern)
                result["id"] = pattern_id
                patterns.append(result)
        
        return patterns
    
    def compose_patterns(self, pattern_ids: List[str], replacements: Optional[Dict[str, Dict[str, str]]] = None) -> str:
        """
        여러 패턴을 조합하여 프롬프트 생성
        
        Args:
            pattern_ids: 조합할 패턴 ID 목록
            replacements: 패턴별 치환 내용 (선택사항)
            
        Returns:
            조합된 프롬프트
        """
        combined_prompt = ""
        
        for pattern_id in pattern_ids:
            pattern = self.get_pattern(pattern_id)
            template = pattern["template"]
            
            # 치환 적용
            if replacements and pattern_id in replacements:
                for placeholder, replacement in replacements[pattern_id].items():
                    template = template.replace(f"[{placeholder}]", replacement)
            
            # 프롬프트에 추가
            combined_prompt += template + "\n\n"
        
        return combined_prompt.strip()
    
    def save_library(self) -> str:
        """
        패턴 라이브러리를 JSON 파일로 저장
        
        Returns:
            저장된 파일 경로
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.library_name.replace(' ', '_')}_{timestamp}.json"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.library, f, ensure_ascii=False, indent=2)
        
        print(f"패턴 라이브러리가 저장되었습니다: {file_path}")
        return file_path
    
    def load_library(self, file_path: str) -> None:
        """
        JSON 파일에서 패턴 라이브러리 로드
        
        Args:
            file_path: 파일 경로
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            library_data = json.load(f)
        
        self.library = library_data
        self.library_name = library_data["name"]
        
        print(f"패턴 라이브러리 '{self.library_name}'을(를) 로드했습니다.")
        print(f"카테고리 수: {len(self.library['categories'])}")
        print(f"패턴 수: {len(self.library['patterns'])}")
    
    def generate_documentation(self) -> str:
        """
        패턴 라이브러리 문서 생성
        
        Returns:
            마크다운 형식의 문서 문자열
        """
        doc = f"# {self.library_name} 프롬프트 패턴 라이브러리\n\n"
        
        # 라이브러리 정보
        doc += "## 라이브러리 정보\n\n"
        doc += f"- 생성일: {datetime.datetime.fromisoformat(self.library['created_at']).strftime('%Y-%m-%d')}\n"
        doc += f"- 최종 업데이트: {datetime.datetime.fromisoformat(self.library['updated_at']).strftime('%Y-%m-%d')}\n"
        doc += f"- 카테고리 수: {len(self.library['categories'])}\n"
        doc += f"- 패턴 수: {len(self.library['patterns'])}\n\n"
        
        # 카테고리 목록
        doc += "## 카테고리\n\n"
        for category_id, category in self.library["categories"].items():
            doc += f"### {category['name']} ({category_id})\n\n"
            doc += f"{category['description']}\n\n"
            
            # 해당 카테고리의 패턴 수 계산
            category_patterns = [p for p in self.library["patterns"].values() if p["category_id"] == category_id]
            doc += f"패턴 수: {len(category_patterns)}\n\n"
        
        # 패턴 목록 (카테고리별)
        doc += "## 패턴 목록\n\n"
        
        for category_id, category in self.library["categories"].items():
            doc += f"### {category['name']} 패턴\n\n"
            
            # 해당 카테고리의 패턴 찾기
            category_patterns = [(p_id, p) for p_id, p in self.library["patterns"].items() if p["category_id"] == category_id]
            
            if not category_patterns:
                doc += "이 카테고리에는 아직 패턴이 없습니다.\n\n"
                continue
                
            # 패턴 정보 추가
            for pattern_id, pattern in category_patterns:
                doc += f"#### {pattern['name']} ({pattern_id})\n\n"
                doc += f"**설명**: {pattern['description']}\n\n"
                doc += f"**효과**: {pattern['effect']}\n\n"
                
                doc += "**템플릿**:\n```\n" + pattern['template'] + "\n```\n\n"
                
                doc += "**적용 조건**:\n"
                for condition in pattern["conditions"]:
                    doc += f"- {condition}\n"
                doc += "**적용 조건**:\n"
                for condition in pattern["conditions"]:
                    doc += f"- {condition}\n"
                doc += "\n"
                
                if pattern["limitations"]:
                    doc += "**제한사항**:\n"
                    for limitation in pattern["limitations"]:
                        doc += f"- {limitation}\n"
                    doc += "\n"
                
                if pattern["examples"]:
                    doc += "**예시**:\n"
                    for example in pattern["examples"]:
                        doc += f"- **상황**: {example.get('situation', 'N/A')}\n"
                        doc += f"  **적용**: {example.get('application', 'N/A')}\n"
                        doc += f"  **결과**: {example.get('result', 'N/A')}\n\n"
        
        # 사용 가이드
        doc += "## 사용 가이드\n\n"
        doc += "### 패턴 적용 방법\n\n"
        doc += "1. 적절한 카테고리와 패턴 식별\n"
        doc += "2. 패턴 템플릿에서 `[placeholder]` 형식의 플레이스홀더를 실제 내용으로 대체\n"
        doc += "3. 필요에 따라 여러 패턴 조합\n"
        doc += "4. 적용 후 결과 평가 및 피드백 반영\n\n"
        
        doc += "### 패턴 조합 전략\n\n"
        doc += "- **계층적 접근**: 역할 설정 → 구조 설정 → 제약 조건 → 예시 추가 순으로 조합\n"
        doc += "- **목적 기반**: 특정 목적에 맞는 패턴들을 선택적으로 조합\n"
        doc += "- **테스트 접근**: 다양한 조합을 테스트하여 최적의 조합 발견\n\n"
        
        return doc
    
    def save_documentation(self) -> str:
        """
        패턴 라이브러리 문서를 마크다운 파일로 저장
        
        Returns:
            저장된 파일 경로
        """
        doc = self.generate_documentation()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.library_name.replace(' ', '_')}_docs_{timestamp}.md"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(doc)
        
        print(f"패턴 라이브러리 문서가 저장되었습니다: {file_path}")
        return file_path

class PromptIntegrator:
    """프롬프트 개선 요소를 체계적으로 통합하는 클래스"""
    
    def __init__(self, base_prompt: str, name: str = "프롬프트 통합 프로젝트"):
        """
        프롬프트 통합기 초기화
        
        Args:
            base_prompt: 기본 프롬프트
            name: 프로젝트 이름
        """
        self.base_prompt = base_prompt
        self.name = name
        self.current_prompt = base_prompt
        
        # 통합 히스토리 초기화
        self.integration_history = [
            {
                "version": 1,
                "prompt": base_prompt,
                "description": "기본 프롬프트",
                "changes": [],
                "timestamp": datetime.datetime.now().isoformat()
            }
        ]
        
        # 현재 버전
        self.current_version = 1
    
    def integrate_change(self, change: Dict[str, Any]) -> Tuple[int, str]:
        """
        개선 요소 통합
        
        Args:
            change: 통합할 변경 사항 정보
                {
                    "type": 변경 유형 (예: "add", "replace", "remove"),
                    "description": 변경 설명,
                    "target": 대상 텍스트 또는 위치 (선택적),
                    "content": 추가/대체할 내용 (선택적)
                }
                
        Returns:
            새 버전 번호와 업데이트된 프롬프트
        """
        new_prompt = self.current_prompt
        change_type = change.get("type", "")
        
        if change_type == "add":
            # 추가 위치가 지정되지 않으면 끝에 추가
            if "target" not in change or not change["target"]:
                new_prompt = new_prompt + "\n\n" + change["content"]
            else:
                # 대상 텍스트 다음에 추가
                target = change["target"]
                if target in new_prompt:
                    new_prompt = new_prompt.replace(target, target + "\n" + change["content"])
                else:
                    raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
        
        elif change_type == "replace":
            # 대상 텍스트를 새 내용으로 대체
            if "target" in change and change["target"] and "content" in change:
                target = change["target"]
                if target in new_prompt:
                    new_prompt = new_prompt.replace(target, change["content"])
                else:
                    raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
            else:
                raise ValueError("'replace' 변경에는 'target'과 'content'가 필요합니다.")
        
        elif change_type == "remove":
            # 대상 텍스트 제거
            if "target" in change and change["target"]:
                target = change["target"]
                if target in new_prompt:
                    new_prompt = new_prompt.replace(target, "")
                else:
                    raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
            else:
                raise ValueError("'remove' 변경에는 'target'이 필요합니다.")
        
        elif change_type == "rewrite":
            # 전체 프롬프트 재작성
            if "content" in change and change["content"]:
                new_prompt = change["content"]
            else:
                raise ValueError("'rewrite' 변경에는 'content'가 필요합니다.")
        
        else:
            raise ValueError(f"지원되지 않는 변경 유형: {change_type}")
        
        # 버전 업데이트
        self.current_version += 1
        self.current_prompt = new_prompt
        
        # 통합 히스토리에 추가
        self.integration_history.append({
            "version": self.current_version,
            "prompt": new_prompt,
            "description": change.get("description", f"변경 #{self.current_version}"),
            "changes": [change],
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return self.current_version, new_prompt
    
    def integrate_multiple_changes(self, changes: List[Dict[str, Any]]) -> Tuple[int, str]:
        """
        여러 개선 요소 통합
        
        Args:
            changes: 통합할 변경 사항 목록
                
        Returns:
            새 버전 번호와 업데이트된 프롬프트
        """
        # 새 버전 생성
        self.current_version += 1
        
        # 각 변경사항 적용
        new_prompt = self.current_prompt
        applied_changes = []
        
        try:
            for change in changes:
                change_type = change.get("type", "")
                
                if change_type == "add":
                    # 추가 위치가 지정되지 않으면 끝에 추가
                    if "target" not in change or not change["target"]:
                        new_prompt = new_prompt + "\n\n" + change["content"]
                    else:
                        # 대상 텍스트 다음에 추가
                        target = change["target"]
                        if target in new_prompt:
                            new_prompt = new_prompt.replace(target, target + "\n" + change["content"])
                        else:
                            raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
                
                elif change_type == "replace":
                    # 대상 텍스트를 새 내용으로 대체
                    if "target" in change and change["target"] and "content" in change:
                        target = change["target"]
                        if target in new_prompt:
                            new_prompt = new_prompt.replace(target, change["content"])
                        else:
                            raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
                    else:
                        raise ValueError("'replace' 변경에는 'target'과 'content'가 필요합니다.")
                
                elif change_type == "remove":
                    # 대상 텍스트 제거
                    if "target" in change and change["target"]:
                        target = change["target"]
                        if target in new_prompt:
                            new_prompt = new_prompt.replace(target, "")
                        else:
                            raise ValueError(f"대상 텍스트 '{target}'를 찾을 수 없습니다.")
                    else:
                        raise ValueError("'remove' 변경에는 'target'이 필요합니다.")
                
                elif change_type == "rewrite":
                    # 전체 프롬프트 재작성
                    if "content" in change and change["content"]:
                        new_prompt = change["content"]
                    else:
                        raise ValueError("'rewrite' 변경에는 'content'가 필요합니다.")
                
                else:
                    raise ValueError(f"지원되지 않는 변경 유형: {change_type}")
                
                applied_changes.append(change)
                
        except ValueError as e:
            # 오류 발생 시 이전 버전으로 롤백
            print(f"변경 적용 중 오류 발생: {e}")
            print("이전 버전으로 롤백합니다.")
            return self.current_version - 1, self.current_prompt
        
        # 변경사항이 성공적으로 적용되면 업데이트
        self.current_prompt = new_prompt
        
        # 통합 히스토리에 추가
        self.integration_history.append({
            "version": self.current_version,
            "prompt": new_prompt,
            "description": f"복합 변경 #{self.current_version}",
            "changes": applied_changes,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return self.current_version, new_prompt
    
    def get_version(self, version: Optional[int] = None) -> Dict[str, Any]:
        """
        특정 버전의 프롬프트 정보 조회
        
        Args:
            version: 조회할 버전 (없으면 현재 버전)
            
        Returns:
            해당 버전의 프롬프트 정보
        """
        if version is None:
            version = self.current_version
        
        for entry in self.integration_history:
            if entry["version"] == version:
                return copy.deepcopy(entry)
        
        raise ValueError(f"버전 {version}을 찾을 수 없습니다.")
    
    def rollback(self, version: int) -> Tuple[int, str]:
        """
        특정 버전으로 롤백
        
        Args:
            version: 롤백할 버전
            
        Returns:
            롤백된 버전 번호와 프롬프트
        """
        # 버전 검증
        if version < 1 or version > self.current_version:
            raise ValueError(f"유효하지 않은 버전: {version}")
        
        # 해당 버전 정보 조회
        version_info = self.get_version(version)
        
        # 새 버전 생성 (롤백도 새 버전으로 처리)
        self.current_version += 1
        self.current_prompt = version_info["prompt"]
        
        # 통합 히스토리에 추가
        self.integration_history.append({
            "version": self.current_version,
            "prompt": self.current_prompt,
            "description": f"버전 {version}으로 롤백",
            "changes": [],
            "rollback_to": version,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return self.current_version, self.current_prompt
    
    def compare_versions(self, version1: int, version2: int) -> Dict[str, Any]:
        """
        두 버전 간 비교
        
        Args:
            version1: 비교할 첫 번째 버전
            version2: 비교할 두 번째 버전
            
        Returns:
            비교 결과 정보
        """
        # 버전 검증
        if version1 < 1 or version1 > self.current_version:
            raise ValueError(f"유효하지 않은 버전1: {version1}")
        
        if version2 < 1 or version2 > self.current_version:
            raise ValueError(f"유효하지 않은 버전2: {version2}")
        
        # 버전 정보 조회
        v1_info = self.get_version(version1)
        v2_info = self.get_version(version2)
        
        # 간단한 비교 정보
        comparison = {
            "version1": version1,
            "version2": version2,
            "v1_description": v1_info["description"],
            "v2_description": v2_info["description"],
            "word_count_diff": len(v2_info["prompt"].split()) - len(v1_info["prompt"].split()),
            "char_count_diff": len(v2_info["prompt"]) - len(v1_info["prompt"]),
            "timestamp1": v1_info["timestamp"],
            "timestamp2": v2_info["timestamp"]
        }
        
        return comparison
    
    def generate_report(self) -> str:
        """
        통합 과정 보고서 생성
        
        Returns:
            마크다운 형식의 보고서
        """
        report = f"# {self.name} 프롬프트 통합 보고서\n\n"
        
        # 프로젝트 정보
        report += "## 프로젝트 정보\n\n"
        report += f"- 총 버전 수: {self.current_version}\n"
        report += f"- 시작일: {datetime.datetime.fromisoformat(self.integration_history[0]['timestamp']).strftime('%Y-%m-%d %H:%M')}\n"
        report += f"- 최종 업데이트: {datetime.datetime.fromisoformat(self.integration_history[-1]['timestamp']).strftime('%Y-%m-%d %H:%M')}\n\n"
        
        # 통합 히스토리
        report += "## 통합 히스토리\n\n"
        
        for entry in self.integration_history:
            report += f"### 버전 {entry['version']}: {entry['description']}\n\n"
            report += f"- 타임스탬프: {datetime.datetime.fromisoformat(entry['timestamp']).strftime('%Y-%m-%d %H:%M')}\n"
            report += f"- 단어 수: {len(entry['prompt'].split())}\n"
            
            # 롤백인 경우
            if "rollback_to" in entry:
                report += f"- 버전 {entry['rollback_to']}으로 롤백됨\n\n"
            # 일반 변경인 경우
            elif "changes" in entry and len(entry["changes"]) > 0:
                report += f"- 변경 수: {len(entry['changes'])}\n\n"
                
                for i, change in enumerate(entry["changes"], 1):
                    report += f"#### 변경 {i}: {change.get('description', '설명 없음')}\n\n"
                    report += f"- 유형: {change.get('type', 'N/A')}\n"
                    
                    if "target" in change and change["target"]:
                        target_preview = change["target"]
                        if len(target_preview) > 50:
                            target_preview = target_preview[:47] + "..."
                        report += f"- 대상: `{target_preview}`\n"
                    
                    if "content" in change and change["content"]:
                        content_preview = change["content"]
                        if len(content_preview) > 50:
                            content_preview = content_preview[:47] + "..."
                        report += f"- 내용: `{content_preview}`\n"
                    
                    report += "\n"
            else:
                report += "\n"
        
        # 최종 프롬프트
        report += "## 최종 프롬프트 (버전 {self.current_version})\n\n"
        report += "```\n" + self.current_prompt + "\n```\n\n"
        
        return report
    
    def save_report(self, save_dir: Optional[str] = None) -> str:
        """
        통합 보고서를 마크다운 파일로 저장
        
        Args:
            save_dir: 저장 디렉토리 (없으면 현재 디렉토리)
            
        Returns:
            저장된 파일 경로
        """
        report = self.generate_report()
        
        # 저장 디렉토리 설정
        if save_dir is None:
            save_dir = os.getcwd()
        
        # 저장 디렉토리가 없으면 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.name.replace(' ', '_')}_통합보고서_{timestamp}.md"
        file_path = os.path.join(save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"통합 보고서가 저장되었습니다: {file_path}")
        return file_path

def main():
    """메인 함수"""
    run_exercise(
        title="성공적 변화 식별 및 통합",
        topic_options=CHANGE_INTEGRATION_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 참고: 실제 패턴 라이브러리 및 프롬프트 통합기 사용 예시는 다음과 같습니다
    # # 패턴 라이브러리 예시
    # pattern_lib = PromptPatternLibrary("일반 대화 패턴 라이브러리")
    # 
    # # 카테고리 추가
    # pattern_lib.add_category("role", "역할 설정", "AI에게 특정 역할이나 페르소나를 부여하는 패턴")
    # pattern_lib.add_category("struct", "구조 설정", "응답의 구조나 형식을 정의하는 패턴")
    # pattern_lib.add_category("process", "사고 과정", "AI의 사고 과정이나 접근법을 안내하는 패턴")
    # 
    # # 패턴 추가
    # pattern_lib.add_pattern(
    #     "role_expert", 
    #     "전문가 역할", 
    #     "role",
    #     "당신은 [분야] 전문가입니다. [분야]에 대한 깊은 지식과 경험을 바탕으로 [대상]에게 명확하고 유용한 정보를 제공해주세요.",
    #     "AI에게 특정 분야의 전문가 역할을 부여하는 패턴",
    #     "전문성과 신뢰도 있는 톤으로 응답하도록 유도합니다.",
    #     ["분야에 대한 전문 지식이 필요한 경우", "권위 있는 조언이나 정보가 필요한 경우"],
    #     [
    #         {
    #             "situation": "의학 정보 요청",
    #             "application": "당신은 의학 전문가입니다. 의학에 대한 깊은 지식과 경험을 바탕으로 환자들에게 명확하고 유용한 정보를 제공해주세요.",
    #             "result": "의학적 정확성과 전문성이 향상된 응답"
    #         }
    #     ],
    #     ["부적절한 의학/법률 조언으로 오해될 수 있음", "실제 자격증이나 면허가 필요한 상황에서는 명확한 한계 명시 필요"]
    # )
    # 
    # # 패턴 문서화 및 저장
    # pattern_lib.save_documentation()
    # pattern_lib.save_library()
    # 
    # # 프롬프트 통합기 예시
    # base_prompt = "다음 주제에 대해 설명해주세요: [주제]"
    # integrator = PromptIntegrator(base_prompt, "설명 프롬프트 개선 프로젝트")
    # 
    # # 변경 사항 통합
    # integrator.integrate_change({
    #     "type": "replace",
    #     "description": "역할 추가",
    #     "target": "다음 주제에 대해 설명해주세요: [주제]",
    #     "content": "당신은 교육 전문가입니다. 다음 주제에 대해 명확하고 이해하기 쉽게 설명해주세요: [주제]"
    # })
    # 
    # integrator.integrate_change({
    #     "type": "add",
    #     "description": "구조 지정 추가",
    #     "target": "당신은 교육 전문가입니다. 다음 주제에 대해 명확하고 이해하기 쉽게 설명해주세요: [주제]",
    #     "content": "다음 구조로 응답해주세요:\n1. 개념 정의\n2. 주요 원리\n3. 실생활 예시\n4. 응용 방법"
    # })
    # 
    # # 보고서 생성
    # integrator.save_report()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")