import math as m
class Math_Logic():
    def calc_hor_vec(angle,multiplier): #calculate_horizontal_vector
        return m.cos(m.radians(angle)) * multiplier
    def calc_ver_vec(angle,multiplier): #calculate_vertical_vector
        return m.sin(m.radians(angle)) * -multiplier