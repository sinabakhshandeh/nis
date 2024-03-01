from ninja import Schema


class ErrorSchema(Schema):
    message: str


class EmptySchema(Schema):
    pass
