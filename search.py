from search_queue import FIFOQueue, PriorityQueue

# function: breath_first_search
# inputs:
#   image: 2D array of pixels
#   start: (x, y) tuple representing starting pixel
#   goal: (x, y) tuple representing goal pixel
# pre-conditions:
#   image is a non-empty 2D array
#   start and goal are valid pixel coordinates within image
# output:
#   path: list of (x, y) tuples representing path from start to goal
#   visited: dictionary mapping (x, y) tuples to boolean indicating if pixel was visited
# relationships:
#   
# pseudocode:
#   unified_search(image, start, goal, FIFOQueue)
def breath_first_search(image, start, goal):
    return unified_search(image, start, goal, FIFOQueue)

# function: best_first_search
# inputs:
#   image: 2D array of pixels
#   start: (x, y) tuple representing starting pixel
#   goal: (x, y) tuple representing goal pixel
# pre-conditions:
#   image is a non-empty 2D array
#   start and goal are valid pixel coordinates within image
# output:
#   path: list of (x, y) tuples representing path from start to goal
#   visited: dictionary mapping (x, y) tuples to boolean indicating if pixel was visited
# relationships:
#   
# pseudocode:
#   unified_search(image, start, goal, PriorityQueue, manhattan_distance)
def best_first_search(image, start, goal):
    return unified_search(image, start, goal, PriorityQueue, manhattan_distance)


# function: unified_search
# inputs:
#   image: 2D array of pixels
#   start: (x, y) tuple representing starting pixel
#   goal: (x, y) tuple representing goal pixel
#   queue_type: class of search queue to use (FIFOQueue or PriorityQueue)
#   heuristic: function to calculate heuristic distance (optional)
# pre-conditions:
#   image is a non-empty 2D array
#   start and goal are valid pixel coordinates within image
# output:
#   path: list of (x, y) tuples representing path from start to goal
#   visited: dictionary mapping (x, y) tuples to boolean indicating if pixel was visited
# relationships:
#   
# pseudocode:
#   initialize queue of type queue_type
#   initialize visited, distance, prev dictionaries
#   mark start as visited, set its distance
#   insert start into queue with priority
#   while queue not empty and goal not visited:
#    pop vertex u from queue
#    for each neighbor v of u:
#       if v not visited:
#          mark v as visited
#          set distance and prev for v
#          calculate priority and insert v into queue
#   reconstruct path from start to goal using prev
#   return path and visited
def unified_search(image, start, goal, queue_type, heuristic=None):
    queue = queue_type()
    visited = {}
    distance = {}
    prev = {}
    
    # Initial setup
    visited[start] = True
    distance[start] = heuristic(start, goal) if heuristic else 0
    queue.insert(start, distance[start])
    
    while not queue.is_empty() and goal not in visited:
        u = queue.pop()
        
        for v in get_neighbors(u, image):
            if v not in visited:
                visited[v] = True
                distance[v] = distance[u] + 1
                prev[v] = u
                
                # Calculate priority
                priority = distance[v] + (heuristic(v, goal) if heuristic else 0)
                queue.insert(v, priority)
    
    return reconstruct_path(prev, start, goal), visited

# function: manhattan_distance
# inputs:
#   from_vertex: (x, y) tuple representing current pixel
#   goal: (x, y) tuple representing goal pixel
# output:
#   distance: integer representing Manhattan distance between from_vertex and goal
# relationships:
#   used as heuristic in best_first_search
#pseudocode:
#   return abs(from_vertex[0] - goal[0]) + abs(from_vertex[1] - goal[1])
def manhattan_distance(from_vertex, goal):
    return abs(from_vertex[0] - goal[0]) + abs(from_vertex[1] - goal[1])

# function: get_neighbors
# inputs:
#   origin_vertex: (x, y) tuple representing current pixel
#   image: 2D array of pixels
# output:
#   neighbors: list of (x, y) tuples representing valid neighboring pixels
# relationships:
#   used in unified_search to find adjacent pixels
# pseudocode:
#   for each direction in [up, down, left, right]:
#       calculate new coordinates
#       if new coordinates are in bounds and pixel values meet criteria:
#           add to neighbors
#   return neighbors
def get_neighbors(origin_vertex, image):
    row, col = origin_vertex
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    
    neighbors = []
    # up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Check if in bounds
        if 0 <= new_row < height and 0 <= new_col < width:
            # Check if pixel values are: 
            #          R > 100 or G > 100 or B > 100
            pixel = image[new_row][new_col]
            if pixel[0] > 100 or pixel[1] > 100 or pixel[2] > 100:
                neighbors.append((new_row, new_col))
    
    return neighbors

# function: reconstruct_path
# inputs:
#   prev: dictionary mapping (x, y) tuples to their predecessor in the path
#   start: (x, y) tuple representing starting pixel
#   goal: (x, y) tuple representing goal pixel
# output:
#   path: list of (x, y) tuples representing path from start to goal
# relationships:
#   used in unified_search to build the final path
# pseudocode:
#   if goal not in prev and goal != start:
#       return []
#   initialize empty path list
#   set current to goal
#   while current != start:
#       append current to path
#       set current to prev[current]
#   append start to path
#   reverse path
#   return path
def reconstruct_path(prev, start, goal):
    # Check if goal was reached
    if goal not in prev and goal != start:
        return []
    
    path = []
    current = goal
    
    while current != start:
        path.append(current)
        current = prev[current]
    
    # Add start to path
    path.append(start)
    
    # Reverse to get path from start to end
    path.reverse()
    
    return path
