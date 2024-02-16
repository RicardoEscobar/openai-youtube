# OpenAI-YouTube
Este es un conjunto de ejemplos de scripts de inteligencia artificial.

# Crear un ambiente virtual de Python (opcional, recomendado)
Este paso no es obligatorio, pero lo recomiendo.

Para crear el ambiente virtual, abrir una terminal y dentro de la carpeta del proyecto ejecutar lo siguiente:
```bash
python -m venv venv
```
Esto creara una subcarpeta `venv/` dentro de la raiz del proyecto.

## Activando el ambiente virtual
Para activar el ambiente virtual, ejecutar lo siguiente dependiendo la terminal usada:
```bash
# En cmd.exe
venv\Scripts\activate.bat

# En PowerShell
venv\Scripts\Activate.ps1

# En MacOSX, Linux, Git Bash
source venv/Scripts/activate
```
Una vez que esta creado el ambiente virtual y activado, debe aparecer el nombre del ambiente virtual entre parentesis `(venv)`

# Instalando paquetes openai
Se requieren la instalacion de paquetes usando pip:

```bash
pip install --upgrade openai
```

# Instalando el paquete python-dotenv
```bash
pip install --upgrade python-dotenv
```

# Obtener una OPENAI_API_KEY
Visitar el [sitio web de openai.com](https://platform.openai.com/login?launch), y crea una cuenta en el sitio web, esto es requerido para hacer solicitudes a la API de OpenAI. Durante la creacion de la cuenta, es requerido agregar un metodo de pago, ya que se cobra por cada solicitud. Seguir instrucciones en el sitio web para ello.

Una vez creada la cuenta, se debe acceder al menu `API keys` y se debe crear una llave API dando clic en el boton: `+Create new secret key`. Donde se le asigna un nombre a la llave. En esta parte, la cadena de texto debe ser copiada antes de cerrar la ventana o se pierde y habra que crear una llave nueva.

## Guardar la OPENAI_API_KEY en el archivo .env
Con la `OPENAI_API_KEY`, se debe crear un archivo llamado `.env` dentro de la raiz del proyecto, con el siguiguiente contenido:

```bash
# Una vez que agregues tu clave API a continuación, ¡asegúrate de no compartirla con nadie! La clave de API debe permanecer privada
OPENAI_API_KEY=TU_API_KEY
```
__Nota:__ Recomiendo agregar el archivo `.env` al archivo `.gitignore` para evitar que se agregue la clave al repositorio.