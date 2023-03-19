class MyAttributeClass(object):
    def __init__(self, **kwargs) -> None:
        self.count = 0
        for key, val in kwargs.items():
            setattr(self,key,val)
            self.count+=1

    def __len__(self) -> int:
        return self.count


if __name__ == '__main__':
    fptr = open('abc.txt', 'a')
    n = int(input())
    my_dict = {}
    keys = []
    for i in range(n):
        k, v = input().split()
        keys.append(k)
        my_dict[k] = v
    class_object = MyAttributeClass(**my_dict)
    for k, v in my_dict.items():
        assert my_dict[k] == class_object.__getattribute__(k)
    for i in keys:
        fptr.write(f"{i}: {class_object.__getattribute__(i)}\n")
    fptr.write(f"Count of attributes: {len(class_object)}\n")
