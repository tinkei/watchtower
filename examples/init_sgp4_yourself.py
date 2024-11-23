"""Test initializing SGP4's Satrec object without using the two TLE strings."""

from sgp4 import exporter
from sgp4.api import WGS72, Satrec

from watchtower.calculation.unit_conversion import (
    convert_revolutions_per_day_cubed_to_radians_per_minute_cubed,
    convert_revolutions_per_day_squared_to_radians_per_minute_squared,
)

line1_sat1 = "1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991"
line2_sat1 = "2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482"
satellite1 = Satrec.twoline2rv(line1_sat1, line2_sat1)

satellite2 = Satrec()
satellite2.sgp4init(
    WGS72,  # gravity model
    "i",  # "a" = old AFSPC mode, "i" = improved mode
    25544,  # satnum: Satellite number
    25545.69339541,  # epoch: days since 1949 December 31 00:00 UT
    3.8792e-05,  # bstar: drag coefficient (1/earth radii)
    convert_revolutions_per_day_squared_to_radians_per_minute_squared(
        0.00001764
    ),  # ndot: ballistic coefficient (radians/minute^2)
    convert_revolutions_per_day_cubed_to_radians_per_minute_cubed(
        0.0
    ),  # nddot: mean motion 2nd derivative (radians/minute^3)
    0.0007417,  # ecco: eccentricity
    0.3083420829620822,  # argpo: argument of perigee (radians)
    0.9013560935706996,  # inclo: inclination (radians)
    1.4946964807494398,  # mo: mean anomaly (radians)
    0.06763602333248933,  # no_kozai: mean motion (radians/minute)
    3.686137125541276,  # nodeo: R.A. of ascending node (radians)
)

# TODO: Can't figure how to set these using `sgp4init()`.
satellite2.intldesg = "98067A"
satellite2.elnum = 999
satellite2.revnum = 20248

line1_sat2, line2_sat2 = exporter.export_tle(satellite2)

print(line1_sat1)
print(line1_sat2)
print(line2_sat1)
print(line2_sat2)

print(exporter.export_omm(satellite1, object_name="ISS (ZARYA)"))
print(exporter.export_omm(satellite2, object_name="ISS (ZARYA)"))

assert line1_sat2 == line1_sat1
assert line2_sat2 == line2_sat1
