# Python Runtime Architecture

## High-Level Design (HLD)

1. **Program Start** → A new process is created by the OS, and Python initializes its interpreter. 
2. The interpreter creates **main thread** → builds **Main Frame** → loads global namespace. 
3. Code executes line by line by the **Python Virtual Machine (PVM)** after being compiled into **bytecode**. 
4. Function calls create new stack frames → pushed to the **call stack**. 
5. Once the stack is empty and no threads are alive, the interpreter finalizes and exits.

### Key Components 
- **Parser → Compiler → PVM pipeline:** - Source code → AST → Bytecode → Execution. 
- **Call Stack:** manages function calls and stack frames. 
- **Heap:** stores all objects (mutable and immutable). 
- **Garbage Collector:** handles reference counting + cyclic GC.
- **Threading and GIL:** ensures only one thread executes Python bytecode at a time. 
- **AsyncIO loop:** manages coroutines and event loops for async operations.

---

## Low-Level Design (LLD)

### Call Stack and Stack Frames 
- Each function call creates a **stack frame** containing: 
    - Local variables 
    - Return address 
    - Instruction pointer (where to resume after returning) 
- Managed by the **interpreter loop** (ceval.c in CPython). 
- Frames are linked (each has a pointer to its previous frame). 
- Stack frames are destroyed when functions return.

### Heap and Object Model 
- Python stores all data (even numbers and functions) as **objects** on the heap. 
- Stack holds references to those heap objects. 
- **Reference counting**: every object keeps track of how many references exist to it. 
- When refcount = 0 → garbage collector reclaims it.
- For circular references (e.g., self-referencing objects), Python’s **cyclic GC** detects and frees them.

### Global Interpreter Lock (GIL) 
- CPython’s GIL ensures only one thread executes Python bytecode at a time. 
- Prevents race conditions on reference counts. 
- Multithreading helps for I/O-bound tasks, not CPU-bound. 
- Multiprocessing bypasses GIL by creating separate interpreter processes.

### Runtime Environment 
- The runtime environment includes: 
    - **Python standard library (stdlib)** for I/O, networking, async, etc. 
    - **Interpreter state** (PyInterpreterState) 
    - **Thread states** (PyThreadState) 
    - **Event loop (asyncio)** for async functions.
- External C extensions can register runtime hooks, similar to Web APIs in JS.

### Event Loop and AsyncIO 
- Python async runtime is built using **asyncio** module. 
- **Eventloop** runs coroutines (async def functions) using cooperative multitasking. 
- Uses **await** to yield control back to loop until awaited task completes. 
- Internally uses **Task/Future** objects stored in queues (like JS microtasks). 
- Loop constantly checks pending tasks and executes when ready.

### Closures and Variable Lifetime 
- Functions remember variables from enclosing scopes (closure behavior). 
- Variables captured by closures stay alive on the heap as long as the closure exists. 
- Once no more references remain, GC cleans them up.

---

## Example Code Flow

```python 
import asyncio

async def greet_after(delay, msg): 
    await asyncio.sleep(delay) 
    print(msg)

async def main(): 
    print("Start") 
    await greet_after(2, "Hello after 2s") 
    print("End")

asyncio.run(main()) 
```

**Step-by-step Execution:**
1. Program starts → interpreter initialized → main thread & frame created. 
2. `asyncio.run()` creates event loop → schedules `main()` coroutine. 
3. Inside `main()`: - Prints “Start” synchronously. - Calls `greet_after()` which schedules a coroutine → yields control with `await`. 
4. Event loop suspends `main()` and runs `asyncio.sleep()` asynchronously. 
5. After 2s → event loop resumes `greet_after()` → prints message. 
6. Control returns to `main()` → prints “End”. 
7. Event loop closes, interpreter exits.

---

### Key Differences from JavaScript Runtime

| Concept | JavaScript | Python | 
|----------|-------------|--------| 
| Execution Engine | V8, SpiderMonkey | CPython (C eval loop) | 
| Translation | JIT (bytecode + native) | Bytecode interpreted | 
| Async Model | Event Loop + micro/macrotasks | Event Loop (asyncio), cooperative coroutines | 
| Threading | Single-threaded, event-driven | GIL-limited threading | 
| Memory | Stack + Heap | Stack (refs) + Heap (objects) | 
| Closures | Lexical environments | Function cell variables | 
| Garbage Collection | Mark & Sweep | Ref counting + cyclic GC |

---

## Summary
- Python runtime = **interpreter + memory + async system + GC**. 
- All code executes in stack frames; objects live in heap. 
- Async uses **event loop (asyncio)** similar to JS’s event loop. 
- GIL limits concurrent CPU-bound execution. 
- Garbage collector ensures automatic memory management.