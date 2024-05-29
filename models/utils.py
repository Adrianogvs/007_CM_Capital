# models/utils.py
def convert_value(value):
    if value.endswith('C'):
        return float(value[:-1].replace('.', '').replace(',', '.'))
    elif value.endswith('D'):
        return -float(value[:-1].replace('.', '').replace(',', '.'))
    else:
        return float(value.replace('.', '').replace(',', '.'))
