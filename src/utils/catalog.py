CATALOG_ELEMENTS = {
    "Light": [
        
    ],
}

CATALOG_TYPES = {
    "Light": [
        {"name": "DO"},
        {"name": "DALI"},
        {"name": "DIM"},
        {"name": "PWM"},
    ],
    "Key": [
        {"name": "DI"},
    ],
    "Sensor": [
        {"name": "DI"},
        {"name": "UI"},
    ],
    "Engineering": [
        {"name": "DO"},
        {"name": "MODBUS"},
    ]
}

CATALOG_MODULES = {
    "8DI8DO": {"type_input": "DI", "type_output": "DO", "count_inputs": 8, "count_outputs": 8},
    "8UI8DO": {"type_input": "UI", "type_output": "DO", "count_inputs": 8, "count_outputs": 8},
    "4DI4DIM": {"type_input": "DI", "type_output": "DIM", "count_inputs": 4, "count_outputs": 4},
    "4DI4PWM": {"type_input": "DI", "type_output": "PWM", "count_inputs": 4, "count_outputs": 4},
    "8DI": {"type_input": "DI", "count_inputs": 8},
    "8UI": {"type_input": "UI", "count_inputs": 8},
    "6DI_DALI": {"type_input": "DI", "type_interface": "DALI", "count_inputs": 6},
    "MODBUS": {"type_interface": "MODBUS"},
    "3P_METER": {"type_input": "Voltage", "type_output": "Voltage", "count_inputs": 3, "count_outputs": 3},
}