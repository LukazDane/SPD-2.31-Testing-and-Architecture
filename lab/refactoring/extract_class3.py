# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(time, temperature,
                                    pressure, desired_state):
    result = time * temperature * pressure * COOKED_CONSTANT
    well = result >= WELL_DONE
    medium = result >= MEDIUM
    return (well and desired_state == 'well-done') or (medium and desired_state == "medium")


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'

if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
    print('cooking is done.')
else:
    print('ongoing cooking.')
