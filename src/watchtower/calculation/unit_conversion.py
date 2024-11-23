import numpy as np

# Conversion constants.
RADIANS_PER_REVOLUTION = 2 * np.pi
MINUTES_PER_DAY = 24 * 60


def convert_revolutions_per_day_to_radians_per_minute(rev_per_day: float) -> float:
    """
    Convert a value in revolutions/day to radians/minute.

    Parameters
    ----------
    rev_per_day : float
        Value in revolutions per day.

    Returns
    -------
    float
        Value in radians per minute.
    """
    return rev_per_day * RADIANS_PER_REVOLUTION / MINUTES_PER_DAY


def convert_revolutions_per_day_squared_to_radians_per_minute_squared(rev_per_day_squared: float) -> float:
    """
    Convert a value in revolutions/day² to radians/minute².

    Parameters
    ----------
    rev_per_day_squared : float
        Value in revolutions per day squared.

    Returns
    -------
    float
        Value in radians per minute squared.
    """
    return rev_per_day_squared * RADIANS_PER_REVOLUTION / (MINUTES_PER_DAY**2)


def convert_revolutions_per_day_cubed_to_radians_per_minute_cubed(rev_per_day_cubed: float) -> float:
    """
    Convert a value in revolutions/day³ to radians/minute³.

    Parameters
    ----------
    rev_per_day_cubed : float
        Value in revolutions per day cubed.

    Returns
    -------
    float
        Value in radians per minute cubed.
    """
    return rev_per_day_cubed * RADIANS_PER_REVOLUTION / (MINUTES_PER_DAY**3)


# Example usage.
if __name__ == "__main__":
    rev_per_day_squared = 0.00001282
    rev_per_day_cubed = 0.00000001

    rad_per_min_squared = convert_revolutions_per_day_squared_to_radians_per_minute_squared(rev_per_day_squared)
    rad_per_min_cubed = convert_revolutions_per_day_cubed_to_radians_per_minute_cubed(rev_per_day_cubed)

    print(f"Revolutions/day²: {rev_per_day_squared} → Radians/minute²: {rad_per_min_squared}")
    print(f"Revolutions/day³: {rev_per_day_cubed} → Radians/minute³: {rad_per_min_cubed}")
