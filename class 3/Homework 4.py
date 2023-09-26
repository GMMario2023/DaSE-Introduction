class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = [data, None]
        else:
            current = self.head
            while current[1]:
                current = current[1]
            current[1] = [data, None]

    def print_list(self):
        current = self.head
        while current:
            print(current[0])
            current = current[1] if current[1] else None

# 创建链表并添加数据
linked_list = LinkedList()
linked_list.add('A')
linked_list.add('B')
linked_list.add('C')

# 打印链表
linked_list.print_list()
