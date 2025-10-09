sq = StackQueue()

# Stack usage
sq.push(10)
sq.push(20)
sq.push(30)
print("Stack after pushes:", sq)   # [10, 20, 30]
print("Pop:", sq.pop())            # 30
print("Peek (stack):", sq.peek())  # 20

# Queue usage
sq.enqueue(40)
sq.enqueue(50)
print("Queue after enqueues:", sq) # [10, 20, 40, 50]
print("Dequeue:", sq.dequeue())    # 10
print("Peek (queue):", sq.peek())  # 50 (stack style), but front is 20

