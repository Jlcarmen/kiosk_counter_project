
# Kiosk Visit Counter – Stack-Dynamic vs Static Local Variables in Python

This project demonstrates the difference between **stack-dynamic variables** and **static local variables** using two simple Python functions. It simulates a kiosk tracking session visits and total usage throughout the day.

---

## Overview

In programming, **variable lifetime** and **storage duration** affect how data is stored and reused. This project showcases two types:

- `session_counter()` simulates a **stack-dynamic variable** – it resets every time the function is called.
- `kiosk_usage()` simulates a **static local variable** – it retains its value across multiple function calls.

---

## Code Explanation

### `session_counter()` – Stack-Dynamic Behavior

```python
def session_counter():
    counter = 0  # resets every time (stack-dynamic behavior)
    counter += 1
    print(f"Session visits: {counter}")
```

- The variable `counter` is **re-initialized to 0** every time the function is called.
- Mimics how stack-based variables work in many programming languages (e.g., C, Java).

**Output on every call:**
```
Session visits: 1
```

---

### `kiosk_usage()` – Static Local Variable Behavior

```python
def kiosk_usage():
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0  # only initialized once
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")
```

- `total_users` is attached as a **function attribute**, mimicking static variable behavior.
- It is **only initialized once**, and **persists across calls**.

**Example output:**
```
Total users today: 1
Total users today: 2
Total users today: 3
...
```




