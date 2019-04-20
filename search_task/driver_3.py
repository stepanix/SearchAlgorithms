from search_task.puzzle_state import PuzzleState
from _collections import deque
from search_task.stack import Stack
import heapq

n = 3
initialState = 0,8,2,4,1,3,7,6,5
goalState = 0,1,2,3,4,5,6,7,8

def bfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = deque([initState])
    explored = set()
 
    while frontier:
        node = frontier.pop()
        explored.add(node)
            
        if node == goalState:
            print('explored', explored)
            return "SUCCESS"

        puzzle.expand(node)
         
        for generated_node in puzzle.get_generated_node():
            if generated_node not in frontier and generated_node not in explored:
                frontier.appendleft(generated_node)
    
    return "FAILED"

def dfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = list([initState])
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node)
#     
#         if node == goalState:
# #             print(get_nodes_expanded(explored))
# #             print(puzzle.parent_children)
#             return "SUCCESS"
#         puzzle.expand(node)
#         for neighbour in puzzle.generatedNode:
#             print(neighbour)
#             if neighbour.config not in frontier or neighbour not in explored:
#                 print('explored', node)
#                 frontier.append(neighbour)
#     
#          
#     return "FAILED"
# 
# def ast(initState):
#     puzzle = PuzzleState(initState, n)
#     frontier = [];
#     heapq.heapify(frontier)
#     heapq.heappush(frontier, initState)
#     explored = set()
# 
#     while frontier:
#         node = heapq.heappop(frontier)
#         explored.add(node)
#         
#         if node == goalState:
# #             print(get_nodes_expanded(explored))
#             return "SUCCESS"
#         
#         puzzle.expand(node)
#          
#         for neighbour in puzzle.generatedNode:
#             if neighbour not in frontier or neighbour not in explored:
#                 heapq.heappush(frontier, neighbour)
#                 heapq.heapify(frontier)
#             elif neighbour in frontier:
#                 frontier.append(neighbour)
#                 heapq.heapify(frontier)
#                
#     return "FAILED"

print(bfs(initialState))

    
