# Ojectives of this lession - Class - 4
**Learn all about List**<br>
**Constants**<br>
# Python Collections (Arrays)
There are four collection data types in the Python programming language:
Ordered List :-
1. **List** is a collection which is ordered and changeable. Allows duplicate members.
2. **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
3. **Set** is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. **Dictionary** is a collection which is ordered** and changeable. No duplicate members.


## List
```
mylist = ["apple", "banana", "cherry"]
```
List is a collection which is ordered and changeable. Allows duplicate members.<br>
Lists are created using square brackets<br>
List items are indexed, the first item has index [0], the second item has index [1] etc.<br>
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.<br>
If you add new items to a list, the new items will be placed at the end of the list.<br>
**Mutable**, The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.<br>
Since lists are indexed, lists can have items with the same value - duplicate allowed,<br>
```
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
```
List items can be of any data type, A list can contain different data types,<br>
```
list = ["apple", True, 5]
```
From Python's perspective, lists are defined as objects with the data type 'list'<br>
```
<class 'list'>
```

<br>List can be accessed using positive index or negative index, list[0]  present the first item and list[-1] refers to last item.<br>
Index can be range using [start:end -1],  start index value included but end index is not included when specify the range<br>

Check if item exist using if and in or not in  keywords <br>
```
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
```
list has different function as below<br>
***insert***<br>
***append***<br>
***extend***<br>
***remove***<br>
***pop***<br>
***clear***<br>
***sort***<br>
***reverse***<br>
***copy***<br>


## Tuple
```
mytuple = ("apple", "banana", "cherry")
```
## Set
```
myset = {"apple", "banana", "cherry"}
```
## Dictionary
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```
