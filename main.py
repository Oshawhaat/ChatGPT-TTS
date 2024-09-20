from gpt import gpt
import tts
import multiprocessing


test_message = """The meaning of life is a profound and philosophical question that has been contemplated by thinkers, theologians, and individuals throughout history. Answers vary widely depending on cultural, religious, and personal beliefs." +

1. **Philosophical Perspectives**: Some existentialists argue that life has no inherent meaning, and it is up to each individual to create their own purpose. Others, like utilitarians, suggest that the meaning of life could be found in maximizing happiness and well-being.

2. **Religious Views**: Many religious traditions propose that the meaning of life is connected to a divine purpose or the pursuit of spiritual fulfillment. For example, in Christianity, life may be seen as a journey to know God and serve others, while in Buddhism, the focus is on overcoming suffering and achieving enlightenment.

3. **Scientific Approaches**: From a scientific perspective, the meaning of life can be viewed through the lens of evolution and survival, where life is about reproduction and passing on genetic material.

4. **Personal Interpretations**: On an individual level, many people find meaning in relationships, personal achievements, love, creativity, and making a positive impact on others and the world.

Ultimately, the meaning of life may be subjective and can differ dramatically from one person to another. It often involves a combination of personal values, experiences, and beliefs."""


splits = [
        ".",
        "!",
        "?",
        "[",
        "]",
]

def main():
        _gpt = gpt()

        response = "hello world!" #test_message #_gpt.ask_msg()
        response_list = [response]
        
        for split_str in splits:
                new_response_list = []
                for resp in response_list:
                        split_list = resp.split(split_str)
                        if len(split_list) > 1:
                                split_list[0] += split_str
                        
                        print(f"\"{resp}\" splits to {split_list}")
                        new_response_list += split_list
                        
                response_list = new_response_list
        
        response_list = [x for x in response_list if x]
        
        print(response_list)
        
        #with multiprocessing.Pool(5) as p:
                #p.map(tts.add_to_stack, enumerate(response_list))
        for ind_sentence in enumerate(response_list):
                tts.add_to_stack(ind_sentence)


if __name__ == "__main__":
        main()
