<style>
    summary {
        cursor: pointer;
    }
    
    .spoiler {
        opacity: 0;
        transition: all 300s ease-in;
    }
    .spoiler:hover {
        opacity: 1;
        transition: all 0.5s;
    }
</style>

# List Comprehension

A way to create lists from already existing Iterables (like other lists or ranges)

### syntax

```python
new_list = []
for item in Iterable:
    new_list.append(expression)
```

<div class="spoiler">

```python
new_list = [expression for item in Iterable]
```

</div>

And

```python
new_list = []
for item in Iterable:
    if condition:
        new_list.append(expression)
```

<div class="spoiler">

```python
new_list = [expression for item in Iterable if condition]
```

</div>

## Examples

**All numbers ** 2**

```python
numbers = [1, 5, 4, 3, 6, 7, 8, 9, 2]
even_numbers = [x ** 2 for x in numbers]

print(even_numbers)
```

**Even numbers**

```python
numbers = [1, 5, 4, 3, 6, 7, 8, 9, 2]
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```

<details>
<summary><b>Even Numbers ** 2</b>
</summary>

```python
numbers = [1, 5, 4, 3, 6, 7, 8, 9, 2]
even_numbers = [x ** 2 for x in numbers if x % 2 == 0]

print(even_numbers)
```

</details>

<details>
<summary><b>All names to lowercase</b>
</summary>

```python
usernames = ['Pyth0n_P4rty', 'Sn4ke_Ch4rmer', 'F1zz_Buzz', 'C0de_M0nkey', 'Py_D3v',
             'Fl4sk_M4ster', 'D4t4_Sc1ence', 'Py_G4me', 'M0nty_Pyth0n', 'Py_L0ver']

usernames = [name.lower() for name in usernames]

print(usernames)
```

</details>

## Mixing ternary operator and list comprehension

<details>
<summary><b>Turn odd numbers to 0</b>
</summary>

```python
numbers = [1, 5, 4, 3, 6, 7, 8, 9, 2]
even_numbers = [x if x % 2 == 0 else 0 for x in numbers]

print(even_numbers)
```

</details>
