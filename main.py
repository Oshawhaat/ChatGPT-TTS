from gpt import gpt
import tts
import time


SPLIT_POINTS = [
#       ("str", keep_at_end)
        (".", True),
        ("!", True),
        ("?", True),
        ("\n", False),
]

SPLIT_BLACKLIST = [
#       ("split str", "dont split if followed by this")
        ( ".", "\"" ),
        ( "!", "\"" ),
        ( "?", "\"" ),
]


def main():
        _gpt = gpt()
        
        while True:
                if tts.message_stack:
                        continue
                
                message = input("\nWhat kind of joke would you like? : ")
                
                if message == "r":
                        _gpt = gpt()
                        continue
                if message == "q":
                        quit()
                        break

                raw_response = _gpt.ask_msg(message)
                
                response_list = process_response(raw_response)
                
                tts.add_list_to_stack(response_list)
                
                while not tts.message_stack:
                        time.sleep(1)
                time.sleep(2)


def split_response(response: str, split_points: list, split_blacklist: list):
        response_list = [response]
        
        for split_str, keep_at_end in split_points:
                new_response_list = []
                
                for response in response_list:
                        split_response = split_lines(response, split_str, keep_at_end, split_blacklist)
                        
                        new_response_list += split_response
                
                response_list = new_response_list
        
        return response_list


def split_lines(response: str, split_str: str, keep_at_end: bool, split_blacklist: list):
        split_list = response.split(split_str)
        
        if keep_at_end and len(split_list) > 1:
                for ind in range(0, len(split_list) - 1):
                        split_list[ind] += split_str
        
        del_inds = []
        
        for first, last in split_blacklist:
                for ind in range(len(split_list) - 1):
                        if split_list[ind].endswith(first) and split_list[ind+1].startswith(last):
                                split_list[ind] += split_list[ind+1]
                                del_inds.append(ind+1)
        
        for ind in reversed(del_inds):
                del split_list[ind]
        
        return split_list


def clean_response_list(responses: list, str_blacklists: list):
        responses_wo_spaces = [ x.removeprefix(" ") for x in responses ]
        cleaned_responses = [ x for x in responses_wo_spaces if x and x not in str_blacklists ]

        return cleaned_responses


def process_response(raw_response: str):
        raw_split_responses = split_response(raw_response, SPLIT_POINTS, SPLIT_BLACKLIST)
        cleaned_response_list = clean_response_list(raw_split_responses, SPLIT_POINTS)
        
        return cleaned_response_list


if __name__ == "__main__":
        main()
