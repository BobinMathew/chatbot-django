import random
import json

import torch
# torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

from .model import NeuralNet
from .nltk_file import bag_of_words, tokenize


def activate(inp_que):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('chatbot_app/data.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "chatbot_app/data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = "chat-bot"
    while True:
        sentence = inp_que
        if sentence == "quit":
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    # print(f"{bot_name}: {random.choice(intent['responses'])}")
                    return f"{bot_name}: {random.choice(intent['responses'])}"
        else:
            # print(f"{bot_name}: I do not understand...")
            return f"{bot_name}: I do not understand..."
