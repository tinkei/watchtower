from datetime import datetime

import numpy as np
from sgp4.api import Satrec, jday

from watchtower.validation import validate_tle


def propagate_tle(tle_line1: str, tle_line2: str, epoch: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Propagate a satellite's orbit using TLE data and return ECI position and velocity.

    Parameters
    ----------
    tle_line1 : str
        First line of the TLE.
    tle_line2 : str
        Second line of the TLE.
    epoch : str
        Epoch of the propagation in ISO format (e.g., "2024-11-23T00:00:00").

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Position and velocity vectors in ECI coordinates ([x, y, z] and [vx, vy, vz]).
    """
    # Parse the TLE using sgp4.
    validate_tle(tle_line1, tle_line2)
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)

    # Convert epoch to Julian date.
    observation_time = datetime.fromisoformat(epoch)
    jd, fr = jday(
        observation_time.year,
        observation_time.month,
        observation_time.day,
        observation_time.hour,
        observation_time.minute,
        observation_time.second,
    )

    # Propagate to the desired time.
    e, r, v = satellite.sgp4(jd, fr)
    if e != 0:
        raise RuntimeError("SGP4 propagation failed with error code: {}".format(e))

    print("Propagated:", e, r, v)
    return np.array(r), np.array(v)
