import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from geopy.geocoders import Nominatim

class GeocoderWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.search_box = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.result_label = QLabel(self)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.search_box)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)

        # Connect the button click event to the geocode function
        self.search_button.clicked.connect(self.geocode)

    def geocode(self):
        # Get the location from the search box
        loc = self.search_box.text()

        # Create a geolocator instance
        geolocator = Nominatim(user_agent="my_request")

        # Apply geocode method to get the location
        location = geolocator.geocode(loc)

        # Check if location is found
        if location:
            # Display address and coordinates
            address = location.address
            coordinates = (location.latitude, location.longitude)
            result_text = f"Address: {address}\nCoordinates: {coordinates}"
        else:
            result_text = "Location not found."

        # Update the result label
        self.result_label.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GeocoderWidget()
    widget.setWindowTitle("Lattitude Longitude Finder")
    widget.setGeometry(100, 100, 400, 200)
    widget.show()
    sys.exit(app.exec_())