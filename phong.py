import pygame
import math
import numpy as np

def get_z(x, y, R):
    return math.sqrt(R**2 - (x-WIDTH/2)**2 - (y-HEIGHT/2)**2)

#I   – wynikowe natężenie światła
#Ia  – natężenie światła w otoczeniu obiektu
#IP  – natężenie światła punktowego
#ka  – współczynnik odbicia światła otoczenia (tła)
#ks  – współczynnik odbicia światła kierunkowego
#kd  – współczynnik odbicia światła rozproszonego
#Fat – współczynnik tłumienia źródła z odległością
#n   – współczynnik gładkości powierzchni


def illuminate(kd, ks, ka, n, x_l, y_l, z_l, R_b, color):
    text = "n=" + str(n) + " kd=" + str(kd) + " ks=" + str(ks) + " ka=" + str(ka)
    global text_render
    text_render = font.render(text, False, (0, 0, 0))
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            screen.fill((200,230,255),((x,y),(1,1)))
            #screen.fill((0,0,0),((x,y),(1,1)))
            if ((x-WIDTH/2)**2 + (y-HEIGHT/2)**2 <= R_b**2):
                z = get_z(x, y, R_b)

                # N - wektor normalny (znormalizowany wektor [x,y,z])
                N = np.array([x, y, z]) / np.linalg.norm(np.array([x, y, z]))

                # L - wektor kierunku światła (znormalizowany wektor [x_l-x,y_l-y,z_l-z], gdzie _l oznacza wsp. punktu światła)
                L = np.array([x_l - x, y_l - y, z_l - z]) / np.linalg.norm(np.array([x_l - x, y_l - y, z_l - z]))
                
                # beta - między wektorem normalnym N a wektorem L
                beta = math.acos(N[0] * L[0] + N[1] * L[1] + N[2] * L[2] / (math.sqrt(N[0]**2 + N[1]**2 + N[2]**2) * math.sqrt(L[0]**2 + L[1]**2 + L[2]**2)))
                
                # R -  wektor odbity, który jest wynikiem odbicia wektora L względem wektora normalnego N
                R = L - 2 * N * math.cos(beta) / np.linalg.norm(L - 2 * N * math.cos(beta))
                
                # V - wektor widza
                V = np.array([0, 0, 1])

                # I - intensywność oświetlenia
                Ia = 0.25
                I = Ia + (1 * (kd * N.dot(L) + ks * (R.dot(V)**n)))

                c = color.copy()
                for i in range(3):
                    new_value = int(c[i] + ka * I * 255)
                    if new_value > 255:
                        new_value = 255
                    elif new_value < 0:
                        new_value = 0
                    c[i] = new_value
                
                #c = int(z/math.sqrt(R_b**2)*255)
                screen.set_at((x,y),(c[0],c[1],c[2]))
                #screen.fill((0,0,0),((X_L,Y_L),(10,10)))


WIDTH, HEIGHT = 500, 500
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

R = 100

X_L = 270
Y_L = 270
Z_L = -100

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
text = ""
text_render = font.render(text, False, (0, 0, 0))
text_rect = text_render.get_rect()
text_rect.center = (WIDTH *0.1, HEIGHT *.85)


#1:
#illuminate(kd=0.45, ks=0.92, ka=.6, n=20, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
#2:
#illuminate(kd=0.45, ks=0.92, ka=.6, n=40, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
#3:
#illuminate(kd=0.45, ks=0.92, ka=.7, n=100, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
#4
#illuminate(kd=0.85, ks=0.1, ka=.6, n=20, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[220, 220, 220])
#5
#illuminate(kd=0.35, ks=0.35, ka=.6, n=26, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[170, 170, 0])
#6
#illuminate(kd=0.55, ks=0.15, ka=.4, n=3, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[140, 100, 53])
#7
#illuminate(kd=0.25, ks=0.75, ka=.5, n=250, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[100, 100, 100])

button_width = 60
button_height = 40
button_margin = 10
# Utwórz przyciski
button1_rect = pygame.Rect(10, 10, button_width, button_height)
button2_rect = pygame.Rect(button1_rect.right + button_margin, 10, button_width, button_height)
button3_rect = pygame.Rect(button2_rect.right + button_margin, 10, button_width, button_height)
button4_rect = pygame.Rect(button3_rect.right + button_margin, 10, button_width, button_height)
button5_rect = pygame.Rect(button4_rect.right + button_margin, 10, button_width, button_height)
button6_rect = pygame.Rect(button5_rect.right + button_margin, 10, button_width, button_height)
button7_rect = pygame.Rect(button6_rect.right + button_margin, 10, button_width, button_height)

screen.fill((200,230,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Sprawdź, czy któryś przycisk został kliknięty
            if event.button == 1:  # Lewy przycisk myszy
                if button1_rect.collidepoint(event.pos):
                    illuminate(kd=0.45, ks=0.92, ka=0.6, n=20, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
                elif button2_rect.collidepoint(event.pos):
                    illuminate(kd=0.45, ks=0.92, ka=0.6, n=40, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
                elif button3_rect.collidepoint(event.pos):
                    illuminate(kd=0.45, ks=0.92, ka=0.7, n=100, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[0, 0, 0])
                elif button4_rect.collidepoint(event.pos):
                    illuminate(kd=0.85, ks=0.1, ka=.6, n=20, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[220, 220, 220])
                elif button5_rect.collidepoint(event.pos):
                    illuminate(kd=0.35, ks=0.35, ka=.6, n=26, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[170, 170, 0])
                elif button6_rect.collidepoint(event.pos):
                    illuminate(kd=0.55, ks=0.15, ka=.4, n=3, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[140, 100, 53])
                elif button7_rect.collidepoint(event.pos):
                    #illuminate(kd=0.45, ks=0.75, ka=.7, n=250, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[70, 70, 70])
                    illuminate(kd=0.25, ks=0.75, ka=.5, n=250, x_l=X_L, y_l=Y_L, z_l=Z_L, R_b=R, color=[100, 100, 100])

    screen.blit(text_render, text_rect)
    pygame.draw.rect(screen, (200, 200, 200), button1_rect)
    pygame.draw.rect(screen, (200, 200, 200), button2_rect)
    pygame.draw.rect(screen, (200, 200, 200), button3_rect)
    pygame.draw.rect(screen, (200, 200, 200), button4_rect)
    pygame.draw.rect(screen, (200, 200, 200), button5_rect)
    pygame.draw.rect(screen, (200, 200, 200), button6_rect)
    pygame.draw.rect(screen, (200, 200, 200), button7_rect)

    # Wyświetl tekst na przyciskach
    f = pygame.font.Font(None, 24)
    button1_text = f.render("1", True, (0, 0, 0))
    button2_text = f.render("2", True, (0, 0, 0))
    button3_text = f.render("3", True, (0, 0, 0))
    button4_text = f.render("kreda", True, (0, 0, 0))
    button5_text = f.render("plastik", True, (0, 0, 0))
    button6_text = f.render("drewno", True, (0, 0, 0))
    button7_text = f.render("metal", True, (0, 0, 0))

    screen.blit(button1_text, (button1_rect.x + 10, button1_rect.y + 10))
    screen.blit(button2_text, (button2_rect.x + 10, button2_rect.y + 10))
    screen.blit(button3_text, (button3_rect.x + 10, button3_rect.y + 10))
    screen.blit(button4_text, (button4_rect.x + 10, button4_rect.y + 10))
    screen.blit(button5_text, (button5_rect.x + 10, button5_rect.y + 10))
    screen.blit(button6_text, (button6_rect.x + 10, button6_rect.y + 10))
    screen.blit(button7_text, (button7_rect.x + 10, button7_rect.y + 10))


    pygame.display.update()
