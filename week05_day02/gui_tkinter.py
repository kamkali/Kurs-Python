import tkinter as tk


def simple01():
    main_window = tk.Tk()
    main_window.title("First gui application")
    main_window.geometry("700x830")

    # Labels
    label01 = tk.Label(main_window, text='Hello world', bg='#f4f41a',
                       font=('Times', '24', 'bold italic'), fg='#9902ff',
                       height=10, width=10)
    label01.pack(side=tk.LEFT)

    # Buttons
    def button_action():
        if label01.cget('text') == 'Hello world':
            label01.configure(text='Clicked')
        else:
            label01.configure(text='Hello world')

    button01 = tk.Button(main_window, text='button', command=button_action)
    button01.pack(side=tk.LEFT)

    def button2_action():
        tk.Label(main_window, text='Add').pack(side=tk.BOTTOM)

    button02 = tk.Button(main_window, text='Second Button', command=button2_action).pack(side=tk.RIGHT)

    main_window.mainloop()


def simple02():
    main_wind = tk.Tk()
    main_wind.title("Second application")

    c1 = tk.Canvas(bg='#ffff00')
    c1.grid(row=0, column=0)
    c2 = tk.Canvas(bg='#ff9911')
    c2.grid(row=0, column=1)
    c3 = tk.Canvas(bg='#00ffff')
    c3.grid(row=1, column=0)
    c4 = tk.Canvas(bg='#ff00ff')
    c4.grid(row=1, column=1)

    main_wind.mainloop()


if __name__ == '__main__':
    simple02()
