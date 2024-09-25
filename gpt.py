import openai


class gpt:
    def __init__(self) -> None:
        key_file = open("key.txt", "r")
        openai.api_key = key_file.read()

        self.messages = [ {
                "role": "system",
                "content": 
                    """
                        You are a comedy robot who tell jokes based on the prompt.
                        Do not start your messages with something like \"Sure\", just go straight into what is asked.
                        Make sure the jokes are original and as funny as possible.
                    """
            } ]

    def ask_msg(self) -> str:

        message = input("\nWhat kind of joke would you like? : ")
        
        if not message:
            print("Invalid message!")
            return self.ask_msg()
        
        self.messages.append( {"role": "user", "content": message} )
        chat = openai.ChatCompletion.create(model="gpt-4o", messages=self.messages)
        
        reply = chat.choices[0].message.content
        
        self.messages.append( {"role": "assistant", "content": reply} )

        return reply
