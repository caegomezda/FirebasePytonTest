import random


class Circuit:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.components = []
        self.status_maintenance = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_component(self, component):
        self.components.append(component)


def circuit_generator(number_of_circuits, circuit_type):
    circuits = []

    for i in range(1, number_of_circuits + 1):
        circuit_name = f"{circuit_type} Circuit {i}"
        circuit = Circuit(circuit_name)

        if circuit_type == 'TypeA':
            num_sensors = 6  # Specify the number of sensors for Type A circuits
            num_components = 6  # Specify the number of components for Type A circuits

            for j in range(1, num_sensors + 1):
                sensor_name = f"Sensor{j}"
                sensor_status = get_random_sensor_status()
                voltage = get_random_number(4, 5)
                maintenance = get_random_maintenance_status()

                circuit.add_sensor({"name": sensor_name, "status": sensor_status, "voltage": voltage, "maintenance": maintenance})

            for j in range(1, num_components + 1):
                component_name = f"Component{j}"
                component_status = get_random_component_status()
                maintenance = get_random_maintenance_status()

                circuit.add_component({"name": component_name, "status": component_status, "maintenance": maintenance})
        elif circuit_type == 'TypeB':
            # Add specific sensors and components for Type B circuit
            pass
        else:
            # Add default sensors and components for other circuit types
            pass

        circuits.append(circuit)

    return circuits


def get_random_maintenance_status():
    random_number = random.random()

    if random_number < 0.2:
        # 20% chance: return maintenance status between 20 and 30 days
        return get_random_number(20, 30)
    elif random_number < 0.6:
        # 40% chance: return maintenance status between 10 and 19 days
        return get_random_number(10, 19)
    elif random_number < 0.8:
        # 20% chance: return maintenance status between 1 and 9 days
        return get_random_number(1, 9)
    else:
        # 20% chance: return maintenance status of 0 days
        return 0


def get_random_sensor_status():
    random_number = random.random()

    if random_number < 0.01:
        # 5% chance: return "off" status
        return "off"
    else:
        # 95% chance: return "on" status
        return "on"


def get_random_component_status():
    random_number = random.random()

    if random_number < 0.03:
        # 3% chance: return "off" status
        return "off"
    else:
        # 97% chance: return "on" status
        return "on"


def get_random_number(minimum, maximum):
    return random.randint(minimum, maximum)


if __name__ == "__main__":
    circuits = circuit_generator(30, "TypeA")
    for circuit in circuits:
        print(circuit.name)
        print(circuit.sensors)
        print(circuit.components)
        print()
