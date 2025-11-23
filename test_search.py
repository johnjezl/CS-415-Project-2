import pytest
from search import *

#########################################################
# Test cases for get_neighbors function
#########################################################

def test_get_neighbors_center_pixel():
    image = [
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)]
    ]
    neighbors = get_neighbors((1, 1), image)
    assert len(neighbors) == 4
    assert (0, 1) in neighbors
    assert (2, 1) in neighbors

def test_get_neighbors_invalid_pixels():
    # Test RGB threshold
    image = [
        [(50, 50, 50), (255, 0, 0)],  # Left pixel invalid
        [(0, 255, 0), (0, 0, 255)]
    ]
    neighbors = get_neighbors((0, 0), image)
# get_neighbors does not validate the origin pixel itself
#    assert len(neighbors) == 0  # No valid neighbors
    assert len(neighbors) == 2
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors  

def test_get_neighbors_edge_pixel():
    image = [
        [(255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255)]
    ]
    neighbors = get_neighbors((0, 0), image)
    assert len(neighbors) == 2
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors

def test_get_neighbors_corner_pixel():
    image = [
        [(255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255)]
    ]
    neighbors = get_neighbors((0, 1), image)
    assert len(neighbors) == 2
    assert (0, 0) in neighbors
    assert (1, 1) in neighbors

def test_get_neighbors_mixed_pixels():
    image = [
        [(255, 255, 255), (50, 50, 50), (255, 0, 0)],
        [(0, 255, 0), (50, 50, 50), (0, 0, 255)],
        [(255, 255, 255), (255, 255, 255), (50, 50, 50)]
    ]
    neighbors = get_neighbors((1, 1), image)
    assert len(neighbors) == 3
    assert (0, 1) not in neighbors
    assert (1, 0) in neighbors
    assert (1, 2) in neighbors
    assert (2, 1) in neighbors  

def test_get_neighbors_single_valid_neighbor():
    image = [
        [(50, 50, 50), (255, 255, 255)],
        [(50, 50, 50), (50, 50, 50)]
    ]
    neighbors = get_neighbors((0, 0), image)
    assert len(neighbors) == 1
    assert (0, 1) in neighbors

def test_get_neighbors_no_valid_neighbors_origin_invalid():
    image = [
        [(50, 50, 50), (50, 50, 50)],
        [(50, 50, 50), (50, 50, 50)]
    ]
    neighbors = get_neighbors((0, 0), image)
    assert len(neighbors) == 0  # No valid neighbors


#########################################################
# Test cases for reconstruct_path function
#########################################################

def test_reconstruct_path_no_path():
    prev = {}
    path = reconstruct_path(prev, (0, 0), (5, 5))
    assert path == []

def test_reconstruct_path_valid_path():
    prev = {
        (0, 0): None,
        (0, 1): (0, 0),
        (1, 1): (0, 1),
        (1, 2): (1, 1)
    }
    path = reconstruct_path(prev, (0, 0), (1, 2))
    assert path == [(0, 0), (0, 1), (1, 1), (1, 2)]

def test_reconstruct_path_start_equals_goal():
    prev = {}
    path = reconstruct_path(prev, (2, 2), (2, 2))
    assert path == [(2, 2)] 

def test_reconstruct_path_partial_path():
    prev = {
        (0, 0): None,
        (0, 1): (0, 0),
        (1, 1): (0, 1)
    }
    path = reconstruct_path(prev, (0, 0), (1, 2))
    assert path == []  # No path to (1, 2)

def test_get_neighbors_no_valid_neighbors():
    image = [
        [(50, 50, 50), (50, 50, 50)],
        [(50, 50, 50), (50, 50, 50)]
    ]
    neighbors = get_neighbors((0, 0), image)
    assert len(neighbors) == 0  # No valid neighbors
    
def test_reconstruct_path_single_step():
    prev = {
        (0, 0): None,
        (0, 1): (0, 0)
    }
    path = reconstruct_path(prev, (0, 0), (0, 1))
    assert path == [(0, 0), (0, 1)]

def test_reconstruct_path_long_path():
    prev = {
        (0, 0): None,
        (0, 1): (0, 0),
        (0, 2): (0, 1),
        (1, 2): (0, 2),
        (2, 2): (1, 2)
    }
    path = reconstruct_path(prev, (0, 0), (2, 2))
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]



#########################################################
# Additional test cases for manhattan_distance function
#########################################################

def test_manhattan_distance():
    assert manhattan_distance((0, 0), (3, 4)) == 7
    assert manhattan_distance((5, 5), (5, 5)) == 0
    assert manhattan_distance((1, 2), (4, 6)) == 7

def test_manhattan_distance_negative_coordinates():
    assert manhattan_distance((-1, -1), (1, 1)) == 4
    assert manhattan_distance((-3, 2), (3, -2)) == 10
    assert manhattan_distance((0, 0), (-4, -5)) == 9

def test_manhattan_distance_large_coordinates():
    assert manhattan_distance((1000, 2000), (3000, 4000)) == 4000
    assert manhattan_distance((12345, 67890), (54321, 98765)) == 72851
    assert manhattan_distance((0, 0), (100000, 100000)) == 200000

def test_manhattan_distance_same_row(): 
    assert manhattan_distance((2, 3), (2, 10)) == 7
    assert manhattan_distance((5, 0), (5, 15)) == 15
    assert manhattan_distance((0, 7), (0, 2)) == 5

def test_manhattan_distance_same_column():
    assert manhattan_distance((3, 4), (10, 4)) == 7
    assert manhattan_distance((0, 5), (15, 5)) == 15
    assert manhattan_distance((7, 0), (2, 0)) == 5

def test_manhattan_distance_diagonal():
    assert manhattan_distance((1, 1), (4, 4)) == 6
    assert manhattan_distance((2, 3), (5, 6)) == 6
    assert manhattan_distance((0, 0), (3, 3)) == 6

def test_manhattan_distance_zero_coordinates():
    assert manhattan_distance((0, 0), (0, 0)) == 0
    assert manhattan_distance((0, 5), (0, 0)) == 5
    assert manhattan_distance((7, 0), (0, 0)) == 7

def test_manhattan_distance_large_negative_coordinates():
    assert manhattan_distance((-1000, -2000), (-3000, -4000)) == 4000
    assert manhattan_distance((-12345, -67890), (-54321, -98765)) == 72851
    assert manhattan_distance((0, 0), (-100000, -100000)) == 200000

def test_manhattan_distance_mixed_coordinates():
    assert manhattan_distance((-1, 2), (3, -4)) == 10
    assert manhattan_distance((5, -5), (-5, 5)) == 20
    assert manhattan_distance((-10, 0), (0, 10)) == 20

def test_manhattan_distance_fractional_coordinates():
    assert manhattan_distance((1.5, 2.5), (4.5, 6.5)) == 7.0
    assert manhattan_distance((-1.2, -3.4), (2.3, 4.5)) == 11.4
    assert manhattan_distance((0.0, 0.0), (3.3, 4.4)) == 7.7

def test_manhattan_distance_large_mixed_coordinates():
    assert manhattan_distance((-1000, 2000), (3000, -4000)) == 10000
    assert manhattan_distance((12345, -67890), (-54321, 98765)) == 233321
    assert manhattan_distance((0, 0), (100000, -100000)) == 200000

def test_manhattan_distance_identical_coordinates():
    assert manhattan_distance((42, 42), (42, 42)) == 0
    assert manhattan_distance((-99, -99), (-99, -99)) == 0
    assert manhattan_distance((0, 0), (0, 0)) == 0


# ============================================================================
# Breadth-First Search Tests
# ============================================================================

def test_bfs_simple_straight_path():
    """Test BFS with a simple straight line path"""
    image = [
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = breath_first_search(image, start, goal)
    
    assert len(path) == 3
    assert path[0] == start
    assert path[-1] == goal
    assert (0, 1) in path  # Should go through middle


def test_bfs_path_with_obstacle():
    """Test BFS pathfinding around an obstacle"""
    image = [
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],  # obstacle in middle
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = breath_first_search(image, start, goal)
    
    # Path must go around the obstacle
    assert len(path) > 3  # Longer than direct path
    assert (0, 1) not in path  # Can't go through obstacle


def test_bfs_no_path_exists():
    """Test BFS when goal is unreachable"""
    image = [
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = breath_first_search(image, start, goal)
    
    assert path == []
    assert goal not in visited


def test_bfs_start_equals_goal():
    """Test BFS when start and goal are the same"""
    image = [[(255, 255, 255)]]
    start = (0, 0)
    goal = (0, 0)
    path, visited = breath_first_search(image, start, goal)
    
    assert len(path) == 1
    assert path[0] == start


def test_bfs_large_maze():
    """Test BFS on a larger grid"""
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (100, 100, 100), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (4, 4)
    path, visited = breath_first_search(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal


def test_bfs_visited_dictionary():
    """Test that BFS visited dictionary is correctly populated"""
    image = [
        [(255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255)]
    ]
    start = (0, 0)
    goal = (1, 1)
    path, visited = breath_first_search(image, start, goal)
    
    assert start in visited
    assert goal in visited
    assert visited[start] == True
    assert visited[goal] == True


def test_bfs_single_pixel_image():
    """Test BFS with a 1x1 image"""
    image = [[(200, 200, 200)]]
    start = (0, 0)
    goal = (0, 0)
    path, visited = breath_first_search(image, start, goal)
    
    assert path == [(0, 0)]
    assert visited[(0, 0)] == True


def test_bfs_diagonal_path():
    """Test BFS diagonal path (requires multiple steps, not direct diagonal)"""
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (2, 2)
    path, visited = breath_first_search(image, start, goal)
    
    assert len(path) == 5  # Manhattan distance of 4, plus start
    assert path[0] == start
    assert path[-1] == goal


# ============================================================================
# Best-First Search (A*) Tests
# ============================================================================

def test_astar_simple_straight_path():
    """Test A* with a simple straight line path"""
    image = [
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)]
    ]
    start = (0, 0)
    goal = (2, 2)
    path, visited = best_first_search(image, start, goal)
    
    assert len(path) == 5  # Shortest path in 4-connected grid
    assert path[0] == start
    assert path[-1] == goal


def test_astar_path_with_obstacle():
    """Test A* pathfinding around an obstacle"""
    image = [
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = best_first_search(image, start, goal)
    
    assert len(path) > 3
    assert (0, 1) not in path


def test_astar_no_path_exists():
    """Test A* when goal is unreachable"""
    image = [
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = best_first_search(image, start, goal)
    
    assert path == []
    assert goal not in visited


def test_astar_start_equals_goal():
    """Test A* when start and goal are the same"""
    image = [[(255, 255, 255)]]
    start = (0, 0)
    goal = (0, 0)
    path, visited = best_first_search(image, start, goal)
    
    assert len(path) == 1
    assert path[0] == start


def test_astar_fewer_visited_than_bfs():
    """Test that A* visits fewer or equal nodes than BFS"""
    # Create a grid where the goal is in a specific direction
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (4, 4)
    
    bfs_path, bfs_visited = breath_first_search(image, start, goal)
    astar_path, astar_visited = best_first_search(image, start, goal)
    
    # Both should find a path of the same length
    assert len(bfs_path) == len(astar_path)
    
    # A* should visit fewer or equal nodes
    assert len(astar_visited) <= len(bfs_visited)


def test_astar_same_path_length_as_bfs():
    """Test that both algorithms find shortest path of same length"""
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (2, 3)
    
    bfs_path, _ = breath_first_search(image, start, goal)
    astar_path, _ = best_first_search(image, start, goal)
    
    # Both should find paths of the same length (both optimal)
    assert len(bfs_path) == len(astar_path)


def test_astar_large_grid():
    """Test A* on a larger grid"""
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (100, 100, 100), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (100, 100, 100), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (4, 5)
    path, visited = best_first_search(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal


# ============================================================================
# Tests for Both Algorithms (using parametrize)
# ============================================================================

@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_l_shaped_path(search_func):
    """Test an L-shaped path"""
    image = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(100, 100, 100), (100, 100, 100), (255, 0, 0)],
        [(100, 100, 100), (100, 100, 100), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (2, 2)
    path, visited = search_func(image, start, goal)
    
    assert len(path) == 5
    assert path[0] == start
    assert path[-1] == goal


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_rgb_threshold_r_channel(search_func):
    """Test that R > 100 makes a valid pixel"""
    image = [
        [(200, 0, 0), (200, 0, 0)],
        [(200, 0, 0), (200, 0, 0)]
    ]
    start = (0, 0)
    goal = (1, 1)
    path, visited = search_func(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_rgb_threshold_g_channel(search_func):
    """Test that G > 100 makes a valid pixel"""
    image = [
        [(0, 200, 0), (0, 200, 0)],
        [(0, 200, 0), (0, 200, 0)]
    ]
    start = (0, 0)
    goal = (1, 1)
    path, visited = search_func(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_rgb_threshold_b_channel(search_func):
    """Test that B > 100 makes a valid pixel"""
    image = [
        [(0, 0, 200), (0, 0, 200)],
        [(0, 0, 200), (0, 0, 200)]
    ]
    start = (0, 0)
    goal = (1, 1)
    path, visited = search_func(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_rgb_threshold_exactly_100(search_func):
    """Test that exactly 100 is NOT valid (must be > 100)"""
    image = [
        [(101, 0, 0), (100, 100, 100), (101, 0, 0)],
        [(101, 0, 0), (100, 100, 100), (101, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 2)
    path, visited = search_func(image, start, goal)
    
    # Must go around (100,100,100) pixels
    assert len(path) > 3 or path == []


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_2x2_grid(search_func):
    """Test both algorithms on a simple 2x2 grid"""
    image = [
        [(255, 255, 255), (255, 255, 255)],
        [(255, 255, 255), (255, 255, 255)]
    ]
    start = (0, 0)
    goal = (1, 1)
    path, visited = search_func(image, start, goal)
    
    assert len(path) == 3  # (0,0) -> (0,1) -> (1,1) or (0,0) -> (1,0) -> (1,1)
    assert path[0] == start
    assert path[-1] == goal


@pytest.mark.parametrize("search_func", [breath_first_search, best_first_search])
def test_narrow_corridor(search_func):
    """Test pathfinding through a narrow corridor"""
    image = [
        [(255, 0, 0), (100, 100, 100), (100, 100, 100), (100, 100, 100), (255, 0, 0)],
        [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
        [(255, 0, 0), (100, 100, 100), (100, 100, 100), (100, 100, 100), (255, 0, 0)]
    ]
    start = (0, 0)
    goal = (0, 4)
    path, visited = search_func(image, start, goal)
    
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == goal
    # Must go through the middle row
    assert any(p[0] == 1 for p in path)
