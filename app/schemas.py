from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.String(required=True,validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=4))

class UserUpdateSchema(Schema):
    name = fields.String(validate=validate.Length(min=1))
    email = fields.Email()
    password = fields.String(validate=validate.Length(min=4))