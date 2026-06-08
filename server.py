import io
import sys

import Ice
from PIL import Image, UnidentifiedImageError

import DistributedPhotoProcessor


DEFAULT_ENDPOINT = "tcp -h 0.0.0.0 -p 10000"
MESSAGE_SIZE_MAX_KB = 32768


class ImageProcessorI(DistributedPhotoProcessor.ImageProcessor):
    def Ping(self, current=None):
        return "Servidor activo"

    def Color2BW(self, inputImage, current=None):
        image = self._open_image(inputImage)
        output = image.convert("L")
        return self._save_image(output)

    def Resize(self, inputImage, width, height, current=None):
        if width <= 0 or height <= 0:
            raise DistributedPhotoProcessor.InvalidImageException(
                "El ancho y alto deben ser mayores que cero"
            )

        image = self._open_image(inputImage)
        output = image.resize((width, height))
        return self._save_image(output)

    def Rotate(self, inputImage, degrees, current=None):
        image = self._open_image(inputImage)
        output = image.rotate(degrees, expand=True)
        return self._save_image(output)

    def _open_image(self, input_image):
        if not input_image:
            raise DistributedPhotoProcessor.InvalidImageException("La imagen esta vacia")

        try:
            image_bytes = bytes(input_image)
            image = Image.open(io.BytesIO(image_bytes))
            image.load()
            return image
        except (UnidentifiedImageError, OSError, ValueError) as exc:
            raise DistributedPhotoProcessor.InvalidImageException(
                f"La imagen no es valida: {exc}"
            )

    def _save_image(self, image):
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        return list(buffer.getvalue())


def main():
    endpoint = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ENDPOINT
    init_data = Ice.InitializationData()
    init_data.properties = Ice.createProperties(sys.argv)
    init_data.properties.setProperty("Ice.MessageSizeMax", str(MESSAGE_SIZE_MAX_KB))

    with Ice.initialize(sys.argv, initData=init_data) as communicator:
        adapter = communicator.createObjectAdapterWithEndpoints(
            "ImageProcessorAdapter", endpoint
        )
        servant = ImageProcessorI()
        adapter.add(servant, Ice.stringToIdentity("ImageProcessor"))
        adapter.activate()

        print(f"Servidor escuchando en: {endpoint}")
        print("Identidad del objeto: ImageProcessor")
        print(f"Tamano maximo de mensaje: {MESSAGE_SIZE_MAX_KB} KB")
        communicator.waitForShutdown()


if __name__ == "__main__":
    main()
