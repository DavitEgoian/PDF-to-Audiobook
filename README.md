# PDF to Audiobook

Python script that takes a PDF file and converts it into speech.

## 📝 Project Overview
This desktop tool converting text-to-speech (via **pyttsx3**) to turn PDFs into audio files. Users can load a PDF, view its text in a Tkinter interface, and save an MP3 file with a default timestamped filename and a progress bar to track downloading progress.

## 🚀 Features

- **Offline TTS**: Uses `pyttsx3`, so there’s no need for external APIs or internet access.  
- **PDF Extraction**: Powered by **PyPDF2** for reliable text extraction across multiple pages.  
- **Live Preview**: Inspect the PDF text in the built-in editor before exporting.  
- **Progress Indicator**: An indeterminate progress bar appears during conversion, then hides automatically.  
- **Automatic Filename**: Generates a default `audiobook_YYYYMMDD_HHMMSS.mp3` to save time.

## 💻 Installation & Usage

1. **Clone or download** this repository.  
2. Install dependencies:
   ```bash
   pip install PyPDF2 pyttsx3
   ```
3. Launch the app:
   ```bash
   python main.py
   ```
   
## 📂 Project Structure

```
PDF-to-Audiobook/
├── pdf_extractor.py   # Extracts text from a PDF using PyPDF2
├── tts_handler.py     # Wraps pyttsx3 for local text-to-speech synthesis
└── main.py            # Tkinter GUI: load PDF, preview text, and save audio
```

## ⚙️ Customization

- **Voice & Rate**: Tweak `tts_handler.py` to change voice, speaking rate, or volume via `pyttsx3` settings.  
- **GUI Layout**: Modify `main.py`—adjust fonts, widget placement, or add playback controls.  
- **Output Format**: Change the default filename pattern in `main.py`’s `default_filename` logic.

---
