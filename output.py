grey = "\x1b[38;20m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"


def print_custom(log_type, text):
    if log_type == "info":
        print(grey + text + reset)
    if log_type == "warn":
        print(yellow + text + reset)
    if log_type == "error":
        print(red + text + reset)
