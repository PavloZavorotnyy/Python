#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

def fun_search():
    if text_field.get().strip() != "":
        if system_search.get() == "google":
            webbrowser.open('https://www.google.com/search?q='+text_field.get())
        if system_search.get() == "wikipedia":
            webbrowser.open('https://uk.wikipedia.org/wiki/'+text_field.get())
        if system_search.get() == 'gmail':
            webbrowser.open('https://mail.google.com/mail/u/0/?shva=1#inbox')
        if system_search.get() == 'facebook':
            webbrowser.open('https://www.facebook.com/')
    else:
        if system_search.get() == 'gmail':
            webbrowser.open('https://mail.google.com/mail/u/0/?shva=1#inbox')
        if system_search.get() == 'facebook':
            webbrowser.open('https://www.facebook.com/')

def fun_event_click_search():
    fun_search()

def fun_event_enter_text_field(event):
    fun_search()

app = tk.Tk()

app.title("Search system")

search_lable = ttk.Label(app, text='Search')

search_lable.grid(row=0, column=0)

text_field = ttk.Entry(app, width=35)

text_field.grid(row=0, column=1)

system_search = StringVar()

text_field.bind('<Return>', fun_event_enter_text_field)

btn_search = ttk.Button(app, text='Search', width=15, command=fun_event_click_search)

btn_search.grid(row=0, column=2)

radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=system_search)
radio_wiki = ttk.Radiobutton(app, text='Wikipedia', value='wikipedia', variable=system_search)
radio_gmail = ttk.Radiobutton(app, text='GMail', value='gmail', variable=system_search)
radio_fasebook = ttk.Radiobutton(app, text='Facebook', value='facebook', variable=system_search)

radio_google.grid(row=1, column=1, sticky=W)
radio_wiki.grid(row=1, column=2, sticky=W)
radio_gmail.grid(row=2, column=1, sticky=W)
radio_fasebook.grid(row=2, column=2, sticky=W)

app.wm_attributes('-topmost', True)

# main loop
app.mainloop()

