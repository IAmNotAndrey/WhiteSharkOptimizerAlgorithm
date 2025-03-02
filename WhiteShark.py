import numpy as np

class WhiteShark:
    def __init__(self, velocity: float, 
                       position : list[float], 
                       search_space : list[tuple[float, float]]
                ):
        self.velocity = velocity
        self.position = position
        self.lower_bounds = np.array([b[0] for b in search_space])
        self.upper_bounds = np.array([b[1] for b in search_space])
        
    def adjust_position(self):
        self.position = np.clip(self.position, self.lower_bounds, self.upper_bounds)
