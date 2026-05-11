"""Atia's Blessing smart contract interaction module."""

from typing import Dict, Any
from web3 import Web3
from eth_account import Account

from ..config import get_keys
from ..colors import RedColors

RPC = "https://api.roninchain.com/rpc"
CHAIN_ID = 2020
PREFIX = "Atia's Blessing"

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(RPC))

# Smart contract ABI
ATIA_ABI = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
        ],
        "name": "activateStreak",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
        ],
        "name": "getStreak",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "currentStreakCount",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "lastActivated",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "longestStreakCount",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "lostStreakCount",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
        ],
        "name": "getActivationStatus",
        "outputs": [
            {
                "internalType": "bool",
                "name": "isLostStreak",
                "type": "bool",
            },
            {
                "internalType": "bool",
                "name": "hasPrayedToday",
                "type": "bool",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
]

ATIA_CONTRACT_ADDRESS = Web3.to_checksum_address("0x9d3936dbd9a794ee31ef9f13814233d435bd806c")
atia_contract = w3.eth.contract(address=ATIA_CONTRACT_ADDRESS, abi=ATIA_ABI)


def check_blessings() -> None:
    """Main function to check and activate blessings for all configured addresses."""
    keys = get_keys("keys")
    header = f"Starting {PREFIX} daily pray ({len(keys)} addr)"
    print(f"{RedColors.RED}⚙️ {header}{RedColors.RESET}")

    for key in keys:
        if not key.get("prayerPrivateKey"):
            print(f"{RedColors.RED}⚠️ {PREFIX}: No private key found!{RedColors.RESET}")
            print(key)
            return

        # Create wallet from private key
        account = Account.from_key(key["prayerPrivateKey"])
        signer_address = account.address

        # Set delegatee addresses
        delegatee_addresses = key.get("delegateeAddresses")
        if not delegatee_addresses:
            delegatee_addresses = [signer_address]

        if len(delegatee_addresses) > 5:
            print(
                f"{RedColors.RED}❌ {PREFIX}: Too much delegatees for prayer "
                f"{signer_address[-4:]}{RedColors.RESET}"
            )
            return

        for delegatee in delegatee_addresses:
            activation_result = is_activated(delegatee)
            if activation_result["status"]:
                msg = f"{PREFIX}: Already activated for {delegatee[-4:]} (streak: {activation_result['streak']})"
                print(f"{RedColors.RED}⏱️ {msg}{RedColors.RESET}")
            else:
                streak_result = activate_streak(account, delegatee)
                if streak_result["status"]:
                    msg = f"{PREFIX}: Activated for {delegatee[-4:]} (streak: {streak_result['streak']})"
                    print(f"{RedColors.RED}✅ {msg}{RedColors.RESET}")


def is_activated(address: str) -> Dict[str, Any]:
    """Check if an address has already activated their blessing today.

    Args:
        address: The wallet address to check

    Returns:
        Dictionary with 'status' (bool) and 'streak' (int)
    """
    try:
        current_streak_count = atia_contract.functions.getStreak(address).call()[0]
        _, has_prayed_today = atia_contract.functions.getActivationStatus(
            address
        ).call()
        return {"status": has_prayed_today, "streak": int(current_streak_count)}
    except Exception as e:
        print(f"{RainbowColors.ORANGE}⚠️ {PREFIX}: Error checking activation status: {e}{RainbowColors.RESET}")
        return {"status": False, "streak": 0}


def activate_streak(account: Account, delegatee: str) -> Dict[str, Any]:
    """Activate the blessing streak for a delegatee address.

    Args:
        account: The signer account (from private key)
        delegatee: The address to activate blessing for

    Returns:
        Dictionary with 'status' (bool) and optional 'streak' (int)
    """
    try:
        current_streak_count = atia_contract.functions.getStreak(delegatee).call()[0]

        # Build and send transaction
        tx_data = atia_contract.functions.activateStreak(delegatee).build_transaction(
            {
                "from": account.address,
                "nonce": w3.eth.get_transaction_count(account.address),
                "gas": 100000,
                "gasPrice": w3.eth.gas_price,
                "chainId": CHAIN_ID,
            }
        )

        signed_tx = w3.eth.account.sign_transaction(tx_data, account.key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        return {"status": True, "streak": int(current_streak_count) + 1}
    except Exception as e:
        error_msg = str(e)
        msg = f"{PREFIX}: Failed to pray for {delegatee[-4:]} {error_msg}"
        print(f"{RainbowColors.RED}⚠️ {RainbowColors.rainbow_text(msg)}{RainbowColors.RESET}")
        return {"status": False}
