import logging
from typing import Any

from erdpy import cli_contracts, cli_shared, facade, proxy
from erdpy.facade import get_transaction_cost

logger = logging.getLogger("cli.cost")


def setup_parser(subparsers: Any) -> Any:
    parser = cli_shared.add_group_subparser(subparsers, "cost", "Estimate cost of Transactions")
    subparsers = parser.add_subparsers()

    sub = cli_shared.add_command_subparser(subparsers, "cost", "gas-price", "Query minimum gas price")
    cli_shared.add_proxy_arg(sub)
    sub.set_defaults(func=get_gas_price)

    sub = cli_shared.add_command_subparser(subparsers, "cost", "tx-transfer", "Query cost of regular transaction (transfer)")
    cli_shared.add_proxy_arg(sub)
    sub.add_argument("--data", required=True, help="a transaction payload, required to estimate the cost")
    sub.set_defaults(func=lambda args: get_transaction_cost(args, proxy.TxTypes.MOVE_BALANCE))

    sub = cli_shared.add_command_subparser(subparsers, "cost", "sc-deploy", "Query cost of Smart Contract deploy transaction")
    cli_shared.add_proxy_arg(sub)
    cli_contracts._add_project_or_bytecode_arg(sub)
    cli_contracts._add_arguments_arg(sub)
    sub.set_defaults(func=lambda args: get_transaction_cost(args, proxy.TxTypes.SC_DEPLOY))

    sub = cli_shared.add_command_subparser(subparsers, "cost", "sc-call", "Query cost of Smart Contract call transaction")
    cli_shared.add_proxy_arg(sub)
    cli_contracts._add_contract_arg(sub)
    cli_contracts._add_function_arg(sub)
    cli_contracts._add_arguments_arg(sub)
    sub.set_defaults(func=lambda args: get_transaction_cost(args, proxy.TxTypes.SC_CALL))

    parser.epilog = cli_shared.build_group_epilog(subparsers)
    return subparsers


def get_gas_price(args: Any):
    facade.get_gas_price(args)
