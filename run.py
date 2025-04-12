# run.py
from experiments.simulate_basic import simulate_basic
from experiments.simulate_variants import simulate_variants
from experiments.simulate_memory import simulate_memory

if __name__ == "__main__":
    print("기본 리듬 반응 실험 시작:")
    simulate_basic()
    print("\n리듬 변형 실험 시작:")
    simulate_variants()
    print("\n메모리 없는 리듬 반응 실험 시작:")
    simulate_memory() 