from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    selling_price: int
    year: float
    km_driven: float
    max_power: float
    transmission: str

# Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ['selling_price', 'year', 'km_driven', 'max_power', 'transmission']