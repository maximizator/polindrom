# class MyFile:
#     def __init__(self, filename, mode, encoding='utf-8'):
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode, encoding=self.encoding)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()
#
#
# with MyFile('27.txt', 'r') as file:
#     data = file.read()
#     print(data)


class InfiniteIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += 1
        return result


for num in InfiniteIterator():
    print(num)











