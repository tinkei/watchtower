def validate_tle(line1: str, line2: str) -> bool:
    """
    Validate the format of the two TLE strings.

    Because TLE is an old punch-card fixed-width format, it's very sensitive to whether exactly the right number of spaces
    are positioned in exactly the right columns.
    If you suspect that your satellite elements aren't getting loaded correctly, try calling the slow pure-Python version
    of `twoline2rv()`, which performs extra checks that the fast C++ doesn't.
    """
    from sgp4.earth_gravity import wgs72
    from sgp4.io import twoline2rv

    try:
        twoline2rv(line1, line2, wgs72)
    except ValueError:
        return False
    return True
