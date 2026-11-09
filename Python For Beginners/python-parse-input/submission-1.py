from typing import List

def read_integers() -> List[int]:
    user_input = input()
    return [int(n) for n in user_input.split(",")]

    # ret_list = user_input.split(",")

    # for i,s in enumerate(ret_list):
    #     ret_list[i] = int(s)

    # return ret_list
        

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
