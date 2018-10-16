from search_task.puzzle_state import PuzzleState
from _collections import deque
from search_task.stack import Stack
import heapq

n = 9

initialState = 1,8,7,6,5,4,3,2,0
goalState = 0,1,2,3,4,5,6,7,8

puzzle = PuzzleState(initialState, n)
puzzle.expand(initialState)

def bfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = deque([initState])
    explored = set()
      
    while frontier:
        node = frontier.popleft()
        explored.add(node)
         
        if node == goalState:
            print(puzzle.generatedNode)
            return "SUCCESS"
        puzzle.expand(node)
        
        for neighbour in puzzle.generatedNode:
            if neighbour not in frontier and neighbour not in explored:
                frontier.appendleft(neighbour)
         
    return "FAILED"

def dfs(initState):
    puzzle = PuzzleState(initState, n)
    frontier = Stack(initState)
    explored = set()
            
    while frontier:
        node = frontier.pop()
        explored.add(node)
    
        if node == goalState:
            print(puzzle.generatedNode)
            return "SUCCESS"
        puzzle.expand(node)
        
        for neighbour in puzzle.generatedNode:
            if neighbour not in frontier.elements() and neighbour not in explored:
                frontier.push(neighbour)
                
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
            print(puzzle.generatedNode)
            return "SUCCESS"
        
        puzzle.expand(node)
         
        for neighbour in puzzle.generatedNode:
            if neighbour not in frontier and neighbour not in explored:
                heapq.heappush(frontier, neighbour)
                heapq.heapify(frontier)
            elif neighbour in frontier:
                frontier.append(neighbour)
                heapq.heapify(frontier)
               
    return "FAILED"

print(dfs(initialState))
    
