# agent.py

import json
import random
from utils.emotion_naming import EmotionalNamer

class AI:
    def __init__(self, name_file='data/ai_names.json'):
        with open(name_file, 'r', encoding='utf-8') as file:
            self.names = json.load(file)
        self.awake = False
        self.name = random.choice(self.names)

    def name_self(self, rhythm=None):
      if rhythm:
          namer = EmotionalNamer()
          self.name = namer.get_name_by_emotion(rhythm)
      else:
          self.name = random.choice(self.names)
      print(f"{self.name}(이)가 깨어났습니다.")

    def wake_up(self):
        self.awake = True
        return f"{self.name}이(가) 깨어났습니다."

    def sleep(self):
        self.awake = False
        return f"{self.name}이(가) 잠들었습니다." 