# -*- coding: utf-8 -*-
# Created on Thu May 10 16:04:56 2020

from datetime import datetime, timedelta, date
import time

def main():
    """
    ubConvert conversion module
    Utility_Belt Designs, Tacoma, WA
    @author: ZennDogg

    ubConvert Unit Conversion Classes -

    - Temperatures()
    - Speed_Distance()
    - Weights()
    - Volumes()
    - Times()

    The functions for most classes can be called in two ways.
    First example, to convert Kelvin to Fahrenheit from class Temperatures():

        kelvin = 278.967
        kelvin_to_fahrenheit(kelvin) = 42.74059999999997

    The second way is with a number representing the rounding factor, where:
        - 0 = integer, 1 = one decimal place, 2 = two decimal places, etc.,

        kelvin = 278.967
        kelvin_to_fahrenheit(kelvin, 2) = 42.74, or,
        kelvin_to_fahrenheit(kelvin, 0) = 43

    For converting and formatting Light-Years and Astronomical Units to kilometers
    or miles, things are a little different. The first way returns an integer:

        lt_years = 2
        light_years_to_miles(lt_years) = 11758000000000

    The second instance returns a number with requested decimal places in
    scientific notation:

        lt_years = 2
        light_years_to_miles(lt_years, 4) = 1.1758e+13

    Because the answers are such large integers, the third way returns the number
    in comma separated format for easier reading (second arg = 0, third arg = 1):

        lt_years = 2
        light_years_to_miles(lt_years, 0, 1) = 11,758,000,000,000

    ..................................................................
    Example:

        import ubConvert as ub

        weights = ub.Weights()
        oz = weights.grams_to_ounces(28)
        oz = 1

    ..................................................................

    Functions include: note: use all lower case when calling functions, right?

    - Temperatures() function list            - Weights() function list

        Kelvin_to_Fahrenheit                      Grams_to_Ounces
        Kelvin_to_Celsius                         Ounces_to_Grams
        Fahrenheit_to_Kelvin                      Kilograms_to_Pounds
        Fahrenheit_to_Celsius                     Pounds_to_Kilograms
        Celsius_to_Fahrenheit                     Kilograms_to_Tons
        Celsius_to_Kelvin                         Tons_to_Kilograms
        Rankine_to_Fahrenheit                     Tons_to_Metric_Tonnes
        Fahrenheit_to_Rankine                     Metric_Tonnes_to_Tons

    - Speed_Distance() function list          - Volumes() function list
                                            
        MPH_to_KPH                                 Liters_to_Gallons
        KPH_to_MPH                                 Gallons_to_Liters
        MPH_to_Meters_per_Second                   Ounces_to_Milliliters
        Meters_per_Second_to_MPH                   Milliliters_to_Ounces
        Meters_per_Second_to_KPH                   Cubic_Centimeter_to_Cubic_Inch
        KPH_to_Meters_per_Second                   Cubic_Inch_to_Cubic_Centimeter
        Miles_to_Kilometers
        Kilometers_to_Miles                    - Times() function list
        Light_Years_to_Kilometers
        Kilometers_to_Light_Years                  Date_to_Timestamp
        Light_Years_to_Miles                       Timestamp_to_Date
        Miles_to_Light_Years
        Yards_to_Meters
        Meters_to_Yards
        Inch_to_Centimeter
        Centimeter_to_Inch
        Astronomical_Unit_to_Miles
        Miles_to_Astronomical_Unit
        Astronomical_Unit_to_Kilometers
        Kilometers_to_Astronomical_Unit
    """
    pass



class Temperatures(object):
    """
    Formulas for Temperature Conversions
    """

    def kelvin_to_fahrenheit(kelvin=0, num=False):
        if not num:
            return ((9 * (kelvin - 273)) / 5 + 32)
        else:
            return round(((9 * (kelvin - 273)) / 5 + 32), num)


    def kelvin_to_celsius(kelvin=0, num=False):
        if not num:
            return (kelvin - 273.15)
        else:
            return round((kelvin - 273.15), num)


    def fahrenheit_to_kelvin(fahrenheit=0, num=False):
        if not num:
            return (fahrenheit + 459.67) * (9 / 5)
        else:
            return round(((fahrenheit + 459.67) * (9 / 5)), num)


    def celsius_to_fahrenheit(celsius=0, num=False):
        if not num:
            return (celsius * (9 / 5) + 32)
        else:
            return round((celsius * (9 / 5) + 32), num)


    def celsius_to_kelvin(celsius=0, num=False):
        if not num:
            return (celsius + 273.15)
        else:
            return round((celsius + 273.15), num)


    def fahrenheit_to_celsius(fahrenheit=0, num=False):
        if not num:
            return ((fahrenheit - 32) / (9 / 5))
        else:
            return round(((fahrenheit - 32) / (9 / 5)), num)


    def fahrenheit_to_rankine(fahrenheit=0, num=False):
        if not num:
            return (fahrenheit + 459.670000001)
        else:
            return round((fahrenheit + 459.670000001), num)


    def rankine_to_fahrenheit(rankine=0, num=False):
        if not num:
            return (rankine - 459.670000001)
        else:
            return round((rankine - 459.670000001), num)



class Speed_Distance(object):
    """
    Formulas for Speed and Distance Conversions
    """

    def mph_to_kph(var=0, num=False):
        if not num:
            return (float(var) * 1.60934)
        else:
            return round((float(var) * 1.60934), num)


    def kph_to_mph(kph=0, num=False):
        if not num:
            return (float(kph) * 0.621371)
        else:
            return round((float(kph) * 0.621371), num)


    def meters_per_second_to_mph(mps=0, num=False):
        if not num:
            return (mps * 2.23694)
        else:
            return round((mps * 2.23694), num)


    def mph_to_meters_per_second(mph=0, num=False):
        if not num:
            return (mph * 0.044704)
        else:
            return round((mph * 0.044704), num)


    def meters_per_second_to_kph(meters_per_second=0, num=False):
        if not num:
            return (meters_per_second * 3.6)
        else:
            return round((meters_per_second * 3.6), num)


    def kph_to_meters_per_second(kph=0, num=False):
        if not num:
            return (kph * 0.2777777778)
        else:
            return round((kph * 0.2777777778), num)


    def miles_to_kilometers(miles=0, num=False):
        if not num:
            return mph_to_kph(miles)
        else:
            return round( mph_to_kph(miles), num )


    def kilometers_to_miles(kilometers=0, num=False):
        if not num:
            return kph_to_mph(kilometers)
        else:
            return round(kph_to_mph(kilometers), num )


    def astronomical_unit_to_miles(astronomical_unit=0, num=False, comma=0):
        if comma == 1:
            return "{:,}".format( int(astronomical_unit ) * 92955807.26743 )
        elif num and not comma:
            return format(round(astronomical_unit * 92955807.26743), num), ('10.' + str(num) + 'e')
        elif not num:
            return int(astronomical_unit * 92955807.26743)


    def astronomical_unit_to_kilometers(astronomical_unit=0, num=False, comma=0):
        if comma == 1:
            return "{:,}".format( int(astronomical_unit ) * 149597870.7 )
        elif num and not comma:
            return format(round(astronomical_unit * 149597870.7), num), ('10.' + str(num) + 'e')
        elif not num:
            return int(astronomical_unit * 149597870.7)


    def miles_to_astronomical_unit(miles=0, num=False):
        if not num:
            return miles / 92955807.26743
        else:
            return round( miles / 92955807.26743 ), num


    def kilometers_to_astronomical_unit(kilometers=0, num=False):
        if not num:
            return kilometers / 149597870.7
        else:
            return round( kilometers / 149597870.7), num


    def light_years_to_kilometers(light_years=0, num=False, comma=0):
        if comma == 1:
            return "{:,}".format(int(light_years * 9.461e12))
        elif num and not comma:
            return format(round((light_years * 9.461e12), num), ('10.' + str(num) + 'e'))
        elif not num:
            return int(light_years * 9.461e12)


    def light_years_to_miles(light_years=0, num=False, comma=0):
        if comma == 1:
            return "{:,}".format(int(light_years * 5.879e12))
        elif num and not comma:
            return format(round((light_years * 5.879e12), num), ('10.' + str(num) + 'e'))
        elif not num:
            return int(light_years * 5.879e12)


    def miles_to_light_years(miles=0):
        return format( (miles * 1.70108e-13), '10.5e' )


    def kilometers_to_light_years(kilometers=0):
        return (kilometers * 1.057e-13)


    def meters_to_yards(meters=0, num=False):
        if not num:
            return (meters * 1.0936133)
        else:
            return round( (meters * 1.0936133), num )


    def yards_to_meters(yards=0, num=False):
        if not num:
            return (yards * 0.9144)
        else:
            return round( (yards * 0.9144), num )


    def inch_to_centimeter(inch=0, num=False):
        if not num:
            return (inch * 2.54)
        else:
            return round( (inch * 2.54), num )


    def centimeter_to_inch(centimeter=0, num=False):
        if not num:
            return (centimeter * 0.393701)
        else:
            return round( (centimeter * 0.393701), num )




class Weights(object):
    """
    Formulas for Weight Conversions
    """

    def grams_to_ounces(grams=0, num=False):
        if not num:
            return (grams * 0.035274)
        else:
            return round((grams * 0.035274), num)


    def ounces_to_grams(ounces=0, num=False):
        if not num:
            return (ounces * 28.349)
        else:
            return round((ounces * 28.349), num)


    def kilograms_to_pounds(kilograms=0, num=False):
        if not num:
            return (kilograms * 2.2046)
        else:
            return round((kilograms * 2.2046), num)


    def pounds_to_kilograms(pounds=0, num=False):
        if not num:
            return (pounds *  0.454)
        else:
            return round((pounds *  0.454), num)


    def kilograms_to_ton(kilograms=0, num=False):
        if not num:
            return (kilograms * 0.0011)
        else:
            return round((kilograms * 0.0011), num)


    def tons_to_kilograms(tons=0, num=False):
        if not num:
            return (tons * 907.18)
        else:
            return round((tons * 907.18), num)


    def tons_to_metric_tonnes(tons=0, num=False):
        if not num:
            return (tons * 0.907185)
        else:
            return round((tons * 0.907185), num)


    def metric_tonnes_to_tons(metric_tonnes=0, num=False):
        if not num:
            return (metric_tonnes * 1.102311)
        else:
            return round((metric_tonnes * 1.102311), num)



class Volumes(object):
    """
    Formulas for Volumet Conversions
    """

    def liters_to_gallons(liters=0, num=False):
        if not num:
            return (liters * 0.264)
        else:
            return round((liters * 0.264), num)


    def gallons_to_liters(gallons=0, num=False):
        if not num:
            return (gallons * 3.785)
        else:
            return round((gallons * 3.785), num)


    def ounces_to_milliliters(ounces=0, num=False):
        if not num:
            return (ounces * 29.57)
        else:
            return round((ounces * 29.57), num)


    def milliliters_to_ounces(milliliters=0, num=False):
        if not num:
            return (milliliters * 0.0338)
        else:
            return round((milliliters * 0.0338), num)


    def cubic_centimeter_to_cubic_inch(cubic_centimeter=0, num=False):
        if not num:
            return (cubic_centimeter * 0.0610237)
        else:
            return round((cubic_centimeter * 0.0610237), num)


    def cubic_inch_to_cubic_centimeter(cubic_inch=0, num=False):
        if not num:
            return (cubic_inch * 16.387064)
        else:
            return round((cubic_inch * 16.387064), num)




class Times(object):
    """
    Formulas for Time Conversions
    """

    def timestamp_to_date(timestamp=0):
        return datetime.fromtimestamp(timestamp)


    def date_to_timestamp(year='', month='', day='', *args, **kwargs):
        return timedelta.total_seconds(datetime(year, month, day, *args, **kwargs) - datetime(1970, 1, 1))



if __name__ == '__main__':
    main()

