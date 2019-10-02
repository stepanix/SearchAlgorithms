from ast import literal_eval


class puzzle_state:
    
    generatedNode = []
    current_move = []
    parent_children = dict()
    node_count = 0
             
    def __init__(self, config, cost=0):
         
        self.cost = cost
 
        self.config = config
 
        self.children = []
         
        self.generatedNode.append(tuple(config))
     
    def get_generated_node(self):
        return self.generatedNode
    
    def get_reverse_generated_node(self):
        rev = self.generatedNode
        rev.reverse()
        return rev
    
    def get_moves(self):
        return self.current_move
     
    def __node_already_generated(self,testNode):
        for nd in self.generatedNode:
            if nd == testNode:
                return True
             
        return False
             
    def __get_next_movable_element(self, config):
        return min(config)
    
    def expand(self, config):
        self.node_count += 1
        self.generate_child_nodes(config)
        
    def _can_move_up(self, index, blank_element):
        return blank_element == 0 and index != 0 and index != 1 and index != 2
        
    def _can_move_down(self, index, blank_element):
        return blank_element == 0 and index != 6 and index != 7 and index != 8
        
    def _can_move_left(self, index, blank_element):
        return blank_element == 0 and index != 0 and index != 3 and index != 6
    
    def _can_move_right(self, index, blank_element):
        return blank_element == 0 and index != 2 and index != 5 and index != 8
    
    def generate_child_nodes(self, config_tuple):
        config_list = list(config_tuple)
        frontierList = list()
        
        for index, element in enumerate(config_list):

            if self._can_move_up(index, element):
                up_config_child = list(config_tuple)
                target_up_position = self.__move_up(index)
                up_config_child[index], up_config_child[target_up_position] = up_config_child[target_up_position], up_config_child[index]
                 
                if not self.__node_already_generated(tuple(up_config_child)):
                    self.generatedNode.append(tuple(up_config_child))
                    frontierList.append((tuple(up_config_child)))
                    self.current_move.append('up')
              
            if self._can_move_down(index, element):
                down_config_child = list(config_tuple)
                target_down_position = self.__move_down(index)
                down_config_child[index], down_config_child[target_down_position] = down_config_child[target_down_position], down_config_child[index]
                 
                if not self.__node_already_generated(tuple(down_config_child)):
                    self.generatedNode.append(tuple(down_config_child))
                    frontierList.append((tuple(down_config_child)))
                    self.current_move.append('down')
                 
            if self._can_move_left(index, element):
                left_config_child = list(config_tuple)
                target_left_position = self.__move_left(index)
                left_config_child[index], left_config_child[target_left_position] = left_config_child[target_left_position], left_config_child[index]
                
                if not self.__node_already_generated(tuple(left_config_child)):
                    self.generatedNode.append(tuple(left_config_child))
                    frontierList.append((tuple(left_config_child)))
                    self.current_move.append('left')
             
            if self._can_move_right(index, element):
                right_config_child = list(config_tuple)
                target_right_position = self.__move_right(index)
                right_config_child[index], right_config_child[target_right_position] = right_config_child[target_right_position], right_config_child[index]
                 
                if not self.__node_already_generated(tuple(right_config_child)):
                    self.generatedNode.append(tuple(right_config_child))
                    frontierList.append((tuple(right_config_child)))
                    self.current_move.append('right')
     
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
    
            
            
            