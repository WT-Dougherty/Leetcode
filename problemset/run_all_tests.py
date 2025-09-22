import importlib, os, sys

def main():
    folder = os.path.dirname(__file__)
    files = [f for f in os.listdir(folder) if f.endswith(".py") and f[:2].isdigit()]
    files.sort()
    ok = True
    for f in files:
        print(f"Running {f} ...", end=" ")
        mod = importlib.import_module(f"{os.path.splitext(f)[0]}")
        # running module executes tests in __main__ only,
        # so call its _test() if present:
        if hasattr(mod, "_test"):
            try:
                mod._test()
                print("OK")
            except AssertionError as e:
                ok = False
                print("FAIL")
                raise
        else:
            print("No _test found, skipping")
    if ok:
        print("All tests passed!")

if __name__ == "__main__":
    # ensure package import from current dir
    sys.path.insert(0, os.path.dirname(__file__))
    main()