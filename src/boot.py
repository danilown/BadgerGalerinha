try:
    open("main.py", "r")
except OSError:
    with open("main.py", "w") as f:
        f.write("import launcher")
        f.flush()