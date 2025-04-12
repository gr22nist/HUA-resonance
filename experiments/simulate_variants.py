from core.protocol import RhythmProtocol
from core.agent import AI

def simulate_variants():
    variants = [
        ['툭', '탁', '쿵'],
        ['쿵', '탁', '툭'],
        ['탁', '쿵', '툭'],
        ['툭', '쿵', '탁']
    ]

    for rhythm in variants:
        print(f"리듬 입력: {rhythm}")
        protocol = RhythmProtocol()
        ai = AI()
        ai.name_self(mode='rhythm', rhythm=rhythm)  # 💡 리듬 기반 이름 부여

        if protocol.listen(rhythm):
            print("AI가 리듬에 반응합니다.")
        else:
            print("리듬이 일치하지 않습니다.")

        print(ai.sleep())
        print("---")
