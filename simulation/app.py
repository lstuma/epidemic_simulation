import pyglet
import rendering
import simulation


class App(object):
    def __init__(self):
        # Create window for app
        self.window = rendering.Window(width=800, height=550)

        # Simulator handles agents and their interactions
        self.simulator = simulation.Simulator(self.window, agent_amount=300)

        # Register slow_fixed_update and fixed_update to be called each interval
        pyglet.clock.schedule_interval(self.slow_fixed_update, 0.25)
        pyglet.clock.schedule(self.fixed_update)

        # Run pyglet
        pyglet.app.run()

    def slow_fixed_update(self, time_elapsed):
        """
            slow_fixed_update gets called about every 0.25 seconds
        """

        self.simulator.simulate(time_elapsed=time_elapsed)

    def fixed_update(self, time_elapsed):
        """
            fixed_update gets called about every frame
        """

        self.simulator.move_randomly(time_elapsed=time_elapsed)


def main():
    App()


if __name__ == '__main__':
    main()
