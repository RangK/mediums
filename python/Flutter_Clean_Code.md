## Introduction:
Clean code is essential in every programming language to make the code more readable, maintainable, and understandable.\
The same is true for Flutter. Clean code practices in Flutter are the best way to ensure that your code is easy to understand,\
easy to maintain, and easy to modify. In this article, we will discuss some of the best clean code practices in Flutter with examples.

> Clean code는 모든 프로그래밍 언어에서 더 높은 수준의 Readable, Maintainable, Understandable 코드를 만들기 위한 필수적인 요소 입니다.
> Flutter에서도 마찬가지입니다. Flutter에서 Clean code를 사용하는 것은 코드를 이해하기 쉽고, 관리하기 쉽고, 수정하기 쉽게 만드는 가장 좋은 방법 입니다.
> 이 글에서 우리는 Flutter에 적용된 몇 가지 엄선된 Clean Code 사례를 예제와 함께 얘기해볼 예정 입니다.

## Follow Flutter Naming Conventions:
When writing code in Flutter, it is essential to follow the naming conventions recommended by the Flutter team.
Flutter follows the Dart language naming conventions. These conventions help other developers to understand your code easily.

> Flutter에서 코드를 작성할 때, Flutter Team에서 권장하는 Naming Conventions을 따르는 건 중요합니다.
> Flutter는 Dart 언어의 Naming Conventions를 따르며, 이 규치들은 당신의 코드를 다른 개발자들이 쉽게 이해할 수 있도록 도와줍니다.

Here is an example of how to name a class in Flutter:
> 여기 Class 이름을 정하는 예제가 있습니다.
``` Dart
// Good naming convention
class MyClass {}

// Bad naming convention
class my_class {}
```

## Use Descriptive Variable and Function Names:
Use descriptive variable and function names so that other developers can understand the purpose of the variable or function.
Avoid using generic names such as “data” or “value” as it does not convey the purpose of the variable or function.

> 변수와 함수 이름들을 서술적인 이름을 사용하게되면, 다른 개발자들이 변수와 함수의 목적을 이해할 수 있습니다.
> "data" 또는 "value"와 같은 일반적인 이름들의 사용하는 것은 목적을 전달하고 있지 않기 때문에 사용하지 마세요.

``` Dart
// Good variable name
final String fullName = 'John Doe';

// Bad variable name
final String name = 'John Doe';
```

## Use Proper Indentation and Formatting:
Proper indentation and formatting make the code more readable and understandable.
Use consistent indentation and formatting throughout the code. 
Use 2 or 4 spaces for indentation and keep the line length below 80 characters.

> 적절한 Indentation과 Formatting은 코드를 더 이해하고 읽기 쉽게 만들어 줍니다.
> 코드 전반에서 일관성있는 Indentation과 Formatting을 사용하세요.
> Indentation은 2 또는 4개의 space로 사용하고, 한줄의 길이는 80자를 넘지 않도록 하세요.

``` Dart
// Good indentation and formatting
void myFunction() {
  if (condition) {
    doSomething();
  } else {
    doSomethingElse();
  }
}

// Bad indentation and formatting
void myFunction() {if(condition){doSomething();}else{doSomethingElse();}}
```

## Use Comments to Explain Code:
Comments are essential to explain the code and its purpose. 
Use comments to explain complex code, business logic, or any other critical information that may be required by other developers.

> 코드와 프로젝트 자체의 목적을 설명하는 주석은 필수적인 요소 입니다.
> 복잡한 코드, Business Logic, 다른 개발자들에게 필요한 중요한 정보들을 설명하기 위해 주석을 사용하세요.

``` Dart
// Good comment
// This function calculates the sum of two integers
int sum(int a, int b) {
  return a + b;
}

// Bad comment
// Adds two numbers
int add(int a, int b) {
  return a + b;
}
```

## Single Responsibility Principle (SRP):
Each class or function should have a single responsibility and should not be responsible for multiple tasks. 
For example, separating UI components, business logic, and data access logic into separate classes.

> 각 Class 와 Function는 한 가지 책임만을 가져야 합니다. 여러가지 작업에 대한 책임을 가져서는 안됩니다.
> 예를 들어, UI 커포넌트들과 Business Logic, Data Access Logic을 여러개의 Class로 분리합니다.

``` Dart
// Example of SRP in Flutter

// Bad practice - UI component handling business logic and data access
class CounterScreen extends StatefulWidget {
  int count = 0;

  void incrementCounter() {
    // Business logic
    count++;
    // Update UI
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    // UI rendering
    return Text('Count: $count');
  }
}

// Good practice - Separating UI component, business logic, and data access
class CounterScreen extends StatelessWidget {
  final int count;
  final VoidCallback onIncrement;

  CounterScreen({required this.count, required this.onIncrement});

  @override
  Widget build(BuildContext context) {
    // UI rendering
    return Text('Count: $count');
  }
}

class CounterBloc {
  int count = 0;

  void incrementCounter() {
    // Business logic
    count++;
  }
}

class CounterRepository {
  int getCount() {
    // Data access logic
    // Fetch count from external source
    return 0;
  }

  void saveCount(int count) {
    // Data access logic
    // Save count to external source
  }
}
```
