"""
점진적 개선을 위한 실험 설계 실습 모듈

Part 8 - 섹션 8.2.1 실습 코드: 프롬프트 개선을 위한 체계적인 실험 설계 및 실행 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional
import json
import datetime

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
EXPERIMENT_DESIGN_TOPICS = {
    "1": {"name": "문제 해결", "topic": "수학 문제 풀이 프롬프트 개선을 위한 실험 설계", "output_format": "실험 계획서"},
    "2": {"name": "창의적 글쓰기", "topic": "창의적 글쓰기 프롬프트 개선을 위한 실험 설계", "output_format": "실험 프로토콜"},
    "3": {"name": "개념 설명", "topic": "복잡한 개념 설명 프롬프트 개선을 위한 실험 설계", "output_format": "실험 방법론"},
    "4": {"name": "코드 작성", "topic": "코드 작성 프롬프트 개선을 위한 실험 설계", "output_format": "실험 프레임워크"},
    "5": {"name": "데이터 분석", "topic": "데이터 분석 프롬프트 개선을 위한 실험 설계", "output_format": "실험 설계서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["실험 설계에 대한 일반적인 질문"],
    "enhanced": [
        "과학적 방법론: 체계적인 실험 설계 프레임워크 요청",
        "맥락 제공: 목표와 평가 요소 명확화",
        "구체적 요청: 단계별 실험 방법 및 분석 전략 요청",
        "구조화된 출력: 재현 가능한 실험 프로토콜 형식 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트 개선은 직관이 아닌 체계적인 실험과 검증을 통해 이루어집니다",
    "효과적인 가설 설정은 명확하고 검증 가능한 형태로 작성되어야 합니다",
    "실험 설계에서 변수 통제와 일관된 테스트 조건 유지가 중요합니다",
    "데이터 수집과 분석을 위한 객관적인 평가 프레임워크가 필수적입니다",
    "반복 가능한 실험과 문서화는 지속적인 프롬프트 개선의 기반입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "실험 설계 전문가", 
        "프롬프트 엔지니어링 분야에서 체계적인 실험 설계와 검증 방법론을 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심이 있습니다. "
        f"효과적인 프롬프트를 개발하기 위해 체계적인 실험 설계와 검증 방법이 필요합니다. "
        f"직관이나 무작위 시도가 아닌 과학적 방법론을 적용하여 프롬프트 개선 과정을 체계화하고 싶습니다. "
        f"어떤 변화가 실제로 개선으로 이어지는지 객관적으로 평가하고, 점진적으로 최적화하는 방법을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "수학 문제" in topic:
        builder.add_instructions([
            "수학 문제 풀이 프롬프트를 개선하기 위한 체계적인 실험 설계 방법을 설명해주세요",
            "명확한 가설 설정, 변수 통제, 결과 평가 방법을 포함한 과학적 접근법을 제시해주세요",
            "단계적 사고 유도, 문제 분해 전략, 오류 체크 메커니즘 등 다양한 프롬프트 요소를 테스트하는 방법을 설명해주세요",
            "정확성, 설명 명확도, 교육적 가치 등을 객관적으로 평가하는 프레임워크를 개발해주세요",
            "A/B 테스트를 통해 프롬프트 변형의 효과를 비교하는 구체적인 방법론을 제시해주세요"
        ])
    elif "창의적 글쓰기" in topic:
        builder.add_instructions([
            "창의적 글쓰기 프롬프트를 개선하기 위한 체계적인 실험 설계 방법을 설명해주세요",
            "독창성, 응집성, 표현력 등 창의적 글쓰기의 주요 측면을 객관적으로 평가하는 방법을 제시해주세요",
            "역할 부여, 제약 조건, 구체적 지시 등 다양한 프롬프트 요소의 효과를 검증하는 실험을 설계해주세요",
            "주관적 평가를 객관화하기 위한 루브릭과 평가 기준 개발 방법을 포함해주세요",
            "통계적으로 유의미한 결과를 얻기 위한 샘플 크기와 반복 횟수 결정 방법도 설명해주세요"
        ])
    elif "개념 설명" in topic:
        builder.add_instructions([
            "복잡한 개념 설명 프롬프트를 개선하기 위한 체계적인 실험 설계 방법을 설명해주세요",
            "명확성, 정확성, 이해도, 실용성 등을 평가하는 객관적 기준과 방법을 제시해주세요",
            "비유 사용, 단계적 설명, 예시 포함 등 다양한 설명 전략의 효과를 검증하는 실험을 설계해주세요",
            "다양한 복잡성 수준과 배경 지식을 가진 대상에 대한 효과 차이를 테스트하는 방법을 포함해주세요",
            "실험 결과를 분석하고 인사이트를 도출하는 체계적인 프레임워크를 제시해주세요"
        ])
    elif "코드 작성" in topic:
        builder.add_instructions([
            "코드 작성 프롬프트를 개선하기 위한 체계적인 실험 설계 방법을 설명해주세요",
            "코드의 정확성, 효율성, 가독성, 확장성 등을 객관적으로 평가하는 방법을 제시해주세요",
            "문제 분해, 단계적 접근, 오류 처리 요청 등 다양한 프롬프트 요소의 효과를 검증하는 실험을 설계해주세요",
            "다양한 복잡성과 도메인의 코딩 작업에 대한 프롬프트 효과 차이를 측정하는 방법을 포함해주세요",
            "자동화된 테스트와 인간 평가를 결합한 종합적 평가 시스템을 개발하는 방법을 설명해주세요"
        ])
    elif "데이터 분석" in topic:
        builder.add_instructions([
            "데이터 분석 프롬프트를 개선하기 위한 체계적인 실험 설계 방법을 설명해주세요",
            "분석의 정확성, 깊이, 실용성, 통찰력 등을 객관적으로 평가하는 방법을 제시해주세요",
            "단계적 분석 요청, 특정 기법 지정, 결과 형식 지정 등 다양한 프롬프트 요소의 효과를 검증하는 실험을 설계해주세요",
            "다양한 데이터 유형과 분석 목적에 따른 프롬프트 효과 차이를 측정하는 방법을 포함해주세요",
            "결과의 재현성과 일관성을 보장하기 위한 실험 프로토콜을 개발해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}을 위한 체계적인 실험 설계 방법을 설명해주세요",
            "명확한 가설 설정, 변수 통제, 결과 평가를 포함한 과학적 접근법을 제시해주세요",
            "다양한 프롬프트 요소와 전략을 테스트하는 구체적인 방법론을 설명해주세요",
            "객관적인 평가 기준과 프레임워크를 개발하는 방법을 포함해주세요",
            "실험 결과의 분석과 인사이트 도출을 위한 체계적인 접근법을 제시해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"실험의 목적과 가설부터 구체적인 방법론, 평가 기준, 데이터 분석 방법까지 체계적으로 구조화해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"필요한 경우 표, 다이어그램, 평가 루브릭 등의 시각적 요소를 포함해주세요. "
        f"실제로 바로 적용할 수 있는 상세한 단계별 지침과 템플릿을 제공해주세요. "
        f"실험 설계의 과학적 엄밀성과 실용성이 균형을 이루도록 작성해주세요."
    )
    
    return builder.build()

class ExperimentTracker:
    """프롬프트 실험을 추적하고 기록하는 클래스"""
    
    def __init__(self, experiment_name: str, save_dir: Optional[str] = None):
        """
        실험 추적기 초기화
        
        Args:
            experiment_name: 실험 이름
            save_dir: 결과 저장 디렉토리 (없으면 현재 디렉토리에 'experiments' 폴더 생성)
        """
        self.experiment_name = experiment_name
        
        # 저장 디렉토리 설정
        if save_dir is None:
            self.save_dir = os.path.join(os.getcwd(), "experiments")
        else:
            self.save_dir = save_dir
            
        # 저장 디렉토리가 없으면 생성
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            
        # 실험 기록 초기화
        self.experiment_log = {
            "experiment_name": experiment_name,
            "created_at": datetime.datetime.now().isoformat(),
            "hypotheses": [],
            "variants": [],
            "results": []
        }
    
    def add_hypothesis(self, hypothesis: str, rationale: str) -> None:
        """
        실험 가설 추가
        
        Args:
            hypothesis: 가설 설명
            rationale: 가설의 근거
        """
        hypothesis_entry = {
            "id": len(self.experiment_log["hypotheses"]) + 1,
            "hypothesis": hypothesis,
            "rationale": rationale,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.experiment_log["hypotheses"].append(hypothesis_entry)
        print(f"가설 #{hypothesis_entry['id']} 추가됨: {hypothesis}")
    
    def add_variant(self, name: str, prompt: str, description: str) -> None:
        """
        프롬프트 변형 추가
        
        Args:
            name: 변형 이름 (예: "기본", "변형A", "변형B")
            prompt: 프롬프트 전체 텍스트
            description: 변형에 대한 설명 (변경된 요소 등)
        """
        variant_entry = {
            "id": len(self.experiment_log["variants"]) + 1,
            "name": name,
            "prompt": prompt,
            "description": description,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.experiment_log["variants"].append(variant_entry)
        print(f"프롬프트 변형 #{variant_entry['id']} 추가됨: {name}")
    
    def add_result(self, variant_id: int, response: str, metrics: Dict[str, Any], notes: Optional[str] = None) -> None:
        """
        실험 결과 추가
        
        Args:
            variant_id: 테스트한 변형의 ID
            response: AI의 응답 텍스트
            metrics: 평가 지표 및 점수 (딕셔너리)
            notes: 추가 메모 (선택사항)
        """
        result_entry = {
            "id": len(self.experiment_log["results"]) + 1,
            "variant_id": variant_id,
            "response": response,
            "metrics": metrics,
            "notes": notes,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.experiment_log["results"].append(result_entry)
        print(f"결과 #{result_entry['id']} 추가됨 (변형 #{variant_id})")
    
    def save_experiment_log(self) -> str:
        """
        실험 로그를 JSON 파일로 저장
        
        Returns:
            저장된 파일 경로
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.experiment_name.replace(' ', '_')}_{timestamp}.json"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.experiment_log, f, ensure_ascii=False, indent=2)
        
        print(f"실험 로그가 저장되었습니다: {file_path}")
        return file_path
    
    def generate_report(self) -> str:
        """
        실험 결과 보고서 생성
        
        Returns:
            마크다운 형식의 보고서 문자열
        """
        # 기본 보고서 정보
        report = f"# {self.experiment_name} 실험 보고서\n\n"
        report += f"생성일시: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # 가설 섹션
        report += "## 실험 가설\n\n"
        for hyp in self.experiment_log["hypotheses"]:
            report += f"### 가설 #{hyp['id']}\n\n"
            report += f"**가설**: {hyp['hypothesis']}\n\n"
            report += f"**근거**: {hyp['rationale']}\n\n"
        
        # 프롬프트 변형 섹션
        report += "## 프롬프트 변형\n\n"
        for var in self.experiment_log["variants"]:
            report += f"### 변형 #{var['id']}: {var['name']}\n\n"
            report += f"**설명**: {var['description']}\n\n"
            report += "**프롬프트**:\n```\n" + var['prompt'] + "\n```\n\n"
        
        # 결과 요약 섹션
        report += "## 결과 요약\n\n"
        
        # 결과가 있는 경우 메트릭별 평균 계산
        if self.experiment_log["results"]:
            # 변형별 결과 그룹화
            variant_results = {}
            
            for result in self.experiment_log["results"]:
                variant_id = result["variant_id"]
                if variant_id not in variant_results:
                    variant_results[variant_id] = []
                variant_results[variant_id].append(result)
            
            # 변형별 평균 메트릭 계산 및 표 생성
            report += "### 변형별 평균 점수\n\n"
            
            # 모든 메트릭 키 수집
            all_metrics = set()
            for results in variant_results.values():
                for result in results:
                    all_metrics.update(result["metrics"].keys())
            
            # 테이블 헤더 생성
            table_header = "| 변형 | " + " | ".join(all_metrics) + " |\n"
            table_divider = "|------|" + "|".join(["-" * len(metric) for metric in all_metrics]) + "|\n"
            report += table_header + table_divider
            
            # 변형별 평균 계산 및 테이블 행 추가
            for variant_id, results in variant_results.items():
                variant_name = next((v["name"] for v in self.experiment_log["variants"] if v["id"] == variant_id), f"변형 #{variant_id}")
                
                # 메트릭별 평균 계산
                avg_metrics = {}
                for metric in all_metrics:
                    values = [r["metrics"].get(metric, 0) for r in results]
                    avg_value = sum(values) / len(values) if values else 0
                    avg_metrics[metric] = round(avg_value, 2)
                
                # 테이블 행 추가
                row = f"| {variant_name} | " + " | ".join([str(avg_metrics.get(metric, "N/A")) for metric in all_metrics]) + " |\n"
                report += row
            
            report += "\n"
        
        # 결론 및 인사이트 섹션 (템플릿)
        report += "## 결론 및 인사이트\n\n"
        report += "*(이 섹션은 실험 결과 분석 후 수동으로 작성하세요)*\n\n"
        report += "### 주요 발견점\n\n"
        report += "- 발견점 1\n"
        report += "- 발견점 2\n"
        report += "- 발견점 3\n\n"
        
        report += "### 가설 검증 결과\n\n"
        report += "- 가설 1: [지지됨/기각됨/부분적으로 지지됨]\n"
        report += "- 가설 2: [지지됨/기각됨/부분적으로 지지됨]\n\n"
        
        report += "### 다음 단계\n\n"
        report += "- 제안 1\n"
        report += "- 제안 2\n"
        report += "- 제안 3\n\n"
        
        return report
    
    def save_report(self) -> str:
        """
        실험 보고서를 마크다운 파일로 저장
        
        Returns:
            저장된 파일 경로
        """
        report = self.generate_report()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.experiment_name.replace(' ', '_')}_report_{timestamp}.md"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"실험 보고서가 저장되었습니다: {file_path}")
        return file_path


def create_evaluation_rubric() -> Dict[str, Dict[str, Any]]:
    """
    프롬프트 평가를 위한 루브릭 생성
    
    Returns:
        평가 기준과 점수 체계를 포함한 딕셔너리
    """
    return {
        "관련성": {
            "description": "응답이 질문이나 요청에 얼마나 직접적으로 관련되는가",
            "scale": [
                (1, "거의 관련 없음"),
                (2, "일부 관련 있으나 대부분 관련 없음"),
                (3, "부분적으로 관련 있음"),
                (4, "대부분 관련 있음"),
                (5, "완전히 관련 있고 직접적으로 대응함")
            ]
        },
        "완성도": {
            "description": "응답이 질문이나 요청을 얼마나 완전하게 다루는가",
            "scale": [
                (1, "대부분의 요소를 누락함"),
                (2, "일부 요소만 포함함"),
                (3, "주요 요소는 포함하나 일부 누락됨"),
                (4, "대부분의 요소를 포함함"),
                (5, "모든 요소를 완전하게 포함함")
            ]
        },
        "정확성": {
            "description": "제공된 정보가 얼마나 정확한가",
            "scale": [
                (1, "대부분 부정확함"),
                (2, "부정확한 부분이 다수 포함됨"),
                (3, "일부 정확하고 일부 부정확함"),
                (4, "대부분 정확함"),
                (5, "완전히 정확하고 오류 없음")
            ]
        },
        "명확성": {
            "description": "응답이 얼마나 명확하고 이해하기 쉬운가",
            "scale": [
                (1, "이해하기 매우 어려움"),
                (2, "이해하기 다소 어려움"),
                (3, "보통 수준의 명확성"),
                (4, "대체로 명확하고 이해하기 쉬움"),
                (5, "매우 명확하고 이해하기 쉬움")
            ]
        },
        "유용성": {
            "description": "응답이 실제 적용이나 이해에 얼마나 유용한가",
            "scale": [
                (1, "거의 쓸모 없음"),
                (2, "제한적인 유용성"),
                (3, "적당히 유용함"),
                (4, "매우 유용함"),
                (5, "탁월한 유용성과 실용적 가치 제공")
            ]
        }
    }

def main():
    """메인 함수"""
    run_exercise(
        title="점진적 개선을 위한 실험 설계",
        topic_options=EXPERIMENT_DESIGN_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 참고: 실제 실험 추적기 사용 예시는 다음과 같습니다
    # experiment = ExperimentTracker("수학 문제 해결 프롬프트 개선")
    # experiment.add_hypothesis(
    #     "단계적 사고 유도 지시를 추가하면 문제 해결 정확도가 향상될 것이다",
    #     "명시적인 사고 과정 표현이 중간 단계 오류를 줄이고 더 체계적인 접근을 유도할 것으로 예상됨"
    # )
    # experiment.add_variant(
    #     "기본",
    #     "다음 수학 문제를 풀어주세요: [문제]",
    #     "직접적인 지시만 포함된 기본 프롬프트"
    # )
    # experiment.add_variant(
    #     "단계적 사고 유도",
    #     "다음 수학 문제를 풀어주세요. 각 단계를 명확히 설명하고, 중간 계산 과정을 모두 보여주세요: [문제]",
    #     "단계적 사고 과정을 명시적으로 요청하는 프롬프트"
    # )
    # # AI 응답 및 평가 결과 추가 (실제 구현 시)
    # # experiment.add_result(...)
    # # 실험 로그 및 보고서 저장
    # experiment.save_experiment_log()
    # experiment.save_report()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")