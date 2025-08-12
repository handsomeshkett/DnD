from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QMessageBox, QFrame, QSizePolicy
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DnD Master Menu")
        self.setGeometry(100, 100, 500, 350)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Боковое меню
        self.menu_layout = QVBoxLayout()
        self.menu_layout.setContentsMargins(20, 20, 10, 20)
        self.menu_layout.setSpacing(15)
        menu_frame = QFrame()
        menu_frame.setLayout(self.menu_layout)
        menu_frame.setFrameShape(QFrame.StyledPanel)
        menu_frame.setStyleSheet("background: #f3f4f6; border-radius: 16px;")
        menu_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # Контентная область
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(30, 30, 30, 30)
        self.content_layout.setSpacing(20)
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.content_layout)
        self.content_widget.setStyleSheet("background: #fff; border-radius: 16px;")

        main_layout.addWidget(menu_frame)
        main_layout.addWidget(self.content_widget)

        self.init_menu()
        self.show_welcome()

    def init_menu(self):
        # Заголовок меню
        label = QLabel("Меню мастера DnD")
        label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; margin-bottom: 10px;")
        self.menu_layout.addWidget(label)

        # Стили для кнопок
        button_style = """
            QPushButton {
                background-color: #e0e7ff;
                color: #222;
                border-radius: 12px;
                border: 1px solid #b6b6b6;
                padding: 8px 0;
                font-size: 16px;
                min-height: 40px;
                margin-bottom: 8px;
            }
            QPushButton:hover {
                background-color: #a5b4fc;
                color: #111;
                border: 2px solid #6366f1;
            }
        """

        # Кнопки меню
        btn_item = QPushButton("🧰  Сгенерировать предмет")
        btn_item.setStyleSheet(button_style)
        btn_item.clicked.connect(self.show_item_tab)
        self.menu_layout.addWidget(btn_item)

        self.menu_layout.addWidget(self.make_separator())

        btn_quest = QPushButton("🗺️  Сгенерировать квест")
        btn_quest.setStyleSheet(button_style)
        btn_quest.clicked.connect(self.generate_quest)
        self.menu_layout.addWidget(btn_quest)

        self.menu_layout.addWidget(self.make_separator())

        btn_msg = QPushButton("💬  Отправить сообщение")
        btn_msg.setStyleSheet(button_style)
        btn_msg.clicked.connect(self.send_message)
        self.menu_layout.addWidget(btn_msg)

        self.menu_layout.addWidget(self.make_separator())

        btn_history = QPushButton("📜  История игровых событий")
        btn_history.setStyleSheet(button_style)
        btn_history.clicked.connect(self.show_history)
        self.menu_layout.addWidget(btn_history)

    def make_separator(self):
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)
        sep.setStyleSheet("margin: 4px 0; background: #d1d5db; height: 2px;")
        return sep

    def show_welcome(self):
        self.clear_layout(self.content_layout)
        label = QLabel("Добро пожаловать в мастер-меню DnD!")
        label.setStyleSheet("font-size: 22px; color: #222; margin-top: 30px;")
        self.content_layout.addWidget(label)

    def show_item_tab(self):
        self.clear_layout(self.content_layout)
        label = QLabel("ТЕСТ: Здесь будет генерация предмета")
        label.setStyleSheet("font-size: 20px; margin-top: 40px; color: #222;")
        self.content_layout.addWidget(label)
        btn_back = QPushButton("Назад в меню")
        btn_back.setStyleSheet("background-color: #f3f4f6; color: #222; border-radius: 10px; min-height: 30px; margin-top: 20px;")
        btn_back.clicked.connect(self.show_welcome)
        self.content_layout.addWidget(btn_back)

    # show_menu_tab больше не нужен, welcome теперь стартовый экран

    def generate_quest(self):
        self.clear_layout(self.content_layout)
        label = QLabel("Генерация квеста пока не реализована.")
        label.setStyleSheet("font-size: 18px; color: #222; margin-top: 30px;")
        self.content_layout.addWidget(label)
        btn_back = QPushButton("Назад в меню")
        btn_back.setStyleSheet("background-color: #f3f4f6; color: #222; border-radius: 10px; min-height: 30px; margin-top: 20px;")
        btn_back.clicked.connect(self.show_welcome)
        self.content_layout.addWidget(btn_back)

    def send_message(self):
        self.clear_layout(self.content_layout)
        label = QLabel("Функция отправки сообщения пока не реализована.")
        label.setStyleSheet("font-size: 18px; color: #222; margin-top: 30px;")
        self.content_layout.addWidget(label)
        btn_back = QPushButton("Назад в меню")
        btn_back.setStyleSheet("background-color: #f3f4f6; color: #222; border-radius: 10px; min-height: 30px; margin-top: 20px;")
        btn_back.clicked.connect(self.show_welcome)
        self.content_layout.addWidget(btn_back)

    def show_history(self):
        self.clear_layout(self.content_layout)
        label = QLabel("Функция истории пока не реализована.")
        label.setStyleSheet("font-size: 18px; color: #222; margin-top: 30px;")
        self.content_layout.addWidget(label)
        btn_back = QPushButton("Назад в меню")
        btn_back.setStyleSheet("background-color: #f3f4f6; color: #222; border-radius: 10px; min-height: 30px; margin-top: 20px;")
        btn_back.clicked.connect(self.show_welcome)
        self.content_layout.addWidget(btn_back)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
