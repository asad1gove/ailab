import random

def get_conflicts(state):
    """Calculate the number of conflicts (attacking pairs of queens) in the current state."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(state):
    """Generate all possible neighbor states by moving one queen in its column."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(n):
    """Hill climbing search for N-Queens."""
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = get_conflicts(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
            
        neighbor_conflicts = [(neighbor, get_conflicts(neighbor)) for neighbor in neighbors]
        best_neighbor, min_conflicts = min(neighbor_conflicts, key=lambda x: x[1])
        
        if min_conflicts >= current_conflicts:
            break
            
        current_state = best_neighbor
        current_conflicts = min_conflicts
        
    return current_state, current_conflicts

def solve_n_queens(n, max_restarts=1000):
    """Solves N-Queens using Hill Climbing with random restarts to escape local extrema."""
    for attempt in range(max_restarts):
        state, conflicts = hill_climbing(n)
        if conflicts == 0:
            print(f"Solution found after {attempt + 1} restarts:")
            print_board(state)
            return state
    print("Could not find a solution within the maximum number of restarts.")
    return None

def print_board(state):
    """Helper function to visualize the board state."""
    n = len(state)
    for r in range(n):
        line = ""
        for c in range(n):
            if state[c] == r:
                line += " Q "
            else:
                line += " . "
        print(line)
    print(f"State representation: {state}\n")


solved_state = solve_n_queens(8)