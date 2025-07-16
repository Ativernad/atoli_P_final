from PyQt5 import QtWidgets, QtWebEngineWidgets
import sys
from threading import Thread
from app import app  # Імпортуємо Flask-застосунок

def run_flask():
    app.run(debug=False, use_reloader=False)

if __name__ == '__main__':
    # Запускаємо Flask у окремому потоці
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Створюємо PyQt5 додаток
    qt_app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Морепродукти – Замовлення")
    browser = QtWebEngineWidgets.QWebEngineView()
    browser.setUrl("http://127.0.0.1:5000")
    window.setCentralWidget(browser)
    window.resize(800, 600)
    window.show()
    sys.exit(qt_app.exec_())