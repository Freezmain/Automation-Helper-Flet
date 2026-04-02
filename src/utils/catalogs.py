import flet as ft

# Список пристроїв
CATALOG_ELEMENTS = {
    "Light": [
        {"name": "Лампа", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Люстра", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Точка", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Торшер", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Бра", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "LED", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "PWM", "base_count_output": 1, "base_voltage": "24V"},
        {"name": "RGB", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "PWM", "base_count_output": 3, "base_voltage": "24V"},
        {"name": "RGBW", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "PWM", "base_count_output": 4, "base_voltage": "24V"},
        {"name": "Трек", "icon": ft.Icons.LIGHTBULB_ROUNDED, "base_type_output": "DALI", "base_count_output": 1, "base_voltage": "220V"},
    ],
    "Climate": [
        {"name": "Тепла підлога", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Радіатор", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Фанкойл", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Конвектор", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Вентилятор", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "ТЕНа", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Кондиціонер", "icon": ft.Icons.CLOUD_ROUNDED, "base_type_output": "MODBUS", "base_count_output": 1},
    ],
    "Drive": [
        {"name": "Штори", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Жалюзі", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Ворота", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Заслінка", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Кран", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
        {"name": "Триходовий клапан", "icon": ft.Icons.COMPARE_ARROWS_ROUNDED, "base_type_output": "DO", "base_count_output": 2, "base_voltage": "220V"},
    ],
    "Sensor": [
        {"name": "Датчик повітря", "icon": ft.Icons.CIRCLE_NOTIFICATIONS, "base_type_input": "UI", "base_count_input": 1},
        {"name": "Датчик підлоги", "icon": ft.Icons.CIRCLE_NOTIFICATIONS, "base_type_input": "UI", "base_count_input": 1},
        {"name": "Датчик руху", "icon": ft.Icons.CIRCLE_NOTIFICATIONS, "base_type_input": "DI", "base_count_input": 1, "base_voltage": "24V"},
        {"name": "Датчик дверей", "icon": ft.Icons.CIRCLE_NOTIFICATIONS, "base_type_input": "DI", "base_count_input": 1},
        {"name": "Датчик потопу", "icon": ft.Icons.CIRCLE_NOTIFICATIONS, "base_type_input": "DI", "base_count_input": 1},
    ],
    "Key": [
        {"name": "Одноклавішний", "icon": ft.Icons.CHECK_BOX_OUTLINE_BLANK, "base_type_input": "DI", "base_count_input": 1},
        {"name": "Двоклавішний", "icon": ft.Icons.CHECK_BOX_OUTLINE_BLANK, "base_type_input": "DI", "base_count_input": 2},
        {"name": "Чотирьохклавішний", "icon": ft.Icons.CHECK_BOX_OUTLINE_BLANK, "base_type_input": "DI", "base_count_input": 4},
        {"name": "Восьмиклавішний", "icon": ft.Icons.CHECK_BOX_OUTLINE_BLANK, "base_type_input": "DI", "base_count_input": 8},
    ],
    "Other": [
        {"name": "Рушникосушка", "icon": ft.Icons.BOLT_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
        {"name": "Насос", "icon": ft.Icons.BOLT_ROUNDED, "base_type_output": "DO", "base_count_output": 1, "base_voltage": "220V"},
    ]
}

# Список можливих входів/виходів для типу пристрою
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

# Список модулів
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