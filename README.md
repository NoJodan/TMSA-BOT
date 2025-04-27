# Discord Bot Project

Este proyecto es un bot de Discord que utiliza cogs para organizar el código y MongoDB para la gestión de datos.

## Estructura del Proyecto

```
discord-bot
├── src
│   ├── bot.py               # Punto de entrada del bot
│   ├── cogs                 # Carpeta que contiene los cogs del bot
│   │   ├── __init__.py      # Inicializa el paquete de cogs
│   │   └── example_cog.py   # Ejemplo de un cog
│   ├── database             # Carpeta que contiene la gestión de la base de datos
│   │   ├── __init__.py      # Inicializa el paquete de la base de datos
│   │   └── mongo_manager.py  # Manejo de la conexión a MongoDB
│   └── utils                # Carpeta que contiene funciones utilitarias
│       └── helpers.py       # Funciones utilitarias
├── requirements.txt         # Dependencias del proyecto
├── .env                     # Variables de entorno
└── README.md                # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd discord-bot
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Configura el archivo `.env` con el token de tu bot de Discord y la URI de conexión a MongoDB.

## Uso

Para ejecutar el bot, utiliza el siguiente comando:
```
python src/bot.py
```

Asegúrate de que el bot tenga los permisos necesarios en tu servidor de Discord y que esté invitado correctamente.