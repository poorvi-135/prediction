import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    BooleanField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

data=pd.read_csv("data_included/housing.csv")
X_data = data.drop(columns=['price'])

class InputForm(FlaskForm):
    area = IntegerField(
        label="Area",
        validators=[DataRequired()]
    )
    furnishingstatus= SelectField(
        label="Furnishingstatus",
        choices=X_data.furnishingstatus.unique().tolist(),
        validators=[DataRequired()]
    )
    mainroad = SelectField(
        label="Mainroad",
        choices=X_data.mainroad.unique().tolist(),
        validators=[DataRequired()]
    )
    airconditioning= SelectField(
        label="Airconditioning",
        choices=X_data.airconditioning.unique().tolist(),
        validators=[DataRequired()]
    )
    parking = SelectField(
        label="Parking",
        choices=X_data.parking.unique().tolist(),
        validators=[DataRequired()]
    )
    basement=SelectField(
        label="Basement",
        choices=X_data.basement.unique().tolist(),
        validators=[DataRequired()]
        
    )
    total_rooms= IntegerField(
        label="Total_rooms",
        validators=[DataRequired()]
    )
    hotwaterheating =SelectField(
        label="hot-water-heating",
        choices=X_data.hotwaterheating.unique().tolist(),
        validators=[DataRequired()]
      
    )
    guestroom = SelectField(
        label="Guestroom",
        choices=X_data.guestroom.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")