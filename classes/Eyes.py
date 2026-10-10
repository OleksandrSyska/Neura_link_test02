from classes.Math_Logic import Math_Logic as m
from pygame import draw as D
import classes.colors as c

class Eyes():
    def lines(self,center_x,center_y,angle,bg,screen,creen_sizes,fl_draw_lines):
        x = float(center_x)
        y = float(center_y)
        distance_FW = 0
        for dis in range(300):
            x += m.calc_hor_vec(angle,1)
            y += m.calc_ver_vec(angle,1) 

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= creen_sizes[0] or iy < 0 or iy >= creen_sizes[1]:
                distance_FW = dis
                break

            color = bg.get_at((ix, iy))

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_FW = dis
                break
        if not distance_FW:
            distance_FW = dis
        if fl_draw_lines:
            D.line(
                screen,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )
    #---------------------------------------------------------------------------
        x = float(center_x)
        y = float(center_y)
        distance_R = 0
        for dis in range(300):
            x += m.calc_hor_vec(angle-90,1)
            y += m.calc_ver_vec(angle-90,1)
            
            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= creen_sizes[0] or iy < 0 or iy >= creen_sizes[1]:
                distance_R = dis
                break

            color = bg.get_at((ix, iy))

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_R = dis
                break
        if not distance_R:
            distance_R = dis
        if fl_draw_lines:
            D.line(
                screen,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )
#---------------------------------------------------------------------------
        x = float(center_x)
        y = float(center_y)
        distance_L = 0
        for dis in range(300):
            x += m.calc_hor_vec(angle+90,1)
            y += m.calc_ver_vec(angle+90,1)

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= creen_sizes[0] or iy < 0 or iy >= creen_sizes[1]:
                distance_L = dis
                break

            color = bg.get_at((ix, iy))

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_L = dis
                break
        if not distance_L:
            distance_L = dis
        if fl_draw_lines:
            D.line(
                screen,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )
#---------------------------------------------------------------------------
        x = float(center_x)
        y = float(center_y)
        distance_R45 = 0
        for dis in range(300):

            x += m.calc_hor_vec(angle-45,1)
            y += m.calc_ver_vec(angle-45,1)

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= creen_sizes[0] or iy < 0 or iy >= creen_sizes[1]:
                distance_R45 = dis
                break

            color = bg.get_at((ix, iy))

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_R45 = dis
                break
        if not distance_R45:
            distance_R45 = dis
        if fl_draw_lines:
            D.line(
                screen,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )
#---------------------------------------------------------------------------
        x = float(center_x)
        y = float(center_y)
        distance_L45 = 0
        for dis in range(300):
            x += m.calc_hor_vec(angle+45,1)
            y += m.calc_ver_vec(angle+45,1)


            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= creen_sizes[0] or iy < 0 or iy >= creen_sizes[1]:
                distance_L45 = dis
                break

            color = bg.get_at((ix, iy))

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_L45 = dis
                break
        if not distance_L45:
            distance_L45 = dis
        if fl_draw_lines:
            D.line(
                screen,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )

        if not (distance_FW and distance_R and distance_L and distance_R45 and distance_L45):
            return 0 
        return [distance_FW,distance_R,distance_L,distance_R45,distance_L45]
