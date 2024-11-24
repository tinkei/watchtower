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


def teme_to_ecef(r_teme: np.ndarray, v_teme: np.ndarray, gmst: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert TEME coordinates to ECEF.

    Parameters
    ----------
    r_teme : np.ndarray
        Position vector in TEME coordinates [x, y, z] in meters.
    v_teme : np.ndarray
        Velocity vector in TEME coordinates [vx, vy, vz] in meters/second.
    gmst : float
        Greenwich Mean Sidereal Time in radians.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Position and velocity vectors in ECEF coordinates.
    """
    # Rotation matrix for TEME to ECEF.
    rotation_matrix = np.array([[np.cos(gmst), np.sin(gmst), 0], [-np.sin(gmst), np.cos(gmst), 0], [0, 0, 1]])

    # Rotate position and velocity vectors.
    r_ecef = rotation_matrix @ r_teme
    v_ecef = rotation_matrix @ v_teme

    return r_ecef, v_ecef


def observer_velocity_ecef(observer_lat: float, observer_lon: float) -> np.ndarray:
    """
    Calculate the velocity of a ground observer in the ECEF frame due to Earth's rotation.

    Parameters
    ----------
    observer_lat : float
        Latitude of the observer in degrees.
    observer_lon : float
        Longitude of the observer in degrees.

    Returns
    -------
    np.ndarray
        Velocity vector in ECEF coordinates [vx, vy, vz] in meters/second.
    """
    # Constants.
    earth_rotation_rate = 7.2921150e-5  # radians per second
    earth_radius = 6378137.0  # meters (WGS84)

    # Convert latitude and longitude to radians.
    lat_rad = np.radians(observer_lat)
    lon_rad = np.radians(observer_lon)

    # Observer's velocity due to Earth's rotation.
    vx = -earth_rotation_rate * earth_radius * np.cos(lat_rad) * np.sin(lon_rad)
    vy = earth_rotation_rate * earth_radius * np.cos(lat_rad) * np.cos(lon_rad)
    vz = 0.0  # No vertical motion due to Earth's rotation

    return np.array([vx, vy, vz])
