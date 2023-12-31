# 6-6 链表最大值-Python
#
# 设计⼀个算法，通过⼀趟遍历确定⻓度为 n 的单链表中值最⼤的结点。
#
# 函数接口定义：
# def max(la):

class LNode:
    def __init__(self, data=None):
        self.data = data  # 结点的数据域
        self.next = None  # 结点的指针域


class LinkList:
    def __init__(self):
        # 生成新结点作为头结点并初始化指针域和数据区域为None，头指针head指向头节点
        self.head = LNode(None)

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def create_list_r(self, l_data: list):
        # 后插法，根据l_data数据列表创建链表
        r = self.head  # 尾指针r指向头结点
        for data in l_data:
            p = LNode(data)  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            r = r.next  # r指向新的尾结点p

    def show(self):
        for p in self:
            if p.data is not None:
                print(p.data, end=' ')


def max(la):
    max = la.head.next.data
    for p in la:
        if p.data is not None:
            if p.data > max:
                max = p.data
    return max


if __name__ == "__main__":
    la = LinkList()

    a = input()
    d1 = [int(x) for x in a.split()]
    la.create_list_r(d1)

    print(max(la))
