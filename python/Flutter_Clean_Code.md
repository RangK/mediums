원본글 : https://medium.com/@santhosh-adiga-u/flutter-clean-code-ba4df36cb40c
저자 : Santhosh Adiga U

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

> Bad Code
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
```

> Clean Code
``` Dart
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

## Modularization:
Breaking down the app into smaller, reusable, and independent modules/components that are easier to understand, maintain, and test. 
For example, separating UI components, business logic, data access logic, and dependencies into separate modules/packages.

> 프로그램을 더 작고, 재사용 가능하며 서로 독립적인 Module 또는 Component들로 나누는 것은 이해하고, 관리하고, 테스트하기 쉽게 만들어 줍니다.
> 예를 들어, UI Components, Business Logic, Data Access Logic와 의존성들을 나누어 별개의 Module과 Package로 만듭니다.

``` Dart
// Example of modularization in Flutter

// Bad practice - Everything in the same file
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // App configuration
    );
  }
  
  // UI components
  Widget buildHomePage() {
    // Home page UI
  }
  
  // Business logic
  void fetchUserData() {
    // Fetch user data
  }
  
  // Data access logic
  void saveUserData() {
    // Save user data
  }
  
  // Dependencies
  void _initializeDependencies() {
    // Initialize dependencies
  }
}
```
``` Dart
// Good practice - Separating modules/components into separate files
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // App configuration
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Home page UI
  }
}

class UserDataBloc {
  // Business logic
  void fetchUserData() {
    // Fetch user data
  }
}

class UserDataRepository {
  // Data access logic
  void saveUserData() {
    // Save user data
  }
}

class Dependencies {
  // Initialize dependencies
}
```

## Test-Driven Development (TDD):
Writing tests for your code before writing the code itself, 
to ensure that the code behaves as expected and to catch any potential issues early in the development process.

> 코드 자체를 작성하기 전에 테스트를 작성하는 것은 그 코드가 예상대로 동작하고, 여러가지 어떤 잠재적 Issue들을 개발 단계에서 확인할 수 있도록 해줍니다.

``` Dart
// Example of TDD in Flutter

// Bad practice - No tests
class Calculator {
  int add(int a, int b) {
    return a + b;
  }
}
```
``` Dart
// Good practice - Writing tests first
class Calculator {
  int add(int a, int b) {
    return a + b;
  }
}

void main() {
  test('Test addition', () {
    Calculator calculator = Calculator();
    expect(calculator.add(2, 3), 5);
  });
}
```

## Use the Proper Flutter Architecture:
The Flutter framework supports several architectures, such as MVC, MVP, MVVM, and Clean Architecture. 
Choose the right architecture for your project based on its complexity and requirements.
Use the Flutter Bloc library to implement Clean Architecture in your project.

> Flutter Framework는 다양한 Architecture(e.g MVC, MVP, MVVM, Clean Arch)를 지원합니다.
> 복잡도와 요구사항을 기반으로 올바른 Architecture를 선택해야 합니다.
> Flutter Bloc Library 사용해서 당신의 Project를 Clean Archi로 구현할 수 있습니다.

Here are some ways in which Bloc can help implement Clean code in a Flutter app:

> Bloc을 사용해 Flutter App에 Clean Code를 구현하는 방법 몇 가지를 소개합니다.

Separation of concerns: Bloc allows you to separate the business logic and presentation logic of your app into distinct classes. 
You can create separate bloc classes for handling different aspects of your app’s functionality, such as authentication, data fetching, and state management. 
This helps in keeping your codebase modular and maintainable.

> Separation of concerns(관심사 분리) : Bloc을 사용해 Business Logic과 Presentation Logic을 서로 다른 Class로 분리할 수 있습니다.
> 그리고 프로그램(App)의 기능들을 서로 다른 관점으로 제어하할 수 있도록 bloc class를 분리시킬 수 있습니다. 예로 인증, 데이터 수집, 상태 관리 등...
> SoC는 당신의 코드의 모듈성과 유지보수성을 유지하는데 도움을 줍니다.

Single Responsibility Principle (SRP): Bloc enforces the SRP, one of the principles of Clean Architecture, by allowing you to define separate blocs for different responsibilities. Each bloc can have a single responsibility, such as handling state management for a particular UI component or managing data fetching for a specific feature. This makes it easier to understand and manage the logic for each individual feature or component in your app.

> Single Responsibility Principle (단일 책임 원칙) : 다른 책임에 따라 각각의 Bloc들을 분리 정의하는 것으로 Clean Archi의 원칙 중 하나인 SRP를 확보할 수 있게 해줍니다.
> 예를 들어 특정 UI Component의 상태 관리를 제어하거나, 특정 Feature의 Data Fetching 관리하는 책임을 각각의 Bloc이 가지도록 할 수 있습니다.
> 이 방법은 각 Feature 와 Component에 대한 Logic을 이해하고 관리하는 것을 더 쉽게 만들어 줍니다. 

Dependency Inversion Principle (DIP): Bloc encourages the use of dependency injection, which is a key principle of Clean Architecture. 
You can inject dependencies into your bloc classes, making it easy to swap out implementations for testing or changing requirements. 
This allows you to decouple your business logic from external dependencies, such as APIs or databases, making your code more flexible and testable.

> Dependency Inversion Principle (의존성 역전) : Bloc은 Dependency Injection(의존성 주입, Aka. DI)의 사용을 적극 권장합니다. 이 기술은 Clean Arch의 핵심 원칙이죠.
> 테스트 또는 요구사항 변경을 위해 구현부의 변경이 발생 했을 때 이 문제를 쉽게 해결 할 수 있도록 bloc class들에 의존성을 주입할 수 있습니다.
> DI는 외부 의존성들로 부터 Business Logic을 분리시킬 수 있습니다.(예를 들어 APIs, Database) Business Logic의 분리는 코드를 더 유연하고 테스트 가능한 상태로 만들어 줍니다.

Unidirectional data flow: Bloc follows the unidirectional data flow pattern, where the UI sends events to the bloc, 
the bloc processes the events and updates the state, and the UI reacts to the state changes. 
This clear flow of data helps in maintaining a predictable and manageable state in your app, 
and makes it easier to reason about the flow of data and business logic.

> Unidirectional data flow (단방향 데이터 흐름) : Bloc은 단방향 데이터 흐름 원칙을 따릅니다. UI가 bloc으로 이벤트를 전달하고, bloc이 event를 처리한 후 상태를 업데이트 합니다.
> UI는 상태 변화를 반영합니다.
> 정리 : UI -- Event --> bloc -- Processing --> New State -- Update --> UI
> 명확한 데이터 흐름은 관리가능하고 예측가능한 상태를 유지할 수 있도록 만들어 줍니다.
> 그리고 Business Logic과 데이터 흐름의 원인을 쉽게 파악할 수 있습니다.

Testing: Bloc makes it easier to write unit tests for your business logic 
because it provides clear separation of concerns and follows the principles of Clean Architecture.
You can write unit tests for each bloc independently, mocking the dependencies, and testing the expected behavior of each bloc in isolation.
This allows for comprehensive testing of your app’s business logic, leading to more reliable and maintainable code.

> 테스트팅(Testing) : Bloc은 Business Logic의 Unit Test(단위테스트)를 작성하는 것을 쉽게 만들어 줍니다. 이유는 Bloc을 사용하게되면 관심사 분리가 명확해지고 Clean Arch 원칙을 잘 따르게 되기 때문입니다.
> 각 bloc들을 독립적으로 테스트하는 단위 테스트를 작성할 수 있고, 의존성을 모의로 주입하거나 각 Bloc의 기대 행동을 독립적으로 테스트 할 수 있습니다.
> 프로그램의 Business logic의 testing을 이해하고 더 높은 신뢰성과 유지보수성을 가지는 코드를 만들어 낼 수 있습니다.
