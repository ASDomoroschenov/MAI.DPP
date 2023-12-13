import sys

import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QWidget, QRadioButton, QVBoxLayout, QMainWindow
)


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        layout = QVBoxLayout()
        self.button = QPushButton()
        self.button.setText('START')
        self.button.move(200, 210)
        layout.addWidget(self.button)
        self.button_mrch = QRadioButton("march 2023")
        layout.addWidget(self.button_mrch)
        self.button_aprl = QRadioButton("april 2023")
        layout.addWidget(self.button_aprl)
        self.button_may = QRadioButton("may 2023")
        layout.addWidget(self.button_may)
        layout.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        layout.setSpacing(60)
        self.setLayout(layout)

    def show_graph(self):
        global tp
        if self.button_mrch.isChecked():
            tp = 1
        if self.button_aprl.isChecked():
            tp = 2
        if self.button_may.isChecked():
            tp = 3

        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("graph")
        all_sprites = pygame.sprite.Group()
        clock = pygame.time.Clock()
        running = True
        fps = 60

        class Line(pygame.sprite.Sprite):
            def __init__(self, pos, x, y, ln):
                pygame.sprite.Sprite.__init__(self)
                if pos == "x":
                    self.image = pygame.Surface((3, ln))
                    self.image.fill((0, 0, 0))
                    self.rect = self.image.get_rect()
                    self.rect.centerx = x
                    self.rect.centery = y
                elif pos == "y":
                    self.image = pygame.Surface((ln, 3))
                    self.image.fill((0, 0, 0))
                    self.rect = self.image.get_rect()
                    self.rect.centerx = x
                    self.rect.centery = y

        class Dot(pygame.sprite.Sprite):
            def __init__(self, x, y, c):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.surface.Surface((5, 5))

                if c == 1:
                    self.image.fill((0, 0, 0))
                if c == 2:
                    self.image.fill((255, 0, 0))
                if c == 3:
                    self.image.fill((252, 15, 192))
                if c == 4:
                    self.image.fill((0, 191, 255))
                self.rect = self.image.get_rect()
                self.rect.centerx = x
                self.rect.centery = y

        per = 7.5

        def Calc(func):
            d = 30
            if tp == 1:
                night = [-6, -4, -1, -2, -1, -3, -3, -8, -2, -6, -6, 1, -5, -3, 5, 3, 1, -4, -2, -5, 3, 4, 5, 8, 4, 7,
                         4, 3, 4, 6, 7]
                day = [-2, -2, 1, 1, -1, -1, 1, -2, -2, -4, -3, 4, -3, 6, 8, 3, 5, 5, 4, 8, 8, 6, 11, 8, 9, 7, 9, 9, 8,
                       4, 5]
                d = 31
            if tp == 2:
                night = [0, 6, 7, 7, 5, 5, 3, 1, 5, 6, 7, 4, 7, 4, 1, 3, 8, 9, 9, 5, 5, 6, 5, 7, 10, 11, 7, 9, 4, 2]
                day = [8, 10, 13, 13, 11, 14, 11, 13, 14, 12, 15, 17, 18, 9, 9, 13, 14, 13, 17, 16, 16, 15, 19, 21, 19,
                       14, 18, 13, 11, 12]
                d = 30
            if tp == 3:
                night = [6, 2, 10, 4, 7, 1, 0, -1, 0, 7, 9, 7, 10, 11, 6, 9, 9, 11, 14, 11, 10, 10, 11, 16, 14, 13, 16,
                         11, 9, 12, 13]
                day = [7, 15, 14, 15, 6, 6, 8, 10, 13, 16, 12, 21, 22, 16, 20, 20, 24, 25, 17, 15, 17, 19, 16, 21, 18,
                       23, 21, 16, 21, 22, 21]
                d = 31

            k = 0
            while k < d:
                dot = Dot(30 + (k + 1) * per * 2, 250 - night[k] * per, 1)
                all_sprites.add(dot)
                dot = Dot(30 + (k + 1) * per * 2, 250 - day[k] * per, 2)
                all_sprites.add(dot)
                ytro = (night[k] + day[k]) / 2
                dot = Dot(30 + (k + 1) * per * 2, 250 - ytro * per, 3)
                all_sprites.add(dot)

                if k < d - 1:
                    vecher = ((night[k + 1] + day[k]) / 2)
                    dot = Dot(30 + (k + 1) * per * 2, 250 - vecher * per, 4)
                    all_sprites.add(dot)
                k = k + 1

        func = "6"
        line = Line("y", 250, 250, 470)
        all_sprites.add(line)
        line1 = Line("x", 30, 250, 470)
        all_sprites.add(line1)
        i = 0

        while i < 7:
            line2 = Line("y", 30, 250 - i * per * 5, 15)
            all_sprites.add(line2)
            line2 = Line("y", 30, 250 + i * per * 5, 15)
            all_sprites.add(line2)
            line2 = Line("x", 30 + i * per * 10, 250, 15)
            all_sprites.add(line2)
            i = i + 1

        calc = Calc(func)

        while running:
            background = pygame.image.load("resources/graph_background.jpg")
            legend = pygame.image.load("resources/legend.png")
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                screen.fill((255, 255, 255))
                screen.blit(background, (0, 0))
                screen.blit(legend, (250, 250))
                font = pygame.font.Font(None, 30)
                text = font.render("t", True, (28, 28, 28))
                screen.blit(text, (80, 30))
                font1 = pygame.font.Font(None, 30)
                text1 = font1.render("date", True, (28, 28, 28))
                screen.blit(text1, (420, 280))
                font2 = pygame.font.Font(None, 20)
                text2 = font2.render("0", True, (0, 0, 255))
                screen.blit(text2, (44, 260))

                for i in range(5, 35, 5):
                    font3 = pygame.font.Font(None, 20)
                    text3 = font3.render(str(i), True, (0, 0, 255))
                    screen.blit(text3, (30 + i * per * 2, 260))
                    text3 = font3.render(str(i), True, (0, 0, 255))
                    screen.blit(text3, (46, 250 - i * per))
                    text3 = font3.render("-" + str(i), True, (0, 0, 255))
                    screen.blit(text3, (40, 250 + i * per))
                    all_sprites.draw(screen)
                    pygame.display.flip()
        pygame.quit()


app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle('MAK')
main_window.setStyleSheet('''
    QPushButton {
        background-color: black;
    }
    QRadioButton {
        background-color: black;
    }
    QWidget {
        background-image: url(resources/main_background.jpg);
    }
''')
main_widget = MainWidget()
main_widget.button.clicked.connect(main_widget.show_graph)
main_window.setCentralWidget(main_widget)
main_window.show()

sys.exit(app.exec())
