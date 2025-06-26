import random

# Basic queue operations for templates
queue_operations = [
    "enqueue", "dequeue", "peek", "isEmpty", "isFull",
    "size", "clear", "front", "rear"
]

# Data types used in scenarios
data_types = [
    "integers", "characters", "strings", "customer IDs",
    "tasks", "print jobs", "URLs", "sensor readings", "tickets"
]

# Question templates categorized by topic and difficulty
queue_topics = {
    "Queue": {
        "subtopics": {
            "Introduction": {
              "easy" = [
    # 1. MCQ
    {
        "type": "MCQ",
        "question": "What is the time complexity of enqueue() in a queue implemented using an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
        "answer": "O(1)"
    },
    {
        "type": "MCQ",
        "question": "Which operation removes the front item from a queue?",
        "options": ["Push", "Enqueue", "Dequeue", "Peek"],
        "answer": "Dequeue"
    },

    # 2. MSQ
    {
        "type": "MSQ",
        "question": "Which of the following are valid queue operations?",
        "options": ["insertFront", "enqueue", "dequeue", "pushBack"],
        "answer": ["enqueue", "dequeue"]
    },
    {
        "type": "MSQ",
        "question": "Queues are used in:",
        "options": ["Printer Spooling", "Call Center Systems", "Backtracking Algorithms", "CPU Scheduling"],
        "answer": ["Printer Spooling", "Call Center Systems", "CPU Scheduling"]
    },

    # 3. Fill in the Blanks (FIB)
    {
        "type": "FIB",
        "question": "In a queue, elements are added at the ____ and removed from the ____.",
        "answer": ["rear", "front"]
    },
    {
        "type": "FIB",
        "question": "A queue follows the ____ principle.",
        "answer": "FIFO"
    },

    # 4. Numerical Answer Type (NAT)
    {
        "type": "NAT",
        "question": "If a queue has 3 elements and 2 dequeue operations are performed, how many elements remain?",
        "answer": 1
    },
    {
        "type": "NAT",
        "question": "A queue has capacity 5. Initially empty. After 4 enqueue and 1 dequeue, what's the size?",
        "answer": 3
    },

    # 5. True/False (TF)
    {
        "type": "TF",
        "question": "The peek() operation removes an element from the queue.",
        "answer": False
    },
    {
        "type": "TF",
        "question": "Circular queues can reuse empty spaces.",
        "answer": True
    },

    # 6. Match the Following
    {
        "type": "Match",
        "question": {
            "Enqueue": ["Add to front", "Remove from front", "Wraps around", "Follows LIFO"],
            "Dequeue": ["Add to front", "Remove from front", "Wraps around", "Follows LIFO"],
            "Circular Queue": ["Add to front", "Remove from front", "Wraps around", "Follows LIFO"],
            "Stack": ["Add to front", "Remove from front", "Wraps around", "Follows LIFO"]
        },
        "answer": {
            "Enqueue": "Add to front",
            "Dequeue": "Remove from front",
            "Circular Queue": "Wraps around",
            "Stack": "Follows LIFO"
        }
    },

    # 7. Assertion/Reason
    {
        "type": "AR",
        "question": {
            "assertion": "A queue is ideal for task scheduling.",
            "reason": "It uses FIFO where the first task gets executed first."
        },
        "options": [
            "A. Both A and R are true, R explains A",
            "B. Both are true, but R doesn’t explain A",
            "C. A is true, R is false",
            "D. A is false, R is true"
        ],
        "answer": "A"
    }
]
,
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
        
        }
    }
}

# Generator function
def generate_queue_question(difficulty: str) -> str:
    """
    Generates a queue-related question based on difficulty level.
    """
    initial_elements = random.sample(range(1, 20), random.randint(3, 6))
    ops = []

    for _ in range(random.randint(3, 5)):
        op = random.choice(queue_operations)
        if op == "enqueue":
            ops.append(f"enqueue({random.randint(20, 50)})")
        elif op in ["dequeue", "peek", "isEmpty", "isFull"]:
            ops.append(f"{op}()")

    # Gather all templates under the selected difficulty
    templates = []
    for subtopic in queue_topics["Queue"]["subtopics"].values():
        templates.extend(subtopic.get(difficulty, []))

    if not templates:
        return "No questions available for this difficulty."

    # Choose a template and fill placeholders
    template = random.choice(templates)
    question = template.format(
        initial_elements=initial_elements,
        operations=", ".join(ops),
        data_type=random.choice(data_types),
        size=random.randint(3, 6),
        duration=f"{random.randint(5,15)} mins"
    ) if '{' in template else template

    return question
