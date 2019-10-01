# kivy.require("1.10.0")
from caesarcipher import caesar_cipher
from affinecipher import affine_cipher
from kivy.app import App
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

"""
Variables are stored in GlobalShared.py
Kivy code is in presentationeffects.kv
"""


class MainScreen(Screen):
    pass

class CaesarSelect(Screen):
    pass

class CaesarEncrypt(Screen):
    def caesar_encrypt(self, message, key):
        if message and key:
            try:
                self.translate_ce = caesar_cipher(message, int(key))
                self.translate_ce.encrypt()
                self.display.text = self.translate_ce.get_caesar_encrypted()

            except Exception:
                self.display.text = "Error"

class CaesarDecrypt(Screen):
    def caesar_decrypt(self, message):
        if message:
            try:
                self.translate_cd = caesar_cipher(message)
                self.translate_cd.decrypt()
                self.display.text = self.translate_cd.get_caesar_decrypted()

            except Exception:
                self.display.text = "Error"

class AffineSelect(Screen):
    pass

class AffineEncrypt(Screen):
    def affine_encrypt(self, message, add, multiply):
        if message and add and multiply:
            try:
                self.translate_ae = affine_cipher(message, int(add),
                                               int(multiply))
                self.translate_ae.encrypt()
                self.display.text = self.translate_ae.get_affine_encrypted()

            except Exception:
                self.display.text = "Error"

class AffineDecrypt(Screen):
    def affine_decrypt(self, message):
        if message:
            try:
                self.translate_ad = affine_cipher(message)
                self.translate_ad.decrypt()
                self.display.text = self.translate_ad.get_affine_decrypted()

            except Exception:
                self.display.text = "Error"

class ScreenManagement(ScreenManager):
    pass

class CustomWidget(Widget):
    pass

class CaesarResponse(Widget):
    pass

presentation = Builder.load_file("presentationeffects.kv")

class MainApp(App):

    def build(self):
        self.title = 'Cipher'

        return presentation

if __name__ == "__main__":
    MainApp().run()

