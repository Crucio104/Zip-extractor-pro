# 📦 Zip Extractor Pro

A modern, user-friendly GUI application for extracting ZIP files with real-time progress tracking and an elegant interface.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Modern GUI Design**: Clean and professional interface with a modern color scheme
- **Real-Time Progress Bar**: Animated progress bar showing extraction progress from 0% to 100%
- **File-by-File Tracking**: See which file is currently being extracted
- **Hover Effects**: Interactive buttons with smooth hover animations
- **Status Messages**: Clear visual feedback for every action
- **Easy File Selection**: Browse buttons for selecting ZIP files and destination folders
- **Error Handling**: Comprehensive error messages for troubleshooting
- **Total Files Count**: Displays the number of files extracted upon completion

## Interface

The application features:
- **Header Section**: Blue header with application title and subtitle
- **Card-Based Layout**: White cards on a light gray background for a modern look
- **Input Fields**: Highlighted input fields for ZIP file and destination folder
- **Progress Tracking**: Percentage display and current file name during extraction
- **Color-Coded Status**: Green for success, red for errors, blue for processing

## Project Structure

```
Zip file extractor/
│
├── ZipExtractor.py      # Main application file
├── requirements.txt     # Project dependencies (standard library only)
├── run.bat             # Windows launch script
├── .gitignore          # Git ignore file
├── LICENSE             # MIT License
└── README.md           # This file
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)
  - **Windows/macOS**: Included by default
  - **Linux**: May need to install separately (see requirements.txt)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd "Zip file extractor"
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```
   Make sure it's Python 3.6 or higher

3. **Check requirements**
   ```bash
   # On Linux, if tkinter is not installed:
   # Ubuntu/Debian: sudo apt-get install python3-tk
   # Fedora: sudo dnf install python3-tkinter
   # Arch Linux: sudo pacman -S tk
   ```

### Running the Application

#### Option 1: Quick Launch (Windows)
Simply double-click the `run.bat` file

#### Option 2: Command Line
```bash
python ZipExtractor.py
```

#### Option 3: PowerShell (Windows)
```powershell
python ZipExtractor.py
```

## How to Use

1. **Launch the Application**: Run `ZipExtractor.py`
2. **Select ZIP File**: Click the "Browse" button next to "ZIP File to Extract" and choose your ZIP file
3. **Choose Destination**: Click the "Browse" button next to "Destination Folder" and select where to extract files
4. **Extract**: Click the "Extract ZIP File" button to start the extraction process
5. **Monitor Progress**: Watch the progress bar and status messages as files are extracted
6. **Complete**: A success message will appear when extraction is finished

## Color Scheme

The application uses a carefully selected modern color palette:

- **Background**: `#f0f2f5` - Light gray for a clean look
- **Primary Color**: `#4A90E2` - Blue for headers and browse buttons
- **Secondary Color**: `#50C878` - Green for the extract button and success messages
- **Text Color**: `#2c3e50` - Dark gray for readable text
- **Card Color**: `#ffffff` - White for content cards

## Technical Details

### Built With

- **Python**: Programming language
- **Tkinter**: GUI framework
- **ttk**: Themed widgets for modern UI components
- **zipfile**: Built-in library for ZIP file operations

### Key Components

- `ZipExtractorApp`: Main application class
- `create_widgets()`: Builds the GUI interface
- `extract_zip()`: Handles file extraction with progress tracking
- `check_inputs()`: Validates user inputs before enabling extraction
- `on_hover()/on_leave()`: Manages button hover effects

## Features Breakdown

### Progress Bar
- **Mode**: Determinate (shows actual progress percentage)
- **Updates**: Real-time updates as each file is extracted
- **Visual Feedback**: Smooth animation from 0% to 100%

### User Experience
- Disabled extract button until both fields are filled
- Visual feedback for file selection
- Current file name displayed during extraction
- Hover effects on all buttons
- Clear success/error messages

## Error Handling

The application handles various error scenarios:
- Invalid ZIP file format
- Permission errors
- Disk space issues
- Corrupted archives
- Missing files or directories

All errors are displayed in user-friendly dialog boxes with clear error messages.

## Requirements

```
Python >= 3.6
tkinter (included with Python on Windows/macOS)
```

**Note**: This application uses only Python's standard library. No external packages need to be installed via pip!

## 🔧 Troubleshooting

### Tkinter not found (Linux only)
If you get an error about tkinter not being available:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### Python not recognized
Make sure Python is added to your system PATH during installation.

### Permission errors during extraction
Ensure you have write permissions for the destination folder.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with Python's standard library
- GUI powered by Tkinter
- Icons: Unicode emoji characters

---

**Enjoy extracting your ZIP files with style!**
