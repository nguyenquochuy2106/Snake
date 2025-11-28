import pygame
from snake_game.snake_class import Snake
from snake_game.food_class import Food

class Game:
    def __init__(self, width=600, height=400):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game - Powered by 22730075")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(screen_width=width, screen_height=height)
        self.running = True

    def check_collision(self):
        # Snake ăn food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.random_position()

        # Snake tự cắn mình
        if self.snake.body[0] in self.snake.body[1:]:
            self.running = False

        # Snake chạm tường
        x, y = self.snake.body[0]
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def show_menu(self):
        font = pygame.font.SysFont(None, 50)
        menu = True
        while menu:
            self.screen.fill((0,0,0))
            title = font.render("Snake Game", True, (255,255,255))
            start = font.render("Press ENTER to Start", True, (255,255,255))
            self.screen.blit(title, (self.width//2 - title.get_width()//2, 100))
            self.screen.blit(start, (self.width//2 - start.get_width()//2, 200))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu = False

        # Chọn mức độ
        self.clock_speed = self.show_difficulty_menu()
        self.game_loop()


    def game_loop(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            self.check_collision()
            self.screen.fill((0,0,0))
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(self.clock_speed)
        self.show_game_over_menu()


    def game_over(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over! Press ESC to Exit.", True, (255,0,0))
        self.screen.blit(text, (self.width//2 - text.get_width()//2, self.height//2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
        pygame.quit()

    def draw_score(self):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {len(self.snake.body)-3}", True, (255,255,255))
        self.screen.blit(score_text, (10, 10))

    def show_difficulty_menu(self):
        font = pygame.font.SysFont(None, 40)
        menu = True
        difficulty = 10  # default
        while menu:
            self.screen.fill((0,0,0))
            title = font.render("Select Difficulty", True, (255,255,255))
            easy = font.render("1. Easy", True, (0,255,0))
            medium = font.render("2. Medium", True, (255,255,0))
            hard = font.render("3. Hard", True, (255,0,0))
            
            self.screen.blit(title, (self.width//2 - title.get_width()//2, 100))
            self.screen.blit(easy, (self.width//2 - easy.get_width()//2, 180))
            self.screen.blit(medium, (self.width//2 - medium.get_width()//2, 240))
            self.screen.blit(hard, (self.width//2 - hard.get_width()//2, 300))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        difficulty = 5
                        menu = False
                    elif event.key == pygame.K_2:
                        difficulty = 10
                        menu = False
                    elif event.key == pygame.K_3:
                        difficulty = 15
                        menu = False
        return difficulty

    def show_game_over_menu(self):
        font = pygame.font.SysFont(None, 40)
        menu = True
        while menu:
            self.screen.fill((0,0,0))
            over_text = font.render("Game Over!", True, (255,0,0))
            replay = font.render("R - Replay", True, (0,255,0))
            exit_game = font.render("ESC - Exit", True, (255,255,255))
            self.screen.blit(over_text, (self.width//2 - over_text.get_width()//2, 100))
            self.screen.blit(replay, (self.width//2 - replay.get_width()//2, 180))
            self.screen.blit(exit_game, (self.width//2 - exit_game.get_width()//2, 240))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # reset snake và food
                        self.snake = Snake()
                        self.food = Food(screen_width=self.width, screen_height=self.height)
                        self.running = True
                        self.clock_speed = self.show_difficulty_menu()
                        self.game_loop()
                        menu = False
                    elif event.key == pygame.K_ESCAPE:
                        menu = False
                        self.running = False
        pygame.quit()
