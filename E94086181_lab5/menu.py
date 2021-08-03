import pygame
import os

from settings import BASE

#將圖片匯入
MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_BIN_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_BIN_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        '''
            將圖片initialize之後,把upgrade按鈕和sell按鈕裝上
            並且設定中央在哪
        :param x:
        :param y:
        '''
        self.image_menu = pygame.transform.scale(MENU_IMAGE, (200, 200))
        self.image_button_upgrade = pygame.transform.scale(UPGRADE_BIN_IMAGE, (60, 60))
        self.image_button_sell = pygame.transform.scale(SELL_BIN_IMAGE, (40, 40))

        self.rect = self.image_menu.get_rect()
        self.rect.center = (x, y)
        '''self.__buttons = [Button(UPGRADE_BIN_IMAGE, "upgrade", self.rect.centerx, self.rect.centery - 75),
                          Button(SELL_BIN_IMAGE, "sell", self.rect.centerx,self.rect.centery + 75)]  # (Q2) Add buttons here'''

        self.rect_image_button_upgrade_menu = self.image_button_upgrade.get_rect()
        self.rect_image_button_upgrade_menu.center = (x, y-70)

        self.rect_image_button_sell_menu = self.image_button_sell.get_rect()
        self.rect_image_button_sell_menu.center = (x, y+75)

        self.__buttons = [Button(self.image_button_upgrade, "upgrade", self.rect.centerx, self.rect.centery - 75),
                          Button(self.image_button_sell, "sell", self.rect.centerx,self.rect.centery + 75)]  # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        # draw button
        # (Q2) Draw buttons here
        '''
            加入圖片到視窗
        '''
        win.blit(self.image_menu, self.rect)
        win.blit(self.image_button_upgrade,self.rect_image_button_upgrade_menu)
        win.blit(self.image_button_sell, self.rect_image_button_sell_menu)
        return None

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons



class Button:
    def __init__(self, image, name, x, y):
        '''
            定義照片且iniyialize圖片資訊
        :param image:
        :param name:
        :param x:
        :param y:
        '''
        self.name = name
        self.image = image
        self.rect=image.get_rect()#矩形是圖片轉成的
        self.rect.center=(x,y)#矩形的中心點
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        #有點擊在框框中,回傳True
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name










