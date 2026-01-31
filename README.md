# Price Negotiation Game using Nash Equilibrium

A modern, interactive Python application demonstrating game theory concepts using Nash equilibrium for price negotiation between two players. Features a beautiful PyQt5 GUI with dark/light mode, animations, and clear result visualization.

## Features
- **Nash Equilibrium Calculation:** Simulates a two-player price negotiation using Nash bargaining solution.
- **Modern UI:** Clean, card-based interface with emoji icons, gradients, and smooth animations.
- **Dark/Light Mode:** Instantly toggle between dark and light themes.
- **Visual Effects:** Animated result card, vivid color coding for clarity, and responsive design.

## How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Price_Negotiation.git
   cd Price_negotiation
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install PyQt5
   ```
4. **Run the app:**
   ```bash
   python app.py
   ```

## How to Use
- Enter the minimum and maximum price range for both Player 1 and Player 2.
- Click **Negotiate!** to see the Nash equilibrium price and each player's utility.
- Toggle between dark and light mode using the button in the top right.

## Project Structure
```
├── app.py                # Main entry point
├── nash_logic.py         # Nash equilibrium logic
├── ui/
│   └── main_ui.py        # PyQt5 UI code
└── README.md             # This file
```

## License
MIT License. See [LICENSE](LICENSE) for details.

## Author
- [Thet Hmue Khin](https://github.com/AThet01)

