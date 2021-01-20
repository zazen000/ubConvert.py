# -*- coding: utf-8 -*-
# Created on Thu May 10 16:04:56 2019
  
# @author: David W Robinson Jr
from datetime import datetime, timedelta, date
import time

def main():
    '''
    Unit Conversions - Basic unit conversions for the following modes:

        - Temperature
        - Speed
        - Weight
        - Volume
        - Distance

    Each function can be called in two ways. For example,
    to convert Kelvin to Fahrenheit:

        Kelvin = 278.967
        k2f(Kelvin) = 42.74059999999997, a float

    The second way is with an integer representing the rounding factor, where:
        - 0 = integer, 1 = one decimal place, 2 = two decimal places, etc., ie:

        k2f(Kelvin, 2) = 42.74, or
        k2f(Kelvin, 0) = 43

    The exception is for converting Light-Years to kilometers or miles.
    First instance returns an integer:

        lt_years = 2
        ly2mi(lt_years) = 11758000000000

    The second instance returns number with requested decimal places in
    scientific notation:

        ly2mi(lt_years, 4) = 1.1758e+13

    The third instance returns the number in comma separated format
    (second arg = 0, third arg = 1):

        ly2mi(ly, 0, 1) = 11,758,000,000,000


    Functions include:

    - Temperature                          - Weight

        Kelvin to Fahrenheit - k2f()           Grams to Ounces       - gr2oz()
        Kelvin to Celsius    - k2c()           Ounces to Grams       - oz2gr()
        Fahrenheit to Kelvin - f2k()           Kilograms to Pounds   - kg2lbs()
        Fahrenheit to Celsius- f2c()           Pounds to Kilograms   - lbs2kg()
        Celsius to Fahrenheit- c2f()           Kilograms to Tons     - kg2ton()
        Celsius to Kelvin    - c2k()           Tons to Kilograms     - ton2kg()
        Rankine to Fahrenheit- r2f()           Tons to Metric Tonnes - ton2mt()
        Fahrenheit to Rankine- f2r()           Metric Tonnes to tons - mt2ton()

    - Speed                                - Volume
                                            
        MPH to KPH           - mph2kph()       Liters to Gallons     - l2gal()
        KPH to MPH           - kph2mph()       Gallons to Liters     - gal2l()
        MPH to Meters/Second - mph2mps()       Ounces to Milliliters - oz2ml()
        Meters/Second to MPH - mps2mph()       Milliliters to Ounces - ml2oz()
        Meters/Second to KPH - mps2kph()       Cubic Centimeters to Cubic Inches - cc2ci()
        KPH to Meters/Second - kph2mps()       Cubic Inches to Cubic Centimeters - ci2cc()
                                            
    - Distance                             - Time   
                                            
        Miles to Kilometers       - mi2km()    Timestamp to Time     - ts2tm()
        Kilometers to Miles       - km2mi()    Timestamp to Date     - ts2d8()
        Light Years to Kilometers - ly2km()    
        Kilometers to Light Years - km2ly()    
        Light Years to Miles      - ly2mi()
        Miles to Light Years      - mi2ly()
        Yards to Meters           - yd2m()
        Meters to Yards           - m2yd()
        Inches to Centimeters     - in2cm()
        Centimeters to Inches     - cm2in()
    '''

# ---Temperature Conversions---------------------------

# Kelvin to Fahrenheit
def k2f(K, num=False):
    if not num:
        return ((9 * (K - 273)) / 5 + 32)
    else:
        return round(((9 * (K - 273)) / 5 + 32), num)



# Kelvin to Celsius
def k2c(K, num=False):
    if not num:
        return (K - 273.15)
    else:
        return round((K - 273.15), num)



# Fahrenheit to Kelvin
def f2k(F, num=False):
    if not num:
        return (F + 459.67) * (9 / 5)
    else:
        return round(((F + 459.67) * (9 / 5)), num)



# Celsius to Fahrenheit
def c2f(C, num=False):
    if not num:
        return (C * (9 / 5) + 32)
    else:
        return round((C * (9 / 5) + 32), num)



# Celsius to Kelvin
def c2k(C, num=False):
    if not num:
        return (C + 273.15)
    else:
        return round((C + 273.15), num)



# Fahrenheit to Celsius
def f2c(F, num=False):
    if not num:
        return ((F - 32) / (9 / 5))
    else:
        return round(((F - 32) / (9 / 5)), num)


# Fahrenheit to Rankine
def f2r(F, num=False):
    if not num:
        return (F + 459.670000001)
    else:
        return round((F + 459.670000001), num)



# Rankine to Fahrenheit
def r2f(R, num=False):
    if not num:
        return (R - 459.670000001)
    else:
        return round((R - 459.670000001), num)



# ---Speed Conversions---------------------------------


# Miles/Hour to Kilometers/Hour
def mph2kph(mph, num=False):
    if not num:
        return (mph * 1.60934)
    else:
        return round((mph * 1.60934), num)



# Kilometers/Hour to Miles/Hour
def kph2mph(kph, num=False):
    if not num:
        return (kph * 0.621371)
    else:
        return round((kph * 0.621371), num)



# Meters/Second to Miles/Hour
def mps2mph(mps, num=False):
    if not num:
        return (mps * 2.23694)
    else:
        return round((mps * 2.23694), num)



# Miles/Hour to Meters/Second
def mph2mps(mph, num=False):
    if not num:
        return (mph * 0.044704)
    else:
        return round((mph * 0.044704), num)



# Meters/Second to Kilometers/Hour
def mps2kph(mps, num=False):
    if not num:
        return (mps * 3.6)
    else:
        return round((mps * 3.6), num)



# Kilometers/Hour to Meters/Second
def kph2mps(kph, num=False):
    if not num:
        return (kph * 0.2777777778)
    else:
        return round((kph * 0.2777777778), num)



# ---Weight Conversions-------------------------------------


# Grams to Ounces
def gr2oz(gr, num=False):
    if not num:
        return (gr * 0.035274)
    else:
        return round((gr * 0.035274), num)



# Ounces to Grams
def oz2gr(oz, num=False):
    if not num:
        return (oz * 28.349)
    else:
        return round((oz * 28.349), num)



# Kilograms to Pounds
def kg2lbs(kg, num=False):
    if not num:
        return (kg * 2.2046)
    else:
        return round((kg * 2.2046), num)


# Pounds to Kilograms
def lbs2kg(lbs, num=False):
    if not num:
        return (lbs *  0.454)
    else:
        return round((lbs *  0.454), num)



# Kilograms to Tons
def kg2ton(kg, num=False):
    if not num:
        return (kg * 0.0011)
    else:
        return round((kg * 0.0011), num)



# Tons to Kilograms
def ton2kg(ton, num=False):
    if not num:
        return (ton * 907.18)
    else:
        return round((ton * 907.18), num)



# Tons to Metric Tonnes
def ton2mt(ton, num=False):
    if not num:
        return (ton * 0.907185)
    else:
        return round((ton * 0.907185), num)



# Metric Tonnes to Tons
def mt2ton(mt, num=False):
    if not num:
        return (mt * 1.102311)
    else:
        return round((mt * 1.102311), num)



# ---Volume Conversions-----------------------------------------


# Liters to Gallons
def l2gal(li, num=False):
    if not num:
        return (li * 0.264)
    else:
        return round((li * 0.264), num)



# Gallons to Liters
def gal2l(gal, num=False):
    if not num:
        return (gal * 3.785)
    else:
        return round((gal * 3.785), num)



# Ounces to Milliliters
def oz2ml(oz, num=False):
    if not num:
        return (oz * 29.57)
    else:
        return round((oz * 29.57), num)


# Milliliters to Ounces
def ml2oz(ml, num=False):
    if not num:
        return (ml * 0.0338)
    else:
        return round((ml * 0.0338), num)


# Cubic Centimeters to Cubic Inches
def cc2ci(cc, num=False):
    if not num:
        return (cc * 0.0610237)
    else:
        return round((cc * 0.0610237), num)



# Cubic Inches to Cubic Centimeters
def ci2cc(ci, num=False):
    if not num:
        return (ci * 16.387064)
    else:
        return round((ci * 16.387064), num)



# ---Distance Conversions-------------------------------------------


# Miles to Kilometers
def mi2km(mi, num=False):
    if not num:
        return (mi * 1.609344)
    else:
        return round((mi * 1.609344), num)



# Kilometers to Miles
def km2mi(km, num=False):
    if not num:
        return (int(km) * 0.6214)
    else:
        return round((km * 0.6214), num)



# Light-Years to Kilometers
def ly2km(ly, num=False, comma=0):
    a = 0
    if comma != 0:
        return "{:,}".format(int(ly * 9.461e12))
    elif num and not comma:
        return format(round((ly * 9.461e12), num), ('10.' + str(num) + 'e'))
    elif not num:
        return int(ly * 9.461e12)



# Light-Years to Miles
def ly2mi(ly, num=False, comma=0):
    if comma != 0:
        return "{:,}".format(int(ly * 5.879e12))
    elif not num:
        return int(ly * 5.879e12)
    elif num and not comma:
        return format(round((ly * 5.879e12), num), ('10.' + str(num) + 'e'))



# Miles to Light-Years
def mi2ly(mi):
    return format((mi * 1.70108e-13), '10.5e')


# Kilometers to Light-Years
def km2ly(km):
    return (km * 1.057e-13)



# Meters to Yards
def m2yd(m, num=False):
    if not num:
        return (m * 1.0936133)
    else:
        return round((m * 1.0936133), num)



# Yards to Meters
def yd2m(yd, num=False):
    if not num:
        return (yd * 0.9144)
    else:
        return round((yd * 0.9144), num)



# Inches to Centimeters
def in2cm(inch, num=False):
    if not num:
        return (inch * 2.54)
    else:
        return round((inch * 2.54), num)



# Centimeters to Inches
def cm2in(cm, num=False):
    if not num:
        return (cm * 0.393701)
    else:
        return round((cm * 0.393701), num)


# Astronomical Unit to Miles
def au2mi(au): return round(au * 92955807.26743), 2


# Miles to Astronomical Unit
def mi2au(mi, num=False):
    if not num:
        return mi / 92955807.26743
    else:
        return round(mi / 92955807.26743), 2

# ---Time Conversions


# Tinestamp to Date
def ts2d8(ts=0):
    return datetime.fromtimestamp(ts)


#print(ts2d8(1579543604))
# Date to Timestamp:  - Required setup: d = (2019, 5, 21)
def d82ts(y, m, d, *args, **kwargs):
    return timedelta.total_seconds(datetime(y, m, d, *args, **kwargs) - datetime(1970, 1, 1))



if __name__ == '__main__':
    main()

