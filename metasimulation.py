from typing import Callable, Any, Dict, List

class CellularAutomaton:
    def __init__(self, states: List[Any], transition_function: Callable[[Any, Any, Any], Any], default_state: Any):
        self.states = set(states)
        self.f = transition_function
        self.default = default_state
        assert default_state in self.states, "Le symbole par défaut doit faire partie de l'ensemble des états."
    
    def step(self, config: Dict[int, Any]) -> Dict[int, Any]:
        new_config = {}
        indices = list(config.keys())
        min_index = min(indices) - 1
        max_index = max(indices) + 1
        
        for i in range(min_index, max_index + 1):
            left = config.get(i - 1, self.default)
            center = config.get(i, self.default)
            right = config.get(i + 1, self.default)
            new_config[i] = self.f(left, center, right)
        return new_config

    def display(self, config: Dict[int, Any]) -> str:
        min_index = min(config)
        max_index = max(config)
        return ''.join(str(config.get(i, self.default)) for i in range(min_index, max_index + 1))

def rule_110(a, b, c):
    return {
        (1, 1, 1): 0,
        (1, 1, 0): 1,
        (1, 0, 1): 1,
        (1, 0, 0): 0,
        (0, 1, 1): 1,
        (0, 1, 0): 1,
        (0, 0, 1): 1,
        (0, 0, 0): 0
    }[(a, b, c)]

init_config = {i: int(c) for i, c in enumerate("0001000")}
automaton = CellularAutomaton(states=[0, 1], transition_function=rule_110, default_state=0)

print(automaton.display(init_config))
for _ in range(4):
    init_config = automaton.step(init_config)
    print(automaton.display(init_config))
