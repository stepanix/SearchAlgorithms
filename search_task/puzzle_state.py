
class PuzzleState(object):
    
    generatedNode = set()
            
    def __init__(self, config, n, parent=None, cost=0):
        
        self.cost = cost

        self.parent = parent

        self.config = config

        self.children = []
        
        self.n = n
        
        self.generatedNode.add(tuple(config))
        
    
    def node_already_generated(self,testNode):
        for nd in self.generatedNode:
            if nd == testNode:
                return True
            
        return False

            
    def get_next_movable_element(self, config):
        return min(config)

    def expand(self, config):
        board_elements = []
        for n, i in enumerate(config):
            if n != i:
                board_elements.append(i)
        
        next_movable_item = self.get_next_movable_element(board_elements)
        self.generate_child_nodes(next_movable_item, config)
    
    def generate_child_nodes(self, item, config_tuple):
        config_list = list(config_tuple)
        for n, i in enumerate(config_list):
            if i == item:
                if n != 0 and n != 1 and n != 2:
                    up_config_child = list(config_tuple)
                    target_up_position = self.move_up(n)
                    up_config_child[n], up_config_child[target_up_position] = up_config_child[target_up_position], up_config_child[n]
                    self.cost += 1
                    if not self.node_already_generated(tuple(up_config_child)):
                        self.generatedNode.add(tuple(up_config_child))
                 
                if n != 6 and n != 7 and n != 8:
                    down_config_child = list(config_tuple)
                    target_down_position = self.move_down(n)
                    down_config_child[n], down_config_child[target_down_position] = down_config_child[target_down_position], down_config_child[n]
                    self.cost += 1
                    if not self.node_already_generated(tuple(down_config_child)):
                        self.generatedNode.add(tuple(down_config_child))
                    
                if n != 0 and n != 3 and n != 6:
                    left_config_child = list(config_tuple)
                    target_left_position = self.move_left(n)
                    left_config_child[n], left_config_child[target_left_position] = left_config_child[target_left_position], left_config_child[n]
                    self.cost += 1
                    if not self.node_already_generated(tuple(left_config_child)):
                        self.generatedNode.add(tuple(left_config_child))
                
                if n != 2 and n != 5 and n != 8:
                    right_config_child = list(config_tuple)
                    target_right_position = self.move_right(n)
                    right_config_child[n], right_config_child[target_right_position] = right_config_child[target_right_position], right_config_child[n]
                    self.cost += 1
                    if not self.node_already_generated(tuple(right_config_child)):
                        self.generatedNode.add(tuple(right_config_child))
                           
            
        
    def move_left(self, position):
        return position - 1
    
    def move_right(self, position):
        return position + 1
    
    def move_up(self, position):
        return position - 3
    
    def move_down(self, position):
        return position + 3
    
    def get_cost(self):
        print(self.cost)
           
            
#     def move_left(self):
# 
#         if self.blank_col == 0:
# 
#             return None
# 
#         else:
# 
#             blank_index = self.blank_row * self.n + self.blank_col
# 
#             target = blank_index - 1
# 
#             new_config = list(self.config)
# 
#             new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
# 
#             return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)
            
            
#     def move_right(self):
# 
#         if self.blank_col == self.n - 1:
# 
#             return None
# 
#         else:
# 
#             blank_index = self.blank_row * self.n + self.blank_col
# 
#             target = blank_index + 1
# 
#             new_config = list(self.config)
# 
#             new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
# 
#             return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)
        
        
#     def move_up(self):
# 
#         if self.blank_row == 0:
# 
#             return None
# 
#         else:
# 
#             blank_index = self.blank_row * self.n + self.blank_col
# 
#             target = blank_index - self.n
# 
#             new_config = list(self.config)
# 
#             new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
# 
#             return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

#     def move_down(self):
# 
#         if self.blank_row == self.n - 1:
# 
#             return None
# 
#         else:
# 
#             blank_index = self.blank_row * self.n + self.blank_col
# 
#             target = blank_index + self.n
# 
#             new_config = list(self.config)
# 
#             new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
# 
#             return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)
        
        
#     def expand(self):
# 
#         """expand the node"""
# 
#         # add child nodes in order of UDLR
# 
#         if len(self.children) == 0:
# 
#             up_child = self.move_up()
# 
#             if up_child is not None:
# 
#                 self.children.append(up_child)
# 
#             down_child = self.move_down()
# 
#             if down_child is not None:
# 
#                 self.children.append(down_child)
# 
#             left_child = self.move_left()
# 
#             if left_child is not None:
# 
#                 self.children.append(left_child)
# 
#             right_child = self.move_right()
# 
#             if right_child is not None:
# 
#                 self.children.append(right_child)
# 
#         return self.children
            
            
            
            