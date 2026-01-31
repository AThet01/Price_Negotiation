# Main UI for Nash Negotiation Game
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from nash_logic import nash_negotiation

from PyQt5.QtWidgets import QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QLinearGradient, QPalette, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

class NashNegotiationUI(QWidget):
    DARK_STYLE = {
        'bg': "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #232946, stop:1 #393e46);",
        'card': "background: rgba(255,255,255,0.07); border-radius: 18px; border: 2px solid #eebbc3; padding: 24px 18px 18px 18px;",
        'result': "background: rgba(238,187,195,0.13); border-radius: 14px; border: 1.5px solid #eebbc3; margin-top: 18px; padding: 18px 10px;",
        'text': "color: #eebbc3;",
        'input': "background: #121629; color: #eebbc3; border-radius: 8px; padding: 6px;"
    }
    LIGHT_STYLE = {
        'bg': "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #f7f7ff, stop:1 #e2eafc);",
        'card': "background: rgba(0,0,0,0.04); border-radius: 18px; border: 2px solid #232946; padding: 24px 18px 18px 18px;",
        'result': "background: rgba(200,220,255,0.13); border-radius: 14px; border: 1.5px solid #232946; margin-top: 18px; padding: 18px 10px;",
        'text': "color: #1a237e;",  # Changed to a deeper blue for better clarity
        'input': "background: #f7f7ff; color: #232946; border-radius: 8px; padding: 6px; border: 1px solid #232946;"
    }
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Price Negotiation Game using Nash Equilibrium")
        self.setWindowIcon(QIcon.fromTheme("applications-games"))
        self.setMinimumSize(520, 420)
        self.dark_mode = True
        self.anim = None
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        font = QFont("Segoe UI", 13)
        title = QLabel("\U0001F4B0 Nash Equilibrium Negotiation")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("margin-bottom: 18px;")

        # Theme toggle button
        self.theme_btn = QPushButton("🌙 Dark Mode")
        self.theme_btn.setCheckable(True)
        self.theme_btn.setChecked(True)
        self.theme_btn.setStyleSheet("padding: 6px 18px; border-radius: 10px; background: #eebbc3; color: #232946; font-weight: bold;")
        self.theme_btn.clicked.connect(self.toggle_theme)

        # Card frame for input
        self.card = QFrame()
        card_layout = QVBoxLayout()

        # Player 1
        p1_label = QLabel("\U0001F464 Player 1 Price Range:")
        p1_label.setFont(font)
        self.p1_min = QLineEdit()
        self.p1_min.setPlaceholderText("Min")
        self.p1_max = QLineEdit()
        self.p1_max.setPlaceholderText("Max")
        for w in (self.p1_min, self.p1_max):
            w.setFont(font)
        p1_inputs = QHBoxLayout()
        p1_inputs.addWidget(self.p1_min)
        p1_inputs.addWidget(QLabel("to"))
        p1_inputs.addWidget(self.p1_max)

        # Player 2
        p2_label = QLabel("\U0001F465 Player 2 Price Range:")
        p2_label.setFont(font)
        self.p2_min = QLineEdit()
        self.p2_min.setPlaceholderText("Min")
        self.p2_max = QLineEdit()
        self.p2_max.setPlaceholderText("Max")
        for w in (self.p2_min, self.p2_max):
            w.setFont(font)
        p2_inputs = QHBoxLayout()
        p2_inputs.addWidget(self.p2_min)
        p2_inputs.addWidget(QLabel("to"))
        p2_inputs.addWidget(self.p2_max)

        # Button
        calc_btn = QPushButton("\U0001F91D Negotiate!")
        calc_btn.setFont(QFont("Segoe UI", 14, QFont.Bold))
        calc_btn.clicked.connect(self.calculate_nash)

        # Result card
        self.result_card = QFrame()
        self.result = QLabel("")
        self.result.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.result.setAlignment(Qt.AlignCenter)
        self.result_card.setLayout(QVBoxLayout())
        self.result_card.layout().addWidget(self.result)

        # Assemble card
        card_layout.addWidget(p1_label)
        card_layout.addLayout(p1_inputs)
        card_layout.addSpacing(10)
        card_layout.addWidget(p2_label)
        card_layout.addLayout(p2_inputs)
        card_layout.addSpacing(10)
        card_layout.addWidget(calc_btn)
        self.card.setLayout(card_layout)

        # Main layout
        vbox = QVBoxLayout()
        vbox.addSpacing(18)
        vbox.addWidget(title)
        vbox.addWidget(self.theme_btn, alignment=Qt.AlignRight)
        vbox.addSpacing(10)
        vbox.addWidget(self.card)
        vbox.addWidget(self.result_card)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def calculate_nash(self):
        try:
            p1_min = float(self.p1_min.text())
            p1_max = float(self.p1_max.text())
            p2_min = float(self.p2_min.text())
            p2_max = float(self.p2_max.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers for all fields.")
            return
        price, (u1, u2) = nash_negotiation((p1_min, p1_max), (p2_min, p2_max))
        if price is None:
            self.result.setText("\U0001F6AB <b>No agreement possible.</b><br>Ranges do not overlap.")
            self.result.setStyleSheet("color: #ffadad; font-weight: bold;")
        else:
            # Use strong blue for Player 1 and strong green for Player 2, good for both modes
            p1_color = "#1976d2"  # vivid blue
            p2_color = "#388e3c"  # vivid green
            agreed_color = "#ffd803"  # gold/yellow
            text_color = self.DARK_STYLE['text'] if self.dark_mode else self.LIGHT_STYLE['text']
            self.result.setText(
                f"<b>\U0001F91D Agreed Price:</b> <span style='color:{agreed_color};'>{price:.2f}</span><br>"
                f"<b>\U0001F464 Player 1 Utility:</b> <span style='color:{p1_color};'>{u1:.2f}</span><br>"
                f"<b>\U0001F465 Player 2 Utility:</b> <span style='color:{p2_color};'>{u2:.2f}</span>"
            )
            self.result.setStyleSheet(text_color + " font-weight: bold;")

    def animate_result_card(self):
        self.result_card.setMaximumHeight(0)
        self.anim = QPropertyAnimation(self.result_card, b"maximumHeight")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(120)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.start()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.theme_btn.setText("🌙 Dark Mode" if self.dark_mode else "☀️ Light Mode")
        self.apply_theme()

    def apply_theme(self):
        style = self.DARK_STYLE if self.dark_mode else self.LIGHT_STYLE
        self.setStyleSheet(f"background-color: {style['bg']}")
        self.card.setStyleSheet(style['card'])
        self.result_card.setStyleSheet(style['result'])
        for w in (self.p1_min, self.p1_max, self.p2_min, self.p2_max):
            w.setStyleSheet(style['input'] + " transition: background 0.3s, color 0.3s;")
        self.result.setStyleSheet(style['text'] + " font-weight: bold;")
        self.theme_btn.setStyleSheet(
            ("padding: 6px 18px; border-radius: 10px; font-weight: bold;" +
             ("background: #eebbc3; color: #232946;" if self.dark_mode else "background: #232946; color: #eebbc3;"))
        )

def run_ui():
    app = QApplication(sys.argv)
    window = NashNegotiationUI()
    window.show()
    sys.exit(app.exec_())
