#!/usr/bin/env python
# Simple paint program
# Current functionality: choose foreground and background colours based on rgb values, draws, saves to program location, sets brush size, lines, pencil, rectangle and 3 undos
# Future functionality: fill, ellipse, click-and-drag w/ sample outline, choose canvas size

import pygame
from pygame.locals import *
from sys import exit
import InputBox

offset = [153, 3]

class storer():
    def __init__(self, newone):
        self.new = newone
        self.color = [80, 80, 80]
        self.size = 3 # Brush size
        self.esize = 10 # Eraser size
        self.down = False # Left mouse button is not down
        self.down2 = False # Right mouse button is not down
        self.bgcolor = [240, 240, 240]
        self.fill = False # Not functional yet: errors
        self.pen = False
        self.draw = True
        self.line = False
        self.rect = False
        self.pos1set = False
        self.pos1 = [0, 0]
        self.pos2set = False
        self.pos2 = [0, 0]
        self.save = "drawing"
        
    # Brush functions
    def drawline(self, color, point_one, point_two, size):
        one = (point_one[0]-offset[0]-(size/2), point_one[1]-offset[1]-(size/2))
        two = (point_two[0]-offset[0]-(size/2), point_two[1]-offset[1]-(size/2))
        pygame.draw.line(drawspace, color, one, two, size)

    def aaline(self, color, point_one, point_two):
        one = (point_one[0]-offset[0], point_one[1]-offset[1])
        two = (point_two[0]-offset[0], point_two[1]-offset[1])
        pygame.draw.aaline(drawspace, color, one, two)

    def drawrect(self, color, point_one, point_two, size):
        if self.fill:
            pygame.draw.rect(drawspace, color, (point_one[0]-offset[0], point_one[1]-offset[1], point_two[0]-point_one[0], point_two[1]-point_one[1]), 0)
        else:
            pygame.draw.rect(drawspace, color, (point_one[0]-offset[0], point_one[1]-offset[1], point_two[0]-point_one[0], point_two[1]-point_one[1]), size)

mem_top = pygame.surface.Surface([640, 380])
mem_middle = pygame.surface.Surface([640, 380])
mem_bottom = pygame.surface.Surface([640, 380])
        
store = storer([]) # Create new variable storing object

# Save options
savex = 8
savey = 8
save_w = 140
save_h = 20

# Color box dimensions
box_size = 70
fgx = 8
fgy = 45
bgx = fgx+box_size
bgy = fgy+box_size+12
box_w = 50
box_h = 20
boxx = fgx+box_size+6
boxx2 = bgx-box_w-6
boxy = box_h+5

# Brush size box dimensions
bsx = 8
bsy = 210
bs_w = 105
bs_h = 20
e = 26

# Tool coords
tooly = 25
penx = 8
peny = 270
drawx = 8
drawy = peny + tooly
linex = 8
liney = drawy + tooly
rectx = 8
recty = liney + tooly
filly = recty

bgcolor = [110, 100, 120]
dark = [80, 80, 80]
light = [240, 240, 240]

# Initializes pygame and display
pygame.init()

screen = pygame.display.set_mode((800, 400), 0, 32)
screen.fill(bgcolor)
pygame.display.set_caption("Strange.Paint >-O-<")

border = pygame.surface.Surface([644, 384])
border.fill(dark)

drawspace = pygame.surface.Surface([640, 380])
drawspace.fill(light)

mem_top.blit(drawspace, [0,0])
mem_middle.blit(drawspace, [0,0])
mem_bottom.blit(drawspace, [0,0])

font_tools = pygame.font.Font("Vera.ttf", 13)
text_pen = font_tools.render("pen", 1, light)
text_draw = font_tools.render("brush", 1, light)
text_line = font_tools.render("line", 1, light)
text_rect = font_tools.render("rectangle", 1, light)
text_fill = font_tools.render("fill", 1, light)

text_save = font_tools.render("save", 1, light)
box_save = pygame.surface.Surface([save_w, save_h])
box_save.fill(dark)
box_save.blit(text_save, [3,1])
screen.blit(box_save, [savex, savey])

InputBox.display_box(screen, "save: ", savex, savey, save_w, save_h)

box_pen = pygame.surface.Surface([text_pen.get_width()+6, text_pen.get_height()+2])
box_draw = pygame.surface.Surface([text_draw.get_width()+6, text_draw.get_height()+2])
box_line = pygame.surface.Surface([text_line.get_width()+6, text_line.get_height()+2])
box_rect = pygame.surface.Surface([text_rect.get_width()+6, text_rect.get_height()+2])
box_fill = pygame.surface.Surface([text_fill.get_width()+6, text_fill.get_height()+2])

pen_w = box_pen.get_width()
draw_w = box_draw.get_width()
line_w = box_line.get_width()
rect_w = box_rect.get_width()
fill_w = box_fill.get_width()
box_h = box_draw.get_height()

fillx = rectx + rect_w + 6

box_pen.fill(dark)
box_draw.fill(dark)
box_line.fill(dark)
box_rect.fill(dark)
box_fill.fill(dark)

box_pen.blit(text_pen, [3,1])
box_draw.blit(text_draw, [3,1])
box_line.blit(text_line, [3,1])
box_rect.blit(text_rect, [3,1])
box_fill.blit(text_fill, [3,1])

screen.blit(box_pen, [penx, peny])
screen.blit(box_draw, [drawx, drawy])
screen.blit(box_line, [linex, liney])
screen.blit(box_rect, [rectx, recty])
screen.blit(box_fill, [fillx, recty])

pygame.draw.rect(screen, light, (drawx, drawy, box_draw.get_width(),box_draw.get_height()), 1)

box_color = pygame.surface.Surface([box_size, box_size])
box_bgcolor = pygame.surface.Surface([box_size, box_size])

InputBox.display_box(screen, "r: " + str(store.color[0]), boxx, fgy, box_w, box_h)
InputBox.display_box(screen, "g: " + str(store.color[1]), boxx, fgy+boxy, box_w, box_h)
InputBox.display_box(screen, "b: " + str(store.color[2]), boxx, fgy+boxy*2, box_w, box_h)

InputBox.display_box(screen, "r: " + str(store.bgcolor[0]), boxx2, bgy, box_w, box_h)
InputBox.display_box(screen, "g: " + str(store.bgcolor[1]), boxx2, bgy+boxy, box_w, box_h)
InputBox.display_box(screen, "b: " + str(store.bgcolor[2]), boxx2, bgy+boxy*2, box_w, box_h)

InputBox.display_box(screen, "brush size: " + str(store.size), bsx, bsy, bs_w, bs_h)
InputBox.display_box(screen, "eraser size: " + str(store.esize), bsx, bsy+e, bs_w, bs_h)

mouse = pygame.mouse.get_pos()
coord = [mouse[0]-offset[0], mouse[1]-offset[1]]
font_coord = pygame.font.Font("VeraMono.ttf", 9)
box_coord = pygame.surface.Surface([60, 15])

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 25)

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_z and pygame.key.get_mods() & KMOD_LCTRL:
                drawspace.blit(mem_top, [0,0])
                mem_top.blit(mem_middle, [0,0])
                mem_middle.blit(mem_bottom, [0,0])
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if store.line or store.rect:
                    if store.pos1set == False and store.pos2set == False:
                        if pos[0] > offset[0]-4:
                            store.pos1 = pos
                            store.pos1set = True
                            mem_bottom.blit(mem_middle, [0,0])
                            mem_middle.blit(mem_top, [0,0])
                            mem_top.blit(drawspace, [0,0])
                if store.draw or store.pen:
                    if pos[0] > offset[0]-4:
                        store.down = True
                        mem_bottom.blit(mem_middle, [0,0])
                        mem_middle.blit(mem_top, [0,0])
                        mem_top.blit(drawspace, [0,0])
                if pos[0] > savex and pos[0] < savex+save_w and pos[1] > savey and pos[1] < savey+save_h:
                    save = InputBox.ask(screen, "save", savex, savey, save_w, save_h, 1, initial=store.save)
                    pygame.image.save(drawspace, save + ".jpg")
                    store.save = save
                if pos[0] > boxx and pos[0] < boxx+box_w:
                    if pos[1] > fgy and pos[1] < fgy+box_h:
                        r_input = InputBox.ask(screen, "r", boxx, fgy, box_w, box_h)
                        store.color[0] = int(r_input)
                    if pos[1] > fgy+boxy and pos[1] < fgy+boxy+box_h:
                        g_input = InputBox.ask(screen, "g", boxx, fgy+boxy, box_w, box_h)
                        store.color[1] = int(g_input)
                    if pos[1] > fgy+boxy*2 and pos[1] < fgy+boxy*2+box_h:
                        b_input = InputBox.ask(screen, "b", boxx, fgy+boxy*2, box_w, box_h)
                        store.color[2] = int(b_input)
                if pos[0] > boxx2 and pos[0] < boxx2+box_w:
                    if pos[1] > bgy and pos[1] < bgy+box_h:
                        r_input = InputBox.ask(screen, "r", boxx2, bgy, box_w, box_h)
                        store.bgcolor[0] = int(r_input)
                    if pos[1] > bgy+boxy and pos[1] < bgy+boxy+box_h:
                        g_input = InputBox.ask(screen, "g", boxx2, bgy+boxy, box_w, box_h)
                        store.bgcolor[1] = int(g_input)
                    if pos[1] > bgy+boxy*2 and pos[1] < bgy+boxy*2+box_h:
                        b_input = InputBox.ask(screen, "b", boxx2, bgy+boxy*2, box_w, box_h)
                        store.bgcolor[2] = int(b_input)
                if pos[0] > bsx and pos[0] < bsx+bs_w and pos[1] > bsy and pos[1] < bsy+bs_h:
                    new_size = InputBox.ask(screen, "brush size", bsx, bsy, bs_w, bs_h)
                    store.size = int(new_size)
                if pos[0] > bsx and pos[0] < bsx+bs_w and pos[1] > bsy+e and pos[1] < bsy+bs_h+e:
                    new_size = InputBox.ask(screen, "eraser size", bsx, bsy+e, bs_w, bs_h)
                    store.esize = int(new_size)
                if pos[0] > penx and pos[0] < penx+pen_w and pos[1] > peny and pos[1] < peny+box_h:
                    store.pen = True
                    pygame.draw.rect(screen, light, (penx, peny, pen_w, box_h), 1)
                    store.draw = False
                    pygame.draw.rect(screen, dark, (drawx, drawy, draw_w, box_h), 1)
                    store.line = False
                    pygame.draw.rect(screen, dark, (linex, liney, line_w, box_h), 1)
                    store.rect = False
                    pygame.draw.rect(screen, dark, (rectx, recty, rect_w, box_h), 1)
                if pos[0] > drawx and pos[0] < drawx+draw_w and pos[1] > drawy and pos[1] < drawy+box_h:
                    store.pen = False
                    pygame.draw.rect(screen, dark, (penx, peny, pen_w, box_h), 1)
                    store.draw = True
                    pygame.draw.rect(screen, light, (drawx, drawy, draw_w, box_h), 1)
                    store.line = False
                    pygame.draw.rect(screen, dark, (linex, liney, line_w, box_h), 1)
                    store.rect = False
                    pygame.draw.rect(screen, dark, (rectx, recty, rect_w, box_h), 1)
                if pos[0] > linex and pos[0] < linex+line_w and pos[1] > liney and pos[1] < liney+box_h:
                    store.pen = False
                    pygame.draw.rect(screen, dark, (penx, peny, pen_w, box_h), 1)
                    store.draw = False
                    pygame.draw.rect(screen, dark, (drawx, drawy, draw_w, box_h), 1)
                    store.line = True
                    pygame.draw.rect(screen, light, (linex, liney, line_w, box_h), 1)
                    store.rect = False
                    pygame.draw.rect(screen, dark, (rectx, recty, rect_w, box_h), 1)
                if pos[0] > rectx and pos[0] < rectx+box_rect.get_width() and pos[1] > recty and pos[1] < recty+box_h:
                    store.pen = False
                    pygame.draw.rect(screen, dark, (penx, peny, pen_w, box_h), 1)
                    store.draw = False
                    pygame.draw.rect(screen, dark, (drawx, drawy, draw_w, box_h), 1)
                    store.line = False
                    pygame.draw.rect(screen, dark, (linex, liney, line_w, box_h), 1)
                    store.rect = True
                    pygame.draw.rect(screen, light, (rectx, recty, rect_w, box_h), 1)
                if pos[0] > fillx  and pos[0] < fillx+fill_w and pos[1] > recty and pos[1] < recty+box_h:
                    if store.fill:
                        store.fill = False
                        pygame.draw.rect(screen, dark, (fillx, filly, fill_w, box_h), 1)
                    else:
                        store.fill = True
                        pygame.draw.rect(screen, light, (fillx, filly, fill_w, box_h), 1)
            elif event.button == 2:
                store.down2 = True
                pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if store.pos1set == True:
                    if pos[0] > 0:
                        store.pos2 = pos
                        store.pos2set = True
                        if store.rect:
                            store.drawrect(store.color, store.pos1, store.pos2, store.size)
                        if store.line:
                            store.drawline(store.color, store.pos1, store.pos2, store.size)
                        store.pos1set = False
                        store.pos2set = False
                store.down = False
            if event.button == 2:
                store.down2 = False
        elif event.type == USEREVENT:
            mouse = pygame.mouse.get_pos()
            coord = [mouse[0]-offset[0], mouse[1]-offset[1]]
            if coord[0] < 0:
                coord[0] = 0
            if coord[0] > drawspace.get_width():
                coord[0] = drawspace.get_width()
            if coord[1] < 0:
                coord[1] = 0
            if coord[1] > drawspace.get_height():
                coord[1] = drawspace.get_height()
            box_coord = pygame.surface.Surface([60, 15])
            box_coord.fill(bgcolor)
            box_coord.blit(font_coord.render(str(coord), 1, light), [0, 0])
            if store.down:
                oldpos = pos
                pos = pygame.mouse.get_pos()
                if store.draw:
                    store.drawline(store.color, oldpos, pos, store.size)
                if store.pen:
                    store.aaline(store.color, oldpos, pos)
            if store.down2:
                oldpos = pos
                pos = pygame.mouse.get_pos()
                store.drawline(store.bgcolor, oldpos, pos, store.esize)
                
        border.blit(drawspace, [2, 2])
        screen.blit(border, [153, 3])
        box_color.fill(store.color)
        box_bgcolor.fill(store.bgcolor)
        screen.blit(box_color, [fgx, fgy])
        screen.blit(box_bgcolor, [bgx, bgy])
        screen.blit(box_coord, (screen.get_width()-60, screen.get_height()-13))
        pygame.display.update()
            
    

    
