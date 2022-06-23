import rendering


def main():
    window = rendering.Window(width=800, height=550)
    # Honestly, garbage collection can piss off
    circle = rendering.Circle(position=(100, 100), batch=window.batch, radius=400, color=(255, 255, 0), layer=1, opacity=255)
    rendering.run_app()
    pass


if __name__ == '__main__':
    main()
