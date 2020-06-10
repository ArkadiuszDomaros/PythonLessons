from queue import PriorityQueue
import numpy as np


class State():
    def __init__(self, state, goal_state, level, parent=None, heuristic_func="a*"):
        self.__state = state
        self.__goal_state = goal_state
        self.__level = level
        self.__heuristic_func = heuristic_func
        self.__heuristic_score = level
        self.__parent = parent
        self.calculate_fitness()

    def __hash__(self):
        return hash(str(self.__state))

    def __lt__(self, other):
        return self.__heuristic_score < other.__heuristic_score

    def __eq__(self, other):
        return self.__heuristic_score == other.__heuristic_score

    def __gt__(self, other):
        return self.__heuristic_score > other.__heuristic_score

    def get_state(self):
        return self.__state

    def get_score(self):
        return self.__heuristic_score

    def get_level(self):
        return self.__level

    def get_parent(self):
        return self.__parent

    def calculate_fitness(self):
        if self.__heuristic_func == "a*":
            for cur_tile in self.__state:
                cur_idx = self.__state.index(cur_tile)
                goal_idx = self.__goal_state.index(cur_tile)
                cur_i, cur_j = cur_idx // int(np.sqrt(len(self.__state))), cur_idx % int(np.sqrt(len(self.__state)))
                goal_i, goal_j = goal_idx // int(np.sqrt(len(self.__state))), goal_idx % int(np.sqrt(len(self.__state)))
                self.__heuristic_score += self.calculate_a(cur_i, cur_j, goal_i, goal_j)
        else:
            print()

    def calculate_a(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)


class AStarSolv():
    def __init__(self, init_state, goal_state, heuristic_func="a*", max_iter=2500):
        self.__init_state = init_state
        self.__goal_state = goal_state
        self.__heuristic_func = heuristic_func
        self.__MAX = 100000
        self.__max_iter = max_iter
        self.__path = []
        self.__number_of_steps = 0
        self.__summary = ""

    def set_max_iter(self, max_iter):
        self.__max_iter = max_iter

    def get_path(self):
        return self.__path

    def get_summary(self):
        return self.__summary

    def solve_a_star(self):
        x_axis = [1, 0, -1, 0]
        y_axis = [0, 1, 0, -1]

        level = 0
        visited_nodes = set()

        nodes = PriorityQueue(self.__MAX)
        init_node = State(self.__init_state.flatten().tolist(), self.__goal_state.flatten().tolist(), level,
                              parent=None, heuristic_func=self.__heuristic_func)
        nodes.put(init_node)

        epochs = 0
        while nodes.qsize() and epochs <= self.__max_iter:
            epochs += 1

            cur_node = nodes.get()
            cur_state = cur_node.get_state()

            if str(cur_state) in visited_nodes:
                continue
            visited_nodes.add(str(cur_state))

            if cur_state == self.__goal_state.flatten().tolist():
                self.__summary = str("A* w " + str(
                    cur_node.get_level()) + " krokach rozwiąło problem ")
                while cur_node.get_parent():
                    self.__path.append(cur_node)
                    cur_node = cur_node.get_parent()
                break

            empty_tile = cur_state.index(0)
            i, j = empty_tile // self.__goal_state.shape[0], empty_tile % self.__goal_state.shape[0]

            cur_state = np.array(cur_state).reshape(self.__goal_state.shape[0], self.__goal_state.shape[0])
            for x, y in zip(x_axis, y_axis):
                new_state = np.array(cur_state)
                if i + x >= 0 and i + x < self.__goal_state.shape[0] and j + y >= 0 and j + y < self.__goal_state.shape[0]:
                    new_state[i, j], new_state[i + x, j + y] = new_state[i + x, j + y], new_state[i, j]
                    game_state = State(new_state.flatten().tolist(), self.__goal_state.flatten().tolist(),
                                           cur_node.get_level() + 1, cur_node, self.__heuristic_func)
                    if str(game_state.get_state()) not in visited_nodes:
                        nodes.put(game_state)
        return self.__path


max_iter = 5000
heuristic = "a*"
n = 3
goal_state = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]])

init_state = np.array([[1, 8, 7],
                        [3, 0, 5],
                        [4, 6, 2]])

init_state = np.array(init_state).reshape(n, n)
goal_state = np.array(goal_state).reshape(n, n)

solver = AStarSolv(init_state, goal_state, heuristic, max_iter)
path = solver.solve_a_star()
for i in range(goal_state.shape[0]):
    print(init_state[i, :])
print()
for node in reversed(path):
    for i in range(goal_state.shape[0]):
        print(np.array(node.get_state()).reshape(goal_state.shape[0], goal_state.shape[0])[i, :])
    print()
print(solver.get_summary())
