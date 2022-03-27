import japanize_kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        label = Label(text='こんにちは世界！')
        return label

if __name__ == "__main__":
    HelloApp().run()