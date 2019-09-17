from search_task.puzzle_state import PuzzleState
from _collections import deque
from search_task.stack import Stack
import heapq

n = 3
initialState = 1,2,5,3,4,0,6,7,8
goalState = 0,1,2,3,4,5,6,7,8

def bfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = deque([initState])
    explored = set()
 
    while frontier:
        node = frontier.pop()
        explored.add(node)
            
        if node == goalState:
            print('nodes_expanded:', puzzle.get_nodes_expanded())
            print('explored nodes:', explored)
            print('parent children:', puzzle.parent_children)
            return "SUCCESS"

        puzzle.expand(node)
         
        for generated_node in puzzle.get_generated_node():
            if generated_node not in frontier and generated_node not in explored:
                frontier.appendleft(generated_node)
    
    return "FAILED"

def dfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = Stack(initState)
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node)

        if node == goalState:
            print('nodes_expanded:', puzzle.get_nodes_expanded())
            return "SUCCESS"
        
        puzzle.expand(node)
        
        for generated_node in puzzle.get_generated_node():
            if generated_node not in frontier.elements() and generated_node not in explored:
                frontier.push(generated_node)
          
    return "FAILED"

def ast(initState):
    puzzle = PuzzleState(initState, n)
    frontier = [];
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
         
        for neighbour in puzzle.get_generated_node():
            if neighbour not in frontier and neighbour not in explored:
                heapq.heappush(frontier, neighbour)
                heapq.heapify(frontier)
            elif neighbour in frontier:
                frontier.append(neighbour)
                heapq.heapify(frontier)
               
    return "FAILED"

print(bfs(initialState))


    
