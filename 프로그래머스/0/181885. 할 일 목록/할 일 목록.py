def solution(todo_list, finished):
    return [todo_list[i] for i, bool in enumerate(finished) if bool == False]