from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True, validate=[validate.Length(min=3)], error_messages={
        "required": "The name is required",
        "length": "The min length is 3",
        "invalid": "The name needs to be a string"
    })
    email = String(required=True, validate=[validate.Email()])
    
    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")
        
        if User.query.filter_by(email=email).count():
            raise ValidationError("Email already exists")
    
    class Meta:
        model = User
        load_instance = True
        exclude = ["id"]