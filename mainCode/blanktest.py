import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create the application object
app = QApplication(sys.argv)

# Create a simple window
window = QWidget()
window.setWindowTitle('PyQt6 Example')

# Add a label to the window
label = QLabel('Hello, PyQt6!', window)
label.move(50, 50)

# Set the window size
window.setGeometry(100, 100, 300, 200)



# Show the window
window.show()

# Run the application's event loop
sys.exit(app.exec())

