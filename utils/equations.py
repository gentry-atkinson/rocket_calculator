#Author: Gentry Atkinson
#Organization: Texas University
#Data: 21 December, 2020
#simple equations

import numpy as np

G0 = 9.806

def delta_v_from_isp_and_mass(isp, m0, mf):
    return isp * G0 * np.log(m0/mf)
