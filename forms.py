from flask_wtf import FlaskForm
from wtforms import(
    TextAreaField,
   
SubmitField,

)
from wtforms.validators import (
    DataRequired,
    Length,
    
)

class Smschecker(FlaskForm):
    sms_check = TextAreaField(
        "Sms_check_Box",
        validators=[DataRequired(), Length(2, 400)],
         render_kw={"class": "custom-textarea"}
    )
   
    submit = SubmitField("Predict", render_kw={"class" : "predict-button"})



    