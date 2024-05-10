import pygame, sys, random, time

#global variables agaraerg

blah = 0
screen_width = 1024
screen_height = 768
'''---------------------------------SPRITES/CLASSES---------------------'''


class Background(pygame.sprite.Sprite):

    def __init__(self, which):
        super().__init__()
        self.image = pygame.image.load("assets/Chinese Restaurant.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


class Equipment(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def click(self, mouse):
        self.rect.center = (mouse)

    def not_clicking(self):
        self.rect.center = (self.x, self.y)

    def collide(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


class Orders(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.orders = ["Scallion Pancake",'scal---Your Heart']
        self.num = random.randint(1,2)
        self.order_list = []
        self.order = ''
        for x in range(self.num):
            self.order_list.append(random.choice(self.orders))
            print(self.order_list)
        for order in self.order_list:
            self.order = f'{self.order} {str(order)},'
        self.font = pygame.font.SysFont("Garamond", 25)
        self.text = self.font.render((self.order), True, "black")
        self.fontrect = self.text.get_rect()
        self.fontrect.topleft = (self.x,self.y)

    def generate_new(self):
        if self.order_list == []:
            for x in range(2):
                self.order_list.append(random.choice(self.orders))
            for order in self.order_list:
                self.order = f'{self.order} {str(order)},'
            self.text = self.font.render((self.order), True, "black")

    def get_text(self):
        return self.text

    def rect_pos(self):
        return self.fontrect.topleft

    def order_complete(self, namey):
        for order in self.order_list:
            if namey == order[:4].lower():
                self.order_list.remove(order)
                self.order = ''
                for order in self.order_list:
                    self.order = f'{self.order} {str(order)},'
                self.text = self.font.render((self.order), True, "black")
                return True


class White(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("assets/White.png"), (300,75))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


class Pan(Equipment):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/pan.png"), (170, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Plate(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(pygame.image.load("assets/plate.png"), (100, 66))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def not_clicking(self):
        self.rect.center = (self.x, self.y)



class Scallion_Pancake(Food):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/Scallion Pancake.png"), (87, 87))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Savory_Bun(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/Savory Bun.png"), (87, 87))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Sweet_Bun(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/Sweet Bun.png"), (87, 87))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Scallion(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/scallion.png"), (90, 90))
        self.image = pygame.transform.rotate(self.image,-37)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if pygame.MOUSEBUTTONUP:
            self.rect.center = (self.x, self.y)


class ChoppedScallion(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/chopped scallion.png"), (120, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Dough(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/dough.png"), (200, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class ScallionDough(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/Scallion Dough.png"), (120, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        


class CuttingBoard(Equipment):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/cutting board.png"), (150, 103))
        # self.image = pygame.transform.rotate(self.image, -12 + 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


def main():
    '''---------------------------------SETUP-------------------------------'''
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game Title')

    # Define Custom Events

    # Instantiate objects and groups
    bg_group = pygame.sprite.Group()
    bg_group.add(Background(0))
    
    plate1 = Plate(screen_width/2 - 25, screen_height/2 - 17)
    plate2 = Plate(screen_width/2 - 175, screen_height/2 - 17)
    plate3 = Plate(screen_width/2 - 25, screen_height/2 + 63)
    plate4 = Plate(screen_width/2 - 175, screen_height/2 + 63)
    plate5 = Plate(screen_width/2 - 25, screen_height/2 + 143)
    plate6 = Plate(screen_width/2 - 175, screen_height/2 + 143)
    
    plate_gp = pygame.sprite.Group(plate1, plate2, plate3, plate4, plate5, plate6)
    plate_gp2 = pygame.sprite.Group()
    plate_list = []
    for x in range(6):
        plate_list.append(f'plate{x + 1}')

    #FINAL FOOD
    scal_pancake_gp = pygame.sprite.Group()
    s_pancake_gp = pygame.sprite.Group()
    for x in range(6):
        s_pancake = Scallion_Pancake(-1000, -1000)
        s_pancake.add(s_pancake_gp)
    s_pancake_list = []
    for x in range(6):
        s_pancake_list.append(f's_pancake{x + 1}')


    savory_bun_gp = pygame.sprite.Group()
    savory_gp = pygame.sprite.Group()
    for x in range(6):
        sav_bun = Savory_Bun(-1000, -1000)
        sav_bun.add(savory_gp)
    savory_bun_list = []
    for x in range(6):
        savory_bun_list.append(f'savory_bun{x + 1}')

    sweet_bun_gp = pygame.sprite.Group()
    sweet_gp = pygame.sprite.Group()
    for x in range(6):
        sweet_bun = Savory_Bun(-1000, -1000)
        sweet_bun.add(sweet_gp)
    sweet_bun_list = []
    for x in range(6):
        sweet_bun_list.append(f'sweet_bun{x + 1}')
    
    #EQUIPMENT
    pan = Pan(screen_width / 2 + 145, screen_height / 2 + 100)
    pan_gp = pygame.sprite.Group(pan)

    cutting_board = CuttingBoard(20 * screen_width / 22, 440)
    cutting_board_gp = pygame.sprite.Group(cutting_board)

    #INGREDIENTS
    scallion = Scallion(screen_width / 4 - 70 + 183, screen_height / 4 * 3 + 50)
    scallion_gp = pygame.sprite.Group(scallion)

    chopped_scallion = ChoppedScallion(-1000, -1000)
    chopped_scallion_gp = pygame.sprite.Group(chopped_scallion)

    dough = Dough(screen_width / 4 - 70, screen_height / 2)
    dough_gp = pygame.sprite.Group(dough)

    scallion_dough = ScallionDough(-1000,-1000)
    scallion_dough_gp = pygame.sprite.Group(scallion_dough)

    

    
    scallion_chopping = 0

    order1 = Orders(30,40)
    order2 = Orders(360,40)
    order3 = Orders(690,40)
    order_gp = pygame.sprite.Group(order1, order2, order3)
    
    

    white1 = White(30,30)
    white2 = White(360, 30)
    white3 = White(690, 30)
    white_gp = pygame.sprite.Group(white1, white2, white3)


    food_gp = pygame.sprite.Group(scallion, chopped_scallion, dough, scallion_dough)

    
    clicking = False

    money = 100
    
    '''----------------------------------LOOP-------------------------------'''
    while True:
        #Handling input (EVENTS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                count = 0
                for scal_pancake in scal_pancake_gp:
                    if scal_pancake.collide() == True:
                        clicking = True
                        sprite = s_pancake_list[count]
                        break
                    count += 1
             
                count1 = 0
                # for plate in plate_gp2:
                #     if plate.collide() == True:
                #         clicking = True
                #         sprite = plate_list[count1]
                #         break
                #     count1 += 1
                    
                for food in food_gp: 
                    if food.collide() == True:
                        clicking = True
                        sprite = str(food)
                

            if event.type == pygame.MOUSEBUTTONUP:
                clicking = False
                scallion.not_clicking()
                for plate in plate_gp:
                    plate.not_clicking()

            if event.type == pygame.MOUSEMOTION:
                if clicking:
                    mouse_pos = pygame.mouse.get_pos()

                    count2 = 0
                    count3 = 0
                    for s_pancake_name in s_pancake_list:
                        if sprite == s_pancake_name:
                            for s_pancake in scal_pancake_gp:
                                if count2 == count3:
                                    s_pancake.click(mouse_pos)
                                count3 += 1
                        count2 += 1

                        
                    count4 = 0
                    count5 = 0
                    for plate_name in plate_list:
                        if sprite == plate_name:
                            for plate in plate_gp:
                                if count4 == count5:
                                    plate.click(mouse_pos)
                                count4 += 1
                        count5 += 1
                    
                    for food in food_gp:
                        if sprite == str(food):
                            food.click(mouse_pos)
                    
                  

        # Updating Sprites
        

        # Drawing
        #Background
        screen.fill('white')  #replace with image or whatever you use up top
        bg_group.draw(screen)
        white_gp.draw(screen)
        font = pygame.font.SysFont('Courier', 28)
        text = font.render(f"Money: {money} coins", True, "black", (255,255,255))
        screen.blit(text, ((40, 724)))
        screen.blit(order1.get_text(), order1.rect_pos())
        screen.blit(order2.get_text(), order2.rect_pos())
        screen.blit(order3.get_text(), order3.rect_pos())

        #equipment
        pan_gp.draw(screen)
        cutting_board_gp.draw(screen)

        #plate
        plate_gp.draw(screen)
        plate_gp2.draw(screen)
        
        #food
        scallion_gp.draw(screen)
        scallion_dough_gp.draw(screen)
        dough_gp.draw(screen)
        chopped_scallion_gp.draw(screen)
        scal_pancake_gp.draw(screen)
        s_pancake_gp.draw(screen)

        #update
        if scallion_chopping == 1:
            scallion_gp.update()

        # Collisions

    #Collision of order
        count6 = 0
        count7 = 0
        for white in white_gp:
            for scal in scal_pancake_gp:
                if pygame.sprite.collide_rect(white, scal):
                    scal.rect.center = (-1000,-1000)
                    scal.remove(scal_pancake_gp)
                    for order in order_gp:
                        if count7 == count6:
                            name = str(scal)[1:5].lower()
                            if order.order_complete(name):
                                order.generate_new()
                                # if (update - start)//60 < 2:
                                #     money += 15
                                # elif (update - start)//60 < 5:
                                #     money += 10
                                # elif (update - start)//60 < 10:
                                #     money += 5
                                # else:
                                #     money += 1
                        count7 += 1
            count6 += 1
        for white in white_gp:
            for plate in plate_gp2:
                if pygame.sprite.collide_rect(white, plate):
                    for pancake in scal_pancake_gp:
                        if pygame.sprite.collide_rect(pancake, plate):
                            pancake.rect.centery -= 20
                            pancake.rect.centerx -= 20
                            plate.remove(plate_gp2)
                            plate.add(plate_gp)
                            
                    
                        
                    
                
    #COLLISION SCALLION AND DOUGH
        if pygame.sprite.groupcollide(chopped_scallion_gp, dough_gp, False, False):
            scallion_dough.rect.center = (screen_width / 4 - 70, screen_height / 2 + 100)
            chopped_scallion.rect.center = (-1000, -1000)    
            if pygame.sprite.Sprite.alive(scallion_dough) == False:
                scallion_dough = ScallionDough(screen_width / 4 - 70, screen_height / 2 + 100)
                scallion_dough_gp = pygame.sprite.Group(scallion_dough)
                food_gp.add(scallion_dough_gp)

    #COLLISION OF SCALLION AND CUTTING BOARD
        for scal in scallion_gp:
            for cut in cutting_board_gp:
                if pygame.sprite.collide_rect(scal, cut):
                    scallion_chopping = 1
                    chopped_scallion.rect.center = cutting_board.rect.center

    #COLLISION ON SCALLION DOUGH AND PAN
        if pygame.sprite.groupcollide(scallion_dough_gp, pan_gp, False, False):
            scallion_chopping = 0
            if not pygame.sprite.groupcollide(pan_gp, scal_pancake_gp, False, False):
                pygame.sprite.Sprite.kill(scallion_dough)
                for s_pancake in s_pancake_gp:
                    if s_pancake not in pygame.sprite.Group.sprites(
                                    scal_pancake_gp):
                        scal_pancake_gp.add(s_pancake)
                        s_pancake.rect.center = (screen_width / 2 + 120,
                                                             screen_height / 2 + 110)
                        print(len(scal_pancake_gp))
                        break
            else:
                scallion_dough.rect.center = (screen_width / 4 - 70, screen_height / 2 + 100)
        
    #COLLISION OF PLATE AND COOKED FOOD
        for plate in plate_gp:
            for pancake in scal_pancake_gp: 
                if pygame.sprite.collide_rect(plate, pancake):
                    if event.type == pygame.MOUSEBUTTONUP:

                        print('collide')
                        pancake.rect.center = plate.rect.center
                        plate_gp2.add(plate)
                        plate_gp.remove(plate)
                        print(plate_gp)
                        
        

        # Updating the window
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
