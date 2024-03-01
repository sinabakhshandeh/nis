from ninja import Schema


class ErrorSchema(Schema):
    message: str


class SampleSchema(Schema):
    name: str
