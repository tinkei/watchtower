import numpy as np


def eci_to_enu(r_eci: np.ndarray, observer_lat: float, observer_lon: float) -> np.ndarray:
    """
    Convert an ECI position vector to ENU coordinates for a ground observer.

    Parameters
    ----------
    r_eci : np.ndarray
        Position vector in ECI coordinates [x, y, z] in meters.
    observer_lat : float
        Latitude of the observer in degrees.
    observer_lon : float
        Longitude of the observer in degrees.

    Returns
    -------
    np.ndarray
        Position vector in ENU coordinates [x, y, z] in meters.
    """
    # Convert latitude and longitude to radians.
    lat_rad = np.radians(observer_lat)
    lon_rad = np.radians(observer_lon)

    # Transformation matrix from ECI to ENU.
    t_matrix = np.array(
        [
            [-np.sin(lon_rad), np.cos(lon_rad), 0],
            [-np.sin(lat_rad) * np.cos(lon_rad), -np.sin(lat_rad) * np.sin(lon_rad), np.cos(lat_rad)],
            [np.cos(lat_rad) * np.cos(lon_rad), np.cos(lat_rad) * np.sin(lon_rad), np.sin(lat_rad)],
        ]
    )

    # Convert position vector.
    r_enu = t_matrix @ r_eci
    return r_enu
