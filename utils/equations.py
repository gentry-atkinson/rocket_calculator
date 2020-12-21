#Author: Gentry Atkinson
#Organization: Texas University
#Data: 21 December, 2020
#simple equations

import numpy as np

G0 = 9.806      #g, the og little g
P0 = 1013.25    #mean sea level air pressure

def delta_v_from_isp_and_mass(isp, m0, mf):
    return isp * G0 * np.log(m0/mf)

def isp_from_exhaust_vel(ve):
    return ve/G0

def drag_from_b_and_vel(b, vel):
    return b * v * v

def b_from_dc_density_and_area(dc, ro, area):
    return 0.5 * dc * ro * area

def ro_from_pres_temp_and_humidity(pres, temp, hum):
    #temp should be in degrees celsius
    #pres is in hPa
    #hum is the dew point in degrees celsium
    p1 = 6.1078 * 10^(7.5*temp /(temp + 237.3))
    #pv is water vapor pressure in Pascal
    pv = p1 * hum
    #pd is pressure of dry air in Pascal
    pd = pres - pv
    #rd is the specific gas constant for dry air
    rd = 287.058
    #rv is the specific gas costant for water vapor
    rv = 461.495
    #ρ = (pd / (Rd * T)) + (pv / (Rv * T))
    return (pd / (rd * temp)) + (pv / (rv * temp))

def pres_from_altitude(temp, alt):
    #alt is height above sea level
    M = 0.0289644 #molar mass of air
    R = 8.31432 #universal gas constant
    return P0 * np.exp((-1*G0*M*alt)/(R*temp))
