# Tic Tac Toe – Python Project 

A Python-based implementation of the classic Tic Tac Toe game, featuring both a **Graphical User Interface (GUI)** and an optional **computer opponent** powered by simple artificial intelligence (AI).

This project is designed to deepen practical skills in Python, Git, GitHub Copilot, and application development workflows — moving from a basic console game to a feature-rich application.

---

## 📋 Project Overview

The goal of this project is to build a **fully functional Tic Tac Toe game** with two playable modes:

- **Player vs Computer (PvC)** – A human player competes against an AI opponent. 
- **Player vs Player (PvP)** – Two human players take turns.

The project will evolve in stages:
1. **Console version** — Text-based gameplay to establish core logic.
2. **GUI version** — A visual interface using Tkinter for improved user experience.
3. **AI integration** — Enable computer to play intelligently.

---

## 🚀 Features

- [x] Display 3×3 board
- [x] Player move input with validation
- [x] Automatic turn switching
- [x] Win and draw detection
- [x] Game restart option
- [x] Graphical User Interface (Tkinter)
- [x] Player vs Computer mode (AI opponent)
- [X] AI opponent with rule based (heuristic) AI - decisions using simple logic
- [ ] AI opponent with Minimax algorithm
- [x] Visual win highlighting
- [ ] Score tracking (optional)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| Tkinter | GUI development |
| Git & GitHub | Version control & project hosting |
| GitHub Copilot | AI-powered coding assistant |
| VS Code | Integrated development environment (IDE) |
| `unittest` (optional) | Unit testing framework |
| Black / Pylint (optional) | Code formatting & linting |

---

## 📂 Project Structure

```bash
tic_tac_toe/
├── .gitignore
├── README.md
├── requirements.txt       # (Optional) dependencies list
├── src/
│   ├── __init__.py
│   ├── ai.py              # AI opponent logic (PvC mode)
│   ├── board.py           # Board class & rendering logic
│   ├── game.py            # Initial terminal based Game engine - replaced by gui.py
│   ├── main.py            # Entry point
│   ├── player.py          # Player management
│   └── gui.py             # Tkinter GUI interface with game engine
├── tests/
│   ├── __init__.py
│   ├── test_board.py
│   ├── test_game.py
│   └── test_ai.py
└── assets/                # (Optional) images, icons, etc.
