import sys

def pass_input(prompt="Password: "):
    if sys.platform == "win32":
        return _pass_input_win(prompt)
    else:
        return _pass_input_unix(prompt)

def _pass_input_win(prompt):
    import msvcrt
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getwch()
        if ch in ("\r", "\n"):
            print()
            break
        elif ch == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += ch
            print("*", end="", flush=True)
    return password

def _pass_input_unix(prompt):
    import tty
    import termios
    print(prompt, end="", flush=True)
    password = ""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch in ("\r", "\n"):
                print()
                break
            elif ch == "\x7f":  # Backspace on Unix sends DEL
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            elif ch == "\x03":  # Ctrl+C
                raise KeyboardInterrupt
            else:
                password += ch
                print("*", end="", flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return password