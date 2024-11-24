import numpy as np


def decompose_velocity_vector(velocity: np.ndarray, position: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Decompose a velocity vector into radial and tangential components.

    Parameters
    ----------
    velocity : np.ndarray
        Velocity vector in ECI coordinates [vx, vy, vz] in m/s.
    position : np.ndarray
        Position vector in ECI coordinates [x, y, z] in meters.

    Returns
    -------
    tuple[np.ndarray, np.ndarray, np.ndarray]
        The original velocity vector, its radial component, and its tangential component.
    """
    radial_unit = position / np.linalg.norm(position)
    radial_component = np.dot(velocity, radial_unit) * radial_unit
    tangential_component = velocity - radial_component
    return velocity, radial_component, tangential_component
