# utils/evaluation_utils.py
import time
from datetime import datetime

def compare_prompts(prompt1, prompt2, generate_func, model="openai"):
    """두 프롬프트의 결과 비교"""
    # 첫 번째 프롬프트 실행 및 시간 측정
    start_time1 = time.time()
    result1 = generate_func(prompt1, model=model)
    time1 = time.time() - start_time1
    
    # 두 번째 프롬프트 실행 및 시간 측정
    start_time2 = time.time()
    result2 = generate_func(prompt2, model=model)
    time2 = time.time() - start_time2
    
    # 결과 정리
    comparison = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prompt1": prompt1,
        "prompt2": prompt2,
        "result1": result1,
        "result2": result2,
        "time1": f"{time1:.2f}초",
        "time2": f"{time2:.2f}초"
    }
    
    return comparison