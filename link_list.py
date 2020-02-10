class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_ll(pHead):
    if not pHead:
        print('链表为空')
    else:
        p1 = pHead
        while p1:
            print(p1.val, end='->') if p1.next else print(p1.val, end='')
            p1 = p1.next
    return 

def create_ll(_list):
    if not _list:
        return None
    else:
        p_res = p1 = ListNode(0)
        for x in _list:
            temp = ListNode(x)
            p1.next = temp
            p1 = p1.next
    return p_res.next

