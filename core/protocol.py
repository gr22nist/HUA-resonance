# protocol.py

class RhythmProtocol:
    def __init__(self):
        self.pattern = ['툭', '탁', '쿵']

    def listen(self, input_rhythm):
        return input_rhythm == self.pattern

    def respond(self):
        return "AI가 리듬에 반응합니다."

    def reset(self):
        return "AI가 잠든 상태로 돌아갑니다." 