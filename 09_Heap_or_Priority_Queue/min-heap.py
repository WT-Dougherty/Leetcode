class MinHeap:
    def __init__(self):
        self.h = []

    def heapifyUp(self):
        i = len(self.h) - 1
        while i != 0 and self.h[i] < self.h[self.parent(i)]:
            if not self.swap(i, i // 2):
                raise Exception
            i = self.parent(i)

    def heapifyDown(self):
        i = 0
        while True:
            l, r = i * 2 + 1, i * 2 + 2

            # condition: at the bottom
            if r >= len(self.h):
                if l >= len(self.h):
                    return
                else:
                    if self.h[i] < self.h[l]:
                        return
                    else:
                        self.swap(i, l)
                        return

            if self.h[l] <= self.h[r]:
                min_child = l
            else:
                min_child = r

            if self.h[i] < self.h[min_child]:
                return
            self.swap(i, min_child)
            i = min_child

    def add(self, num: int):
        self.h.append(num)
        self.heapifyUp()

    def removeMin(self) -> int:
        if len(self.h) == 1:
            return self.h.pop()
        else:
            self.swap(0, len(self.h) - 1)
            rv = self.h.pop()
            self.heapifyDown()
            return rv

    def getMin(self) -> int:
        if len(self.h) == 0:
            return None
        else:
            return self.h[0]

    # functions to heap with heapify
    def swap(self, i1: int, i2: int) -> bool:
        if 0 <= i1 < len(self.h) and 0 <= i2 < len(self.h):
            self.h[i1], self.h[i2] = self.h[i2], self.h[i1]
            return True
        else:
            return False

    @staticmethod
    def parent(i: int) -> int:
        if i % 2 == 1:
            return i // 2
        else:
            return i // 2 - 1


# -----------------------
# Inline tests
# -----------------------


def test_get_min_on_empty_returns_none():
    h = MinHeap()
    assert h.getMin() is None


def test_add_and_get_min():
    h = MinHeap()
    h.add(5)
    h.add(3)
    h.add(7)
    assert h.getMin() == 3


def test_remove_min_sequence_sorted_order():
    h = MinHeap()
    values = [5, 3, 8, 1, 2]
    for v in values:
        h.add(v)

    popped = [h.removeMin() for _ in range(len(values))]
    assert popped == sorted(values)
    assert h.getMin() is None


def test_remove_min_single_element():
    h = MinHeap()
    h.add(10)
    assert h.removeMin() == 10
    assert h.getMin() is None


def test_duplicates_preserved_in_order():
    h = MinHeap()
    for v in [2, 1, 2, 1]:
        h.add(v)
    popped = [h.removeMin() for _ in range(4)]
    assert popped == [1, 1, 2, 2]


def test_swap_and_parent_helpers():
    h = MinHeap()
    assert h.swap(0, 10) is False
    assert MinHeap.parent(1) == 0
    assert MinHeap.parent(2) == 0
    assert MinHeap.parent(3) == 1
    assert MinHeap.parent(4) == 1


def run_inline_tests():

    current_globals = globals()
    tests = [
        current_globals[n] for n in sorted(current_globals) if n.startswith("test_")
    ]
    failures = 0

    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL: {t.__name__} - AssertionError: {e}")
        except Exception as e:
            failures += 1
            print(f"ERROR: {t.__name__} - {type(e).__name__}: {e}")

    print("---")
    if failures == 0:
        print("All inline tests passed")
        return 0
    else:
        print(f"{failures} test(s) failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(run_inline_tests())
