ubConvert.py
Weights and Measures conversion module

    - Utility_Belt Designs, Tacoma, WA
    - www.pythonOver60.rocks
    - @author: ZennDogg
    - zenndogg@outlook.com

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
          - 0=integer, 1=one decimal place, 2=two decimal places, etc.,

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

     Usage Example:

          import ubConvert as ub

          weights = ub.Weights()
          oz = weights.grams_to_ounces(28)
          oz = 1


      Functions include: 
      - note: use all lower case when calling functions, right?

      - Temperatures() function list

          - Kelvin_to_Fahrenheit
          - Kelvin_to_Celsius
          - Fahrenheit_to_Kelvin
          - Fahrenheit_to_Celsius
          - Celsius_to_Fahrenheit
          - Celsius_to_Kelvin
          - Rankine_to_Fahrenheit
          - Fahrenheit_to_Rankine

      - Speed_Distance() function list

          - MPH_to_KPH
          - KPH_to_MPH
          - MPH_to_Meters_per_Second
          - Meters_per_Second_to_MPH
          - Meters_per_Second_to_KPH
          - KPH_to_Meters_per_Second   
          - Light_Years_to_Miles
          - Miles_to_Light_Years
          - Light_Years_to_Kilometers
          - Kilometers_to_Light_Years
          - Yards_to_Meters
          - Meters_to_Yards
          - Inch_to_Centimeter
          - Centimeter_to_Inch
          - Astronomical_Unit_to_Miles
          - Miles_to_Astronomical_Unit
          - Astronomical_Unit_to_Kilometers
          - Kilometers_to_Astronomical_Unit

      - Weights() function list

         - Grams_to_Ounces
         - Ounces_to_Grams
         - Kilograms_to_Pounds
         - Pounds_to_Kilograms
         - Kilograms_to_Tons
         - Tons_to_Kilograms
         - Tons_to_Metric_Tonnes
         - Metric_Tonnes_to_Tons

      - Volumes() function list

         - Liters_to_Gallons
         - Gallons_to_Liters
         - Ounces_to_Milliliters
         - Milliliters_to_Ounces
         - Cubic_Centimeter_to_Cubic_Inch
         - Cubic_Inch_to_Cubic_Centimeter

      - Times() function list

         - Date_to_Timestamp
         - Timestamp_to_Date

  - note: use all lower case when calling functions, right?
