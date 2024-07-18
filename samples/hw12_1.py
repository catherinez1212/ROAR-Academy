import numpy as np

v = np.array([2., 2., 4.])
v_mag = np.sqrt(sum(v**2))
unit_x = np.array([1,0,0])
unit_y = np.array([0,1,0])
unit_z = np.array([0,0,1])

cos_theta_x = np.dot(v, unit_x)/(v_mag*1)
e0 = v_mag*cos_theta_x*unit_x
print(e0)

cos_theta_y = np.dot(v, unit_y)/(v_mag*1)
e1 = v_mag*cos_theta_y*unit_y
print(e1)

cos_theta_z = np.dot(v, unit_z)/(v_mag*1)
e2 = v_mag*cos_theta_z*unit_z
print(e2)