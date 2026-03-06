CATALOG_ELEMENTS = {
    "Light": [
        {"name": "Лампа", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Люстра", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Точка", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Торшер", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Бра", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "LED", "base_type_output": "PWM", "base_count_output": 1, "base_voltage": "24V"},
        {"name": "RGB", "base_type_output": "PWM", "base_count_output": 3, "base_voltage": "24V"},
        {"name": "RGBW", "base_type_output": "PWM", "base_count_output": 4, "base_voltage": "24V"},
        {"name": "Трек", "base_type_output": "DALI", "base_count_output": 1, "base_voltage": "220V"},
    ],
    "Climate": [
        {"name": "Тепла підлога", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Радіатор", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Фанкойл", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Конвектор", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Вентилятор", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "ТЕНа", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Кондиціонер", "base_type_output": "MODBUS", "base_count_output": 1},
    ],
    "Drive": [
        {"name": "Штори", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Жалюзі", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Ворота", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Заслінка", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Кран", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Триходовий клапан", "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
    ],
    "Sensor": [
        {"name": "Датчик повітря", "base_type_input": "UI", "base_count_input": 1},
        {"name": "Датчик підлоги", "base_type_input": "UI", "base_count_input": 1},
        {"name": "Датчик руху", "base_type_input": "DI", "base_count_input": 1, "base_voltage": "24V"},
        {"name": "Датчик дверей", "base_type_input": "DI", "base_count_input": 1},
        {"name": "Датчик потопу", "base_type_input": "DI", "base_count_input": 1},
    ],
    "Key": [
        {"name": "Одноклавішний", "base_type_input": "DI", "base_count_input": 1},
        {"name": "Двоклавішний", "base_type_input": "DI", "base_count_input": 2},
        {"name": "Чотирьохклавішний", "base_type_input": "DI", "base_count_input": 4},
        {"name": "Восьмиклавішний", "base_type_input": "DI", "base_count_input": 8},
    ],
    "Other": [
        {"name": "Рушникосушка", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Насос", "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
    ]
}

CATALOG_TYPES = {
    "Light": [
        {"name": "DO"},
        {"name": "DIM"},
        {"name": "PWM"},
        {"name": "DALI"},
    ],
    "Climate": [
        {"name": "DO"},
        {"name": "MODBUS"},
    ],
    "Drive": [
        {"name": "DO"},
    ],
    "Sensor": [
        {"name": "DI"},
        {"name": "UI"},
    ],
    "Key": [
        {"name": "DI"},
    ],
    "Other": [
        {"name": "DI"},
        {"name": "UI"},
        {"name": "DO"},
        {"name": "DIM"},
        {"name": "PWM"},
        {"name": "DALI"},
        {"name": "MODBUS"},
    ],
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