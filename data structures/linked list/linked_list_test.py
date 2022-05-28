from linked_list import *

def main():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(12)
    linked_list.append(5)
    linked_list.remove_at(2)
    print(str(linked_list))

if __name__ == "__main__":
    main()
