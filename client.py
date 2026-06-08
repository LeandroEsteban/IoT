import sys

import Ice

import DistributedPhotoProcessor


DEFAULT_HOST = "localhost"
DEFAULT_PORT = "10000"


def read_image(path):
    with open(path, "rb") as file:
        return list(file.read())


def write_image(path, data):
    with open(path, "wb") as file:
        file.write(bytes(data))


def usage():
    print("Uso:")
    print("  python client.py ping [host] [port]")
    print("  python client.py bw <entrada> <salida> [host] [port]")
    print("  python client.py resize <entrada> <salida> <ancho> <alto> [host] [port]")
    print("  python client.py rotate <entrada> <salida> <grados> [host] [port]")


def connect_processor(communicator, host, port):
    proxy = communicator.stringToProxy(
        f"ImageProcessor:default -h {host} -p {port}"
    )
    processor = DistributedPhotoProcessor.ImageProcessorPrx.checkedCast(proxy)
    if not processor:
        raise RuntimeError("No se pudo conectar con el servidor ImageProcessor")
    return processor


def main():
    if len(sys.argv) < 2:
        usage()
        return 1

    operation = sys.argv[1].lower()

    try:
        with Ice.initialize(sys.argv) as communicator:
            if operation == "ping":
                host = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_HOST
                port = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_PORT
                processor = connect_processor(communicator, host, port)
                print(processor.Ping())
                return 0

            if operation == "bw":
                if len(sys.argv) not in (4, 6):
                    usage()
                    return 1
                input_path, output_path = sys.argv[2], sys.argv[3]
                host = sys.argv[4] if len(sys.argv) == 6 else DEFAULT_HOST
                port = sys.argv[5] if len(sys.argv) == 6 else DEFAULT_PORT
                processor = connect_processor(communicator, host, port)
                result = processor.Color2BW(read_image(input_path))

            elif operation == "resize":
                if len(sys.argv) not in (6, 8):
                    usage()
                    return 1
                input_path, output_path = sys.argv[2], sys.argv[3]
                width, height = int(sys.argv[4]), int(sys.argv[5])
                host = sys.argv[6] if len(sys.argv) == 8 else DEFAULT_HOST
                port = sys.argv[7] if len(sys.argv) == 8 else DEFAULT_PORT
                processor = connect_processor(communicator, host, port)
                result = processor.Resize(read_image(input_path), width, height)

            elif operation == "rotate":
                if len(sys.argv) not in (5, 7):
                    usage()
                    return 1
                input_path, output_path = sys.argv[2], sys.argv[3]
                degrees = int(sys.argv[4])
                host = sys.argv[5] if len(sys.argv) == 7 else DEFAULT_HOST
                port = sys.argv[6] if len(sys.argv) == 7 else DEFAULT_PORT
                processor = connect_processor(communicator, host, port)
                result = processor.Rotate(read_image(input_path), degrees)

            else:
                usage()
                return 1

            write_image(output_path, result)
            print(f"Imagen procesada guardada en: {output_path}")
            return 0

    except DistributedPhotoProcessor.InvalidImageException as exc:
        print(f"Error de imagen: {exc.reason}")
        return 1
    except (Ice.Exception, OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
