from typing import Optional
import asyncio
import httpx
from sqlmodel import SQLModel
from pydantic import BaseModel

# Modelo de Exoplaneta (ahora permite valores nulos en los campos numéricos)
class Exoplanet(BaseModel):
    pl_name: str
    disc_year: int
    pl_orbper: Optional[float]  # Este campo puede ser None
    pl_bmassj: Optional[float]  # Este campo puede ser None

# Función para obtener datos de la NASA Exoplanet Archive
async def fetch_exoplanets():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    query = """
    SELECT pl_name, disc_year, pl_orbper, pl_bmassj
    FROM ps
    WHERE disc_year >= 2020
    AND ROWNUM <= 5
    """
    params = {
        "query": query,
        "format": "json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            return []
        
        try:
            data = response.json()
        except ValueError:
            print("La respuesta no es JSON válida. Contenido de la respuesta:")
            print(response.text)
            return []

        return [Exoplanet(**row) for row in data]

# Función principal que ejecuta la consulta
async def main():
    exoplanets = await fetch_exoplanets()
    for planet in exoplanets:
        print(f"Nombre: {planet.pl_name}, Año de descubrimiento: {planet.disc_year}, "
              f"Periodo orbital (días): {planet.pl_orbper}, Masa (Júpiter): {planet.pl_bmassj}")

if __name__ == "__main__":
    asyncio.run(main())
