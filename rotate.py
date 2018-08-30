from math import sin, cos, radians
import numpy as np

def rotate_point(point, angle, center_point=(0, 0)):
    """Rotates a point around center_point(origin by default)
    Angle is in degrees.
    Rotation is counter-clockwise
    """
    angle_rad = radians(angle % 360)
    # Shift the point so that center_point becomes the origin
    new_point = (point[0] - center_point[0], point[1] - center_point[1])
    new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
                 new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
    # Reverse the shifting we have done
    new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
    return new_point


print(rotate_point((1, 1), 90, (2, 1)))
# This prints (2.0, 0.0)
print(rotate_point((1, 1), -90, (2, 1)))
# This prints (2.0, 2.0)
print(rotate_point((2, 2), 45, (1, 1)))
# This prints (1.0, 2.4142) which is equal to (1,1+sqrt(2))

def rotate_polygon(polygon, angle, center_point=(0, 0)):
    """Rotates the given polygon which consists of corners represented as (x,y)
    around center_point (origin by default)
    Rotation is counter-clockwise
    Angle is in degrees
    """
    rotated_polygon = []
    for i in range(len(polygon)):
        rotated_corner = rotate_point(polygon[i], angle, center_point)
        rotated_polygon.append(rotated_corner)
    return np.array(rotated_polygon)






