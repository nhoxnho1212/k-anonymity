from Node import Node

class DGH:
    def __init__(self, file_name = None):
        self.__flat_list = []
        self.domain = self.read_file(file_name)
        self.max_height = self.__max_height(self.domain)

    def read_file(self, file_name = None):
        dgh = []
        with open(file_name, 'r') as fr:
            arr_row = fr.readlines()
            for cur_row in arr_row:
                cur_row = cur_row.replace('\n', '')
                sub_tree = cur_row.split(';')
                child = [[Node(i) for i in idx.split(',')] for idx in sub_tree]
                dgh.append(child)

        for idx_group_node in range(len(dgh)-1):
            group_node = dgh[idx_group_node]
            next_flat_group_node = [i for idx in dgh[idx_group_node + 1] for i in idx]
            self.__flat_list.append([i.data for idx in dgh[idx_group_node] for i in idx])
            for idx_node, node_list in enumerate(group_node):
                for node in node_list:
                    node.next = next_flat_group_node[idx_node]

        self.__flat_list.append([i.data for idx in dgh[-1] for i in idx])
        return dgh

    def next_gen(self, value):
        status = False
        result = None
        for group_node in self.domain:
            for node_list in group_node:
                for node in node_list:
                    if node.data == value:
                        status = True
                        if node.next:
                            result = node.next.data
                        break
                if status:
                    break
        
        return (status, result)

    def __max_height(self, domain = None):
        return len(domain)

    def height(self, value):
        height = None
        for idx, l in enumerate(self.__flat_list):
            if value in l:
                height = idx
                break
        return height


