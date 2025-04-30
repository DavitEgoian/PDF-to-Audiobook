import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_extractor import PDFExtractor
from tts_handler import LocalTTS
import os
from datetime import datetime
import threading

class PDFAudioApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title('PDF to Audiobook')
        self.text_widget = tk.Text(root, wrap='word')
        self.text_widget.pack(expand=True, fill='both', padx=10, pady=10)
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill='x', padx=10, pady=(0,5))
        tk.Button(btn_frame, text='Load PDF', command=self.load_pdf).pack(side='left', padx=(0,5))
        tk.Button(btn_frame, text='Save Audio', command=self.save_audio).pack(side='left')
        self.progress = ttk.Progressbar(root, mode='indeterminate')

    def load_pdf(self) -> None:
        pdf_path = filedialog.askopenfilename(title='Select PDF', filetypes=[('PDF', '*.pdf')])
        if not pdf_path:
            return
        content = PDFExtractor(pdf_path).extract_text()
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert(tk.END, content)

    def save_audio(self) -> None:
        text = self.text_widget.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning('No Text', 'Load a PDF first.')
            return

        default_filename = f"audiobook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        out_path = filedialog.asksaveasfilename(defaultextension='.mp3', initialfile=default_filename, filetypes=[('MP3', '*.mp3')])
        if not out_path:
            return

        self.progress.pack(fill='x', padx=10, pady=(0,10))
        self.progress.start()

        def convert():
            try:
                LocalTTS().synthesize(text, out_path)
                messagebox.showinfo('Saved', f'Audio saved to: {out_path}')
            except Exception as e:
                messagebox.showerror('Error', f'TTS failed: {e}')
            finally:
                self.progress.stop()
                self.progress.pack_forget()

        threading.Thread(target=convert).start()

if __name__ == '__main__':
    root = tk.Tk()
    PDFAudioApp(root)
    root.mainloop()
