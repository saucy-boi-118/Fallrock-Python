import pygame
import math


def drawTriangle(position:pygame.Vector2, size:int, outline:bool, color:str, screen:pygame.surface.Surface):
    if (outline == False):
        pygame.draw.polygon(screen, color, [
        (position.x + size, position.y + size), 
        (position.x - size, position.y + size), 
        (position.x, position.y - size)])
    else:
        # actual shape
        pygame.draw.polygon(screen, color, [
        (position.x + size, position.y + size), 
        (position.x - size, position.y + size), 
        (position.x, position.y - size)])
        # outline
        pygame.draw.polygon(screen, "black", [
        (position.x + size, position.y + size), 
        (position.x - size, position.y + size), 
        (position.x, position.y - size)], width = 5)

def findDistance(pos1:pygame.Vector2, pos2:pygame.Vector2):
    return math.sqrt(math.pow((pos2.x - pos1.x), 2) + math.pow((pos2.y - pos1.y), 2))

def collideCircs(circle1:pygame.Vector2, circle2:pygame.Vector2, circle1Radius:int, circle2Radius:int):
    
    if findDistance(circle1, circle2) < circle1Radius + circle2Radius:
        return True
    elif findDistance(circle1, circle2) == circle1Radius + circle2Radius:
        return True
    else:
        return False

def getHighScore():
    with open("highscore.txt", "r") as f:
        return f.read()
