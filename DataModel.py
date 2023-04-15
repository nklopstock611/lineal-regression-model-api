from pydantic import BaseModel

class DataModel(BaseModel):
    selling_price: int
    year: float
    km_driven: float
    max_power: float
    transmission: str

    def columns(self):
        return ['selling_price', 'year', 'km_driven', 'max_power', 'transmission']
