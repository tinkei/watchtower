import numpy as np
from sgp4.api import Satrec, jday

from watchtower.calculation import calculate_doppler_shift, decompose_velocity_vector, propagate_tle


def calculate_relative_velocities(positions: list[np.ndarray], velocities: list[np.ndarray]) -> list[np.ndarray]:
    """
    Calculate pairwise relative velocities between all parties.

    Parameters
    ----------
    positions : list[np.ndarray]
        List of position vectors in ECI coordinates.
    velocities : list[np.ndarray]
        List of velocity vectors in ECI coordinates.

    Returns
    -------
    list[np.ndarray]
        List of relative velocity vectors between all pairs.
    """
    relative_velocities = []
    n = len(positions)
    # TODO: Wrong loop logic it seems.
    for i in range(n):
        for j in range(i + 1, n):
            relative_velocity = velocities[i] - velocities[j]
            relative_velocities.append(relative_velocity)
    return relative_velocities


def main():
    """
    Example demonstrating ECI to ENU conversion, relative velocity calculations,
    and Doppler shift analysis for multiple parties.
    """
    # Example TLEs (ISS and a GPS satellite).
    tle_iss_line1 = "1 25544U 98067A   20356.55504791  .00001282  00000-0  29609-4 0  9993"
    tle_iss_line2 = "2 25544  51.6466 212.3523 0001540  71.6672  44.1667 15.49107850260485"

    tle_gps_line1 = "1 24876U 97035A   20356.89748757  .00000033  00000-0  00000-0 0  9996"
    tle_gps_line2 = "2 24876  56.8476 310.8984 0158397  90.5550 270.3784  2.00561866123015"

    # Observer location (latitude and longitude in degrees).
    observer_lat = 52.3676  # Amsterdam
    observer_lon = 4.9041

    # Epoch of observation.
    epoch = "2024-11-23T00:00:00"

    # Propagate ISS and GPS satellites.
    r_iss, v_iss = propagate_tle(tle_iss_line1, tle_iss_line2, epoch)
    r_gps, v_gps = propagate_tle(tle_gps_line1, tle_gps_line2, epoch)

    # Ground observer's position and velocity (assume stationary in ECI frame).
    r_observer = np.zeros(3)
    v_observer = np.zeros(3)

    # Calculate relative velocities.
    positions = [r_iss, r_gps, r_observer]
    velocities = [v_iss, v_gps, v_observer]
    relative_velocities = calculate_relative_velocities(positions, velocities)

    # Carrier frequency (example: GPS L1 frequency in Hz).
    carrier_frequency = 1575.42e6

    # Analyze each relative velocity.
    print("Relative Velocities and Doppler Shifts:")
    for i, rv in enumerate(relative_velocities):
        vel, rad_comp, tan_comp = decompose_velocity_vector(rv, positions[i % len(positions)])
        doppler_shift = calculate_doppler_shift(rad_comp, carrier_frequency)
        print(f"Relative Velocity {i + 1} (m/s): {vel}")
        print(f"  Radial Component (m/s): {rad_comp}")
        print(f"  Tangential Component (m/s): {tan_comp}")
        print(f"  Doppler Shift (Hz): {doppler_shift:.2f}")


if __name__ == "__main__":
    main()
