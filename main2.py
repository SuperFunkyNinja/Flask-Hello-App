from flask import Flask
from flask import request
import pantilthat

app = Flask(__name__)


@app.route("/")
def index():
    pan_value = request.args.get("pan_value", "")
    tilt_value = request.args.get("tilt_value", "")
    if pan_value:
        tilt_value = tilt_value_from(pan_value)
    if tilt_value:
        pan_value = pan_value_from(tilt_value)
    return (
        """<form action="" method="get">
                pan_value: <input type="text" name="pan_value">
                tilt_value: <input type="text" name="tilt_value">
                <input type="submit" value="Activate">
            </form>"""
        + "tilt_value: "
        + tilt_value
        + " "
        + "pan_value: "
        + pan_value
    )


def tilt_value_from(pan_value):
    try:
        pantilthat.pan(int(pan_value))
        return str(pan_value)
    except ValueError:
        return "invalid input"


def pan_value_from(tilt_value):
    """Convert tilt_value to Celius degrees."""
    try:
        pantilthat.tilt(int(tilt_value))
        return str(tilt_value)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="192.168.0.20", port=8080, debug=True)
