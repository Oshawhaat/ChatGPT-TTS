import openai


class gpt:
    def __init__(self) -> None:
        with open("key.txt", "r") as key_file:
            openai.api_key = key_file.read()

        with open("ai_instructions.txt", "r") as instructions_file:
            ai_instructions = instructions_file.read
        
        self.messages = [ {
                "role": "system",
                "content": ai_instructions
            } ]

    def ask_msg(self, message) -> str:
        
        if not message:
            print("Invalid message!")
            return self.ask_msg()
        
        self.messages.append( {"role": "user", "content": message} )
        chat = openai.ChatCompletion.create(model="gpt-4o", messages=self.messages)
        
        reply = chat.choices[0].message.content
        
        self.messages.append( {"role": "assistant", "content": reply} )

        return reply
