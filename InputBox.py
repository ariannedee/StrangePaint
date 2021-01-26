# Original code by Timothy Downs, edited by Arianne Dee to accept input box locations

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message, x, y, w, h, f=0):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font('Vera.ttf',13)
  pygame.draw.rect(screen, (80,80,80),
                   (x, y, w, h), f)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)), (x+2, y+2))
  pygame.display.flip()

def ask(screen, question, x, y, w, h, f=0, initial=""):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = initial
  display_box(screen, question + ": " + current_string, x, y, w, h, f)
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string += "_"
    elif inkey <= 127:
      current_string += chr(inkey)
    display_box(screen, question + ": " + current_string, x, y, w, h, z)
  return current_string
