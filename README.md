# Cassini Hackathon #8: Project Watchtower

**_Watchtower_** is an entry to the 8th [Cassini](https://www.cassini.eu/hackathons/) [Hackathon](https://taikai.network/cassinihackathons/hackathons/euspace-defence-security)

This repo contains example scripts to:

- Query ESA DOSCOS API for object dimensions (among other things).
- Query Space-Track API for object TLE (Two-Line Element set).
- Load TLE into SGP4 model (a Simplified General Perturbations model).
- Propagate TLE in SGP4 model to current epoch.
- Transform SGP4 model output to observer coordinates (ECI, ENU).
- Calculate relative velocities.
- Compute expected Doppler shift.

## Set up

- `git clone https://github.com/tinkei/watchtower.git` and `cd .\watchtower` to the root of this repository.
- Create virtual environment once: `python -m venv $env:HomeDrive$env:HomePath\venvs\watchtower`
- Activate virtual environment in PowerShell: `& "$env:HomeDrive$env:HomePath\venvs\watchtower\Scripts\Activate.ps1"`
- Install this repository and all its dependencies to the active virtual environment: `pip install -e .`
