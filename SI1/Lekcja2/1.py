from treelib import Tree, Node


def reachable_states(state):
    if state[0] == "Gdansk":
        return [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]]
    if state[0] == "Gdynia":
        return [["Gdansk", 24], ["Lebork", 58], ["Wladyslawowo", 33]]
    if state[0] == "Koscierzyna":
        return [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]]
    if state[0] == "Tczew":
        return [["Elblag", 53], ["Gdansk", 33], ["Koscierzyna", 59]]
    if state[0] == "Elblag":
        return [["Gdansk", 63], ["Tczew", 53]]
    if state[0] == "Chojnice":
        return [["Koscierzyna", 70], ["Bytow", 65]]
    if state[0] == "Bytow":
        return [["Koscierzyna", 40], ["Chojnice", 65], ["Slupsk", 70]]
    if state[0] == "Slupsk":
        return [["Bytow", 70], ["Lebork", 55], ["Ustka", 21]]
    if state[0] == "Ustka":
        return [["Slupsk", 21], ["Leba", 64]]
    if state[0] == "Leba":
        return [["Lebork", 29], ["Ustka", 64], ["Wladyslawowo", 66]]
    if state[0] == "Lebork":
        return [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]]
    if state[0] == "Wladyslawowo":
        return [["Leba", 66], ["Gdynia", 42], ["Hel", 35]]
    if state[0] == "Hel":
        return [["Wladyslawowo", 35]]
    return []


def breadth_first_search(start_state, target_state):
    id = 0
    fifo_queue = []

    tree = Tree()
    fifo_queue.append([start_state, 0, id])
    tree.create_node([start_state, 0, id], id)
    while True:
        print(fifo_queue)
        tree.show()
        if len(fifo_queue) == 0:
            print("failed to reach the target state")
            return 1
        temp = fifo_queue[0]

        if temp[0] == target_state:
            print("the target state " + temp[0] + " has been reached after " + str(temp[1]) + " kms!")
            return 0
        del (fifo_queue[0])
        for elem in reachable_states(temp):
            id += 1
            new_elem = [elem[0], temp[1] + elem[1], id]
            fifo_queue.append(new_elem)
            tree.create_node(new_elem, id, parent=temp[2])


print(breadth_first_search("Gdansk","Ustka"))