import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のSurface
    bg_img_f = pg.transform.flip(bg_img,True,False) #背景画像のSurface
    kk_img = pg.image.load("fig/3.png") #こうかとん画像のSurface
    kk_img = pg.transform.flip(kk_img,True,False) #こうかとん画像の左右反転
    kk_rct = kk_img.get_rect() #こうかとんSurfaceに対応するこうかとんRectの取得
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        rctx=0
        rcty=0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: #上移動
            rctx=-1
        if key_lst[pg.K_DOWN]: #下移動
            rctx=1
        if key_lst[pg.K_LEFT]: #左移動
            rcty=-1
        if key_lst[pg.K_RIGHT]: #右移動
            rcty=2
        kk_rct.move_ip(rcty-1,rctx) #こうかとんを移動させる

        x=tmr%3200 #3200フレーム後にもとに戻る（ループ）
        screen.blit(bg_img, [-x,0]) #背景画像のblit
        screen.blit(bg_img_f, [-x+1600,0])#背景画像を1600フレーム後にblit
        screen.blit(bg_img, [-x+3200,0]) #背景画像を3200フレーム後にblit
        #screen.blit(kk_img, [300, 200]) #こうかとん画像のblit
        screen.blit(kk_img,kk_rct)#こうかとん画像のblit
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()