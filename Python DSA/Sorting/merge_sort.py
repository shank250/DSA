class MySort:
    def __init__(self, list = []) -> None:
        self.list = list

    def mergeSort(self, list):
        if(len(list) <= 1):
            return list

        l1 = self.mergeSort(list[:len(list)//2])
        l2 = self.mergeSort(list[len(list)//2:])

        return self.merge(l1, l2)

    def merge(self, l1, l2):

        p1, p2 = 0, 0
        lfinal = []

        while(p1 < len(l1) and p2 < len(l2)):
            if l1[p1] <= l2[p2]:
                lfinal.append(l1[p1])
                p1 += 1
            else:
                lfinal.append(l2[p2])
                p2 += 1
        
        if p1 == len(l1):
            while(p2 < len(l2)):
                lfinal.append(l2[p2])
                p2 += 1
        else:
            while(p1 < len(l1)):
                lfinal.append(l1[p1])
                p1 += 1
        
        return lfinal
    

lst = [2,3,5,61,4,5]
soorting = MySort(lst)
asn = soorting.mergeSort(lst)
print(asn)