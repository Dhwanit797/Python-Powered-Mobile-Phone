# 📱 PyPhone — Python Command-Line Mobile Phone

## 📌 Description

**PyPhone** is a Python-powered command-line “mobile phone” simulation that provides multiple built-in applications through a centralized menu system.

The project demonstrates **modular programming**, **CLI interaction**, and integration of different utilities like a calculator, notes manager, games, and even a GUI web browser using PyQt5.

It acts as a mini operating system where users can navigate between apps from a main menu.

---

## 🚀 Features

### 🧮 Calculator

* Evaluate mathematical expressions
* Continuous calculation loop
* Custom exit condition

### 🎯 Perfect Guess Game

* Random number guessing game
* Attempt counter
* Replay support

### ⏰ Current Time Display

* Shows real-time clock updates
* Automatic exit after 5 seconds

### 📝 Notes Manager

* Create new notes
* Rewrite existing notes
* Read saved notes
* File-based storage system

### 🌐 Web Browser (GUI)

* Built with **PyQt5**
* Back, Forward, Refresh & Home buttons
* URL navigation bar
* Embedded web rendering

---

## 🧱 Project Structure

```
PyPhone/
│
├── main.py
├── calc.py
├── current_time.py
├── notes.py
├── perfect_guess.py
├── web_browser.py
│
└── README.md
```

---

## ⚙️ Requirements

* Python 3.x
* PyQt5
* PyQtWebEngine

Install dependencies:

```bash
pip install PyQt5 PyQtWebEngine
```

---

## ▶️ How to Run

```bash
python main.py
```

You will see:

```
====== My Phone ======
1. Calculator
2. Perfect Guess Game
3. Current Time Display
4. Notes
5. Web Browser
6. Exit
```

Select an option to launch an app.

---

## 🧠 Concepts Demonstrated

* Modular programming
* Python CLI applications
* File handling
* Exception handling
* Game logic
* Time & system utilities
* PyQt5 GUI integration
* Event-driven programming

---

## ⚠️ Notes

* The calculator uses `eval()` which can be unsafe for untrusted input.
* The web browser requires a GUI environment.
* Notes are stored as `.txt` files in the project directory.

---

## 🔮 Future Improvements (Ideas)

* Add authentication / lock screen
* Music player module
* Contact manager
* Settings menu
* Voice assistant
* Replace `eval()` with safe parser
* Convert CLI UI into full GUI phone
* Add themes / colors
* Mobile APK using Kivy

---

## 👨‍💻 Author

**Dhwanit**
Python Developer & Student

---
