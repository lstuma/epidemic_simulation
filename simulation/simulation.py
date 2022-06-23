import random
import rendering
import math_tools

class Simulator(object):
    def __init__(self, window=None, agent_amount=30):
        # All agents in the simulation
        self.agents: list = list()

        # The window the agents will be rendered in
        self.window = window

        # Generate some agents
        self.gen_agents(amount=agent_amount)


    def gen_agents(self, amount):
        for i in range(0, amount):
            self.agents.append(Agent(position=(random.randint(200, 600), random.randint(100, 400))))
            self.agents[-1].circle.configure(batch=self.window.batch, radius=5, color=(200, random.randint(150, 255), 0), layer=1, opacity=255)
        self.agents[-1].infected = True

    def simulate(self, time_elapsed):
        # Go through all agents
        for agent in self.agents:
            # Check if agent is infected
            if agent.infected:
                agent.circle.configure(color=(255, 50, 50))
                # Check if agent can infect others
                for other_agent in self.agents:
                    # Get distance between both agents
                    distance = math_tools.get_distance(agent.position, other_agent.position)
                    # Try to infect other agent depending on distance
                    other_agent.infected = (random.randint(1, 10) - distance > 0) or other_agent.infected

            # Non infected agents
            else:
                pass

            self.move_randomly(agent)

    def move_randomly(self, agent):
        agent.set_position((agent.position[0] + random.randint(-15, 15), agent.position[1] + random.randint(-15, 15)))



class Agent(object):
    def __init__(self, position=(0, 0)):
        # Create a circle which will represent the agent on the screen
        self.circle: rendering.Circle = rendering.Circle(position=position)

        # Whether the agent has been infected (since this is supposed to be a virus simulation)
        self.infected: bool = False

        # Position of the agent
        self.position: tuple = position

    def set_position(self, position: tuple):
        # Update position
        self.position = position
        # Update circle position
        self.circle.configure(position=position)
