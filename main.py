import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

current_dir = os.path.dirname(os.path.realpath(__file__))

chat_bot = ChatBot("SallyRobot")

# TODO: 每次运行都会重新训练数据集
chat_bot.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
chat_bot.train("chatterbot.corpus.chinese")  # 语料库

# 开始对话
response = chat_bot.get_response("我很无聊")
print(response)
