# 6-5 链表分解-Python
#
# 设计算法将⼀个带头结点的单链表 A 分解为两个具有相同结构的链表 B 和 C，其中 B 表的结点为 A 表中值⼩于零的结点，⽽ C 表的结点为 A 表中值⼤于零的结点（链表 A 中的元素 为⾮零整数，要求 B、C 表利⽤ A 表的结点）。
#
# 函数接口定义：
# def decompose(la):

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

def decompose(la):
    pa = la.head.next
    lb = LinkList()
    lc = LinkList()
    lb.head.next = None
    lc.head.next = None
    pb = lb.head
    pc = lc.head

    while pa is not None:
        q = pa.next
        if pa.data < 0:
            pa.next = pb.next
            pb.next = pa
        elif pa.data > 0:
            pa.next = pc.next
            pc.next = pa
        pa = q

    return lb, lc

if __name__ == "__main__":
    la = LinkList()
    lb = LinkList()
    lc = LinkList()

    a = input()
    d1 = [int(x) for x in a.split()]

    la.create_list_r(d1)

    lb, lc = decompose(la)

    lb.show()
    lc.show()