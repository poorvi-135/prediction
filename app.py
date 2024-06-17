import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            area=[form.area.data],
            furnishingstatus =[form.furnishingstatus.data],
            mainroad=[form.mainroad.data],
            guestroom=[form.guestroom.data],
            basement=[form.basement.data],
            hotwaterheating=[form.hotwaterheating.data],
            airconditioning=[form.airconditioning.data],
            parking=[form.parking.data],
            total_rooms=[form.total_rooms.data]
        ))
        prediction = model.predict(x_new)[0]
        message = f"The predicted price is {prediction:,.0f} INR!"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)


if __name__ == "__main__":
    app.run(debug=True)