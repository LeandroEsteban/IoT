import io
import sys

import Ice
from PIL import Image, UnidentifiedImageError

import DistributedPhotoProcessor


DEFAULT_ENDPOINT = "tcp -h 0.0.0.0 -p 10000"
MESSAGE_SIZE_MAX_KB = 32768


class ImageProcessorI(DistributedPhotoProcessor.ImageProcessor):
    def Ping(self, current=None):
        print("[Ping] Solicitud recibida", flush=True)
        return "Servidor activo"

    def Color2BW(self, inputImage, current=None):
        self._log_received("Color2BW", inputImage)
        image = self._open_image(inputImage, "Color2BW")
        output = image.convert("L")
        return self._save_image(output, "Color2BW")

    def Resize(self, inputImage, width, height, current=None):
        self._log_received("Resize", inputImage, f"width={width}, height={height}")
        if width <= 0 or height <= 0:
            print("[Resize] Error: ancho y alto invalidos", flush=True)
            raise DistributedPhotoProcessor.InvalidImageException(
                "El ancho y alto deben ser mayores que cero"
            )

        image = self._open_image(inputImage, "Resize")
        output = image.resize((width, height))
        return self._save_image(output, "Resize")

    def Rotate(self, inputImage, degrees, current=None):
        self._log_received("Rotate", inputImage, f"degrees={degrees}")
        image = self._open_image(inputImage, "Rotate")
        output = image.rotate(degrees, expand=True)
        return self._save_image(output, "Rotate")

    def _log_received(self, operation, input_image, details=None):
        message = f"[{operation}] Imagen recibida: {len(input_image)} bytes"
        if details:
            message = f"{message} ({details})"
        print(message, flush=True)

    def _open_image(self, input_image, operation):
        if not input_image:
            print(f"[{operation}] Error: imagen vacia", flush=True)
            raise DistributedPhotoProcessor.InvalidImageException("La imagen esta vacia")

        try:
            image_bytes = bytes(input_image)
            image = Image.open(io.BytesIO(image_bytes))
            image.load()
            print(
                f"[{operation}] Imagen valida: formato={image.format}, tamano={image.size}",
                flush=True,
            )
            return image
        except (UnidentifiedImageError, OSError, ValueError) as exc:
            print(f"[{operation}] Error: imagen no valida: {exc}", flush=True)
            raise DistributedPhotoProcessor.InvalidImageException(
                f"La imagen no es valida: {exc}"
            )

    def _save_image(self, image, operation):
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        output = buffer.getvalue()
        print(
            f"[{operation}] Imagen devuelta: {len(output)} bytes, tamano={image.size}, formato=PNG",
            flush=True,
        )
        return list(output)


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
