from marshmallow import Schema, fields

class ItemSchema(Schema):
    description = fields.Str()
    quantity = fields.Int()
    amount = fields.Int()
    additional_data = fields.Str(dump_to="additionalData")
    expire = fields.Int()

class TransactionCreateRequestSchema(Schema):
    external_unique_number = fields.Str(dump_to="externalUniqueNumber")
    total = fields.Int()
    items_quantity = fields.Int(dump_to = "itemsQuantity")
    issued_at = fields.Integer(dump_to = "issuedAt")
    items = fields.Nested(ItemSchema, many = True)
    callback_url = fields.Str(dump_to = "callbackUrl")
    channel = fields.Str()
    app_scheme = fields.Str(dump_to = "appScheme")
    app_key = fields.Str(dump_to = "appKey")
    api_key = fields.Str(dump_to = "apiKey")
    generate_ott_qr_code = fields.Bool(dump_to = "generateOttQrCode")
    signature = fields.Str()

class TransactionCreateResponseSchema(Schema):
    occ = fields.Str()
    ott = fields.Int()
    signature = fields.Str()
    external_unique_number = fields.Str(load_from="externalUniqueNumber")
    issued_at = fields.Int(load_from="issuedAt")
    qr_code_as_base64 = fields.Str(load_from="qrCodeAsBase64")

class SendTransactionResponseSchema(Schema):
    response_code = fields.Str(load_from="responseCode")
    description = fields.Str()
    result = fields.Nested(TransactionCreateResponseSchema)