from gpt import gpt
import tts


split_points = [
        ".",
        "!",
        "?",
        "\n",
        "[",
        "]",
]

def main():
        _gpt = gpt()

        response = _gpt.ask_msg()
        response_list = [response]
        
        for split_str in split_points:
                new_response_list = []
                for resp in response_list:
                        split_list = resp.split(split_str)
                        
                        if len(split_list) > 1:
                                for x in range(0, len(split_list) - 1):
                                        split_list[x] += split_str
                        
                        new_response_list += split_list
                        
                response_list = new_response_list
        
        response_list = [x.removeprefix(" ") for x in response_list if x and x not in split_points]
        
        for resp in response_list:
                print(f"\"{resp}\"")
        
        for ind_sentence in enumerate(response_list):
                tts.add_to_stack(ind_sentence)


if __name__ == "__main__":
        main()
