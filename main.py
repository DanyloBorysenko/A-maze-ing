try:
    int("a")
except Exception as e:
    print(f"{type(e).__name__}")