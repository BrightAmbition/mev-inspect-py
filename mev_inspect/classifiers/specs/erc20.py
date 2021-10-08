from mev_inspect.schemas.classified_traces import DecodedCallTrace
from mev_inspect.schemas.classifiers import (
    ClassifierSpec,
    TransferClassifier,
)
from mev_inspect.schemas.transfers import ERC20Transfer


class ERC20TransferClassifier(TransferClassifier):
    @staticmethod
    def get_transfer(trace: DecodedCallTrace) -> ERC20Transfer:
        return ERC20Transfer(
            block_number=trace.block_number,
            transaction_hash=trace.transaction_hash,
            trace_address=trace.trace_address,
            amount=trace.inputs["amount"],
            to_address=trace.inputs["recipient"],
            from_address=trace.inputs.get("sender", trace.from_address),
            token_address=trace.to_address,
        )


ERC20_SPEC = ClassifierSpec(
    abi_name="ERC20",
    classifiers={
        "transferFrom(address,address,uint256)": ERC20TransferClassifier,
        "transfer(address,uint256)": ERC20TransferClassifier,
    },
)

ERC20_CLASSIFIER_SPECS = [ERC20_SPEC]
