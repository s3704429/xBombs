'''
Created on 19 Mar. 2018

@author: Andrew Sturt
'''

import pygame


class App:
    def __init__(self):
        self._running = True
        self.display_surf = None
        self.size = self.weight, self.height = 640, 400
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._running = True
            
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
            
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
    
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
            
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
