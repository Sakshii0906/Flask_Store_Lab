from marshmallow import Schema, fields, validate


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    location = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )