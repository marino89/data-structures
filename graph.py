from collections import deque


def breath_first_search(graph, root):
    graph_queue = deque([root])
    visited_vertices = [root]
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adjacent_nodes = graph[node]
        
        visited_nodes = set(visited_vertices)
        remaining_nodes = set(adjacent_nodes).difference(visited_nodes)
        
        if len(remaining_nodes) > 0:
            for elt in sorted(remaining_nodes):
                visited_vertices.append(elt)
                graph_queue.append(elt)
    
    return visited_vertices


def depth_first_search(graph, root):
    visited_vertices = []
    graph_stack = [root]

    node = root
    while len(graph_stack) > 0:

        if node not in visited_vertices:
            visited_vertices.append(node)
        
        adjacent_nodes = graph[node]

        if set(adjacent_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()    
       
            if len(graph_stack):
                node = graph_stack[-1]
                continue
        else:
            remaining_elements = set(adjacent_nodes).difference(set(visited_vertices))
            first_adjacent_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adjacent_node)
            node = first_adjacent_node
    
    return visited_vertices


if __name__ == '__main__':
    graph_dict = {
    'A': ['B', 'C'],
    'B': ['E', 'A'],
    'C': ['A', 'B', 'E', 'F'],
    'E': ['B', 'C'],
    'F': ['C'],
    }
    matrix_elements = sorted(graph_dict.keys())
    n_cols = n_rows = len(matrix_elements)
    adjacency_matrix = [[0 for _ in range(n_rows)] for _ in range(n_cols)]
    edges_list = []

    for key in matrix_elements:
        for neighbor in graph_dict[key]:
            edges_list.append((key, neighbor))

    for edge in edges_list:
        index_of_first_vertex = matrix_elements.index(edge[0])
        index_of_second_vertex = matrix_elements.index(edge[1])
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

    print(adjacency_matrix)

    print(breath_first_search(graph_dict, root='A'))

    print(depth_first_search(graph_dict, root='A'))
