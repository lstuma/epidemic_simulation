import random
import rendering
import math_tools

class Simulator(object):
    def __init__(self, window=None, agent_amount=30):
        # All agents in the simulation
        self.agents: list = list()

        # The window the agents will be rendered in
        self.window = window

        # Where the agents are allowed to go inside the window
        self.constraints = (self.window.width, self.window.height)

        # The distance between all the agents
        self.agent_relations: dict = dict()

        # Generate some agents
        self.gen_agents(amount=agent_amount)


    def gen_agents(self, amount):
        for i in range(0, amount):
            self.agents.append(Agent(position=(random.randint(50, 750), random.randint(50, 500))))
            self.agents[-1].circle.configure(batch=self.window.batch, radius=5, color=(random.randint(0, 100), random.randint(100, 255), random.randint(0, 150)), layer=1, opacity=255)
        self.agents[-1].set_infection_status(True)

        # Calc relations because otherwise simulation will try to access unset dictionary elements
        self.calc_relations()

    def calc_relations(self):
        for agent in self.agents:
            for other_agent in [self.agents[i] for i in range(self.agents.index(agent), len(self.agents))]:
                # Get distance between both agents
                self.agent_relations[agent, other_agent] = self.agent_relations[other_agent, agent] = math_tools.get_distance(agent.position, other_agent.position)

    def simulate(self, time_elapsed):
        # Calculate the relations
        self.calc_relations()

        # Go through all agents
        for agent in self.agents:
            # Check if agent is infected
            if agent.infected:
                # Check if agent can infect others
                for other_agent in self.agents:
                    if not other_agent.infected and not other_agent == agent:
                        # Get distance between both agents
                        distance = self.agent_relations[agent, other_agent]
                        # Try to infect other agent depending on distance
                        other_agent.set_infection_status((random.randint(1, 10) - distance > 0) or other_agent.infected)

    def move_randomly(self, time_elapsed):
        print(time_elapsed)
        for agent in self.agents:
            agent.set_position(((agent.position[0] + time_elapsed*random.randint(-30, 30))%self.constraints[0],
                                (agent.position[1] + time_elapsed*random.randint(-30, 30))%self.constraints[1]))



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

    def set_infection_status(self, infected):
        if infected:
            # Change infected status to true
            self.infected = True

            # Change color to red
            self.circle.configure(color=(random.randint(200, 255), random.randint(0, 55), random.randint(0, 55)))
        elif self.infected:
            # Change color to yellow
            self.circle.configure(color=(random.randint(100, 255), random.randint(100, 255), random.randint(0, 50)))