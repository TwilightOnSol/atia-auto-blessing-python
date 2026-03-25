# Rainbow Color Gradient Demo

## How Rainbow Colors Work

The application uses ANSI 256-color escape sequences to display rainbow text in the console.

## Color Spectrum

```
Red → Orange → Yellow → Green → Cyan → Blue → Magenta → (repeat)
```

## Implementation

Each character in a message can be assigned a color from the rainbow. The colors cycle through:

1. **Red** (#196) - Errors, critical messages
2. **Orange** (#214) - Warnings, important info
3. **Yellow** (#226) - Highlights
4. **Green** (#46) - Success, confirmations
5. **Cyan** (#51) - Information, status
6. **Blue** (#21) - Details
7. **Magenta** (#201) - Special events

## Usage Examples

### Rainbow Text
```python
from src.colors import RainbowColors

# Apply rainbow gradient to any text
text = RainbowColors.rainbow_text("Atia's Blessing")
print(text)
```

### Individual Colors
```python
from src.colors import RainbowColors

# Use individual colors
print(f"{RainbowColors.RED}Error Message{RainbowColors.RESET}")
print(f"{RainbowColors.GREEN}Success Message{RainbowColors.RESET}")
print(f"{RainbowColors.BLUE}Info Message{RainbowColors.RESET}")
```

### Color by Index
```python
from src.colors import RainbowColors

# Get a color by cycling through the spectrum
color = RainbowColors.get_color(0)  # Red
color = RainbowColors.get_color(1)  # Orange
color = RainbowColors.get_color(2)  # Yellow
# ... and so on
```

## Application Output

### Startup Message
```
Atia's Blessing - Rainbow Colors Activated!
```
(Each character has a different color from the rainbow)

### Status Message
```
✅ Activated for 0682 (streak: 42)
```
(Entire message in green with rainbow text)

### Warning Message
```
⚠️ Error checking activation status: connection timeout
```
(Entire message in orange/yellow with rainbow text)

### Error Message
```
❌ Too much delegatees for prayer 0682
```
(Entire message in red with rainbow text)

## Color Codes Used

| ANSI Code | Color | Hex | Usage |
|-----------|-------|-----|-------|
| 38;5;196 | Red | #FF0000 | Errors |
| 38;5;214 | Orange | #FFA500 | Warnings |
| 38;5;226 | Yellow | #FFFF00 | Highlights |
| 38;5;46 | Green | #00FF00 | Success |
| 38;5;51 | Cyan | #00FFFF | Info |
| 38;5;21 | Blue | #0000FF | Details |
| 38;5;201 | Magenta | #FF00FF | Special |

## Console Support

✅ **Windows Terminal** - Full support
✅ **Windows 11** - Native ANSI support
✅ **Windows 10** - With ANSI support enabled
✅ **PowerShell 7+** - Full support
✅ **VS Code Terminal** - Full support

## Customization

To modify colors, edit `src/colors.py`:

```python
class RainbowColors:
    RED = "\033[38;5;196m"      # Edit these codes
    ORANGE = "\033[38;5;214m"   # to customize colors
    YELLOW = "\033[38;5;226m"
    GREEN = "\033[38;5;46m"
    CYAN = "\033[38;5;51m"
    BLUE = "\033[38;5;21m"
    MAGENTA = "\033[38;5;201m"
```

## Performance Impact

- Zero performance cost - ANSI codes are simple strings
- No additional dependencies required
- Works natively with Python 3.10+
- Minimal memory overhead

## Visual Examples

### Before (Plain Text)
```
Starting Atia's Blessing daily pray (3 addr)
Already activated for 0682 (streak: 42)
Activated for 87Cf (streak: 15)
Failed to pray for ebae insufficient funds
```

### After (Rainbow Colors)
```
[GREEN with rainbow]✅ Starting Atia's Blessing daily pray (3 addr)
[CYAN with rainbow]⏱️ Already activated for 0682 (streak: 42)
[GREEN with rainbow]✅ Activated for 87Cf (streak: 15)
[RED with rainbow]⚠️ Failed to pray for ebae insufficient funds
```

Each character has its own color from the rainbow spectrum!

## Features

✅ Automatic color cycling
✅ Emoji support
✅ Multi-line text support
✅ Graceful fallback if colors not supported
✅ No external dependencies
✅ Works on Windows, Linux, macOS
✅ Respects RESET codes
✅ Customizable color palette
