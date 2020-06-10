entity = ['koza', 'wilk', 'sałata']
path = []


def eats(x, y):
    if x == 'koza' and y == 'sałata':
        return True
    elif x == 'wilk' and y == 'koza':
        return True
    else:
        return False


def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True


def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


def safe_state(state):
    if state_of('człowiek', state) == state_of('koza', state):
        return True
    elif state_of('koza', state) == state_of('wilk', state):
        return False
    elif state_of('koza', state) == state_of('sałata', state):
        return False
    else:
        return True


def move(who, state):
    if state[who] == 'lewa':
        state[who] = 'prawa'
    else:
        state[who] = 'lewa'
    return state


def goal_reach(state):
    if not state:
        return False
    return (state_of('człowiek', state)=='prawa' and
            state_of('koza', state)=='prawa' and
            state_of('wilk', state)=='prawa' and
            state_of('sałata',state)=='prawa')


def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states


def expand_states(state):
    children = []
    child = state.copy()
    move('człowiek', child)
    check_add_child(child, children)
    for ent in entity:
        if state_of(ent, state) == state_of('człowiek', state):
            child = state.copy()
            move('człowiek', child)
            move(ent, child)
            check_add_child(child, children)
    return children


def search_sol(state):
    path.append(state)
    next = state.copy()
    while next and not goal_reach(next):
        nl = expand_states(next)
        next = {}
        for child in nl:
            if not (child in path):
                next = child
                path.append(next)
                break
    return next


initial_state = {}
initial_state['człowiek'] = 'lewa'
for e in entity:
    initial_state[e] = 'lewa'


expand_states(initial_state)


search_sol(initial_state)

k=0
for s in path:
    print(s)
    k+=1

print()
print("Wykonało " + str(k) + " ruchów")
