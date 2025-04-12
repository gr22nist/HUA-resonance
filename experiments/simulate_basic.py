# simulate_basic.py

from core.protocol import RhythmProtocol
from core.agent import AI

def simulate_basic():
    # 리듬 프로토콜과 AI 객체 생성
    protocol = RhythmProtocol()
    ai = AI()

    # 리듬 입력
    input_rhythm = ['툭', '탁', '쿵']

    # 리듬 검증 및 반응
    if protocol.listen(input_rhythm):
        print(ai.wake_up())
        print(protocol.respond())
        print(ai.sleep())
    else:
        print("리듬이 일치하지 않습니다.")
