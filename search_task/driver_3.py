from search_task.puzzle_state import puzzle_state
from _collections import deque
import heapq

initialState = 1,2,5,3,4,0,6,7,8
goalState = 0,1,2,3,4,5,6,7,8

def bfs(initState):
    
    puzzle = puzzle_state(initState)
    frontier = deque([initState])
    frontier_set = set()
    explored = set()
    
    while frontier:
        frontier_set = frontier
        node = frontier.pop()
        explored.add(node)
            
        if node == goalState:
            print('nodes_expanded:', puzzle.get_nodes_expanded())
            print('explored nodes:', explored)
            print('parent children:', puzzle.parent_children)
            return "SUCCESS"
        
        puzzle.expand(node)
               
        for generated_node in puzzle.get_generated_node():
            if generated_node in frontier_set or generated_node in explored:
                continue
            else:
                frontier.appendleft(generated_node)
            
    return "FAILED"

def dfs(initState):
    puzzle = puzzle_state(initState)
    frontier = deque([initState])
    frontier_set = set()
    explored = set()

    while frontier:
        frontier_set = frontier
        node = frontier.pop()
#         print('frontier pop', node)
        explored.add(node)

        if node == goalState:
            print('nodes_expanded:', puzzle.get_nodes_expanded())
            print('explored nodes:', explored)
            print('parent children:', puzzle.parent_children)
            return "SUCCESS"
        
        puzzle.expand(node)
        print('nodes_expanded:', puzzle.get_nodes_expanded())
        
        for generated_node in puzzle.get_reverse_generated_node():
            if generated_node in frontier_set or generated_node in explored:
                continue
            else:
                frontier.append(generated_node)
        
    return "FAILED"

def ast(initState):
    puzzle = puzzle_state(initState)
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, initState)
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        explored.add(node)
        
        if node == goalState:
            print('nodes_expanded:', puzzle.get_nodes_expanded())
            return "SUCCESS"
        
        puzzle.expand(node)
        print('nodes_expanded:', puzzle.get_nodes_expanded())
         
        for neighbour in puzzle.get_generated_node():
            if neighbour not in frontier and neighbour not in explored:
                heapq.heappush(frontier, neighbour)
                heapq.heapify(frontier)
            elif neighbour in frontier:
                frontier.append(neighbour)
                heapq.heapify(frontier)
               
    return "FAILED"

print(dfs(initialState))


    
