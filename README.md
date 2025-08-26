# 🏓 Ping Pong Game in Python

Welcome to the classic **Ping Pong** game — built using Python's `turtle` module! This game allows **two players** to compete in real time using simple keyboard controls.

---

## 🎮 Gameplay

- Two paddles on either side of the screen.
- A ball that bounces off walls and paddles.
- Each time a player misses the ball, the other player scores a point.
- After each point, the game pauses and asks if you want to continue.
- First to whatever score you choose (or just play for fun)!

---

## 👥 Two-Player Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| Left   | `W`     | `S`       |
| Right  | `↑`     | `↓`       |

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required — just the standard `turtle` module, which comes with Python.

---

## 🚀 How to Run

1. Clone this repository or download the `.py` files.
2. Make sure the following files are in the same directory:
    - `main.py` (or your main game file)
    - `paddle.py`
    - `ball.py`
    - `scoreboard.py`
3. Run the game:

```bash
python main.py
```

---

## 🧩 Project Structure

```
ping-pong/
├── main.py            # Game logic and event loop
├── paddle.py          # Paddle class (movement, position)
├── ball.py            # Ball class (movement, bouncing)
├── scoreboard.py      # Scoreboard class (keeping and displaying score)
```

---

## ✨ Features

- Real-time multiplayer
- Smooth ball movement and collision
- Scoring system
- User prompt to continue or end game
- Keyboard controls with `turtle.onkey()`

---

## 📸 Screenshots

> *(Add screenshots or GIFs of your game here if possible)*

---

## 📌 Notes

- The game currently pauses after each point to ask players if they want to continue. If controls stop working after resuming, make sure to call `screen.listen()` after each prompt (this is handled in the code).
- You can easily expand the game with:
  - Sound effects
  - Increasing ball speed
  - Game timer or round limits

---

## 📚 Learnings

This project is a great introduction to:
- Python OOP (Object-Oriented Programming)
- Using the `turtle` graphics module
- Handling keyboard events
- Game loops and collision detection

---

## 🙌 Credits

Developed with ❤️ using Python and Turtle graphics.
