import math
""" distance_to_home = 384400
gravity = 9.8

thrust = math.sqrt(distance_to_home*gravity)
print(f'Thrust needed {thrust}') """

base_length = 15
height = 20
angle_redius = math.atan(height/base_length)
print(f'The angle in redius is {angle_redius}')
angle_degree = math.degrees(angle_redius)
print(f'the angle in degree is {angle_degree}')