from colorama import Fore, Back, Style, init
init()

def forecolor(text: str, color: str, style: str = "NORMAL"):
    """
    * Color Print Foreground — prints text with a foreground (text) color
    ? color options: black, red, green, yellow, blue, magenta, cyan, white
    ? style options: normal, bright, dim
    ! resets style after print to avoid bleeding into next print
    """
    return(getattr(Style, style.upper()) + getattr(Fore, color.upper()) + text + Style.RESET_ALL)

def backcolor(text: str, color: str, style: str = "NORMAL"):
    """
    * Color Print Background — prints text with a background color
    ? color options: black, red, green, yellow, blue, magenta, cyan, white
    ? style options: normal, bright, dim
    ! resets style after print to avoid bleeding into next print
    """
    return(getattr(Style, style.upper()) + getattr(Back, color.upper()) + text + Style.RESET_ALL)