"""
Helpers for converting Strava's units to something more practical.

These are really just thin wrappers to the brilliant 'units' python library. 
"""
from units import unit
import units.predefined


METRIC = 'metric'
STANDARD = 'standard'

# Setup the units we will use in this module.
units.predefined.define_units()

meter = meters = unit('m')
second = seconds = unit('s')
hour = hours = unit('h')
foot = feet = unit('ft')
mile = miles = unit('mi')
kilometer = kilometers = unit('km')

meters_per_second = meter / second
miles_per_hour = mph = mile / hour
kilometers_per_hour = kph = kilometer / hour
    