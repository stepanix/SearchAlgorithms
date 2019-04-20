from search_task.puzzle_state import PuzzleState

import time

import resource

import sys

import math

def main():

#     sm = sys.argv[1].lower()
    
    init_state = '6,1,8,4,0,2,7,3,5'

    begin_state = init_state.split(",")

    begin_state = tuple(map(int, begin_state))
    print(begin_state)
# 
    size = int(math.sqrt(len(begin_state)))
# 
    hard_state = PuzzleState(begin_state, size)
    hard_state.expand()
    hard_state.display()

#     if sm == "bfs":
# 
#         bfs_search(hard_state)
# 
#     elif sm == "dfs":
# 
#         dfs_search(hard_state)
# 
#     elif sm == "ast":
# 
#         A_star_search(hard_state)
# 
#     else:
# 
#         print("Enter valid command arguments !")

if __name__ == '__main__':

    main()