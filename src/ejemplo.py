from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass
class Resultado:
    media: float
    desvio: float

def resumen_columna(df: pd.DataFrame, columna: str) -> Resultado:
    """Devuelve media y desviación estándar de una columna numérica."""
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe")
    serie = pd.to_numeric(df[columna], errors="coerce").dropna()
    return Resultado(media=float(np.mean(serie)), desvio=float(np.std(serie, ddof=1)))