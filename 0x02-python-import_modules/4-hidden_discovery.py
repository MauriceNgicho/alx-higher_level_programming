#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)   # Get all hidden names

    # Filter out names starting with '__"
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort name in alphabetic order and print in a new line
    for name in sorted(filtered_names):
        print(name)
