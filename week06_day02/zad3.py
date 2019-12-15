import tkinter as tk


def gui():
    window = tk.Tk()
    window.title('Zadanie 3')
    window.geometry('700x700')

    panel_width = 500
    panel_height = 500

    label_width = 100
    label_height = 25

    max_width = panel_width - label_width
    max_height = panel_height - label_height

    panel = tk.Frame(window, bg='#0ff000', width=panel_width, height=panel_height)
    panel.grid(row=0, column=0)

    label = tk.Button(panel, bg='#124356')
    label.place(width=label_width, height=label_height)

    def set_text():
        label.configure(text=f'{vert_val.get()},{horiz_val.get()}')

    def move_sliders(val):
        label.place(width=label_width, height=label_height,
                    x=horiz_val.get() * max_width, y=vert_val.get() * max_height)
        set_text()

    vert_val = tk.DoubleVar()
    horiz_val = tk.DoubleVar()

    set_text()

    slider_horizontal = tk.Scale(window, orient=tk.HORIZONTAL, from_=0, to=1, resolution=0.01, showvalue=False,
                                 command=move_sliders, variable=horiz_val)
    slider_horizontal.grid(row=1, column=0, sticky=tk.EW)

    slider_vertical = tk.Scale(window, orient=tk.VERTICAL, from_=0, to=1, resolution=0.01, showvalue=False,
                               command=move_sliders, variable=vert_val)
    slider_vertical.grid(row=0, column=1, sticky=tk.NS)

    window.mainloop()


if __name__ == '__main__':
    gui()
