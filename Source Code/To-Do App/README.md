# To-Do App (GUI Programming & Data Persistence)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python ToDoApp.py
```

> **Note**: On Ubuntu/Linux, you may need to install Tkinter: `sudo apt install python3-tk`

## 1. Definition
A **To-Do Application** is a task management utility that allows users to create, read, update, and delete (CRUD) records. This implementation uses **Tkinter** for the graphical user interface and **Pickle** for binary serialization and data persistence.

## 2. Mathematical Explanation
The data model is a key-value store implemented as a hash map:

$$
DB: K \rightarrow R
$$

Where:
- $K$: Set of unique string keys
- $R$: Set of record tuples $(key, name, description, status)$

Operations follow standard hash table complexity:
- **Fetch**: $O(1)$ average case
- **Update**: $O(1)$ average case
- **Delete**: $O(1)$ average case

## 3. Computer Science Theory
- **Event-Driven Programming**: Tkinter uses a main loop that waits for and responds to user events (button clicks, key presses).
- **Serialization (Pickle)**: Python's `pickle` module converts objects to a byte stream for storage, enabling persistent data across sessions.
- **MVC Pattern**: The implementation separates concerns with a Service layer (Model), GUI class (View), and event handlers (Controller).
- **CRUD Operations**: The four fundamental database operations—Create, Read, Update, Delete—form the basis of most data-driven applications.

## 4. Python Implementation Logic
- **Service Pattern**: `ToDoService` encapsulates all data operations, making the code testable and maintainable.
- **Tkinter Grid Layout**: Uses `grid()` geometry manager for precise widget placement.
- **Error Handling**: Provides user feedback via `messagebox` dialogs for success and error states.
- **File Initialization**: Automatically creates the database file if it doesn't exist.

## 5. Visual Representation

```mermaid
graph TD
    A[User Action] --> B{Action Type}
    B -->|Fetch| C[Load DB from Pickle]
    C --> D[Lookup Key in Hash]
    D --> E[Display in GUI Fields]
    B -->|Update| F[Read GUI Fields]
    F --> G[Save to Hash]
    G --> H[Serialize to Pickle]
    B -->|Delete| I[Remove from Hash]
    I --> H
    B -->|Quit| J[Close Application]
```

```mermaid
classDiagram
    class ToDoService {
        +db_file: str
        +fields: tuple
        +fetch(key) Record
        +update(record) bool
        +delete(key) bool
    }
    class ToDoAppGUI {
        +service: ToDoService
        +entries: Dict
        +run() void
    }
    ToDoAppGUI --> ToDoService : uses
```

## 6. Screenshots

### Application Screen
![To-Do App Main Screen](Output/ToDoApp_Screen.png)

### Input Data
![Entering Task Data](Output/ToDoApp_Input.png)

### Update Confirmation
![Update Success Message](Output/ToDoApp_Update.png)

### Fetch Record
![Fetching Saved Record](Output/ToDoApp_Fetch.png)
