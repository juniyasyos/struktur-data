from linked_list import *

def soal5_1():
    linked_try = LinkedList()
    linked_try.insert_at_start(1)
    linked_try.insert_at_start(2)
    linked_try.insert_at_start(3)
    linked_try.insert_at_start(4)
    
    print("\nBerikut list yang sudah dibuat:")
    linked_try.traverse_list()

    length = linked_try.get_length()
    print("Panjang linked list adalah:", length)

def soal5_2():
    linked_try = LinkedList()
    linked_try.insert_at_start(1)
    linked_try.insert_at_start(2)
    linked_try.insert_at_start(3)
    linked_try.insert_at_end(4)
    
    print("\nBerikut list yang sudah dibuat:")
    linked_try.traverse_list()

    total = linked_try.calculate_sum()
    print("Jumlah semua bilangan dalam linked list adalah:", total)

def soal5_3():
    linked_try = LinkedList()
    linked_try.insert_at_start(1)
    linked_try.insert_at_start(2)
    linked_try.insert_at_start(3)
    linked_try.insert_at_start(4)
    
    print("\nBerikut list 1 yang sudah dibuat:")
    linked_try.traverse_list()

    linked_other = LinkedList()
    linked_other.insert_at_start(5)
    linked_other.insert_at_start(6)
    linked_other.insert_at_start(7)
    linked_other.insert_at_start(8)
    
    print("\nBerikut list 2 yang sudah dibuat:")
    linked_other.traverse_list()

    linked_try.concatenate(linked_other,append_other_first=True)
    
    print("\nBerikut list yang sudah digabung:")
    linked_try.traverse_list()

def soal5_4():
    linked_try = LinkedList()
    linked_try.insert_at_start(1)
    linked_try.insert_at_start(2)
    linked_try.insert_at_start(3)
    linked_try.insert_at_start(4)
    
    print("\nBerikut list 1 yang sudah dibuat:")
    linked_try.traverse_list()

    linked_other = LinkedList()
    linked_other.insert_at_start(5)
    linked_other.insert_at_start(6)
    linked_other.insert_at_start(7)
    linked_other.insert_at_start(8)
    
    print("\nBerikut list 2 yang sudah dibuat:")
    linked_other.traverse_list()

    linked_try.concatenate(linked_other,append_other_first=True)
    
    print("\nBerikut list yang sudah digabung:")
    linked_try.traverse_list()

    print("\nBerikut list yang sudah urutkan:")
    linked_try.sorted_list()

    linked_try.traverse_list()

def soal5_5():
    linked_try = LinkedList()
    linked_try.insert_at_start(1)
    linked_try.insert_at_start(2)
    linked_try.insert_at_start(3)
    linked_try.insert_at_start(4)
    
    print("\nBerikut list yang sudah dibuat:")
    linked_try.traverse_list()

    linked_try.reverse_list()

    print("\nBerikut list yang sudah di balik:")
    linked_try.traverse_list()

# soal5_1()
# soal5_2()
# soal5_3()
# soal5_4()
# soal5_5()