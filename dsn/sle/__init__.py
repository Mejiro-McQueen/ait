# Advanced Multi-Mission Operations System (AMMOS) Instrument Toolkit (AIT)
# Bespoke Link to Instruments and Small Satellites (BLISS)
#
# Copyright 2017, by the California Institute of Technology. ALL RIGHTS
# RESERVED. United States Government Sponsorship acknowledged. Any
# commercial use must be negotiated with the Office of Technology Transfer
# at the California Institute of Technology.
#
# This software may be subject to U.S. export control laws. By accepting
# this software, the user agrees to comply with all applicable U.S. export
# laws and regulations. User has the responsibility to obtain export licenses,
# or other export authority as may be required before exporting such
# information to foreign countries or providing access to foreign persons.

import sys

from .raf import RAF
from .rcf import RCF
from .cltu import CLTU

# Default port to which Frames will be emitted by SLE RAF/RCF ('FRAM')
sys.modules['ait'].DEFAULT_FRAME_PORT = 3726

# Default frame type for incoming frame bytearrays
sys.modules['ait'].DEFAULT_FRAME_TYPE = 'TMTransFrame'
