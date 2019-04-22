from ast import literal_eval


class PuzzleState:
    
    generatedNode = set()
    current_move = set()
    parent_children = dict()
    node_count = 0
             
    def __init__(self, config, n, cost=0):
         
        self.cost = cost
 
        self.config = config
 
        self.children = []
         
        self.n = n
         
        self.generatedNode.add(tuple(config))
         
     
    def get_generated_node(self):
        return self.generatedNode
     
    def __node_already_generated(self,testNode):
        for nd in self.generatedNode:
            if nd == testNode:
                return True
             
        return False
             
    def __get_next_movable_element(self, config):
        return min(config)
 
    def expand(self, config):
        self.node_count += 1
        board_elements = []
        for n, i in enumerate(config):
            if n != i:
                board_elements.append(i)
         
        next_displaced_element = self.__get_next_movable_element(board_elements)
        self.generate_child_nodes(next_displaced_element, config)
     
    def generate_child_nodes(self, item, config_tuple):
        config_list = list(config_tuple)
        frontierList = list()
        for n, i in enumerate(config_list):
            if i == item:
                if n != 0 and n != 1 and n != 2:
                    up_config_child = list(config_tuple)
                    target_up_position = self.__move_up(n)
                    up_config_child[n], up_config_child[target_up_position] = up_config_child[target_up_position], up_config_child[n]
                     
                    if not self.__node_already_generated(tuple(up_config_child)):
                        self.generatedNode.add(tuple(up_config_child))
                        frontierList.append((tuple(up_config_child)))
                  
                if n != 6 and n != 7 and n != 8:
                    down_config_child = list(config_tuple)
                    target_down_position = self.__move_down(n)
                    down_config_child[n], down_config_child[target_down_position] = down_config_child[target_down_position], down_config_child[n]
                     
                    if not self.__node_already_generated(tuple(down_config_child)):
                        self.generatedNode.add(tuple(down_config_child))
                        frontierList.append((tuple(down_config_child)))
                     
                if n != 0 and n != 3 and n != 6:
                    left_config_child = list(config_tuple)
                    target_left_position = self.__move_left(n)
                    left_config_child[n], left_config_child[target_left_position] = left_config_child[target_left_position], left_config_child[n]
                    
                    if not self.__node_already_generated(tuple(left_config_child)):
                        self.generatedNode.add(tuple(left_config_child))
                        frontierList.append((tuple(left_config_child)))
                 
                if n != 2 and n != 5 and n != 8:
                    right_config_child = list(config_tuple)
                    target_right_position = self.__move_right(n)
                    right_config_child[n], right_config_child[target_right_position] = right_config_child[target_right_position], right_config_child[n]
                     
                    if not self.__node_already_generated(tuple(right_config_child)):
                        self.generatedNode.add(tuple(right_config_child))
                        frontierList.append((tuple(right_config_child)))
     
        if len(frontierList) > 0:
            parent = str(config_list).replace("[","(").replace("]",")")
            parent = literal_eval(parent)
            child = str(frontierList)
            child = literal_eval(child)
            self.parent_children.update({parent: child})
            frontierList.clear()
             
         
    def __move_left(self, position):
        return position - 1
     
    def __move_right(self, position):
        return position + 1
     
    def __move_up(self, position):
        return position - 3
     
    def __move_down(self, position):
        return position + 3
     
    def get_cost(self):
        return self.cost
    
    def get_nodes_expanded(self):
        return self.node_count
            
#     def get_goal_path(self):
#         for n, i in enumerate(self.parent_children):
#                 print(i, ":", self.parent_children.get(i))
#                 if self.get_goal_parent(self.parent_children.get(i)) == "found":
#                     print(i, self.parent_children.get(i))
#                     return
#      
#     def get_goal_parent(self, children):
#         goalNode = 0,1,2,3,4,5,6,7,8
#         for n, i in enumerate(children):
#             if i == goalNode:
#                 return "found"
#         return "not found"
            
            
            
            