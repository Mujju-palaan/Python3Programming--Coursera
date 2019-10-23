import test

test.testEqual(sorted([1, 7, 4]), [1, 4, 7])
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])
