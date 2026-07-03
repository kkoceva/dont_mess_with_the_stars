

from game.settings import WHITE, LIGHT, DARK, BG

class GameMenu:
    def __init__(self, screen):
       self.screen = screen

    # def start_menu(self):
        # while True:

        #     self.screen.fill(BG)
           

            # play_button = pygame.Rect(300, 300, 140, 50)
            # quit_button = pygame.Rect(300, 380, 140, 50)

            # pygame.draw.rect(self.screen, LIGHT if play_button.collidepoint(mouse) else DARK, play_button)
            # pygame.draw.rect(self.screen, LIGHT if quit_button.collidepoint(mouse) else DARK, quit_button)

            # play_text = font.render("Play", True, WHITE)
            # quit_text = font.render("Quit", True, WHITE)

            # self.screen.blit(play_text, (335, 305))
            # self.screen.blit(quit_text, (335, 385))

            # for event in pygame.event.get():

            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()

            #     if event.type == pygame.MOUSEBUTTONDOWN:

            #         if play_button.collidepoint(mouse):
            #             game()

            #         if quit_button.collidepoint(mouse):
            #             pygame.quit()
            #             sys.exit()

            # pygame.display.update()