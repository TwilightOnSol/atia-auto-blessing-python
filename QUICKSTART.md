# Quick Start Guide

## Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup configuration
cp privateKeys.example privateKeys
```

## Configuration

Edit `privateKeys` with your wallet details:

```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x...",
      "delegateeAddresses": ["0x...", "0x..."]
    }
  ]
}
```

## Run

```bash
python src/main.py
```

The application runs continuously and activates blessings daily at **05:05 UTC**.

## Project Structure

```
.
├── src/
│   ├── main.py          # Entry point & scheduler
│   ├── config.py        # Configuration management
│   └── modules/
│       └── atia.py      # Blockchain interaction
├── requirements.txt     # Python dependencies
├── README.md           # Full documentation
├── privateKeys.example # Config template
└── LICENSE
```

## Requirements

- Python 3.10+
- pip

## What It Does

- Loads wallet configuration from `privateKeys` file
- Connects to Ronin Chain RPC
- Checks daily blessing status at 05:05 UTC
- Activates blessings for configured addresses
- Supports delegating prayers to up to 5 addresses per wallet
