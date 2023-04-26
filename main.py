from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from ruffier import *
from kivy.core.window import Window

txt_instruction = '''
Данное приложение позволит вам с помощью теста Руфье \n провести первичную диагностику вашего здоровья.\n
Проба Руфье представляет собой нагрузочный комплекс, \n предназначенный для оценки работоспособности сердца при физической нагрузке.\n
У испытуемого определяют частоту пульса за 15 секунд.\n
Затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n
После окончания нагрузки пульс подсчитывается вновь: \nчисло пульсаций за первые 15 секунд, 30 секунд отдыха,\n число пульсаций за последние 15 секунд.\n'''

txt_test1 = '''Замерьте пульс за 15 секунд.\n
Результат запишите в соответствующее поле.'''

txt_test2 = '''Выполните 30 приседаний за 45 секунд.\n 
Нажмите кнопку "Начать", чтобы запустить счетчик приседаний.\n
Делайте приседания со скоростью счетчика.'''

txt_test3 = '''В течение минуты замерьте пульс два раза:\n 
за первые 15 секунд минуты, затем за последние 15 секунд.\n
Результаты запишите в соответствующие поля.'''

txt_sits = 'Выполните 30 приседаний за 45 секунд.'

b1_1 = ''
b1_2 = 7
b2_3, b3_1, b3_2 = 0, 0, 0


# Создадим класс-наследник App. В нём будет дописываться функционал приложения.
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="main"))
        sm.add_widget(Screen2(name='scr2'))
        sm.add_widget(Screen3(name='scr3'))
        sm.add_widget(Screen4(name='scr4'))
        sm.add_widget(Screen5(name='scr5'))
        return sm


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        b1 = Label(text=txt_instruction)
        v1.add_widget(b1)
        h1 = BoxLayout(size_hint=(0.3, 0.1), pos_hint={'x': 0.1})
        b1_1 = Label(text='Введите имя')
        self.ti_1 = TextInput()
        h1.add_widget(b1_1)
        h1.add_widget(self.ti_1)
        v1.add_widget(h1)
        h2 = BoxLayout(size_hint=(0.3, 0.1), pos_hint={'x': 0.1})
        b1_2 = Label(text='Введите возраст')
        self.ti_2 = TextInput()
        h2.add_widget(b1_2)
        h2.add_widget(self.ti_2)
        v1.add_widget(h2)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        v1.add_widget(self.btn)
        self.btn.on_press = self.next
        self.add_widget(v1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "scr2"
        global b1_1
        global b1_2
        b1_1 = self.ti_1.text
        b1_2 = int(self.ti_2.text)


class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v2 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        h3 = BoxLayout(size_hint=(0.6, 0.1), pos_hint={'x': 0.3})
        b2_3 = Label(text='Введите результат')
        self.ti_3 = TextInput()
        b2_2 = Label(text=txt_test1)
        self.b2 = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        v2.add_widget(b2_2)
        h3.add_widget(b2_3)
        h3.add_widget(self.ti_3)
        v2.add_widget(h3)
        v2.add_widget(self.b2)
        self.b2.on_press = self.next
        self.add_widget(v2)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "scr3"
        global b2_3
        b2_3 = int(self.ti_3.text)


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v3 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        b4_1 = Label(text=txt_test2)
        self.b4 = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        v3.add_widget(b4_1)
        v3.add_widget(self.b4)
        self.add_widget(v3)
        self.b4.on_press = self.next

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "scr4"


class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v4 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        b1 = Label(text=txt_test3)
        v4.add_widget(b1)
        h1 = BoxLayout(size_hint=(0.3, 0.1), pos_hint={'x': 0.1})
        b3_1 = Label(text='Результат')
        self.ti_1 = TextInput()
        h1.add_widget(b3_1)
        h1.add_widget(self.ti_1)
        v4.add_widget(h1)
        h2 = BoxLayout(size_hint=(0.3, 0.1), pos_hint={'x': 0.1})
        b3_2 = Label(text='Результат после отдыха')
        self.ti_2 = TextInput()
        h2.add_widget(b3_2)
        h2.add_widget(self.ti_2)
        v4.add_widget(h2)
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        v4.add_widget(self.btn)
        self.btn.on_press = self.next
        self.add_widget(v4)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "scr5"
        global b3_1
        global b3_2
        b3_1 = int(self.ti_1.text)
        b3_2 = int(self.ti_2.text)


class Screen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v5 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.b5 = Label(text='')
        v5.add_widget(self.b5)
        self.add_widget(v5)
        self.on_enter = self.before

    def before(self):
        global b1_1
        self.b5.text = b1_1 + '\n' + test(b2_3, b3_1, b3_2, b1_2)


app = MyApp()
app.run()