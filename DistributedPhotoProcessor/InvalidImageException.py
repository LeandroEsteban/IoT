# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from Ice.UserException import UserException

from dataclasses import dataclass


@dataclass
class InvalidImageException(UserException):
    """
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::DistributedPhotoProcessor::InvalidImageException``.
    """
    reason: str = ""

    _ice_id = "::DistributedPhotoProcessor::InvalidImageException"

_DistributedPhotoProcessor_InvalidImageException_t = IcePy.defineException(
    "::DistributedPhotoProcessor::InvalidImageException",
    InvalidImageException,
    (),
    None,
    (("reason", (), IcePy._t_string, False, 0),))

setattr(InvalidImageException, '_ice_type', _DistributedPhotoProcessor_InvalidImageException_t)

__all__ = ["InvalidImageException", "_DistributedPhotoProcessor_InvalidImageException_t"]
