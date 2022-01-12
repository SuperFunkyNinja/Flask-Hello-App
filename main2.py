from flask import Flask
from flask import request
import pantilthat

app = Flask(__name__)


@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    fahrenheit = request.args.get("fahrenheit", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    if fahrenheit:
        celsius = celsius_from(fahrenheit)
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                Fahrenheit temperature: <input type="text" name="fahrenheit">
                <input type="submit" value="Convert">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
        + " "
        + "Celsius: "
        + celsius
    )


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        pantilthat.pan(int(celsius))
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


def celsius_from(fahrenheit):
    """Convert Fahrenheit to Celius degrees."""
    try:
        pantilthat.tilt(int(fahrenheit))
        celsius = (float(fahrenheit) - 32) * 5 / 9
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="192.168.0.20", port=8080, debug=True)
