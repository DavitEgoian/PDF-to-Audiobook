# 🎧 PDF to Audiobook

A robust Python desktop application that transforms written PDF documents into spoken audio files, allowing you to listen to your books and papers on the go.

## 📝 Project Overview

This tool provides a seamless interface for converting text-to-speech without requiring an internet connection or paid APIs. Users can load a PDF, preview the extracted text in a GUI editor to make necessary adjustments, and export the result as an MP3 file. It leverages `pyttsx3` for synthesis and `PyPDF2` for extraction.

## 🚀 Features

- **Offline Text-to-Speech**: Powered by **pyttsx3**, enabling completely offline conversion with no API limits or costs.
- **PDF Text Extraction**: Uses **PyPDF2** to reliably extract text content from multi-page documents.
- **Interactive Preview**: Review and edit the extracted text within the app before conversion to ensure audio accuracy.
- **Smart UI**: Built with **Tkinter**, featuring extraction feedback and a progress bar that indicates processing status.
- **Auto-Export**: Automatically generates timestamped filenames (e.g., `audiobook_YYYYMMDD.mp3`) for quick saving.

## 💻 Installation & Usage

### Prerequisites
- Python 3.x

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DavitEgoian/PDF-to-Audiobook.git
   cd PDF-to-Audiobook
   ```

2. **Create a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install PyPDF2 pyttsx3
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📂 Project Structure

```text
PDF-to-Audiobook/
├── pdf_extractor.py   # Logic: Extracts raw text from PDF pages using PyPDF2
├── tts_handler.py     # Logic: Wrapper for pyttsx3 engine configuration and saving
└── main.py            # Interface: Tkinter GUI for file loading, editing, and controls
```

## ⚙️ Customization

- **Voice Settings**: Modify `tts_handler.py` to adjust the speaking rate (words per minute), volume, or switch between male/female system voices.
- **Extraction Logic**: Update `pdf_extractor.py` if you need to handle specific PDF layouts or encrypted files.
- **Output Format**: Change the default naming convention in `main.py` to suit your file organization needs.

## 📄 License

This project is open source and available for personal and educational use.
