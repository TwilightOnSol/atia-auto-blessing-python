# Windows Installation Guide

## 🚀 Easiest Way - Use the Installer

Simply **double-click `install.bat`** and follow the prompts. It will:
- ✅ Check for Python
- ✅ Install dependencies
- ✅ Create configuration file
- ✅ Open config editor (optional)

Then run the application with **`run.bat`**

---

## 📋 What's Included

```
atia-shrine-automated-python/
├── install.bat          ← Run this first!
├── run.bat              ← Run this to start
├── check.bat            ← Verify setup
├── SETUP.md             ← Detailed setup guide
├── QUICKSTART.md        ← Quick reference
├── README.md            ← Full documentation
├── requirements.txt     ← Python dependencies
├── privateKeys.example  ← Config template
└── src/                 ← Application code
    ├── main.py
    ├── config.py
    └── modules/atia.py
```

---

## ⚡ 3 Quick Steps

### Step 1: Install
Double-click **`install.bat`**

This will automatically:
- Check for Python 3.10+
- Install web3, schedule, colorama
- Create the `privateKeys` configuration file

### Step 2: Configure
Edit **`privateKeys`** with your wallet details

Example:
```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x...",
      "delegateeAddresses": ["0x..."]
    }
  ]
}
```

### Step 3: Run
Double-click **`run.bat`**

The application starts and runs continuously, activating blessings at 05:05 UTC daily.

---

## 🔧 Available Batch Scripts

| File | Purpose |
|------|---------|
| **install.bat** | One-time setup (dependencies, config) |
| **run.bat** | Start the application |
| **check.bat** | Verify installation |

### Run as Administrator

If you get permission errors, right-click any `.bat` file and select **"Run as administrator"**

---

## ⚙️ System Requirements

- **Windows 7** or newer
- **Python 3.10+** ([download here](https://www.python.org/downloads/))
  - **Important:** Check "Add Python to PATH" during installation!
- Internet connection (for blockchain RPC)

---

## 🐛 Troubleshooting

### Python not found?
1. Install Python from https://www.python.org/downloads/
2. **CHECK "Add Python to PATH"** ✓
3. Restart your computer
4. Run `install.bat` again

### Permission denied?
Right-click `install.bat` → **"Run as administrator"**

### Dependencies failed to install?
1. Check your internet connection
2. Run as administrator
3. Try again

### Check your setup
Run **`check.bat`** to verify everything is working

---

## 📖 Configuration Details

The `privateKeys` file uses JSON format:

**Single wallet, self-pray:**
```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x9165004be40eb157edf922afe9decec26cc930d208877b547dba58039a786e1a"
    }
  ]
}
```

**Single wallet, multiple delegatees:**
```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x9165004be40eb157edf922afe9decec26cc930d208877b547dba58039a786e1a",
      "delegateeAddresses": [
        "0x40ae3EfE4bE1Bb0402c075C0E42902Ba5B930682",
        "0x021E95f0043c4E94dd39a5cB008CF2aF2Ca187Cf"
      ]
    }
  ]
}
```

**Multiple wallets:**
```json
{
  "keys": [
    {
      "prayerPrivateKey": "0x1111...",
      "delegateeAddresses": ["0xaaaa..."]
    },
    {
      "prayerPrivateKey": "0x2222..."
    },
    {
      "prayerPrivateKey": "0x3333...",
      "delegateeAddresses": ["0xbbbb...", "0xcccc..."]
    }
  ]
}
```

---

## 🔐 Security

⚠️ **IMPORTANT:**
- Keep `privateKeys` file **private** and **secure**
- Don't share it with anyone
- Don't commit it to git
- Consider an encrypted volume
- This file contains your wallet's private keys!

---

## 📊 How It Works

1. **Loads** your wallet configuration from `privateKeys`
2. **Connects** to Ronin Chain blockchain
3. **Schedules** blessings for 05:05 UTC daily
4. **Activates** blessings for configured addresses
5. **Logs** all activity to console

The app runs continuously in the background once started.

---

## ❓ Need Help?

1. Read **SETUP.md** for detailed instructions
2. Read **QUICKSTART.md** for quick reference
3. Run **check.bat** to diagnose issues
4. Check **README.md** for full documentation

---

## ✅ Success Indicators

When you run `run.bat`, you should see:

```
============================================
  Atia's Blessing Automation
============================================

Starting Atia's Blessing automation...
Runs daily at 05:05 UTC

Press Ctrl+C to stop the application
```

If you see this, you're ready to go! The app will activate blessings automatically.

---

**Enjoy! 🙏**
