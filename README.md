# LMS7002M Python package

The pyLMS7002Soapy Python package is platform-independent, and is intended for fast prototyping
and algorithm development. It provides low level register access and high level convenience functions
for controlling the LMS7002M chip and evaluation boards. Supported evaluation boards are:

* LimeSDR
* LimeSDR Mini

The package consists of Python classes which correspond to physical or logical entities. For
example, each module of LMS7002M (AFE, SXT, TRF, ...) is a class. The LMS7002M chip is also a
class containing instances of on-chip modules. The evaluation board class contains instances of
on-board chips, such as LMS7002, ADF4002, etc. Classes follow the hierarchy and logical
organization from evaluation board down to on-chip register level.

SoapySDR interface is required for establishing an USB connection, and can be used
for high level functions, such as reading samples.

## Installation

The pyLMS7002Soapy package is installed in a usual way:

  python setup.py install

Module installation can be verified from Python:

  python
  >>> from pyLMS7002Soapy import *

If there is no error, the module is correctly installed.

## Examples

* Vector Network Analyser (VNA)
* Scalar Network Analyser (SNA)

Scalar network analyzer is preferred for measurements and is much faster than VNA.

## Licensing

pyLMS7002Soapy is copyright 2018 Lime Microsystems and provided under the Apache 2.0 License.
