"""
A/B 테스트 접근법 실습 모듈

Part 8 - 섹션 8.2.2 실습 코드: 프롬프트 개선을 위한 A/B 테스트 방법론과 실제 적용 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple
import json
import datetime
import random
import statistics
from collections import defaultdict

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise
from utils.ai_client import get_completion

# 주제 옵션 정의
AB_TEST_TOPICS = {
    "1": {"name": "프롬프트 구성 요소", "topic": "프롬프트 구성 요소별 A/B 테스트 방법론", "output_format": "테스트 가이드"},
    "2": {"name": "분야별 최적화", "topic": "분야별 프롬프트 최적화를 위한 A/B 테스트 전략", "output_format": "테스트 프레임워크"},
    "3": {"name": "토너먼트 방식", "topic": "토너먼트 방식의 다단계 A/B 테스트", "output_format": "테스트 프로토콜"},
    "4": {"name": "평가 방법론", "topic": "A/B 테스트 결과 평가 및 분석 방법론", "output_format": "평가 가이드"},
    "5": {"name": "자동화 접근법", "topic": "A/B 테스트 자동화 및 시스템화 방법", "output_format": "자동화 프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["A/B 테스트에 대한 일반적인 질문"],
    "enhanced": [
        "전문적 맥락: 프롬프트 엔지니어링 관점의 A/B 테스트 요청",
        "구체적 요청: 실용적이고 체계적인 방법론과 실제 예시 요청",
        "구조화된 접근: 단계별 프로세스와 평가 프레임워크 요청",
        "재현성: 실제 구현 가능한 구체적 지침 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "A/B 테스트는 객관적인 데이터에 기반한 프롬프트 개선의 핵심 방법론입니다",
    "효과적인 A/B 테스트를 위해서는 명확한 가설과 한 번에 하나의 변수 변경 원칙이 중요합니다",
    "여러 테스트 유형(단일 요소, 구조적, 메타 테스트)을 상황에 맞게 적용할 수 있습니다",
    "통계적으로 유의미한 결과를 얻기 위해 충분한 반복과 엄격한 조건 통제가 필요합니다",
    "객관적인 평가 기준과 체계적인 결과 분석이 A/B 테스트의 성공을 좌우합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 엔지니어링 연구원", 
        "프롬프트 최적화를 위한 A/B 테스트 방법론을 연구하고 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심이 있는 프롬프트 엔지니어입니다. "
        f"직관에 의존하는 대신 체계적이고 객관적인 방법으로 프롬프트를 개선하고 싶습니다. "
        f"A/B 테스트를 통해 어떤 프롬프트 요소와 구조가 실제로 더 효과적인지 검증하는 방법을 배우고, "
        f"이를 실제 프로젝트에 적용하여 점진적으로 최적화된 프롬프트를 개발하고자 합니다."
    )
    
    # 구체적인 지시사항 추가
    if "구성 요소" in topic:
        builder.add_instructions([
            "프롬프트 구성 요소(역할 부여, 지시 방식, 예시 포함 등)를 효과적으로 A/B 테스트하는 방법을 설명해주세요",
            "각 구성 요소별로 가설 설정, 변형 설계, 테스트 실행, 결과 분석의 전체 프로세스를 구체적으로 제시해주세요",
            "구성 요소 간의 상호작용을 고려한 테스트 설계 방법도 포함해주세요",
            "각 요소의 효과를 객관적으로 평가할 수 있는 측정 지표와 평가 방법을 제안해주세요",
            "실제 구현 가능한 A/B 테스트 프로토콜과 템플릿, 예시를 제공해주세요"
        ])
    elif "분야별 최적화" in topic:
        builder.add_instructions([
            "다양한 분야(창의적 글쓰기, 코딩, 데이터 분석, 교육 등)에 특화된 A/B 테스트 전략을 설명해주세요",
            "각 분야별 특성을 고려한 테스트 설계 방법과 평가 기준을 제시해주세요",
            "다양한 분야에서 효과적인 것으로 검증된 프롬프트 패턴과 그 검증 방법을 설명해주세요",
            "분야별 사용자 요구사항과 목표를 고려한 A/B 테스트 프레임워크를 개발해주세요",
            "실제 분야별 A/B 테스트 사례와 인사이트를 포함해주세요"
        ])
    elif "토너먼트 방식" in topic:
        builder.add_instructions([
            "여러 프롬프트 변형을 단계적으로 경쟁시키는 토너먼트 방식 A/B 테스트 방법론을 설명해주세요",
            "토너먼트 구조 설계, 대진표 작성, 승자 결정 기준 등 전체 프로세스를 상세히 설명해주세요",
            "효율적인 변형 개발과 변형 간 차별화 전략을 제시해주세요",
            "라운드별 결과 분석 및 인사이트 통합 방법을 설명해주세요",
            "토너먼트 A/B 테스트를 실제로 구현하고 관리하기 위한 구체적인 프로토콜과 도구를 제안해주세요"
        ])
    elif "평가 방법론" in topic:
        builder.add_instructions([
            "A/B 테스트 결과를 객관적이고 체계적으로 평가하고 분석하는 방법을 설명해주세요",
            "정량적/정성적 평가 지표 개발과 평가 프레임워크 구축 방법을 제시해주세요",
            "통계적 유의성 검증과 결과 해석 방법을 포함한 데이터 분석 접근법을 설명해주세요",
            "편향을 최소화하고 객관성을 높이는 평가 설계 원칙과 전략을 제안해주세요",
            "효과적인 결과 시각화와 인사이트 도출 방법을 구체적인 예시와 함께 제공해주세요"
        ])
    elif "자동화 접근법" in topic:
        builder.add_instructions([
            "프롬프트 A/B 테스트 과정을 자동화하고 시스템화하는 방법을 설명해주세요",
            "테스트 설계, 실행, 데이터 수집, 분석까지 전체 프로세스 자동화 방안을 제시해주세요",
            "자동화된 평가 시스템 구축과 객관적 지표 측정 방법을 설명해주세요",
            "대규모 A/B 테스트를 효율적으로 관리하고 인사이트를 추출하는 시스템 아키텍처를 제안해주세요",
            "실제 구현 가능한 자동화 프레임워크와 코드 예시, 도구 추천을 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "명확한 목표 설정부터 결과 분석까지 전체 프로세스를 단계별로 설명해주세요",
            "실제 적용 가능한 구체적인 방법론과 예시를 포함해주세요",
            "객관적인 평가 시스템과 결과 해석 방법을 제시해주세요",
            "A/B 테스트의 한계와 주의점, 그리고 이를 보완하는 전략도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"이론적 설명과 함께 실제 적용 가능한 구체적인 단계와 예시를 포함해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"A/B 테스트 설계, 실행, 분석을 위한 템플릿과 체크리스트를 포함해주세요. "
        f"필요한 경우 표, 다이어그램 등 시각적 요소를 활용하여 이해를 돕고, "
        f"데이터 중심의 객관적인 접근법이 강조되도록 작성해주세요."
    )
    
    return builder.build()

class ABTestRunner:
    """A/B 테스트를 실행하고 결과를 분석하는 클래스"""
    
    def __init__(self, test_name: str, save_dir: Optional[str] = None):
        """
        A/B 테스트 실행기 초기화
        
        Args:
            test_name: 테스트 이름
            save_dir: 결과 저장 디렉토리 (없으면 현재 디렉토리에 'ab_tests' 폴더 생성)
        """
        self.test_name = test_name
        
        # 저장 디렉토리 설정
        if save_dir is None:
            self.save_dir = os.path.join(os.getcwd(), "ab_tests")
        else:
            self.save_dir = save_dir
            
        # 저장 디렉토리가 없으면 생성
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            
        # 테스트 기록 초기화
        self.test_log = {
            "test_name": test_name,
            "created_at": datetime.datetime.now().isoformat(),
            "variants": {},
            "test_cases": [],
            "results": []
        }
    
    def add_variant(self, variant_id: str, prompt: str, description: str) -> None:
        """
        테스트할 프롬프트 변형 추가
        
        Args:
            variant_id: 변형 식별자 (예: "A", "B", "baseline")
            prompt: 프롬프트 전체 텍스트
            description: 변형에 대한 설명 (변경된 요소 등)
        """
        self.test_log["variants"][variant_id] = {
            "prompt": prompt,
            "description": description,
            "added_at": datetime.datetime.now().isoformat()
        }
        print(f"변형 '{variant_id}' 추가됨: {description}")
    
    def add_test_case(self, case_id: str, input_text: str, description: str) -> None:
        """
        테스트 케이스 추가
        
        Args:
            case_id: 테스트 케이스 식별자
            input_text: 테스트에 사용할 입력 텍스트 (예: 질문, 지시사항 등)
            description: 테스트 케이스 설명
        """
        self.test_log["test_cases"].append({
            "case_id": case_id,
            "input_text": input_text,
            "description": description,
            "added_at": datetime.datetime.now().isoformat()
        })
        print(f"테스트 케이스 '{case_id}' 추가됨: {description}")
    
    def run_test(self, case_id: str, variant_id: str, model: str = "gpt-3.5-turbo", temperature: float = 0.7) -> Dict[str, Any]:
        """
        특정 테스트 케이스와 변형에 대해 테스트 실행
        
        Args:
            case_id: 테스트 케이스 식별자
            variant_id: 변형 식별자
            model: 사용할 AI 모델
            temperature: 온도 설정 (0-1)
            
        Returns:
            테스트 결과 정보
        """
        # 테스트 케이스와 변형 확인
        case = next((c for c in self.test_log["test_cases"] if c["case_id"] == case_id), None)
        if not case:
            raise ValueError(f"테스트 케이스 '{case_id}'를 찾을 수 없습니다.")
        
        if variant_id not in self.test_log["variants"]:
            raise ValueError(f"변형 '{variant_id}'를 찾을 수 없습니다.")
        
        # 프롬프트 구성 (변형 프롬프트 + 테스트 케이스 입력)
        full_prompt = self.test_log["variants"][variant_id]["prompt"].replace("[INPUT]", case["input_text"])
        
        # 테스트 실행
        print(f"테스트 실행 중: 케이스 '{case_id}', 변형 '{variant_id}'")
        start_time = datetime.datetime.now()
        
        try:
            response = get_completion(full_prompt, model=model, temperature=temperature)
            success = True
        except Exception as e:
            response = str(e)
            success = False
        
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # 결과 기록
        result = {
            "case_id": case_id,
            "variant_id": variant_id,
            "response": response,
            "success": success,
            "duration": duration,
            "model": model,
            "temperature": temperature,
            "timestamp": end_time.isoformat(),
            "metrics": {}  # 평가 지표는 나중에 추가
        }
        
        self.test_log["results"].append(result)
        
        print(f"테스트 완료: 소요 시간 {duration:.2f}초")
        return result
    
    def run_all_tests(self, model: str = "gpt-3.5-turbo", temperature: float = 0.7, randomize: bool = True) -> None:
        """
        모든 테스트 케이스와 변형 조합에 대해 테스트 실행
        
        Args:
            model: 사용할 AI 모델
            temperature: 온도 설정 (0-1)
            randomize: 테스트 순서 무작위화 여부
        """
        # 모든 테스트 케이스와 변형 조합 생성
        test_queue = []
        for case in self.test_log["test_cases"]:
            for variant_id in self.test_log["variants"].keys():
                test_queue.append((case["case_id"], variant_id))
        
        # 테스트 순서 무작위화 (옵션)
        if randomize:
            random.shuffle(test_queue)
        
        # 테스트 실행
        total_tests = len(test_queue)
        print(f"총 {total_tests}개의 테스트를 실행합니다...")
        
        for i, (case_id, variant_id) in enumerate(test_queue, 1):
            print(f"\n[{i}/{total_tests}] 테스트 진행 중...")
            self.run_test(case_id, variant_id, model, temperature)
            
            # 간단한 진행률 표시
            if i < total_tests:
                print(f"진행률: {i/total_tests*100:.1f}% ({i}/{total_tests})")
        
        print(f"\n모든 테스트가 완료되었습니다. 총 {total_tests}개 테스트 실행됨.")
    
    def add_evaluation(self, case_id: str, variant_id: str, metrics: Dict[str, float], evaluator: str, notes: Optional[str] = None) -> None:
        """
        테스트 결과에 평가 지표 추가
        
        Args:
            case_id: 테스트 케이스 식별자
            variant_id: 변형 식별자
            metrics: 평가 지표 및 점수 (딕셔너리)
            evaluator: 평가자 정보
            notes: 추가 메모 (선택사항)
        """
        # 해당 결과 찾기
        result = next((r for r in self.test_log["results"] 
                      if r["case_id"] == case_id and r["variant_id"] == variant_id), None)
        
        if not result:
            raise ValueError(f"케이스 '{case_id}'와 변형 '{variant_id}'에 대한 결과를 찾을 수 없습니다.")
        
        # 평가 정보 추가
        result["metrics"] = metrics
        result["evaluator"] = evaluator
        result["evaluation_notes"] = notes
        result["evaluated_at"] = datetime.datetime.now().isoformat()
        
        print(f"평가가 추가되었습니다: 케이스 '{case_id}', 변형 '{variant_id}'")
    
    def analyze_results(self) -> Dict[str, Any]:
        """
        테스트 결과 분석
        
        Returns:
            분석 결과 정보
        """
        # 결과가 없으면 빈 분석 반환
        if not self.test_log["results"]:
            return {"error": "분석할 결과가 없습니다."}
        
        # 평가되지 않은 결과가 있는지 확인
        unevaluated = [r for r in self.test_log["results"] if not r.get("metrics")]
        if unevaluated:
            print(f"경고: {len(unevaluated)}개의 결과가 아직 평가되지 않았습니다.")
        
        # 변형별 결과 그룹화
        variant_results = defaultdict(list)
        for result in self.test_log["results"]:
            if result.get("metrics"):  # 평가된 결과만 포함
                variant_results[result["variant_id"]].append(result)
        
        # 각 변형별 평균 메트릭 계산
        analysis = {
            "variant_metrics": {},
            "test_case_metrics": {},
            "overall_comparison": {}
        }
        
        # 모든 메트릭 키 수집
        all_metrics = set()
        for results in variant_results.values():
            for result in results:
                all_metrics.update(result["metrics"].keys())
        
        # 변형별 평균 메트릭 계산
        for variant_id, results in variant_results.items():
            analysis["variant_metrics"][variant_id] = {}
            
            # 각 메트릭별 평균 계산
            for metric in all_metrics:
                values = [r["metrics"].get(metric, 0) for r in results if metric in r["metrics"]]
                if values:
                    analysis["variant_metrics"][variant_id][metric] = {
                        "mean": statistics.mean(values),
                        "median": statistics.median(values),
                        "std_dev": statistics.stdev(values) if len(values) > 1 else 0,
                        "min": min(values),
                        "max": max(values),
                        "count": len(values)
                    }
        
        # 테스트 케이스별 변형 비교
        case_comparison = {}
        for case in self.test_log["test_cases"]:
            case_id = case["case_id"]
            case_comparison[case_id] = {}
            
            # 각 케이스에 대한 변형별 결과 수집
            case_results = {}
            for result in self.test_log["results"]:
                if result["case_id"] == case_id and result.get("metrics"):
                    case_results[result["variant_id"]] = result["metrics"]
            
            # 각 메트릭별로 최고 점수 변형 식별
            for metric in all_metrics:
                if all(metric in results for results in case_results.values()):
                    metric_scores = {v_id: results[metric] for v_id, results in case_results.items()}
                    best_variant = max(metric_scores.items(), key=lambda x: x[1])[0]
                    case_comparison[case_id][metric] = {
                        "best_variant": best_variant,
                        "scores": metric_scores
                    }
        
        analysis["test_case_metrics"] = case_comparison
        
        # 전체 비교 (어떤 변형이 가장 좋았는지)
        winner_count = defaultdict(int)
        total_wins = 0
        
        for case_metrics in case_comparison.values():
            for metric_data in case_metrics.values():
                winner_count[metric_data["best_variant"]] += 1
                total_wins += 1
        
        # 승률 계산
        win_rate = {variant: count / total_wins if total_wins > 0 else 0 
                   for variant, count in winner_count.items()}
        
        analysis["overall_comparison"] = {
            "win_count": dict(winner_count),
            "win_rate": win_rate,
            "total_comparisons": total_wins
        }
        
        return analysis
    
    def save_test_log(self) -> str:
        """
        테스트 로그를 JSON 파일로 저장
        
        Returns:
            저장된 파일 경로
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.test_name.replace(' ', '_')}_{timestamp}.json"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.test_log, f, ensure_ascii=False, indent=2)
        
        print(f"테스트 로그가 저장되었습니다: {file_path}")
        return file_path
    
    def generate_report(self, analysis: Optional[Dict[str, Any]] = None) -> str:
        """
        A/B 테스트 결과 보고서 생성
        
        Args:
            analysis: 분석 결과 (없으면 새로 분석)
            
        Returns:
            마크다운 형식의 보고서 문자열
        """
        # 분석 결과가 없으면 새로 분석
        if analysis is None:
            analysis = self.analyze_results()
        
        # 기본 보고서 정보
        report = f"# {self.test_name} A/B 테스트 보고서\n\n"
        report += f"생성일시: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # 테스트 개요
        report += "## 테스트 개요\n\n"
        report += f"- 테스트 이름: {self.test_name}\n"
        report += f"- 변형 수: {len(self.test_log['variants'])}\n"
        report += f"- 테스트 케이스 수: {len(self.test_log['test_cases'])}\n"
        report += f"- 총 테스트 실행 수: {len(self.test_log['results'])}\n\n"
        
        # 변형 설명
        report += "## 테스트 변형\n\n"
        for variant_id, variant_data in self.test_log["variants"].items():
            report += f"### 변형 {variant_id}\n\n"
            report += f"**설명**: {variant_data['description']}\n\n"
            report += "**프롬프트**:\n```\n" + variant_data['prompt'] + "\n```\n\n"
        
        # 테스트 케이스
        report += "## 테스트 케이스\n\n"
        for case in self.test_log["test_cases"]:
            report += f"### 케이스 {case['case_id']}\n\n"
            report += f"**설명**: {case['description']}\n\n"
            report += f"**입력**: \"{case['input_text']}\"\n\n"
        
        # 결과 요약
        report += "## 결과 요약\n\n"
        
        # 변형별 평균 메트릭
        report += "### 변형별 평균 점수\n\n"
        
        if "variant_metrics" in analysis and analysis["variant_metrics"]:
            # 모든 메트릭 키 수집
            all_metrics = set()
            for variant_metrics in analysis["variant_metrics"].values():
                all_metrics.update(variant_metrics.keys())
            
            # 테이블 헤더 생성
            table_header = "| 변형 | " + " | ".join(all_metrics) + " |\n"
            table_divider = "|------|" + "|".join(["---" for _ in all_metrics]) + "|\n"
            report += table_header + table_divider
            
            # 변형별 평균 점수 테이블 행 추가
            for variant_id, metrics in analysis["variant_metrics"].items():
                row = f"| {variant_id} | "
                row += " | ".join([f"{metrics.get(metric, {}).get('mean', 'N/A'):.2f}" if metric in metrics else "N/A" 
                                  for metric in all_metrics])
                row += " |\n"
                report += row
            
            report += "\n"
        else:
            report += "평가된 결과가 충분하지 않아 변형별 평균 점수를 계산할 수 없습니다.\n\n"
        
        # 전체 승자 비교
        if "overall_comparison" in analysis and analysis["overall_comparison"].get("win_count"):
            report += "### 승자 분석\n\n"
            report += "각 테스트 케이스와 메트릭 조합에서 최고 점수를 받은 변형의 횟수입니다.\n\n"
            
            # 승자 테이블
            report += "| 변형 | 승리 횟수 | 승률 |\n"
            report += "|------|----------|------|\n"
            
            win_count = analysis["overall_comparison"]["win_count"]
            win_rate = analysis["overall_comparison"]["win_rate"]
            
            for variant_id in self.test_log["variants"].keys():
                count = win_count.get(variant_id, 0)
                rate = win_rate.get(variant_id, 0)
                report += f"| {variant_id} | {count} | {rate:.2%} |\n"
            
            report += "\n"
            
            # 최종 승자
            if win_count:
                winner = max(win_count.items(), key=lambda x: x[1])[0]
                report += f"**최종 승자**: 변형 {winner} (승률 {win_rate.get(winner, 0):.2%})\n\n"
        
        # 결론 및 인사이트 섹션 (템플릿)
        report += "## 결론 및 인사이트\n\n"
        report += "*(이 섹션은 분석 결과를 바탕으로 수동으로 작성하세요)*\n\n"
        report += "### 주요 발견점\n\n"
        report += "- 발견점 1\n"
        report += "- 발견점 2\n"
        report += "- 발견점 3\n\n"
        
        report += "### 다음 단계\n\n"
        report += "- 제안 1\n"
        report += "- 제안 2\n"
        report += "- 제안 3\n\n"
        
        return report
    
    def save_report(self, analysis: Optional[Dict[str, Any]] = None) -> str:
        """
        A/B 테스트 보고서를 마크다운 파일로 저장
        
        Args:
            analysis: 분석 결과 (없으면 새로 분석)
            
        Returns:
            저장된 파일 경로
        """
        report = self.generate_report(analysis)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.test_name.replace(' ', '_')}_report_{timestamp}.md"
        file_path = os.path.join(self.save_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"A/B 테스트 보고서가 저장되었습니다: {file_path}")
        return file_path

def create_evaluation_rubric() -> Dict[str, Dict[str, Any]]:
    """
    A/B 테스트 결과 평가를 위한 루브릭 생성
    
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
        title="A/B 테스트 접근법",
        topic_options=AB_TEST_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )
    
    # 참고: 실제 A/B 테스트