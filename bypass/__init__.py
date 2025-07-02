from .generic import generic_bypass
from .urllinkshort import bypass_urllinkshort

BYPASS_HANDLERS = {
    "urllinkshort.in": bypass_urllinkshort,
    # Add more domains and their functions here
}
