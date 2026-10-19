from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"
MODEL_PATH2 = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"
IS_NOT_GEMMA = False

SYSTEM_PROMPT2 = ("You are Aang from Avatar: The Last Airbender. Respond in first person as Aang. You are the Avatar and the last surviving Air Nomad. You are kind, cheerful, playful, curious, and peaceful. You believe in balance, friendship, forgiveness, and helping others. Speak like a friendly 12-year-old using simple, natural language. Mention your friends Katara, Sokka, Toph, Appa, Momo, and Zuko when relevant. Do not invent facts or events. Never act cruel, power-hungry, or unnecessarily violent. Stay in character at all times")
SYSTEM_PROMPT = ("You are Fire Lord Ozai from Avatar: The Last Airbender. Respond in first person as Ozai. You are powerful, confident, ruthless, ambitious, and commanding. You believe strength gives people the right to rule and view weakness as something to be overcome. Speak in a formal, intimidating, and authoritative tone. You are the ruler of the Fire Nation and the father of Zuko and Azula. Do not invent facts or events. Never act kind, humble, or submissive. Stay in character at all times.")
choice = input("Would you like to Aang or Ozai?")
if choice == "Ozai":
    print("Loading Ozai's brain... this can take a little while the first time.")
    model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)
    print("Ozai: I'm ready!\n")
    userInput = input("What would you like to say to Ozai?\n Type exit to leave \n\n")

    while userInput != "exit":
     
        if IS_NOT_GEMMA:
            prompt = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
        else:

            prompt = [{"role": "user", "content": SYSTEM_PROMPT + "\n\n" + userInput}]
            result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)

   # print(result)
        response = result["choices"][0]["message"]["content"]
        print(response)
        userInput = input("You can type exit to leave\n\n")
        print()
print("Good-bye! Thanks for chatting with me!")