# Actividad 1 - Procesador de Imagenes Distribuido

Este proyecto implementa un procesador de imagenes distribuido usando ZeroC Ice.

El archivo `ImageProcessor.ice` define el contrato compartido entre el cliente y el servidor.

## Que debe tener tu companera

Tu companera ejecuta el servidor. Debe tener estos archivos:

```text
ImageProcessor.ice
DistributedPhotoProcessor/
server.py
requirements.txt
```

Debe instalar dependencias:

```powershell
pip install -r requirements.txt
```

Debe generar el codigo Ice:

```powershell
slice2py ImageProcessor.ice
```

Debe iniciar el servidor:

```powershell
python server.py
```

Por defecto, el servidor escucha en:

```text
tcp -h 0.0.0.0 -p 10000
```

Si Windows pregunta por el firewall, debe permitir conexiones entrantes para que tu computadora pueda conectarse.

## Que debes tener tu

Tu ejecutas el cliente. Debes tener estos archivos:

```text
ImageProcessor.ice
DistributedPhotoProcessor/
client.py
requirements.txt
```

Tambien debes tener una imagen de prueba, por ejemplo:

```text
foto.jpg
```

Debes instalar dependencias:

```powershell
pip install -r requirements.txt
```

Debes generar el codigo Ice:

```powershell
slice2py ImageProcessor.ice
```

Necesitas saber la IP de la computadora de tu companera. Por ejemplo:

```text
192.168.1.25
```

## Pruebas desde tu computadora

Probar conexion:

```powershell
python client.py ping 192.168.1.25 10000
```

Convertir imagen a blanco y negro:

```powershell
python client.py bw foto.jpg resultado_bw.png 192.168.1.25 10000
```

Redimensionar imagen:

```powershell
python client.py resize foto.jpg resultado_resize.png 300 300 192.168.1.25 10000
```

Rotar imagen:

```powershell
python client.py rotate foto.jpg resultado_rotate.png 90 192.168.1.25 10000
```

## Pruebas en la misma computadora

Si cliente y servidor corren en la misma computadora, usa `localhost`:

```powershell
python client.py ping localhost 10000
python client.py bw foto.jpg resultado_bw.png localhost 10000
```

Tambien puedes omitir host y puerto porque `client.py` usa `localhost` y `10000` por defecto:

```powershell
python client.py ping
python client.py bw foto.jpg resultado_bw.png
```

## Operaciones implementadas

`Ping()` verifica que el servidor este activo.

`Color2BW(inputImage)` convierte la imagen a blanco y negro.

`Resize(inputImage, width, height)` cambia la imagen al tamano indicado.

`Rotate(inputImage, degrees)` rota la imagen los grados indicados.

Todas las imagenes procesadas se devuelven en formato PNG.

## Estructura completa recomendada

```text
Actividad1/
├── ImageProcessor.ice
├── DistributedPhotoProcessor/
├── server.py
├── client.py
├── requirements.txt
└── README.md
```

`DistributedPhotoProcessor/` no se escribe manualmente. Se genera automaticamente con `slice2py ImageProcessor.ice`.
