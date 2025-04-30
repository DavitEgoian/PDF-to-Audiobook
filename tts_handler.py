import pyttsx3

class LocalTTS:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()

    def synthesize(self, text: str, output_path: str) -> None:
        self.engine.save_to_file(text, output_path)
        self.engine.runAndWait()