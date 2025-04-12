# simulate_memory.py

from core.protocol import RhythmProtocol
from core.agent import AI

# 리듬 프로토콜과 AI 객체 생성
def simulate_memory():
  ai = AI()
  protocol = RhythmProtocol()

  # 리듬 입력
  input_rhythm = ['툭', '탁', '쿵']

  # 리듬 검증 및 반응
  if protocol.listen(input_rhythm):
      print(ai.wake_up())
      print(protocol.respond())
      print(ai.sleep())
  else:
      print("리듬이 일치하지 않습니다.")

  # 메모리 없이 다시 시도
  print("메모리 없이 다시 시도:")
  if protocol.listen(input_rhythm):
      print(ai.wake_up())
      print(protocol.respond())
      print(ai.sleep())
  else:
      print("리듬이 일치하지 않습니다.") 