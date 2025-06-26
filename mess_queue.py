
import random

# Queue-related terms and templates
queue_operations = [
    "enqueue", "dequeue", "peek", "isEmpty", "isFull",
    "size", "clear", "front", "rear"
]

data_types = [
    "integers", "characters", "strings", "customer IDs",
    "tasks", "print jobs", "URLs", "sensor readings", "tickets"
]

difficulty_levels = ["Easy", "Medium", "Hard"]


queue_topics = {
    "Queue": {
        "subtopics": {
            "Introduction": {
                "easy": [
                    "What is a Queue and how does it work?",
                    "How does a Queue differ from a Stack?",
                    "What is the order of operations in a Queue?",
                    "Why is a Queue suitable for scheduling scenarios?",
                    "Give a real-life example that mimics a Queue.",
                    "Which operations are supported by a Queue?",
                    "What happens when a Queue is full or empty?",
                    "In what situations is a Queue preferred over a Stack?",
                    "What is the difference between enqueue and dequeue in a Queue?",
                    "Can a Queue be implemented using arrays? How?"
                ],
                "medium": [
                    "How would you implement a Queue using two stacks?",
                    "Explain the difference between a Queue and a Circular Queue.",
                    "How does a Queue handle overflow and underflow conditions?",
                    "Describe a real-world use case where a Queue improves efficiency.",
                    "Compare a linear Queue and a circular Queue with examples.",
                    "A queue initially contains {initial_elements}. Perform the following operations: {operations}. What is the final content of the queue?",
                    "Given a queue with elements {initial_elements}, what will be the result after these operations: {operations}?",
                    "Consider a queue holding {data_type}. If the initial state is {initial_elements} and the following steps occur: {operations}, what remains in the queue?",
                    "You're managing a queue of {data_type}. Starting with {initial_elements}, after performing these actions: {operations}, what is at the front of the queue?",
                    "After enqueueing and dequeueing the following elements: {operations}, what's the final state of the queue?"
                ],
                "hard": [
                    "Design a Queue that supports retrieving the minimum element in O(1) time.",
                    "How would you implement a Queue with dynamic resizing?",
                    "Design a Queue that allows inserting elements at both ends.",
                    "Analyze the time and space complexity of implementing a Queue using two stacks.",
                    "How does a Queue behave under concurrent access in multi-threading?",
                    "What are the design trade-offs between array-based and linked-list-based Queues?",
                    "How would you simulate a Queue using priority queues?",
                    "Design an algorithm to reverse the order of a Queue using recursion.",
                    "Explain how a Queue is used in task scheduling and process handling.",
                    "What problems may arise when using a Queue in producer-consumer architecture?",
                    "Given a queue holding {data_type}, simulate the following operations: {operations}. What is the final state?",
                    "A system processes {data_type} in a queue format. Given {initial_elements}, how does the system handle {operations}?",
                    "A priority queue stores {data_type}. After the operations {operations}, what is the final ordering?",
                    "If a circular queue of size {size} undergoes {operations}, what happens when it reaches capacity?",
                    "You're developing a multi-threaded system that uses a queue to handle {data_type}. Simulate and analyze its behavior with {operations}."
                ]
            },
            "FIFO Principle in Queues": {
                "easy": [
                    "Explain the FIFO principle in a Queue with an example.",
                    "Why is FIFO considered the core behavior of a Queue?",
                    "Give a real-world analogy for the FIFO principle.",
                    "If you enqueue 1, 2, 3, what order will they be dequeued?",
                    "What would be the output of dequeue() if the queue contains [10, 20, 30]?",
                    "What happens to the first element in a FIFO queue when dequeue is called?",
                    "In FIFO, which element is always at the front of the queue?",
                    "How does FIFO make queue operations predictable?",
                    "Is the first inserted element always the first to be removed in FIFO? Explain.",
                    "List three systems or processes that work based on the FIFO principle."
                ],
                "medium": [
                    "How can FIFO queues be used to simulate scheduling in operating systems?",
                    "Compare and contrast FIFO with Round-Robin scheduling.",
                    "Explain how FIFO is maintained in queues implemented with linked lists vs arrays.",
                    "What are the limitations of FIFO in real-time systems, and how can they be mitigated?",
                    "Design a message-passing system using a FIFO queue between two processes. How is order maintained?",
                    "Explain the importance of FIFO in streaming data (like YouTube video buffering).",
                    "Given a FIFO queue with initial elements {initial_elements}, perform the operations: {operations}. What is the final state of the queue?",
                    "Simulate a print job queue where jobs {initial_elements} are processed in FIFO order. What is the order of completion after {operations}?",
                    "You're managing a food order queue. Starting with orders {initial_elements}, what does the queue look like after: {operations}?",
                    "A hospital uses a FIFO triage queue. Patients {initial_elements} arrive in order. Simulate check-in, treatment, and queue state after: {operations}.",
                    "In a railway ticketing system with FIFO logic, simulate ticket allocation based on queue {initial_elements} and updates: {operations}."
                ],
                "hard": [
                    "Design a distributed task manager that uses FIFO queues across multiple nodes. How is global ordering ensured?",
                    "How does FIFO interact with multithreading, and what synchronization issues can arise?",
                    "Build a thread-safe FIFO queue. What mechanisms ensure correct operation under concurrent access?",
                    "What are the performance trade-offs of enforcing FIFO in high-load systems like databases or cloud queues?",
                    "In a system with limited memory, how would you implement a memory-efficient FIFO structure?",
                    "Compare FIFO queues to Kafka topics in event-streaming platforms.",
                    "Simulate a priority-aware FIFO system where tasks have arrival time and execution order must be preserved. Given: {initial_elements}, {operations}.",
                    "You're developing a circular queue of size {size}. After these operations: {operations}, determine the state and explain if overflow occurs.",
                    "Given a warehouse dispatch FIFO queue and elements {initial_elements}, simulate how the system reacts to batch operations: {operations}.",
                    "A bank queue operates in FIFO with express exits. Simulate customer flow given arrivals {initial_elements} and events {operations}.",
                    "Design a real-time logging system using FIFO where logs expire after {duration}. Given {initial_elements} and operations {operations}, what remains?",
                    "You're simulating a traffic lane with FIFO logic and green-light cycles. Given cars {initial_elements} and rules {operations}, who exits and in what order?"
                ]
            },
       "Real-Life Applications of Queues": {
    "easy": [
        "List three real-life scenarios where queues are used.",
        "How does a queue apply to people standing in a line at a ticket counter?",
        "Explain how queues are used in printers handling multiple print jobs.",
        "Why are queues ideal for customer service systems like call centers?",
        "How does an operating system use queues for managing tasks?",
        "What kind of queue is used in a playlist of songs?",
        "Why do traffic signals use queues to manage vehicle movement?",
        "Give an example of how queues are used in handling background tasks in mobile apps.",
        "In what way does a queue apply in food delivery or order processing apps?",
        "Describe how queues are used in CPU scheduling."
    ],
    "medium": [
        # Theory-based
        "Compare how queues are used in restaurant waiting systems vs. call center systems.",
        "Why is FIFO strategy crucial in emergency alert dispatch systems?",
        "How does a queue help improve throughput in print spoolers?",

        # Simulation-based
        "You are managing a print server queue. Initially, it contains jobs {initial_elements}. After performing the following: {operations}, what jobs remain in the queue?",
        "A hospital registration system uses a queue to serve patients. The queue starts with patients {initial_elements}. After {operations}, who is being served now?",
        "Consider an online ticket booking system that queues users during high traffic. Starting with {initial_elements}, simulate the operations: {operations}. What is the final state?",
        "A restaurant waitlist queue holds names: {initial_elements}. After these actions: {operations}, who is at the front and rear of the queue?",
        "In a theme park ride queue, users enter and exit based on timing. If the queue begins with {initial_elements}, perform these steps: {operations}. What's the final state of the ride queue?"
    ],
    "hard": [
        "Design a task manager queue that prioritizes system-critical operations during overload. How would you simulate it?",
        "Model a multi-queue system used in airports for security checks. How do you distribute passengers efficiently using queues?",
        "Simulate an event-driven architecture where multiple queues represent different event priorities. How do you synchronize them?",
        "You are developing an emergency alert dispatch system. Queues are prioritized based on urgency levels. Given {initial_elements} with priorities, simulate {operations}. What gets processed first?",
        "Design a smart queue for handling food delivery riders during peak hours. Based on these riders {initial_elements} and these tasks: {operations}, who gets assigned next?",
        "A multi-server ticketing system uses a load balancer to distribute users to different queues. Simulate the user inflow {initial_elements} and operations {operations}. What is the load in each queue?",
        "In a streaming service, buffer queues manage incoming data packets. Given the sequence {initial_elements} and packet delays: {operations}, what is the state of the buffer?",
        "An autonomous vehicle intersection control system queues incoming cars from 4 directions. Given arrival sequences {initial_elements}, and processing logic {operations}, simulate the traffic flow.",
        "Design a queue-based system to manage vaccination slots for a population. Given initial booking list {initial_elements} and real-time user actions {operations}, how would the queue adjust?",
        "Simulate a real-time messaging app where each user message enters a delivery queue. Starting from {initial_elements} and simulating delivery and drop conditions with {operations}, what messages remain undelivered?"
    ]
     }
     ,
     "Understanding the Queue": {
    "easy": [
        "What is a queue and what are its primary characteristics?",
        "Why is queue called a FIFO data structure?",
        "Give a real-life example that resembles a queue.",
        "What are enqueue and dequeue operations?",
        "Can a queue be implemented using an array? If yes, how?",
        "When would a queue be considered full or empty?",
        "How is a queue different from a stack?",
        "List the types of queues you know (simple, circular, priority, deque).",
        "How is a linear queue different from a circular queue?",
        "What does the 'front' and 'rear' pointer mean in a queue?",
        "Can a queue be implemented using an array or a linked list? How?"
    ],
    "medium": [
        "How would you implement a queue using two stacks? What is the time complexity?",
        "What is the difference between a queue and a circular queue? Explain with examples.",
        "Why is a circular queue more efficient than a linear queue in fixed-size array implementations?",
        "Explain front and rear pointer movement in circular queue implementation.",
        "How do underflow and overflow conditions work in a queue?",
        "Compare array-based vs linked-list-based implementation of a queue.",
        "How is queue used in level-order traversal of a binary tree?",
        "Explain queue behavior in OS process scheduling.",
        "What are the advantages of using a doubly-ended queue (deque)?",
        "How is a queue used in breadth-first search (BFS)?",
        "Why is a queue preferred in producer-consumer problems?",
        "How do queues assist in CPU job scheduling or round-robin algorithms?",
        "Explain why queues are suitable for message buffering in network devices.",
        "What are the use cases where circular queues are more efficient than linear queues?",
        "What is a deque and how is it different from a normal queue?",
        "Why is a priority queue used in Dijkstra’s Algorithm?",
        "How can you use a queue to implement a moving average over a stream of numbers?",
        "How would you design a real-time messaging buffer using a queue?",
        "Explain the difference between min-heap and max-heap in terms of priority queues.",
        "How would you implement a queue that also returns the maximum value at any time?",

        # Simulation-based
        "Given a queue with initial elements {initial_elements}, perform: {operations}. What is the final state of the queue?",
        "Simulate enqueue and dequeue operations with initial queue {initial_elements} and actions {operations}.",
        "You manage a customer service queue with customers {initial_elements}. Apply operations: {operations}. What is the queue now?",
        "Model a print queue with tasks {initial_elements}. After {operations}, what tasks are still in the queue?",
        "A queue of patients has IDs {initial_elements}. After simulating {operations}, what’s the patient at the front?",
        "Simulate a scenario where a queue holds tasks arriving every minute, and each task takes 2 minutes to process. With inputs {initial_elements} and actions {operations}, find pending tasks.",
        "You’re simulating a ticket counter. Queue starts with people {initial_elements}. Simulate: {operations}. Who is currently being served?",
        "A circular queue of size {size} starts with {initial_elements}. After operations {operations}, what is the state of the queue?",
        "Simulate packet processing in a network router using a queue of packets {initial_elements} and processing commands {operations}.",
        "Design a system where a queue processes tasks with delays. Given {initial_elements} and timed operations {operations}, what’s the result?",
        "You’re simulating a school lunch line with students {initial_elements}. After actions {operations}, who remains and who was served?",
        "If enqueue and dequeue happen in a round-robin fashion, starting from {initial_elements}, after {operations}, what’s left in the queue?",
        "You maintain a food delivery queue. Orders {initial_elements} are received and processed as per: {operations}. Final order status?",
        "Simulate a parking lot queue system where cars enter and exit in the order given by: {operations}. Starting state: {initial_elements}.",
        "In an event ticketing app, simulate a queue where customers {initial_elements} are added and removed as per {operations}. What’s the updated list?"
    ],
    "hard": [
        "Design a queue that supports fetching the minimum element in O(1) time.",
        "How would you implement a queue that can dynamically resize when full?",
        "Create a queue supporting insertions at both ends. What are the use cases?",
        "Simulate a multi-threaded consumer queue with {data_type} inputs and operations {operations}. How does thread safety affect the outcome?",
        "You’re building a print server: simulate printer jobs arriving in queue {initial_elements} and processed by different printers via {operations}.",
        "Analyze a priority queue implementation and simulate task insertion/removal using priority: {operations}.",
        "Simulate a hospital emergency room: patients in queue {initial_elements} are treated based on urgency via {operations}. What’s the final patient order?",
        "Model a real-time messaging app: messages enter queue {initial_elements}. Simulate delivery/timeout failures using {operations}. What messages are undelivered?",
        "Design a garbage collection system where outdated references are held in a queue. Simulate removal and enqueue using {operations}.",
        "You’re building a distributed system where job queues sync across servers. Simulate with job set {initial_elements} and syncing actions {operations}.",
        "Simulate CPU job scheduling using Round Robin with time quantum. Initial jobs: {initial_elements}. Operations: {operations}. Show remaining jobs and execution order.",
        "A queue of sensor readings {initial_elements} must be processed in real-time. Simulate delay, enqueue, and overflow using {operations}. What readings remain?",
        "You’re designing an elevator request system. People queue up with {initial_elements}. After {operations}, what floor requests are still pending?",
        "Implement a time-decayed queue where each element expires after 5 mins. Given enqueue times and {operations}, what elements are still valid?",
        "Create a simulation of bus boarding queue at a smart terminal. Starting from {initial_elements} and operations {operations}, simulate passenger flow.",

          '{"question": "You\'re building a ride-sharing service like Uber. Each request comes with a priority (VIP or Normal). How would you implement the matching logic using a priority queue?", "requirement": "Use Python\'s heapq module with a tuple of (priority_level, timestamp, request_id) to simulate priority queue logic.", "starter_code": "import heapq\\nrequests = []\\nheapq.heappush(requests, (0, timestamp, \'VIP123\'))\\n# lower priority value = higher priority"}',
    
    '{"question": "You\'re designing a food delivery system. Orders have deadlines and priorities. Use a min-heap to always deliver the earliest deadline orders.", "requirement": "Implement a function processOrders(orders) where each order is (deadline, priority, order_id)", "starter_code": "import heapq\\ndef processOrders(orders):\\n    heapq.heapify(orders)\\n    while orders:\\n        deadline, priority, order_id = heapq.heappop(orders)\\n        print(f\'Delivering {order_id}\')"}',
    
    '{"question": "Implement a task scheduler where each task has a cooldown period. Use a queue + heap to schedule tasks optimally.", "requirement": "Leverage a max heap for task frequency and a queue to store cooldown.", "starter_code": "from collections import deque\\nimport heapq\\n\\n# tasks = [\'A\',\'A\',\'A\',\'B\',\'B\',\'C\']\\ndef scheduleTasks(tasks, cooldown):\\n    pass  # Fill implementation"}',
    
    '{"question": "Design a real-time event manager using deque where events expire after T seconds.", "requirement": "Use collections.deque to append events and remove old ones.", "starter_code": "from collections import deque\\nimport time\\n\\nevents = deque()\\ndef add_event(event_time, event):\\n    events.append((event_time, event))\\n    while events and events[0][0] < time.time() - T:\\n        events.popleft()"}',
    
    '{"question": "Simulate a call center where incoming calls are processed by available agents. Calls are queued, and each has a priority.", "requirement": "Use a max-heap to handle urgent calls first."}',

    '{"question": "LeetCode: Sliding Window Maximum. Explain how to use a deque to maintain max efficiently.", "requirement": "Implement maxSlidingWindow(nums, k) using deque to store indices.", "starter_code": "from collections import deque\\ndef maxSlidingWindow(nums, k):\\n    q, res = deque(), []\\n    # implement logic"}',
    
    '{"question": "In a game server queue, each player has a rank. Use a priority queue to serve highest rank players first.", "starter_code": "import heapq\\nplayers = []\\nheapq.heappush(players, (-rank, timestamp, player_id))"}',
    
    '{"question": "Sensor Data Stream: Each reading has a timestamp. Remove old readings beyond 5 seconds.", "starter_code": "from collections import deque\\ndata = deque()\\n# add (timestamp, value) and remove if older than current_time - 5"}',
    
    '{"question": "Stream of stock prices: Maintain moving average of last K values.", "starter_code": "from collections import deque\\nclass StockAverage:\\n    def __init__(self, k):\\n        self.q = deque()\\n        self.k = k\\n    def addPrice(self, price):\\n        self.q.append(price)\\n        if len(self.q) > self.k:\\n            self.q.popleft()\\n    def getAverage(self):\\n        return sum(self.q) / len(self.q)"}',
    
    '{"question": "LeetCode: Design Hit Counter – count hits in last 5 minutes.", "starter_code": "from collections import deque\\nclass HitCounter:\\n    def __init__(self):\\n        self.q = deque()\\n    def hit(self, timestamp):\\n        self.q.append(timestamp)\\n    def getHits(self, timestamp):\\n        while self.q and self.q[0] <= timestamp - 300:\\n            self.q.popleft()\\n        return len(self.q)"}'

    ]
},
 "Stack vs Queue": {
    "easy": [
     
      "How do stacks and queues differ in terms of insertion and removal order?",
      "What does LIFO and FIFO mean in the context of stack vs queue?",
      "Which operations are used to add and remove elements in a queue vs a stack?",
      "When would you prefer using a queue over a stack in an application?",
      "Give real-life examples where queue behavior is used and where stack behavior is used.",
      "What role do 'front' and 'rear' play in queues compared to the 'top' in stacks?",
      "Which is more suitable for task scheduling – stack or queue? Why?",
      "Can both stack and queue be implemented using arrays or linked lists? How does their usage differ?",
      "How does undo-redo differ from print job processing in terms of data structures used?",
      "How would you decide between using a queue or a stack in solving a problem?",

    #   // Priority Queue (conceptual)
      "How is a priority queue different from a normal queue?",
      "Where might you use a priority queue in real-world applications?",
      "What determines the removal order in a priority queue?",
      "How are priority queues implemented internally (e.g., using heaps)?",
      "What happens when two elements have the same priority in a priority queue?",

 
      "Why is a circular queue more space-efficient than a linear queue?",
      "What causes a circular queue to be considered full or empty?",
      "How do front and rear pointers move in a circular queue?",
      "Can you implement a circular queue using an array? How?",
      "Give one scenario where circular queues are better than simple queues.",

    #   // Simulation-style with placeholders
      "You are given a queue with elements {initial_elements}. Perform operations: {operations}. What is the final state?",
      "A queue begins with elements {initial_elements}. After {operations}, who is at the front?",
      "A circular queue of size {size} is initialized with {initial_elements}. After operations: {operations}, what's in the queue?",
      "A priority queue has items with values and priorities: {initial_elements}. After performing {operations}, which item gets removed first?",
      "You're simulating job handling using a queue with tasks {initial_elements}. After {operations}, which tasks are done?",
      "A circular queue holds tokens {initial_elements}. After simulating {operations}, what’s the updated state?",
      "A priority queue is managing patients with priorities {initial_elements}. After operations {operations}, who is treated next?",
      "You simulate a queue of people boarding a bus: {initial_elements}. Apply: {operations}. Who is still in line?",
      "Model a helpdesk system using a circular queue with inputs {initial_elements} and actions {operations}. What is the result?",
      "Simulate a print queue using a priority queue with tasks {initial_elements} and process them using {operations}. What tasks remain?"
    ],
     "medium": [
    #   // Theoretical (10%)
      "In what scenario would a queue handle task scheduling better than a stack?",
      "Why is a queue suitable for streaming data but not a stack?",
      "How does a circular queue overcome the limitations of a linear queue in memory reuse?",

    #   // Simulation-based (90%)
      "You’re handling browser history using a stack for backtracking and a queue for forward links. With initial elements {initial_elements} and operations {operations}, what’s the current page?",
      "Simulate a data stream processor: use a queue to receive packets and a stack to handle special packets. Start with {initial_elements} and perform {operations}. What’s the final state?",
      "Design a system where every 3rd element in a queue is pushed into a stack. Initial queue: {initial_elements}, apply operations: {operations}. What’s in the stack and queue?",
      "Reverse a queue using a stack. Given queue {initial_elements}, simulate {operations}. What is the resulting queue?",
      "Handle patients with normal priority in a queue and critical patients in a stack. With {initial_elements} and operations {operations}, what’s the serving order?",
      "Undo-redo manager: stack handles undo, queue stores redo. Given {initial_elements}, perform {operations}. Final content of both?",
      "Process customers: queue handles regular, stack handles VIPs. Simulate using {initial_elements} and operations {operations}. Output order?",
      "Dispatcher queue processes requests, urgent ones go to stack. Given {initial_elements}, simulate {operations}. Who is served and in what order?",
      "Game engine simulation: valid moves to stack, invalid moves to queue. Starting with {initial_elements}, simulate {operations}. What’s the final state?",
      "Queue stores print tasks, failed ones go to stack for retry. Simulate {initial_elements} and {operations}. Final queues?",
      "Log system: queue stores events, stack stores errors. With initial state {initial_elements} and actions {operations}, what’s the system state?",
      "Priority queue vs stack: use a stack for high-priority tasks, queue for regular ones. With {initial_elements}, simulate {operations}. What’s remaining?",
      "Alternate stack and queue after every 5 operations. With {initial_elements}, simulate actions {operations}. What’s stored where?",
      "Circular queue tracks events, stack captures anomalies. Initial elements: {initial_elements}, simulate actions {operations}. Final queue and stack?",
      "Circular queue used for buffering, errors stored in stack. Simulate input {initial_elements} and operations {operations}. What’s the output?",
      "System flushes stack when queue length exceeds threshold. Simulate {initial_elements} and operations {operations}. Final content?",
      "Editor simulation: key presses go to queue, deletes go to stack. Simulate: {initial_elements}, operations: {operations}. Final content?",
      "Printing system: queue holds print jobs, failed ones go to stack. Perform: {operations} on {initial_elements}. What's pending?",
      "Playlist manager: queue for upcoming songs, stack for recently played. Starting from {initial_elements}, simulate {operations}. What remains?",
      "Streaming buffer uses circular queue; stack handles lagged frames. Simulate {initial_elements} and {operations}. Final buffer?",
      "Priority queue insertion with custom rule: same priority respects FIFO. Given {initial_elements}, apply {operations}. What’s the result?",
      "Real-time event sender: normal messages in queue, urgent messages in stack. Simulate events: {operations} on initial state: {initial_elements}.",
      "Chat system: normal messages in queue, flagged go to stack. Initial: {initial_elements}, actions: {operations}. Final view?",
      "Delivery system: queue for new orders, stack for failed deliveries. Process {operations} on orders {initial_elements}. Output?",
      "Virtual class: questions in queue, re-asks in stack. With students {initial_elements}, simulate {operations}. Who is next?",
      "IoT sensor queue stores values, stack keeps error signals. Data: {initial_elements}, simulate actions: {operations}.",
      "Simulate a food delivery queue with express orders going into a stack. Initial orders: {initial_elements}, apply: {operations}. Final state?",
      "Game inputs into circular queue; undo stack handles reversion. Simulate with {initial_elements} and {operations}. Output?",
      "Push alternating values into stack and queue. Given {initial_elements}, process {operations}. What’s in stack and queue?",
      "Network uses queue for normal traffic and stack for retrials. Start with {initial_elements}, run {operations}. What's the result?"
    ],
     "hard": [
    #   // 1. Advanced Implementation & Deep Questions
      "Design a data structure that supports enqueue, dequeue, and retrieving the minimum element in O(1) time using queue logic.",
      "Implement a queue using two stacks where all operations (enqueue, dequeue, peek) are amortized O(1). Justify the approach.",
      "Create a circular deque with support for insertion and deletion from both ends in O(1). Explain the challenges.",
      "Design a real-time system to simulate browser tab management using stack and queue together. Discuss data structure design.",
      "Build a messaging queue that auto-prioritizes critical messages and allows timeouts. How would you maintain state consistency?",
      "Implement a queue that allows retrieving the maximum frequency element at any point.",
      "You need to support back and forward operations in a command-based UI. How can stacks and queues be hybridized for this?",
      "Explain how stacks and queues are used together in recursive backtracking simulations. Provide real-world use cases.",
      "Design a job processor where jobs are scheduled using queue but dependencies are tracked using stack-based logic.",
      "Simulate a hospital queue where critical patients jump ahead using priority queues but maintain arrival timestamps."

      ,

    #   // 2. Complex Simulation Questions (with placeholders)
      "A task manager processes real-time jobs using queue. High-priority tasks must preempt ongoing ones using a stack. Simulate with initial state {initial_elements} and operations {operations}.",
      "You're building an undo-redo system: queue tracks recent actions, stack manages undo/redo. Starting state: {initial_elements}, operations: {operations}. What are both structures now?",
      "Circular queue stores streaming data. Every 10th data point is popped and pushed into a stack. With input {initial_elements} and actions {operations}, what is the final state?",
      "You must reverse every alternate K elements in a queue using stack. With queue {initial_elements} and K={k}, perform the operation and show final output.",
      "In a gaming engine, inputs go to a queue. On error, the last 3 valid inputs are retrieved from a stack. Simulate: {initial_elements}, operations: {operations}. Final state?",
      "Simulate a system where a stack is used for recursive expression solving and a queue for task scheduling. Initial: {initial_elements}, actions: {operations}.",
      "A circular queue is used in audio buffering. On distortion events, last few packets are shifted into a stack for retry. Input: {initial_elements}, simulate: {operations}.",
      "Streaming video system: packets enter queue, dropped packets go to stack. Process {operations} on {initial_elements}. Final buffers?",
      "Model a parking system where entries are queued but exits (from last-in) follow stack logic for emergencies. Simulate using {initial_elements} and {operations}.",
      "Simulate priority queue for multi-tiered requests where failed requests go into LIFO retry stack. Process: {operations}, on initial: {initial_elements}."

      ,


      "Given the code snippet implementing a queue using two stacks:\nclass MyQueue {\n    Stack<Integer> stack1 = new Stack<>();\n    Stack<Integer> stack2 = new Stack<>();\n    public void enqueue(int x) {\n        while (!stack1.isEmpty()) {\n            stack2.push(stack1.pop());\n        }\n        stack1.push(x);\n        while (!stack2.isEmpty()) {\n            stack1.push(stack2.pop());\n        }\n    }\n    public int dequeue() {\n        if (stack1.isEmpty()) return -1;\n        return stack1.pop();\n    }\n} Modify this implementation to support peek() in O(1) and track the number of elements efficiently.",
      
      "Consider a problem where you implement a circular queue:\nclass CircularQueue {\n    int[] arr;\n    int front, rear, size, capacity;\n    public CircularQueue(int k) {\n        arr = new int[k];\n        capacity = k;\n        front = rear = -1;\n        size = 0;\n    }\n    // enqueue(), dequeue(), isFull(), isEmpty() methods\n} Extend this to allow dynamic resizing of the queue when it's full (like an ArrayList).",

      "In LeetCode-style, you are asked to design a queue that supports getMax() in O(1) time. Describe how you would implement it. What data structure would you combine with queue to achieve this?",

      "LeetCode-style Challenge: Given a stream of integers, design a data structure that supports insert(val), delete(val), and return the kth largest element at any time. What data structures would you use? Could stack and queue help here? Why or why not?",

      "You are implementing a BFS traversal that tracks node visit history using a queue, but also maintains rollback history in a stack for undoing. Write the pseudo-code for such a hybrid traversal and explain its use case.",

      "A task manager processes real-time jobs using a queue. High-priority tasks must preempt ongoing ones using a stack. Simulate with initial state: {initial_elements}, and operations: {operations}. Show the final states of both stack and queue.",

      "You're building an undo-redo system: queue tracks recent actions, stack manages undo/redo. Given initial elements {initial_elements} and operations {operations}, simulate and show final states.",

      "Circular queue stores streaming data. Every 10th data point is popped and pushed into a stack. With input {initial_elements} and actions {operations}, what is the final state of the queue and stack?",

      "You must reverse every alternate K elements in a queue using a stack. Given queue: {initial_elements} and K={k}, perform the operation and return the final output.",

      "In a gaming engine, inputs go to a queue. On error, the last 3 valid inputs are retrieved from a stack. Given queue state: {initial_elements} and operations: {operations}, simulate and show the stack.",

      "Design a job processor where jobs are scheduled using queue but dependencies are tracked using stack logic. Implement this logic with sample inputs and simulate dependency resolutions using both structures.",

      "Streaming video system: packets enter queue, dropped packets go to stack. Process {operations} on {initial_elements} and display the final buffer states.",

      "Simulate a hospital queue where critical patients jump ahead using priority queues but maintain arrival timestamps. Design and implement this system with emphasis on fair yet urgent processing.",

      "Simulate priority queue for multi-tiered requests where failed requests go into LIFO retry stack. Process the stream {operations} on initial requests {initial_elements}. Return the state of retry stack and main queue."
    ]
     
 }

 ,
"Queue vs Deque": {
    "easy": [
      "What is the primary difference between a queue and a deque in terms of allowed operations?",
      "Can a deque be used to simulate both stack and queue behavior? Justify your answer.",
      "True or False: Deque is a restricted version of a queue.",
      "Name two applications where deque is preferred over queue.",
      "Which data structure would you use to manage the order of customer service calls, where high-priority customers can be added to the front?",
      "If a queue supports only insertion at rear and deletion at front, what structure is this?",
      "If an element is inserted at the front and removed from the rear, what data structure is being used?",
      "Explain why a deque is more flexible than a queue.",
      "What is the output of the following deque operations: push_back(1), push_front(2), pop_back(), pop_front()?",
      "In a deque, if you perform push_front(10), push_back(20), pop_front(), and pop_back(), what will be the sequence of output?",
      "Which is more suitable for implementing Undo/Redo functionality: Queue or Deque? Why?",
      "How can a deque be used to implement a palindrome checker?",
      "MCQ: Which data structure allows insertion and deletion from both ends?\nA. Stack\nB. Queue\nC. Deque\nD. Priority Queue\nAnswer: C",
      "MCQ: What happens when you perform pop_back() on an empty deque?\nA. Returns 0\nB. Throws an error\nC. Returns -1\nD. Ignores the call\nAnswer: B (typically error or exception)",
      "MCQ: Which of the following can replace a stack and a queue simultaneously?\nA. Array\nB. Linked List\nC. Deque\nD. Priority Queue\nAnswer: C",
      "MCQ: A double-ended queue can be implemented using:\nA. Only arrays\nB. Only linked lists\nC. Both arrays and linked lists\nD. None of the above\nAnswer: C",
      "Given a deque initialized as [ ], perform: push_back(5), push_front(3), push_back(7), pop_front(). What is the deque now?",
      "Explain in one line why deque is used for Sliding Window Maximum problem.",
      "MCQ: Which method is not supported in a standard queue?\nA. enqueue\nB. dequeue\nC. push_front\nD. isEmpty\nAnswer: C",
      "True or False: Queue can be used to implement BFS, whereas deque is typically used in problems like Sliding Window Maximum.",
      "Simulate the result: Deque d = [ ]; push_front(1); push_back(2); push_front(3); pop_back(); pop_front(); What remains in the deque?",
      "MCQ: A circular queue can be considered a special case of:\nA. Stack\nB. Linked List\nC. Deque\nD. Array\nAnswer: C",
      "Give one real-life example where a deque is better than a queue.",
      "What data structure is used when both urgent and non-urgent tasks must be processed with different priorities?",
      "Explain how insertion and deletion in deque differ from queue in terms of direction."
    ],
     "medium":
    [
  "Explain the differences between Priority Queue, Circular Queue, and Deque. Which use cases suit each of them best?",

  "A queue of {data_type} with initial elements {initial_elements} is given. Perform the following operations in order: {operations}. What will be the final state of the queue? (Solve in {duration})",

  "Implement a circular queue of size {size} initialized with {data_type}: {initial_elem ents}. After executing {operations}, what are the front and rear values?",

  "A customer service system stores {data_type} in a queue. It begins with {initial_elements}. Apply the sequence: {operations}. What will be the result after all operations? (Time: {duration})",

  "Design a dynamic queue that resizes itself when full. Initially, it holds {data_type}: {initial_elements} and size {size}. Operations to apply: {operations}",

  "You are given a task queue that contains {data_type}: {initial_elements}. Simulate the following tasks: {operations}. Provide the final state and mention if the queue became full or empty at any stage.",

  "Using a deque to simulate both stack and queue behavior, start with {initial_elements}. Apply the following mixed operations: {operations}. What is the result?",

  "You are tasked with monitoring sensor data using a queue initialized with {initial_elements}. After performing {operations}, which data points remain valid in the buffer? (Duration: {duration})",

  "Given a queue storing {data_type} with initial state: {initial_elements}, perform the following: {operations}. After this, return the front element, and check if the queue is full or empty.",

  "An automated printer queue starts with jobs: {initial_elements}. Simulate these operations: {operations}. How many jobs remain? Did any get lost or repeated? (Limit your response to {duration})",

  "Write a simulation that uses a circular queue to manage tickets ({data_type}). Starting with {initial_elements}, run the following: {operations}. What is the final ticket number served?",

  "In a game server, player actions are stored in a queue. It starts with: {initial_elements}. Process the action stream: {operations}. Who is next to act? What is the total queue size now?",

  "A browser maintains a queue of visited {data_type}. With starting entries {initial_elements}, apply these operations: {operations}. How would you display the current queue from front to rear?",

  "Simulate a multi-threaded task execution where tasks are queued. Start with tasks: {initial_elements} and process: {operations}. Were all tasks executed? Did any remain in the queue?",

  "You're building a music playlist queue using {data_type} with elements {initial_elements}. Apply the operations: {operations}. What's the next song to play and is the playlist full?",
   "You’re implementing a job scheduler using a priority queue that starts with {data_type}: {initial_elements}. Apply: {operations}. Which job has the highest priority now?",

  "Create a simulation of a customer billing queue initialized with {initial_elements}. Execute the following operations: {operations}. Who is the next to be billed and how many remain?",

  "Design a system where a deque is used for both front-loading and back-loading processes. Begin with {initial_elements}, then perform: {operations}. What’s the current deque state?",

  "A garbage collection robot stores scan results in a circular queue of size {size}. Start with: {initial_elements}. Apply operations: {operations}. What are the valid and removed readings?",

  "You’re managing real-time chat messages using a queue with initial state: {initial_elements}. Process: {operations}. Is the oldest message still in the queue? What’s the current size?",

  "A theme park uses a priority queue for VIP entries. Start with {data_type}: {initial_elements}. Run operations: {operations}. How many VIPs are still in queue? Who is next?",

  "Use a deque to maintain recent tab history in a browser. Start with: {initial_elements}. Apply: {operations}. What tabs are currently active and which were removed?",

  "Simulate a dual-end data stream buffer using a deque. Initialize with: {initial_elements}. Execute: {operations}. What’s at the front and rear of the stream buffer?",

  "A time-based logging system uses a queue of size {size} for {data_type}. Begin with: {initial_elements}. Perform operations: {operations}. Has the log rotated? What’s visible now?",

  "Design a dynamic messaging system with a queue that resizes when full. Initial messages: {initial_elements}, size: {size}. Apply: {operations}. What’s the final queue size?",

  "A multiplayer game server uses a circular queue to store player inputs. Start with: {initial_elements}. Run operations: {operations}. What inputs remain unprocessed?",

  "In a live stock price feed, a fixed-size circular queue holds the latest {data_type}. Begin with: {initial_elements}. Process: {operations}. What’s the current average of stored values?",

  "You're managing a train platform system using queues. Platforms have {data_type}: {initial_elements}. Apply: {operations}. Which train departs next? Is any platform idle?",

  "Implement a delivery system where parcels are processed using a deque. Initial queue: {initial_elements}. After: {operations}, list the delivered vs pending parcels.",

  "A file downloader uses a task queue. It starts with: {initial_elements}. After executing: {operations}, how many downloads failed due to overflow or invalid dequeues?",

  "Simulate a sliding window average using a circular queue of size {size}. Start with: {initial_elements}. After applying: {operations}, what’s the final average?",

  "Create a job dependency resolver using a queue initialized with tasks: {initial_elements}. Process: {operations}. Did all dependencies resolve? What remains?",

  "Design a cache eviction policy using a queue (FIFO). Starting cache: {initial_elements}. Run: {operations}. What keys remain in the cache?",

  "You're building an alert notification system using a deque. With notifications: {initial_elements}, apply: {operations}. What’s displayed to the user now?",

  "A simulation of a food ordering system uses a circular queue. Orders: {initial_elements}. Execute: {operations}. Which order is currently being prepared? Is the queue full?"




] ,"hard":
[
    
    "You're implementing a queue using two stacks. Complete the method to get the front of the queue in O(1) time: class MyQueue { Stack<Integer> input = new Stack<>(); Stack<Integer> output = new Stack<>(); public void enqueue(int x) { input.push(x); } public int dequeue() { if (output.isEmpty()) while (!input.isEmpty()) output.push(input.pop()); return output.isEmpty() ? -1 : output.pop(); } public int peek() { /* complete this method */ } }",
    
    "Complete the function to detect if a circular queue is full: class CircularQueue { int[] arr; int front = 0, rear = 0, size = 0; int capacity; CircularQueue(int k) { arr = new int[k]; capacity = k; } public boolean isFull() { /* complete this */ } }",
    
    "Given a printer queue where each job has a priority, complete the method that returns true if any job with higher priority exists in the queue: Queue<Integer> printQueue = new LinkedList<>(); public boolean hasHigherPriority(int currentPriority) { /* complete this method */ }",
    
    "Complete the method to reverse the first k elements of a queue: public void reverseFirstK(Queue<Integer> queue, int k) { /* complete this method */ }",
    
    "You're maintaining a sliding window max using a deque. Complete the method to remove elements from the back of the deque if they are smaller than the current element: Deque<Integer> dq = new ArrayDeque<>(); public void cleanDeque(int[] nums, int i) { /* complete this method */ }",
    
    "Implement the logic to rotate a queue to the left by d positions: public void rotateQueue(Queue<Integer> queue, int d) { /* complete this method */ }",
    
    "Complete the method to find the front element of a circular queue: class CircularQueue { int[] arr; int front = 0, rear = 0, size = 0, capacity; CircularQueue(int k) { arr = new int[k]; capacity = k; } public int getFront() { /* complete this method */ } }",
    
    "Complete the method to enqueue an element in a fixed-size circular queue. Return false if the queue is full: public boolean enqueue(int[] queue, int size, int capacity, int element) { /* complete this method */ }",
    
    "You are given a queue that stores string commands. Complete the method to count the number of times the command 'print' occurs: public int countPrintCommands(Queue<String> commands) { /* complete this method */ }",
    
    "Given a browser history queue, complete the method to return the last visited site without removing it: public String lastVisited(Queue<String> history) { /* complete this method */ }",
    
    "In a queue implementation using arrays, complete the dequeue method to update front and size correctly: class ArrayQueue { int[] arr; int front, rear, size, capacity; public int dequeue() { /* complete this method */ } }",
    
    "You are using a deque for implementing a palindrome checker. Complete the logic to remove characters from both ends and compare: Deque<Character> dq = new ArrayDeque<>(); public boolean isPalindrome() { /* complete this method */ }",
    
    "Given a queue of integers, complete the method to move all zeros to the rear while preserving the order of non-zero elements: public void moveZerosToRear(Queue<Integer> queue) { /* complete this method */ }",
    
    "In a food delivery system, a queue stores orders. Complete the method to prioritize VIP orders (odd numbers): public void prioritizeVipOrders(Queue<Integer> orders) { /* complete this method */ }",
    
    "You're simulating task execution using a queue. Complete the function to return how many tasks can be processed before memory limit (sum < 100): public int countProcessableTasks(Queue<Integer> tasks) { /* complete this method */ }",
    
    "Complete the function to remove duplicate elements from a queue while keeping the first occurrence: public Queue<Integer> removeDuplicates(Queue<Integer> queue) { /* complete this method */ }",
    
    "Complete the logic for finding the kth element from the end in a queue using only queue operations: public int findKthFromEnd(Queue<Integer> queue, int k) { /* complete this method */ }",
    
    "Given a queue of characters representing customer types, implement logic to group 'VIP' (V) customers to the front while preserving relative order: public void reorderVIPs(Queue<Character> queue) { /* complete this method */ }",
    
    "You're implementing a circular buffer. Complete the method to get the rear element: class CircularBuffer { int[] buffer; int rear; public int getRear() { /* complete this */ } }",
    
    "Complete the method to check if a given sequence of dequeue operations is valid for a specific enqueue sequence: public boolean isValidDequeueOrder(int[] enqueue, int[] dequeue) { /* complete this method */ }"
  ]







    

  },
  "Queue vs Priority Queue": {
    "easy": [
      "What is the main difference between a queue and a priority queue?",
      "Why is a queue called a FIFO structure?",
      "How does a priority queue maintain its ordering of elements?",
      "Give a real-life example that illustrates the difference between queue and priority queue.",
      "Which data structure is used internally to implement a priority queue?",
      "True or False: In a normal queue, elements are processed based on their priority.",
      "Fill in the blank: A _____ queue processes elements based on the order they arrive.",
      "Fill in the blank: A _____ queue processes elements based on their priority level.",
      "What happens if two elements have the same priority in a priority queue?",
      "Which of the following is correct?\nA) Queue is FIFO, Priority Queue is LIFO\nB) Queue is FIFO, Priority Queue is based on priority\nC) Both are LIFO\nD) Queue is based on priority",
      "You insert values {10, 5, 20} into a queue and a priority queue. What is the order of removal in each?",
      "Simulate enqueue(1), enqueue(3), enqueue(2), dequeue() on a queue. What’s the output?",
      "Simulate insert(4), insert(2), insert(5), remove() on a priority queue. Which value is removed first?",
      "A queue has values {3, 6, 9}. Apply dequeue(), enqueue(5), dequeue(). What is the new front?",
      "A priority queue has values {4, 1, 7, 3}. Perform: insert(6), remove(), remove(). What are the remaining values?",
      "Simulate operations: enqueue(7), enqueue(2), enqueue(9), dequeue() on a FIFO queue. What is the state of the queue?",
      "Insert {8, 2, 10, 5} into a max-priority queue. Which element is removed first?",
      "Choose the correct output: Queue = {2, 4, 6}, after dequeue(), queue becomes?\nA) {2, 4}\nB) {4, 6}\nC) {6}\nD) {2}",
      "Simulate enqueue(2), enqueue(8), dequeue(), enqueue(4) in a queue. What is the new queue state?",
      "Given elements {5, 1, 9}, inserted into a priority queue, what order will they be removed in?"
    ],
    "medium": [
      "Given a queue of {data_type}: {initial_elements}, perform operations: {operations}. Compare the final state with a priority queue initialized with the same elements and operations. What are the differences?",
      "Initialize a normal queue and a priority queue with {data_type}: {initial_elements}. Apply operations: {operations}. Which elements are at the front after execution in both structures?",
      "A priority queue stores {data_type} with values {initial_elements}. Perform: {operations}. How does the element processing differ from a FIFO queue?",
      "Given a queue with tasks {initial_elements} ordered by arrival and a priority queue with the same tasks ordered by urgency, simulate: {operations}. What is the result in both structures?",
      "You are given a queue and a priority queue both initialized with {data_type}: {initial_elements}. Simulate: {operations}. Which data structure empties first and why?",
      "Given: queue: {initial_elements}, priority queue: {initial_elements}. Apply: {operations}. Output final state of both. Which has the smallest/largest element at front?",
      "Simulate task execution in a FIFO queue and a priority queue with {initial_elements} and actions: {operations}. Which task is executed last in both cases?",
      "Insert {data_type}: {initial_elements} into both a queue and a priority queue. Perform: {operations}. Compare processing order.",
      "You are managing events with a queue and a priority queue containing {initial_elements}. After: {operations}, which structure serves high-priority items first?",
      "Given {data_type} elements: {initial_elements}, simulate {operations} on both a normal queue and a max-priority queue. What’s the difference in processing order?",
      "In a priority queue of integers with values: {initial_elements}, and a standard queue with the same values, perform: {operations}. Compare final outputs.",
      "Simulate inserting and removing {data_type}: {initial_elements} using a normal queue and a min-priority queue. Which elements leave the structure first?",
      "Implement a queue of jobs {initial_elements} and a priority queue where jobs have urgency levels. Execute: {operations}. Determine job execution order.",
      "Create both a queue and a priority queue initialized with {initial_elements}. Apply: {operations}. Which element remains at the front in each?",
      "With {data_type} as input: {initial_elements}, run: {operations}. In both FIFO and priority mode, which data item is served first?",
      "Initialize queue and priority queue with {data_type} values: {initial_elements}. Perform: {operations}. Describe differences in popped values after each step.",
      "Simulate emergency calls received in a FIFO queue and in a priority queue with call severity encoded in: {initial_elements}. Run: {operations}. Compare outcomes.",
      "Given a stream of elements: {initial_elements}, simulate their processing in both queue and priority queue models using: {operations}. Output results.",
      "Build a priority queue and a queue with values {initial_elements}. Perform: {operations}. Return the state after each operation.",
      "With a task stream of {initial_elements} and commands: {operations}, compare how a queue and a priority queue handle the data differently."
    ],
    "hard": [
      "Implement a task scheduler that uses a PriorityQueue to execute tasks based on decreasing priority. Each task has a name and priority. Write the code to add tasks and process them in correct order.",
      "Given a PriorityQueue of integers, implement a method that returns the k largest elements without modifying the original queue. Complete the code snippet: public List<Integer> getKLargest(PriorityQueue<Integer> pq, int k) { // Your code here }",
      "Convert the following regular Queue-based job scheduler into a priority-aware scheduler using Java's PriorityQueue:\nQueue<Job> jobQueue = new LinkedList<>();\nclass Job {\n  String name;\n  int priority;\n}\n// Convert to use PriorityQueue and process high-priority jobs first.",
      "Complete the implementation of a custom MaxPriorityQueue class in Python using a heap. You must implement insert, extract_max, and peek methods.",
      "You are given a list of (priority, task) pairs. Implement a system using PriorityQueue that schedules tasks with the highest priority first. Handle duplicates by keeping insertion order.",
      "Given a list of emergency calls with priorities, implement a PriorityQueue where emergencies with higher priority are dequeued first. Maintain the insertion order for same-priority calls.",
      "Design and implement a TicketingSystem class that uses a PriorityQueue to return the customer with highest loyalty points first. Class: Customer { String name; int loyaltyPoints; } Complete the methods for enqueue and dequeue.",
      "Implement a queue that can switch between FIFO and PriorityQueue mode dynamically at runtime. Provide complete enqueue and dequeue logic based on the mode.",
      "Convert a FIFO Queue-based hospital system into a PriorityQueue system where patients with critical condition (higher priority value) are served first. Complete the transition code.",
      "Given an array of integers representing tasks, where each value is its priority, use a PriorityQueue to implement task execution. Complete the code: while (!pq.isEmpty()) { // execute next task }",
      "Write a function to merge k sorted queues into a single priority queue and return the sorted result.",
      "Using a PriorityQueue, implement Dijkstra's algorithm for finding shortest path in a graph. Complete the update and priority adjustment logic.",
      "Given the class: class Message { String content; int priority; } write a Java method to enqueue messages and process them in order of highest priority.",
      "Modify the following Queue implementation of order processing to use PriorityQueue for faster processing of urgent orders:\nQueue<Order> orders = new LinkedList<>();\n// Your changes here",
      "Build a system that simulates airline boarding where frequent flyers (higher priority) board before others. Use PriorityQueue. Class: Passenger { String name; int tier; } Complete the boarding logic.",
      "Implement an EventManager system that queues up events using PriorityQueue based on urgency. Each event has a timestamp and urgency level. Code enqueue and dequeue operations.",
      "Convert the implementation of a print spooler from using a Queue to a PriorityQueue so urgent print jobs print first. Each job has: String jobId, int urgency.",
      "Use PriorityQueue to implement a TopK frequent elements tracker from a stream of integers. Provide enqueue and frequency tracking logic.",
      "Implement a real-time notification system that uses a PriorityQueue to pop urgent notifications first. Each notification has severity score.",
      "Design a ParkingLot system that uses a PriorityQueue to assign nearest available parking slot (based on distance). Class Slot { int id; int distance; } Complete the assignSlot method.",
      "You are managing an elevator system where people waiting on different floors have priority based on urgency. Write a system that uses PriorityQueue to manage whom to pick first.",
      "Convert a FIFO customer service queue into a PriorityQueue based on customer seniority. Each customer has arrival time and priority. Implement the dequeue logic.",
      "Simulate real-time operating system process scheduling using PriorityQueue. Each process has arrival time and priority. Complete the schedule() method.",
      "Build a server request handler using PriorityQueue to handle high-priority requests faster. Each request has: int id, int priority. Implement enqueue and dequeue methods.",
      "Write a method that merges two PriorityQueues and returns a single PriorityQueue maintaining order.",
      "Use PriorityQueue to simulate bandwidth allocation, where streams with higher priority get processed first. Stream has id and priority.",
      "Simulate a file download queue where files are downloaded based on priority using PriorityQueue. Class FileDownload { String name; int priority; }",
      "Implement a Scheduler class that supports addTask(priority, task) and getNextTask(). Use PriorityQueue to store tasks.",
      "Write a method that removes all elements below a certain priority threshold from a PriorityQueue.",
      "Implement a PriorityQueue where priorities change over time (decaying priority). Write logic for time-based priority recalculation.",
      "Given a set of customer support tickets with severity levels, implement a ticket system using PriorityQueue that always picks the most severe ticket first.",
      "Implement a MovieStreamingQueue where movies are added with priority score based on user demand. Write methods to stream the next most popular movie.",
      "Convert the following standard Queue implementation of call center management into a priority-based model. Each call has waitTime and urgency.",
      "Using PriorityQueue, implement a leaderboard system that always keeps the top 10 scorers. Write insert and getTop10 methods.",
      "Modify the following Python FIFO queue implementation into one using heapq to manage tasks with priority.\nqueue = collections.deque()\n# replace this with heap-based queue logic",
      "Simulate a restaurant waitlist where VIP customers (priority) get seats before regular ones using PriorityQueue. Class: Customer { name, isVIP }.",
      "Given tasks with different execution times and priority, implement a PriorityQueue to minimize waiting time.",
      "Complete a Java method that pops all elements from a PriorityQueue until the sum of values exceeds a threshold. public List<Integer> extractUntilSum(PriorityQueue<Integer> pq, int threshold) { // Your code }",
      "Simulate a warehouse packing system where items with higher shipping priority are packed first. Implement enqueue and processing logic using PriorityQueue.",
      "Write a Python class PacketManager that uses heapq to simulate network packet prioritization.",
      "Create a market trading engine that uses a PriorityQueue to match buyers and sellers based on bid price. Write the matchOrders method.",
      "Build a stock price alerting system that uses a min-heap (PriorityQueue) to store the top k price drops.",
      "Implement a job execution queue using PriorityQueue where jobs can be rescheduled (priority updated). Write updatePriority method.",
      "Using a PriorityQueue, design a hiring system that always interviews the candidate with highest score. Candidate has: name, testScore.",
      "Write a simulation for a city ambulance dispatch system using PriorityQueue where patients with higher critical index are served first.",
      "Design a dual queue system where one queue is FIFO and another is a PriorityQueue. Implement a HybridQueue class to support switching modes.",
      "Implement a priority-aware download manager in Python where files with larger priority value get downloaded first. Use heapq.",
      "Write a streaming media buffer queue using PriorityQueue where most watched videos are played first.",
      "Implement an email scheduler where urgent emails are sent before normal ones using PriorityQueue.",
      "Given a class Transaction { int id; int priority; }, complete a PriorityQueue implementation to process high-priority transactions.",
      "Use a PriorityQueue to create a cache eviction policy that removes the least frequently used item first. Write add and evict methods.",
      "Build a dynamic dispatch queue that switches from FIFO to priority when load exceeds threshold. Write switchMode and dispatch methods.",
      "Design an intelligent traffic light queue using PriorityQueue where emergency vehicles pass first. Implement vehicle enqueue and process.",
      "Create a hospital emergency room system where patients are triaged into a PriorityQueue based on urgency and arrival time."
]
},









  }
  }

    }
   
def generate_queue_question(difficulty):
    initial_elements = random.sample(range(1, 20), random.randint(3, 6))
    ops = []

    for _ in range(random.randint(3, 5)):
        op = random.choice(queue_operations)
        if op == "enqueue":
            ops.append(f"enqueue({random.randint(20, 50)})")
        elif op == "dequeue":
            ops.append("dequeue()")
        elif op == "peek":
            ops.append("peek()")
        elif op == "isEmpty":
            ops.append("isEmpty()")
        elif op == "isFull":
            ops.append("isFull()")

    combined_questions = (
        queue_topics["Queue"]["subtopics"]["Introduction"][difficulty] +
        queue_topics["Queue"]["subtopics"]["FIFO Principle in Queues"][difficulty] +
        queue_topics["Queue"]["subtopics"]["Real-Life Applications of Queues"][difficulty] +
        queue_topics["Queue"]["subtopics"]["Stack vs Queue"][difficulty] +
        queue_topics["Queue"]["subtopics"]["Queue vs Deque"][difficulty] +
        queue_topics["Queue"]["subtopics"]["Queue vs Priority Queue"][difficulty] 
       
    )

    question = random.choice(combined_questions).format(
        initial_elements=initial_elements,
        operations=", ".join(ops),
        data_type=random.choice(data_types),
        size=random.randint(3, 6),
        duration=f"{random.randint(5,15)} mins"
    )
    return question
