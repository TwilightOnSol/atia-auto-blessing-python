#!/usr/bin/env python
"""Rainbow Color Demo - Visual showcase of the color system."""

from src.colors import RainbowColors

def demo():
    """Display a colorful demonstration of the rainbow system."""

    print("\n" + "="*70)
    print("RAINBOW COLOR SYSTEM DEMONSTRATION")
    print("="*70 + "\n")

    # Title
    title = "Atia's Blessing - Rainbow Colors"
    print(f"🌈 {RainbowColors.rainbow_text(title)}")
    print()

    # Color palette
    print("COLOR PALETTE:")
    print("-" * 70)
    colors_demo = [
        (RainbowColors.RED, "Red", "Errors & Critical Alerts"),
        (RainbowColors.ORANGE, "Orange", "Warnings & Important Info"),
        (RainbowColors.YELLOW, "Yellow", "Highlights & Emphasis"),
        (RainbowColors.GREEN, "Green", "Success & Confirmations"),
        (RainbowColors.CYAN, "Cyan", "Information & Status"),
        (RainbowColors.BLUE, "Blue", "Details & Data"),
        (RainbowColors.MAGENTA, "Magenta", "Special Events & Updates"),
    ]

    for color, name, usage in colors_demo:
        text = f"{name:10} - {usage}"
        print(f"{color}{text}{RainbowColors.RESET}")

    print()
    print("-" * 70)
    print()

    # Gradient examples
    print("GRADIENT TEXT EXAMPLES:")
    print("-" * 70)

    examples = [
        "Success! Transaction confirmed on blockchain",
        "Warning! Low wallet balance detected",
        "Error! Connection to RPC server failed",
        "Processing daily blessing activation",
        "Atias Blessing automation system",
        "Rainbow colors make console output beautiful",
        "Welcome to the Python edition",
    ]

    for example in examples:
        colored = RainbowColors.rainbow_text(example)
        print(f"  {colored}")

    print()
    print("-" * 70)
    print()

    # Message types
    print("APPLICATION MESSAGE TYPES:")
    print("-" * 70)

    success_msg = f"{RainbowColors.GREEN}✅ {RainbowColors.rainbow_text('Blessed successfully activated')}{RainbowColors.RESET}"
    info_msg = f"{RainbowColors.CYAN}⏱️ {RainbowColors.rainbow_text('Already activated for this address')}{RainbowColors.RESET}"
    warning_msg = f"{RainbowColors.ORANGE}⚠️ {RainbowColors.rainbow_text('Error checking blessing status')}{RainbowColors.RESET}"
    error_msg = f"{RainbowColors.RED}❌ {RainbowColors.rainbow_text('Too many delegatees configured')}{RainbowColors.RESET}"

    print(f"\n{success_msg}")
    print(f"{info_msg}")
    print(f"{warning_msg}")
    print(f"{error_msg}")

    print()
    print("-" * 70)
    print()

    # Statistics
    print("COLOR SYSTEM STATISTICS:")
    print("-" * 70)
    print(f"  Total Colors:        {len(RainbowColors.COLORS)}")
    print(f"  Color Cycling:       Automatic (loops through spectrum)")
    print(f"  ANSI Mode:           256-color (3-bit + 8-bit)")
    print(f"  Performance Impact:  None (pure string operations)")
    print(f"  Console Compatibility: Windows 10+, WSL, PowerShell 7+")

    print()
    print("-" * 70)
    print()

    # Footer
    footer = "Rainbow Colors Enabled - All Systems Go!"
    print(f"✨ {RainbowColors.rainbow_text(footer)} ✨")

    print()
    print("="*70)
    print()

if __name__ == "__main__":
    demo()
