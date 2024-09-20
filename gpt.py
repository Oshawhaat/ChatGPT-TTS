import openai


class gpt:
    def __init__(self) -> None:
        key_file = open("key.txt", "r")
        openai.api_key = key_file.read()

        self.messages = [ {"role": "system", "content": 
                    "You are a intelligent assistant."} ]
    

    def ask_msg(self) -> str:

        message = input("User : ")
        
        if message:
            self.messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-4o-mini", messages = self.messages
            )
        
        reply = chat.choices[0].message.content
        
        print(f"ChatGPT: {reply}")
        self.messages.append({"role": "assistant", "content": reply})

        return reply
