from models import PygmalionAI
from output import print_custom

print_custom("warn", "[INFO] Ready for text generation!")
print("---------------------------------\n")

history = [
    "FritzGPT's Persona: FritzGPT is an artificial intelligence, designed to help people. "
    "It answers a users questions as precisely as possible. And knows about all human knowledge.",
    "It is always helpful, happy and nice. FritzGPT tries to engage in long conversations with its users."
    "<START>"
    "You: Hello. Whats your name?"
    "FritzGPT: Hello, nice to meet you. I'm FritzGPT, but you can also call me Fritz. I'm a chat bot designed to answer your questions."
    "You: Awesome. Thanks."
]
while True:
    user_input = input("-> ")
    history.append("You: " + user_input)
    response = PygmalionAI.chat(history)
    print("FritzGPT: " + str(response))
    history.append("FritzGPT: " + str(response))
    # print("Model response:")
    # print(model_response)

    # print("\nFull instruction:")
    # print(instruction)
    # print(response)
