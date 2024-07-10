# 0x10-python-network_0

## Table of Contents
1. [cURL body size](#curl-body-size)
2. [cURL to the end](#curl-to-the-end)
3. [cURL Method](#curl-method)
4. [cURL only methods](#curl-only-methods)
5. [cURL headers](#curl-headers)
6. [cURL POST parameters](#curl-post-parameters)
7. [Find a peak](#find-a-peak)

## Tasks

### 1. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

- The size must be displayed in bytes.
- You have to use `curl`.

```sh
#!/bin/bash
# Script to get the body size of a response from a URL
curl -s "$1" | wc -c
```

**Usage:**
```sh
./0-body_size.sh 0.0.0.0:5000
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `0-body_size.sh`

### 2. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

- Display only the body of a 200 status code response.
- You have to use `curl`.

```sh
#!/bin/bash
# Script to get the body of a 200 status code response
curl -sL "$1"
```

**Usage:**
```sh
./1-body.sh 0.0.0.0:5000/route_1
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `1-body.sh`

### 3. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

- You have to use `curl`.

```sh
#!/bin/bash
# Script to send a DELETE request and display the response body
curl -sX DELETE "$1"
```

**Usage:**
```sh
./2-delete.sh 0.0.0.0:5000/route_3
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `2-delete.sh`

### 4. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use `curl`.

```sh
#!/bin/bash
# Script to display all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
```

**Usage:**
```sh
./3-methods.sh 0.0.0.0:5000/route_4
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `3-methods.sh`

### 5. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.

- A header variable `X-School-User-Id` must be sent with the value `98`.
- You have to use `curl`.

```sh
#!/bin/bash
# Script to send a GET request with a custom header
curl -sH "X-School-User-Id: 98" "$1"
```

**Usage:**
```sh
./4-header.sh 0.0.0.0:5000/route_5
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `4-header.sh`

### 6. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

- A variable `email` must be sent with the value `test@gmail.com`.
- A variable `subject` must be sent with the value `I will always be here for PLD`.
- You have to use `curl`.

```sh
#!/bin/bash
# Script to send a POST request with specific parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
```

**Usage:**
```sh
./5-post_params.sh 0.0.0.0:5000/route_6
```

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `5-post_params.sh`

### 7. Find a peak
Write a function that finds a peak in a list of unsorted integers.

- Prototype: `def find_peak(list_of_integers):`
- You are not allowed to import any module.
- Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak).
- `6-peak.py` must contain the function.
- `6-peak.txt` must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n^2).

```python
def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
```

**Complexity:**
- `6-peak.txt`: O(log(n))

**Repository:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `6-peak.py`, `6-peak.txt`
