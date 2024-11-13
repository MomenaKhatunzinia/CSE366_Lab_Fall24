from agent import Agent
from environment import Environment
import pygame


# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
AGENT_COLOR = (0, 128, 255)  # Blue
TEXT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Agent Simulation Framework")


    # Create an environment with dimensions 10x10
env = Environment(WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create an agent within the environment
agent = Agent(x = WINDOW_WIDTH // 2, y = WINDOW_HEIGHT// 2, speed = 5, environment=env)

    # Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)
running = True

while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    dx, dy = 0, 0

        
        #Move the agent
    agent.move(dx,dy)


    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)
    agent_pos = agent.get_position()
    #pygame.draw.(screen,AGENT_COLOR,agent_pos,10)
    pygame.draw.circle(screen,AGENT_COLOR,agent_pos, 15, 3)


    # Display the frame count as an example text (debug info)
    position_text = font.render(f"Position: {agent_pos}", True, TEXT_COLOR)
    screen.blit(position_text, (10, 10))


    # Flip the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame properly
pygame.quit()

