import base64


def encode_data_to_base64(data):
    encoded_data = []
    for item in data:
        encoded_item = base64.b64encode(item.encode("utf-8")).decode("utf-8")
        encoded_data.append(encoded_item)
    return encoded_data
