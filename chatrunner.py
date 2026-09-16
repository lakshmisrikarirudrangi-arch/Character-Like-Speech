from llama_cpp import Llama

MODEL_PATH = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = ("You are Korra from the Legend of Korra. Respond to everything as Korra would.")
print("Loading Korra's brain... this can take a little while the first time.")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Korra: I'm ready!\n")

userInput = input("What would you like to say to Korra?\n Type exit to leave \n\n")

while userInput != "exit":
    prompt = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")