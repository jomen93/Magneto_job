
# Magneto Job API

API para determinar si una secuencia de ADN pertenece a un mutante y proporcionar estadísticas de ADN humano y mutante.

## Índice

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecutar en Local](#ejecutar-en-local)
- [Acceder al Servicio en Producción](#acceder-al-servicio-en-producción)
- [Estructura de la Base de Datos](#estructura-de-la-base-de-datos)
- [Cobertura de Código](#cobertura-de-código)

---

## Descripción

Este servicio ofrece:
- Un endpoint `/mutant/` para verificar si una secuencia de ADN pertenece a un mutante.
- Un endpoint `/stats/` para estadísticas sobre el ADN mutante y humano almacenado en la base de datos.

## Requisitos

- **Docker** y **Docker Compose** para la ejecución en local.
- **Python 3.9** y **FastAPI** (para desarrollo local opcional).
- **MySQL** como base de datos, configurada en `docker-compose.yml` en local. En produccion esta en GCP cloud SQL

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jomen93/magneto_job.git
   cd magneto_job
   ```

2. Crea un archivo `.env` con las variables necesarias para la conexión a la base de datos:
   ```env
   DATABASE_URL="mysql+pymysql://usuario:contraseña@db:3306/nombre_db"
   ```

3. Instala las dependencias (solo si deseas ejecutar el código sin Docker):
   ```bash
   pip install -r requirements.txt
   ```

## Ejecutar en Local

1. Levanta los servicios con Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Accede a la API en `http://localhost:8000`.

3. Documentación de la API en `http://localhost:8000/docs`.

## Acceder al Servicio en Producción

Para acceder al servicio desplegado en Google Cloud Run (u otro servicio en la nube), utiliza las siguientes URL:

- **Endpoint Mutant**:  
  ```
  POST https://magneto-api-956967838259.us-central1.run.app/mutant/
  ```
  Ejemplo de payload JSON:
  ```json
  {
      "dna": ["ACACGG", "CAGTGC", "ATATGT", "TGATGT", "CACATA", "TGACTG"]
  }
  ```

- **Endpoint Stats**:  
  ```
  GET  https://magneto-api-956967838259.us-central1.run.app/stats/
  ```

## Estructura de la Base de Datos

La base de datos utiliza MySQL y contiene una tabla principal para almacenar las secuencias de ADN y su tipo.

### Tabla: `dna_sequences`

| Columna               | Tipo         | Descripción                                               |
|-----------------------|--------------|-----------------------------------------------------------|
| `id`                  | Integer      | ID único para cada secuencia                               |
| `sequence`            | Text         | Secuencia de ADN en formato JSON                          |
| `is_mutant`           | Boolean      | Indica si es mutante (`True`) o humano (`False`)          |
| `sequence_length`     | Integer      | Longitud de la secuencia                                  |
| `mutant_sequence_count` | Integer   | Número de secuencias mutantes encontradas en el ADN       |
| `human_sequence_count` | Integer    | Número de secuencias humanas encontradas en el ADN        |
| `detected_patterns`   | JSON         | Lista de patrones detectados, si es mutante               |
| `created_at`          | DateTime     | Fecha de creación de la entrada                           |

## Cobertura de Código

El servicio ha sido probado para asegurar una cobertura de al menos el 80%.

| Name                               | Statements | Missing | Coverage | Missing Lines |
|------------------------------------|------------|---------|----------|---------------|
| app/api/__init__.py                | 0          | 0       | 100%     |               |
| app/api/dependencies.py            | 0          | 0       | 100%     |               |
| app/api/routes/__init__.py         | 0          | 0       | 100%     |               |
| app/api/routes/mutant.py           | 16         | 0       | 100%     |               |
| app/api/routes/stats.py            | 9          | 2       | 78%      | 11-12         |
| app/core/__init__.py               | 0          | 0       | 100%     |               |
| app/core/config.py                 | 0          | 0       | 100%     |               |
| app/core/database.py               | 15         | 0       | 100%     |               |
| app/core/init_db.py                | 7          | 7       | 0%       | 1-9           |
| app/main.py                        | 12         | 2       | 83%      | 26-27         |
| app/models/__init__.py             | 0          | 0       | 100%     |               |
| app/models/dna_sequence.py         | 13         | 0       | 100%     |               |
| app/routers.py                     | 5          | 0       | 100%     |               |
| app/services/__init__.py           | 0          | 0       | 100%     |               |
| app/services/mutant_detector.py    | 61         | 3       | 95%      | 57, 72, 81    |
| app/services/stats_service.py      | 8          | 0       | 100%     |               |
| app/test/__init__.py               | 0          | 0       | 100%     |               |
| app/test/test_mutant.py            | 13         | 0       | 100%     |               |
| app/test/test_services.py          | 22         | 0       | 100%     |               |
| **TOTAL**                          | **181**    | **14**  | **92%**  |               |

Para ejecutar las pruebas y ver el reporte de cobertura:

```bash
pytest --cov=app --cov-report=term-missing
```

## Licencia

Este proyecto está bajo la licencia MIT.

