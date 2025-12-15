# Count Mentions Per User (LeetCode 3433)

## 🧩 Problem Overview

You are given a list of **events** in a chat system with multiple users. Each event happens at a specific time and can either:

* A **MESSAGE** event — mentions users
* An **OFFLINE** event — makes a user offline for **60 minutes**

Your task is to calculate **how many times each user is mentioned** across all message events, considering users' **online/offline status** rules.

---

## 📌 Rules

1. There are `numberOfUsers` users, labeled from `0` to `numberOfUsers - 1`.
2. All users are **online initially**.
3. When a user goes **OFFLINE at time `t`**, they come back **online at time `t + 60`**.
4. Events must be processed in **time order**.
5. If two events occur at the same time:

   * **OFFLINE events are processed before MESSAGE events**.

---

## 📨 MESSAGE Types

Each MESSAGE event contains one of the following:

### 1. `"ALL"`

Mentions **all users**, whether they are online or offline.

### 2. `"HERE"`

Mentions **only users who are online** at that time.

### 3. Specific user mentions

A space-separated list like:

```
"0 2 3"
```

Mentions only those users.

---

## 🔢 Input Format

```text
numberOfUsers: int
events: List[List[str]]
```

Each event is of the form:

```text
[type, time, data]
```

---

## 📤 Output Format

```text
List[int]
```

Where the value at index `i` represents how many times **user `i` was mentioned**.

---

## ✅ Example 1

### Input

```text
numberOfUsers = 3
events = [
  ["MESSAGE", "2", "HERE"],
  ["OFFLINE", "2", "1"],
  ["OFFLINE", "1", "0"],
  ["MESSAGE", "61", "HERE"]
]
```

### Step-by-step Explanation

| Time | Event        | Explanation                            |
| ---- | ------------ | -------------------------------------- |
| 1    | OFFLINE 0    | User 0 goes offline until time 61      |
| 2    | OFFLINE 1    | User 1 goes offline until time 62      |
| 2    | MESSAGE HERE | Only user **2** is online → +1         |
| 61   | MESSAGE HERE | Users **0 and 2** are online → +1 each |

### Output

```text
[1, 0, 2]
```

---

## ✅ Example 2

### Input

```text
numberOfUsers = 2
events = [
  ["MESSAGE", "1", "ALL"],
  ["OFFLINE", "2", "0"],
  ["MESSAGE", "3", "HERE"]
]
```

### Explanation

* First message mentions **both users**.
* User 0 goes offline at time 2.
* Second message mentions only **user 1**.

### Output

```text
[1, 2]
```

---

## 🛠️ Key Implementation Tips

* Sort events by:

  ```python
  (time, type == "MESSAGE")
  ```

  so OFFLINE events are handled first.

* Track:

  * `online[i]` → whether user `i` is online
  * `online_until[i]` → time when user comes back online

* Before each event, **restore users** whose offline time has expired.

---




