"""
1. Stwórz formularz o wielkości 700x700 o nazwie Klawisz.
2. Dodaj do formularza, panel o wielkości 500x500 i umieść go tak, by z jego lewej strony .
3. Wstaw do panelu klawisz o wielkości 100x25 i dwa suwaki. Jeden poziomy poniżej panelu, drugi
pionowy po jego lewej stronie i ustal im odpowiednie orientację i długości by zrównały się z panelem.
Oprogramuj suwaki tak, aby wraz z przesunięciem suwaków klawisz przesuwał się po całym panelu, ale nie wychodził poza niego.
4. Zmień etykietę klawisza na postać x, y gdzie x jest wartością pozycji suwaka poziomego, a y pionowego.
"""
import tkinter as tk


def run():
    main_form = tk.Tk()
    main_form.geometry('700x700')
    main_form.title('Klawisz')

    panel_width = 500
    panel_height = 500

    panel = tk.Frame(main_form, bg='#ff8800', height=panel_width, width=panel_height)
    panel.grid(row=0, column=1)
    panel.pack_propagate(0)

    # label_frame = tk.Frame(panel, width=100, height=25, bg='#0fff00')
    # label_frame.pack()

    label_width = 100
    label_height = 25

    available_width = panel_width - label_width
    available_height = panel_height - label_height

    label = tk.Button(panel, bg='#000000')
    label.place(width=label_width, height=label_height)

    vertical_var = tk.DoubleVar()
    horizontal_var = tk.DoubleVar()
    vertical_var.set(0)
    horizontal_var.set(0)

    def set_text():
        label.configure(text=f'{horizontal_var.get()},{vertical_var.get()}')

    def move(val):
        label.place(width=label_width, height=label_height,
                    x=horizontal_var.get() * available_width,
                    y=vertical_var.get() * available_height)
        set_text()

    slider_1 = tk.Scale(main_form, variable=vertical_var, from_=0, to=1, orient=tk.VERTICAL, resolution=0.01,
                        showvalue=False, command=move)
    slider_1.grid(row=0, column=0, sticky=tk.NS)

    slider_1 = tk.Scale(main_form, variable=horizontal_var, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.01,
                        showvalue=False, command=move)
    slider_1.grid(row=1, column=1, sticky=tk.EW)

    set_text()

    main_form.mainloop()


if __name__ == '__main__':
    print("hello")
    run()
