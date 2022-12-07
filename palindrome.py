def solution(S):
    
    input_str_list = list(S)
    left_pointer, right_pointer = 0 , len(S) - 1
    while left_pointer <= right_pointer:
        if input_str_list[left_pointer] == "?":
            if input_str_list[right_pointer] == "?":
                input_str_list[left_pointer], input_str_list[right_pointer] = "a", "a"
            else:
                input_str_list[left_pointer] = S[right_pointer]
        if input_str_list[right_pointer] == "?":
            if input_str_list[left_pointer] == "?":
                input_str_list[left_pointer], input_str_list[right_pointer] = "a", "a"
            else:
                input_str_list[right_pointer] = S[left_pointer]
        if input_str_list[left_pointer] != input_str_list[right_pointer]:
            return "NO"
        left_pointer, right_pointer = left_pointer + 1, right_pointer - 1
    return "".join(input_str_list)

print(solution("?ab??aa"))