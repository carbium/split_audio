import math
from tkinter import Tk, Label, Button, filedialog
from pydub import AudioSegment

class AudioSplitterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Audio Splitter")

        self.label = Label(master, text="Seleccione el archivo de audio a dividir:")
        self.label.pack()

        self.select_button = Button(master, text="Seleccionar archivo", command=self.select_file)
        self.select_button.pack()

        self.split_button = Button(master, text="Dividir archivo", state="disabled", command=self.split_audio)
        self.split_button.pack()

    def select_file(self):
        filetypes = (("Archivos de audio", "*.mp3"), ("Todos los archivos", "*.*"))
        self.filepath = filedialog.askopenfilename(title="Seleccione un archivo de audio", filetypes=filetypes)
        if self.filepath:
            self.label.config(text=f"Archivo seleccionado: {self.filepath}")
            self.split_button.config(state="normal")

    def split_audio(self):
        audio = AudioSegment.from_file(self.filepath, format="mp3")
        audio_duration = len(audio)
        segment_duration = 600000  # 10 minutos
        num_segments = math.ceil(audio_duration / segment_duration)

        for i in range(num_segments):
            start = i * segment_duration
            end = start + segment_duration
            segment = audio[start:end]
            segment.export(f"audio_segment_{i+1}.mp3", format="mp3")

        self.label.config(text="Archivo dividido en partes iguales.")
        self.split_button.config(state="disabled")

root = Tk()
my_gui = AudioSplitterGUI(root)
root.mainloop()