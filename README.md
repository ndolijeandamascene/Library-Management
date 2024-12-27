# Library Book Reservation and Borrowing System

This project is a Python-based **Library Book Reservation and Borrowing System** that utilizes data structures like Binary Search Tree (BST), MinHeap, Circular Queue, and standard Queues to manage library operations. The system is designed to handle common library tasks such as book reservations, borrowing, and tracking books efficiently.

---

## Features

1. **Binary Search Tree (BST) for Book Search**
   - Books are stored and searched using their ISBN for fast retrieval.
2. **MinHeap for Reservation Priority Management**
   - Prioritize reservations based on user-defined priorities.
3. **Circular Queue for Borrowed Books**
   - Efficiently manage borrowed books with a fixed capacity queue.
4. **Hierarchical Data Representation**
   - Books are categorized and displayed using a tree structure.
5. **Heap Sort**
   - Sort reservations or books based on priority for better management.
6. **Dynamic Queue for Reservation Tracking**
   - Allows dynamic addition and removal of reservations.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.  
  Check by running:
  ```bash
  python --version
**Installation**
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/library-system.git
Navigate to the project directory:

bash
Copy code
cd library-system
Run the script:

bash
Copy code
python index.py
**Usage**
**Book Creation**
Add books to the system by creating instances of the Book class:

python
Copy code
book1 = Book(1001, "Things Fall Apart", "Chinua Achebe", True)
**Add to Data Structures**
Insert books into the BST, MinHeap, or Circular Queue based on the operation.

**Execute Borrowing and Reservations**
Test the borrowing and reservation workflows with enqueue/dequeue operations:

python
Copy code
cq.enqueue(book1)
dequeued_book = cq.dequeue()
print(f"Dequeued book: {dequeued_book.title}")
Run Sorting and Hierarchical View
Use Heap Sort to prioritize data and the Tree structure to organize categories.

**Project Structure**
plaintext
Copy code
library-system/
│
├── index.py       # Main script
├── README.md      # Documentation
└── data_structures/
    ├── bst.py     # Binary Search Tree implementation
    ├── heap.py    # MinHeap and Heap Sort implementation
    ├── queue.py   # Circular Queue and Dynamic Queue implementation
    └── tree.py    # Hierarchical Tree implementation
Example Output
plaintext
Copy code
Found Book: 1984 by George Orwell
Sorted Reservations by Priority:
- User 2 with priority 1
- User 1 with priority 2
- User 3 with priority 3

Dequeued book: The Great Gatsby
Books in Fiction Category:
- The Great Gatsby
- 1984
Contributing
Contributions are welcome!

Fork the repository.
Create a new branch for your feature (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, feel free to reach out:

Name: Ndoli Jean Damascene
Email: ndolijeandamascene@gmail.com



