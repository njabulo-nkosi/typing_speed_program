import math
import random
import time
from tkinter import *
from words import random_words

TIME = 2 * 60


class SpeedTest:
    def __init__(self, window):
        self.window = window

        self.canvas = None
        self.text_widget = None
        self.cpm_label = None
        self.wpm_label = None
        self.timer_label = None
        self.start_time = None
        self.time_remaining = TIME

        self.setup_window()
        self.create_title()
        self.create_canvas()
        self.create_text_widget()
        self.create_labels()
        self.create_buttons()

    def setup_window(self):
        self.window.title('Typing Speed Test')
        self.window.config(padx=50, pady=50, bg='#31511E')

    def create_title(self):
        title = Label(
            self.window,
            text='Typing Speed Test',
            font=('Arial', 30, 'bold'),
            bg='#31511E',
            fg='#F6FCDF',
        )
        title.grid(column=0, row=0, columnspan=3, pady=(0, 20))

    def create_canvas(self):
        self.canvas = Canvas(self.window, width=370, height=150, bg='#31511E', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=10)

        sample_text = " ".join(random.sample(random_words, 50))
        self.canvas.create_text(
            10, 10,
            text=sample_text,
            fill='white',
            width=350,
            font=('Arial', 10, 'normal'),
            anchor='nw',
        )

    def create_text_widget(self):
        self.text_widget = Text(self.window, font=('Arial', 10, 'normal'), width=50, height=10, padx=10, pady=10)
        self.text_widget.grid(column=0, row=2, columnspan=3, pady=10)
        self.text_widget.insert('insert', 'Type here...')

    def create_labels(self):
        self.cpm_label = Label(self.window, text='CPM: 0', bg='#31511E', fg='#F6FCDF', font=('Arial', 12, 'bold'))
        self.cpm_label.grid(column=0, row=3, pady=10)

        self.wpm_label = Label(self.window, text='WPM: 0', bg='#31511E', fg='#F6FCDF', font=('Arial', 12, 'bold'))
        self.wpm_label.grid(column=2, row=3, pady=10)

        self.timer_label = Label(self.window, text='Countdown: 60', bg='#31511E', fg='#F6FCDF', font=('Arial', 12, 'bold'))
        self.timer_label.grid(column=1, row=4, pady=20)

    def create_buttons(self):
        start_button = Button(self.window, text='Start Test', font=('Arial', 10), command=self.start_test)
        start_button.grid(column=1, row=5)

    def start_test(self):
        self.start_time = time.time()
        self.time_remaining = TIME
        self.update_timer()

    def update_timer(self):

        if self.time_remaining > 0:
            count_minute = math.floor(self.time_remaining / 60)
            count_sec = self.time_remaining % 60
            self.timer_label.config(text=f'Countdown: {count_minute:02}:{count_sec:02}')
            self.time_remaining -= 1
            self.window.after(1000, self.update_timer)

        else:
            self.calculate_speed()

    def calculate_speed(self):
        input_text = self.text_widget.get('1.0', 'end-1c').strip()
        word_count = len(input_text.split())
        char_count = len(input_text)

        time_lapsed = (TIME - self.time_remaining) / 60
        words_per_minute = word_count / time_lapsed
        char_per_minute = char_count / time_lapsed

        self.wpm_label.config(text=f'WPM: {int(words_per_minute)}')
        self.cpm_label.config(text=f'CPM: {int(char_per_minute)}')

