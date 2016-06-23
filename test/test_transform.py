#!/usr/bin/env python
import cosinv.transform
import numpy as np

p = np.array([0.0,0.0,0.0])

T  = cosinv.transform.point_translation([1.0,0.0,0.0])
T *= cosinv.transform.point_rotation_y(np.pi/2.0)
print(T(p))
