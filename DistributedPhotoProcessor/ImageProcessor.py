# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from DistributedPhotoProcessor.ImageData import _DistributedPhotoProcessor_ImageData_t

from DistributedPhotoProcessor.ImageProcessor_forward import _DistributedPhotoProcessor_ImageProcessorPrx_t

from DistributedPhotoProcessor.InvalidImageException import _DistributedPhotoProcessor_InvalidImageException_t

from Ice.Object import Object

from Ice.ObjectPrx import ObjectPrx
from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from collections.abc import Awaitable
    from collections.abc import Buffer
    from collections.abc import Sequence


class ImageProcessorPrx(ObjectPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::DistributedPhotoProcessor::ImageProcessor``.
    """

    def Color2BW(self, inputImage: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> bytes:
        return ImageProcessor._op_Color2BW.invoke(self, ((inputImage, ), context))

    def Color2BWAsync(self, inputImage: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> Awaitable[bytes]:
        return ImageProcessor._op_Color2BW.invokeAsync(self, ((inputImage, ), context))

    def Resize(self, inputImage: Sequence[int] | bytes | Buffer, width: int, height: int, context: dict[str, str] | None = None) -> bytes:
        return ImageProcessor._op_Resize.invoke(self, ((inputImage, width, height), context))

    def ResizeAsync(self, inputImage: Sequence[int] | bytes | Buffer, width: int, height: int, context: dict[str, str] | None = None) -> Awaitable[bytes]:
        return ImageProcessor._op_Resize.invokeAsync(self, ((inputImage, width, height), context))

    def Rotate(self, inputImage: Sequence[int] | bytes | Buffer, degrees: int, context: dict[str, str] | None = None) -> bytes:
        return ImageProcessor._op_Rotate.invoke(self, ((inputImage, degrees), context))

    def RotateAsync(self, inputImage: Sequence[int] | bytes | Buffer, degrees: int, context: dict[str, str] | None = None) -> Awaitable[bytes]:
        return ImageProcessor._op_Rotate.invokeAsync(self, ((inputImage, degrees), context))

    def Ping(self, context: dict[str, str] | None = None) -> str:
        return ImageProcessor._op_Ping.invoke(self, ((), context))

    def PingAsync(self, context: dict[str, str] | None = None) -> Awaitable[str]:
        return ImageProcessor._op_Ping.invokeAsync(self, ((), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ImageProcessorPrx | None:
        return checkedCast(ImageProcessorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ImageProcessorPrx | None ]:
        return checkedCastAsync(ImageProcessorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ImageProcessorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ImageProcessorPrx | None:
        return uncheckedCast(ImageProcessorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::DistributedPhotoProcessor::ImageProcessor"

IcePy.defineProxy("::DistributedPhotoProcessor::ImageProcessor", ImageProcessorPrx)

class ImageProcessor(Object, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::DistributedPhotoProcessor::ImageProcessor``.
    """

    _ice_ids: Sequence[str] = ("::DistributedPhotoProcessor::ImageProcessor", "::Ice::Object", )
    _op_Color2BW: IcePy.Operation
    _op_Resize: IcePy.Operation
    _op_Rotate: IcePy.Operation
    _op_Ping: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::DistributedPhotoProcessor::ImageProcessor"

    @abstractmethod
    def Color2BW(self, inputImage: bytes, current: Current) -> Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]:
        pass

    @abstractmethod
    def Resize(self, inputImage: bytes, width: int, height: int, current: Current) -> Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]:
        pass

    @abstractmethod
    def Rotate(self, inputImage: bytes, degrees: int, current: Current) -> Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]:
        pass

    @abstractmethod
    def Ping(self, current: Current) -> str | Awaitable[str]:
        pass

ImageProcessor._op_Color2BW = IcePy.Operation(
    "Color2BW",
    "Color2BW",
    OperationMode.Normal,
    None,
    (),
    (((), _DistributedPhotoProcessor_ImageData_t, False, 0),),
    (),
    ((), _DistributedPhotoProcessor_ImageData_t, False, 0),
    (_DistributedPhotoProcessor_InvalidImageException_t,),
    False)

ImageProcessor._op_Resize = IcePy.Operation(
    "Resize",
    "Resize",
    OperationMode.Normal,
    None,
    (),
    (((), _DistributedPhotoProcessor_ImageData_t, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), _DistributedPhotoProcessor_ImageData_t, False, 0),
    (_DistributedPhotoProcessor_InvalidImageException_t,),
    False)

ImageProcessor._op_Rotate = IcePy.Operation(
    "Rotate",
    "Rotate",
    OperationMode.Normal,
    None,
    (),
    (((), _DistributedPhotoProcessor_ImageData_t, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), _DistributedPhotoProcessor_ImageData_t, False, 0),
    (_DistributedPhotoProcessor_InvalidImageException_t,),
    False)

ImageProcessor._op_Ping = IcePy.Operation(
    "Ping",
    "Ping",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    ((), IcePy._t_string, False, 0),
    (),
    False)

__all__ = ["ImageProcessor", "ImageProcessorPrx", "_DistributedPhotoProcessor_ImageProcessorPrx_t"]
