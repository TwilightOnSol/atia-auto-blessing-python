"""Color utilities for console output."""

from typing import List, Optional


class RedColors:
    """Red color codes using ANSI escape sequences."""

    # ANSI color codes
    RED = "\033[38;5;196m"
    RESET = "\033[0m"

    @staticmethod
    def colorize(text: str) -> str:
        """Apply red color to text."""
        return f"{RedColors.RED}{text}{RedColors.RESET}"


class RainbowColors:
    """Rainbow color codes using ANSI escape sequences."""

    # ANSI color codes (256-color mode)
    RED = "\033[38;5;196m"
    ORANGE = "\033[38;5;214m"
    YELLOW = "\033[38;5;226m"
    GREEN = "\033[38;5;46m"
    CYAN = "\033[38;5;51m"
    BLUE = "\033[38;5;21m"
    MAGENTA = "\033[38;5;201m"
    RESET = "\033[0m"

    COLORS = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    @staticmethod
    def rainbow_text(text: str, cycle: bool = False) -> str:
        """
        Apply rainbow gradient to text.

        Args:
            text: Text to colorize
            cycle: If True, cycle through colors. If False, apply gradient.

        Returns:
            Colorized text with ANSI codes
        """
        colored = []
        colors = RainbowColors.COLORS

        for i, char in enumerate(text):
            if char == " ":
                colored.append(char)
            else:
                color = colors[i % len(colors)]
                colored.append(f"{color}{char}{RainbowColors.RESET}")

        return "".join(colored)

    @staticmethod
    def rainbow_gradient(text: str) -> str:
        """Apply smooth rainbow gradient to text."""
        return RainbowColors.rainbow_text(text, cycle=False)

    @staticmethod
    def get_color(index: int) -> str:
        """Get a color by index, cycling through rainbow."""
        return RainbowColors.COLORS[index % len(RainbowColors.COLORS)]


def colorize_output(text: str) -> str:
    """Apply red color to output text."""
    return RedColors.colorize(text)
