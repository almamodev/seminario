from marshmallow import Schema, fields, validate

class SequenceSchema(Schema):
    sequence = fields.String(validate=validate.Length(max=50))