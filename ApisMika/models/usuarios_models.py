from datetime import date
from pydantic import BaseModel
from typing import Optional, Any

class UsuariosBase(BaseModel):
    nombre: str
    apellidopaterno: str
    apellidomaterno: str
    correo: str
    telefono: str
    rol_id: int
    sucursal_id: int
    passwordhash: str
    habilitado: bool
    fecha_nacimiento: date

class UsuariosCreate(UsuariosBase):
    pass

class UsuariosUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidopaterno: Optional[str] = None
    apellidomaterno: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    rol_id: Optional[int] = None
    sucursal_id: Optional[int] = None
    passwordhash: Optional[str] = None
    habilitado: Optional[bool] = None
    fecha_nacimiento: Optional[date] = None

class PatchField(BaseModel):
    column: str
    value: Any