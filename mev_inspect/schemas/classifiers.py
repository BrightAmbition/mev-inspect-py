from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Type

from pydantic import BaseModel

from .classified_traces import Classification, DecodedCallTrace, Protocol
from .transfers import ERC20Transfer


class Classifier(ABC):
    @staticmethod
    @abstractmethod
    def get_classification() -> Classification:
        pass


class TransferClassifier(Classifier):
    @staticmethod
    def get_classification() -> Classification:
        return Classification.transfer

    @staticmethod
    @abstractmethod
    def get_transfer(trace: DecodedCallTrace) -> ERC20Transfer:
        pass


class SwapClassifier(Classifier):
    @staticmethod
    def get_classification() -> Classification:
        return Classification.swap


class LiquidationClassifier(Classifier):
    @staticmethod
    def get_classification() -> Classification:
        return Classification.liquidate


class ClassifierSpec(BaseModel):
    abi_name: str
    protocol: Optional[Protocol] = None
    valid_contract_addresses: Optional[List[str]] = None
    classifiers: Dict[str, Type[Classifier]] = {}
