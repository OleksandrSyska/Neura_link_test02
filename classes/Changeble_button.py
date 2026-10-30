from classes.Button import button
class C_Button(button):
    def __init__(self,center_position,texts):
        self.texts = texts
        self.state = 0
        super().__init__(center_position,self.texts[0])

    def Fl_clicked(self,mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            if self.state:
                self.state = 0
            else:
                self.state = 1
            super().change_text(self.texts[self.state])
            return True
        else:
            return False
    def get_state(self):
        return self.state