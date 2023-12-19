## 제목 : 87 Lesser-known Python Features

If you’ve been using Python for years and know enough to get the job done, it’s probably not a wise use of your time to read through several thousand pages of documentation just to maybe discover a handful of new tricks. So I’ve put together a short (by comparison) list of features that aren’t widely used, but are widely applicable to general programming tasks.

> 만약 당신이 Python을 몇 년 동안 사용해 왔고, 주어진 업무를 수행함에 있어서 충분한 지식을 가지고 있다면
> 새로운(유용한) 몇 가지 기술과 지식을 얻기 위해서 수천 페이지의 문서들을 읽는 것은 시간을 현명하게 사용하는 것이 아닐 겁니다.
> 그래서, 내가 일반적인 개발 업무에서 폭넓게 사용될 수 있지만 실제로 많이 사용되지 않는(혹은 많은 사람들이 잘 모르는) 특징들을 
> 짧은 목록으로 정리하였습니다.

This list will of course contain some stuff you already know and have a sprinkling of things you’ll never use, but among them, I hope there are a few that are new and useful to you.

> 물론 이 목록은 당신이 이미 알고 있는 것들도 포함되어 있을 것이고, 당신은 절대 사용하지 않을 것들이 잔뜩 있을 수 있습니다.
> 하지만, 그것들 가운데 몇 가지는 당신에게 유용하고 새로운 것이길 희망 합니다.

First, a bit of housekeeping:
> 먼저, 이 글을 시작하며..

1. I’ll assume you’re on at least Python 3.8. For the few features added after this, I’ll mention when they were added.
2. There’s no strict order to the list, but the more basic features are toward the start.
3. Wherever you see assert on this page, you can assume that the assert passes.
4. If you would like to quench my curiosity, you can highlight the titles of the ones you find useful.
Now, on to the list…

> 1. 당신이 Python 3.8 이상을 사용 중일 것으로 가정 합니다. 몇 가지 특징들은 3.8 이후에 추가된 것들이 있으며 따로 언급할 것 입니다.
> 2. 이 글의 작성된 내용은 특별한 순서가 없지만, 최대한 기본적인 특징들부터 작성되었습니다.
> 3. 이 글에서 "assert" 구분을 보게 된다면, "assert" 구문은 통과된 것으로 가정할 수 있습니다.
> 4. 만약 더 자세한 설명(궁금증을 해소해야 할 부분)이 있다면, 제목을 표시할 수 있습니다.

이제 시작합니다.

### 1. help(x)
help can take a string, an object, or anything. For class instances, this will collect methods from all parent classes, and show you what is inherited from where (and the method resolution order for methods).

This is also useful when you want help on something that’s hard to search for, like or. Typing help('or') will be much faster than trying to find the part of the Python docs that describes how or works.

> help 함수는 "string", "object" 또는 어떤 형태의 데이터든 입력할 수 있습니다. Class Instance의 경우,
> 모든 부모 Class의 함수들을 모아서, 어떤 Class들이 상속 구조를 가지는 지 설명한다.
> 이 기능을 Python Doc에서 검색하기 어려운 정보를 빠르게 확인할 때 유용하다.
> ex : or

### 7. attrgetter and itemgetter
if you need to sort a list of objects by a sepcific property of those objects, you can use `attrgetter` (when the value you're after is an attribute, e.g. for class instances) or `itemgetter` (when the value you're after is an index or ditionary key).

>  list 객체를 특정 속성으로 정렬해야할 때, `attrgetter` (사용할 값이 attribute 일때, 예 : class instances) 또는 `itemgetter` (List의 Index 도는 Dictionary의 key를 하용할 때)를 이용할 수 있습니다.

For example, to sort a list of dicts by the `score` key of the dicts:

> 아래의 예제는, Ditionary를 값으로 가지는 List를 Dictionary의 `score` 키로 정렬합니다.

``` python
for operator import itemgetter
scores = [
    {"name": "Alice", "score": 12},
    {"name": "Bob", "score": 7},
    {"name": "Charlie", "score": 17}
]

scores.sort(key=itemgetter("score"))

assert list(map(itemgetter("name"), scores)) == ["Bob", "Alice", "Charlie"]

```

`attrgetter` is similar, used when you would otherwise use dot notation. This can do nested access too, such as `name.first` in the example below:

> `attrgetter`도 비슷하지만 다른 점은 `내부 참조`가 가능하다는 것 입니다. 아래 예제의 `name.first` 처럼 사용할 수 있습니다.

``` python
from operator import attrgetter
from typing import NamedTuple

class Name(NamedTuple):
    first: str
    last: str

class Person(NamedTuple):
    name: Name
    height: float

people = [
    Person(name=Name("Gertrude", "Stein"), height=1.55),
    Person(name=Name("Shirley", "Temple"), height=1.57),
]

first_names = map(attrgetter("name.first"), people)

assert list(first_names) == ["Gertrude", "Shirley"]
```

There's also a `methodcaller` that does what you might guess.

> 기능의 존재를 예측하고 실행시킬 수 있는 `methodcaller`도 있습니다.

### 8. Operators as functions
All the familiar operators like `+`, `<`, `!=` have functional equivalents in the `operator` module. These are usefull if you're iterating over collections, for example looking for a mismatch between two lists using `is_not`:

> `+`, `<`, `!=`와 같은 모든 operator(연산자)들은 `operator` module 안에 동일한 기능을 하는 함수들이 존재합니다.
> 아래의 예는 두 List 객체를 비교해 서로 다른 값을 찾는 `is_not` 함수 사용을 보입니다.

``` python
import operator

list1 = [1, 2, 3, 4]
list2 = [1, 2, 7, 4]
matches = list(map(operator.is_not, list1, list2))

assert matches == [False, False, True, False]
```

### 9. Sorting a dictionary by its values
You can use `key` to sort a dict by its values. In this case, the function that you pass to `key` will be called with each key of the dict and return a value, which is what the `get` method of a dictionary does.

> Sorted 함수를 이용해 Dict 객체를 정렬할 때, 정렬 기준으로 `key` parameter를 사용할 수 있습니다. 이 경우에 `key` parameter로 전달하는 함수는 Dict 객체의 `key`를 입력 받고 해당하는 `value`를 반환해야 합니다. Dict객체에서 이 역할을 하는 함수가 `get` method 입니다.

``` python
my_dict = {
    "Plan A": 1,
    "Plan B": 3,
    "Plan C": 2
}

my_dict = {key: my_dict[key] for key in sorted(my_dict, key=my_dict.get)}
assert list(my_dict.keys()) == ["Plan A", "Plan C", "Plan B"]
```

### 10. Create a dict from tuples
`dict()` can take a sequence of tuples of key/value pairs. So if you have lists of keys and values, you can zip them together to turn them into a dictionary:

> `dict()` 함수는 key와 value을 쌍으로 가지는 Tuple(or List)의 목록을 사용해서 Dict 객체를 만듭니다. 만약 key와 value에 해당하는 값을 각각 List 객체로 가지고 있다면 아래의 예 처럼 `zip`함수를 사용할 수 있습니다.

``` python
keys = ["a", "b", "c"]
vals = [1, 2, 3]

assert dict(zip(keys, vals)) == {"a": 1, "b": 2, "c": 3}
# Append
assert dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
```

### 11. Combining dicts with **
You can combine dictinoaries by using the `**` operator to unpack the dicts into the body of a dict literal:

> Dict 객체를 하나의 Dict 객체의 literal 값으로 만들기 위해 `**` operator를 사용할 수 있습니다.

``` python
sys_config = {
    "Option A": True,
    "Option B": 13
}

user_config = {
    "Option B": 33,
    "Option C": "yes"
}

config = {
    **sys_config,
    **user_config,
    "Option 12": 700
}
```


