import numpy as np


def calculate_doppler_shift(velocity_radial: np.ndarray, carrier_frequency: float) -> float:
    """
    Calculate the Doppler shift given the radial velocity component.

    Parameters
    ----------
    velocity_radial : np.ndarray
        Radial velocity vector in m/s.
    carrier_frequency : float
        Carrier frequency in Hz.

    Returns
    -------
    float
        Doppler shift in Hz.
    """
    speed_of_light = 299792458  # m/s
    radial_speed = np.linalg.norm(velocity_radial)
    doppler_shift = (carrier_frequency / speed_of_light) * radial_speed
    return doppler_shift
