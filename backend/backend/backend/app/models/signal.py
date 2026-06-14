from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, ConfigDict

class SignalSeverity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SignalBase(BaseModel):
    # Identificação e Rastreabilidade
    tenant_id: str = Field(..., description="ID do cliente/organização (Multi-tenancy desde o dia 1)")
    source_system: str = Field(..., example="ERP-TOTVS", description="Sistema de origem do sinal")
    signal_type: str = Field(..., example="inventory.rupture", description="Tipo/Categoria do sinal para indexação")
    
    # Gravidade do Sinal Fraco
    severity: SignalSeverity = Field(default=SignalSeverity.INFO, description="Nível de severidade inicial mapeado")
    
    # Carga Útil (Onde entram os dados variáveis da operação)
    payload: Dict[str, Any] = Field(
        ..., 
        example={"product_id": "123", "stock_level": 0, "min_required": 15},
        description="Dados brutos e contextuais do evento operacional"
    )

class SignalCreate(SignalBase):
    pass

class SignalInDB(SignalBase):
    id: str = Field(..., description="UUID único do sinal gerado pelo MasterSolver-OS")
    timestamp_received: datetime = Field(default_factory=datetime.utcnow, description="Data/Hora exata da ingestão no ecossistema")
    
    # Configuração do Pydantic v2
    model_config = ConfigDict(from_attributes=True)

