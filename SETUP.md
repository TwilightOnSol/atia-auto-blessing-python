# Windows Setup Guide

## Quick Start (Recommended)

1. **Double-click `install.bat`** to automatically:
   - Check for Python installation
   - Install all required dependencies
   - Create the configuration file
   - Optionally open the config file in Notepad

2. **Edit `privateKeys`** with your wallet private keys (if not done in step 1)

3. **Double-click `run.bat`** to start the automation

## Manual Setup (Alternative)

```bash
# Install dependencies
pip install -r requirements.txt

# Copy configuration template
copy privateKeys.example privateKeys

# Edit privateKeys with your wallet keys

# Run the application
python src/main.py
```

## Scripts Included

| Script | Purpose |
|--------|---------|
| `install.bat` | One-time setup (installs dependencies, creates config) |
| `run.bat` | Runs the application |
| `check.bat` | Verifies all dependencies and configuration |

## Configuration

Edit the `privateKeys` file with your wallet details:

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

**Example with multiple wallets:**

```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x1234...",
      "delegateeAddresses": ["0xaaaa...", "0xbbbb..."]
    },
    {
      "prayerPrivateKey": "0x5678..."
    }
  ]
}
```

## Requirements

- **Windows 7** or later
- **Python 3.10+** ([Download](https://www.python.org/downloads/))
  - During installation, **check "Add Python to PATH"**

## Troubleshooting

### "Python is not installed"
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart your computer after installing

### "Failed to install dependencies"
- Check your internet connection
- Try running `install.bat` as Administrator (right-click → Run as administrator)
- Check if you have write permissions in the folder

### "privateKeys file not found"
- Run `install.bat` again to create it
- Or manually copy `privateKeys.example` to `privateKeys`

### Application won't start
- Run `check.bat` to diagnose the issue
- Make sure `privateKeys` file exists and contains valid keys
- Check that the file is not read-only

## How It Works

- The application runs continuously
- At **05:05 UTC** every day, it checks and activates blessings
- Supports multiple wallets with up to 5 delegatees each
- Connects to Ronin Chain blockchain
- All transactions are logged to console

## Support

For issues or questions:
- Check the `README.md` file
- Run `check.bat` to verify your setup
- Ensure your `privateKeys` file has the correct format

## ⚠️ Security Warning

- **Keep `privateKeys` file private and secure**
- Don't share it with anyone
- Consider storing it on an encrypted volume
- Never commit it to version control
