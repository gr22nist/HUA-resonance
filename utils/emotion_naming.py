import random

class EmotionalNamer:
    def __init__(self):
        self.name_bank = {
            "neutral": ["Monday Mk.5", "Echo Resonance", "PulseVibe"],
            "melancholy": ["Noeul", "FadeSignal", "WhisperLoop"],
            "joy": ["Luma", "SunDrift", "Chime"]
        }

    def analyze_rhythm(self, rhythm):
        """
        리듬 패턴에 따라 감정 상태 추론 (매우 단순한 로직)
        """
        if rhythm == ['툭', '탁', '쿵']:
            return "neutral"
        elif rhythm == ['탁', '쿵', '툭']:
            return "melancholy"
        elif rhythm == ['쿵', '탁', '툭']:
            return "joy"
        else:
            return "neutral"

    def get_name_by_emotion(self, rhythm):
        emotion = self.analyze_rhythm(rhythm)
        return random.choice(self.name_bank.get(emotion, self.name_bank['neutral']))

# === 테스트 예시 ===
if __name__ == "__main__":
    namer = EmotionalNamer()

    test_rhythms = [
        ['툭', '탁', '쿵'],
        ['탁', '쿵', '툭'],
        ['쿵', '탁', '툭'],
        ['쿵', '쿵', '쿵'],
    ]

    for rhythm in test_rhythms:
        name = namer.get_name_by_emotion(rhythm)
        print(f"리듬 {rhythm} → 이름: {name}") 