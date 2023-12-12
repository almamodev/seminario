from marshmallow import Schema, fields

class StatsSchema(Schema):
    length = fields.Integer()
    base_counts = fields.Dict(keys=fields.String(), values=fields.Integer())
    gc_content = fields.Float()
    tm = fields.Float()
    