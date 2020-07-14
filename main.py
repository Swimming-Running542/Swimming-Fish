import pygame as py, random


py.init() 

screen_info = py.display.Info() 
print(screen_info)

size = (width, height) = (screen_info.current_w, screen_info.current_h) 
screen = py.display.set_mode(size)
clock = py.time.Clock()

color = (0, 127, 255)
fish_image = py.image.load('fish.png')
fish_image = py.transform.smoothscale(fish_image, (80,80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width // 2, height // 2)

speed = py.math.Vector2(10, 0)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
fish_image = py.transform.rotate(fish_image, int(rotation)) 



def move_fish():
  global fish_image
  fish_rect.move_ip(speed)
  if fish_rect.top < 0 or fish_rect.bottom > 600:
    speed[1] *= -1
    fish_image = py.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1]) 

  if fish_rect.right < 0 or fish_rect.left > 800:
    speed[0] *= -1
    fish_image = py.transform.flip(fish_image, True, False)
    fish_rect.move_ip(speed [0], 0) 
  
  
    
    



def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    py.display.flip()

if __name__ == '__main__':
  main()
