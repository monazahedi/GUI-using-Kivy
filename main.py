
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class ProgramLayout(FloatLayout):
    pass

class SDOF_LayoutsApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return ProgramLayout()

if __name__ == '__main__':
    SDOF_LayoutsApp().run()







