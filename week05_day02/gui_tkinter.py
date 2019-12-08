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
        print(f'Clicked')

    w = tk.Button(main_window, text='button', command=button_action)
    w.pack(side=tk.LEFT)

    main_window.mainloop()


if __name__ == '__main__':
    simple01()
