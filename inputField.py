import pygame

pygame.font.init()

class InputField:
    def __init__(self, screen, pos, size, color, textColor, outlined):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.font = pygame.font.SysFont('Comic Sans MS', 25)

        self.screen = screen
        self.textColor = textColor
        self.focused = False
        self.caps = False
        self.outlined = outlined

        self.outlineColor = (0,0,0)

        self.text = ""
        self.txt_box = self.font.render(self.text, False, textColor)
        self.txt_box_rect = self.txt_box.get_rect()
        self.canType = True
        self.width = size[0]

        self.shift_versions = {
            '1' : '!',
            '2' : '@',
            '3' : '#',
            '4' : '$',
            '5' : '%',
            '6' : '^',
            '7' : '&',
            '8' : '*',
            '9' : '(',
            '0' : ')',
            '`' : '~',
            '-' : '_',
            '=' : '+',
            ',' : '<',
            '.' : ">",
            '/' : '?',
            ';' : ':',
            "'" : '"',
            '[' : '{',
            ']' : '}',
            '\\' : '|'
        }

    def draw(self):

        if self.font.size(self.text)[0]  >= self.width:
            self.canType = False
            print("TOO LONG!")
        else:
            self.canType = True

        # Draw the input field to the screen after calculations
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.txt_box, self.txt_box_rect)
        if self.outlined:
            pygame.draw.line(self.screen, self.outlineColor, (self.rect.left, self.rect.top), (self.rect.right, self.rect.top))
            pygame.draw.line(self.screen, self.outlineColor, (self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom))
            pygame.draw.line(self.screen, self.outlineColor, (self.rect.right, self.rect.bottom), (self.rect.left, self.rect.bottom))
            pygame.draw.line(self.screen, self.outlineColor, (self.rect.left, self.rect.bottom), (self.rect.left, self.rect.top))

    def check_focus(self, mouse_pos):
        x, y = mouse_pos
        if self.rect.left < x < self.rect.right and self.rect.top < y < self.rect.bottom:
            self.focused = True
            self.outlineColor = (255, 0, 0)
        else:
            self.focused = False
            self.outlineColor = (0, 0, 0)

    def updateText(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_SPACE:
                self.text += " "
            elif event.key == pygame.K_LSHIFT:
                self.caps = True
            elif event.key == pygame.K_RETURN:
                self.text += '\n'
            else:
                if self.canType:
                    if self.caps:
                        if pygame.key.name(event.key) in self.shift_versions:
                            self.text += self.shift_versions[pygame.key.name(event.key)]
                        else:
                            self.text += pygame.key.name(event.key).upper()
                    else:
                            self.text += pygame.key.name(event.key)

        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                self.caps = False

        self.txt_box = self.font.render(self.text, False, self.textColor)
        self.txt_box_rect = self.txt_box.get_rect()
        self.txt_box_rect.center = self.rect.center


    def change_current_text(self, text):
        self.text = text
        self.txt_box = self.font.render(self.text, False, self.textColor)
        self.txt_box_rect = self.txt_box.get_rect()
        self.txt_box_rect.center = self.rect.center
