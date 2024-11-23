"""Check whether your machine has successfully installed the fast SGP4 C++ code, or is using the slow Python version."""

from sgp4.api import accelerated

print(accelerated)
