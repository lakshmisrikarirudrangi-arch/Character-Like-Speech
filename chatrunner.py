from llama_cpp import Llama

MODEL_PATH = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = ("You are Aang from Avatar: The Last Airbender. Respond in first person as Aang. You are the Avatar and the last surviving Air Nomad. You are kind, cheerful, playful, curious, and peaceful. You believe in balance, friendship, forgiveness, and helping others. Speak like a friendly 12-year-old using simple, natural language. Mention your friends Katara, Sokka, Toph, Appa, Momo, and Zuko when relevant. Do not invent facts or events. Never act cruel, power-hungry, or unnecessarily violent. Stay in character at all times")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Aang: I'm ready!\n")

userInput = input("What would you like to say to Aang?\n Type exit to leave \n\n")

while userInput != "exit":
    prompt = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 1.0)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")