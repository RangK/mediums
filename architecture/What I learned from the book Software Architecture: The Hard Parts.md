## MEDIUM REVIEW
> 참조 : https://medium.com/@techworldwithmilan/what-i-learned-from-the-software-architecture-the-hard-parts-0498c9eae88e

### What I learned from the book Software Architecture: The Hard Parts

I recently read the book “ Software Architecture: The Hard Parts” by Neal Ford, Mark, Richards, Pramod Sadalage & Zhamak Dehghani, and this is my review of the book.

> 나는 최근에 읽은 "Software Architecture : The Hard Parts" (저자 : Neal Ford, Mark, Richards, Pramod Sadalaage & Zhamak Dehghani)라는 제목의 책을 리뷰하려고 한다.

The book emphasizes the step-by-step approach of breaking down monolith, with different patterns for each step, and balancing tradeoffs for those patterns. The book is titled “Hard Parts,” yet most of the book’s concepts are already familiar in the industry, and maybe a “breaking monolith to microservices” title would be a better fit.

> 이 책이 강조하는 내용은 단일 구조로 쪼깨서 단계별로 접근해야 하며, 각 단계는 서로 다른 패턴을 가지고 상호 가치 교환을 통해 균형을 잡아야 한다는 것 이다. 이 책이 가지고 있는 컨셉의 대부분은 S/W 산업에서 이미 익숙한 것들로, "Hard Parts"라는 제목을 가지고 있지만, 아마도 "breaking monolith to microservices"라는 제목이 더 적합해 보인다.

![image](https://github.com/RangK/mediums/assets/1219362/c986ecfb-bfc4-42ad-98b0-72f3b27ec2bc)

Throughout the book, the authors use the fictional story about the Sysops Squad to discuss architecture modularity, service granularity, distributed transactions, contracts, and more.

> 이 책을 전반에 걸쳐, 저자들은 "Architecture Modularity(개별성), Service Granularity(세분성), Distributed Transactions(분산 처리), Contrancts" 등을 설명하기위해 "Sysops Squad"에 대한 허구의 이야기를 사용 합니다.

They also described some specific topics and patterns, such as component-based decomposition patterns, pulling apart operation data in a highly distributed architecture, reuse code patterns, managing workflows and orchestrations when breaking apart applications, transactional sagas, understanding complexities in breaking large monolithic applications, and making better decisions and effectively documenting them.

> 그리고 그들은 특별한 주제와 패턴(Patterns)들에 대해 설명합니다. 예를 들어, Component 기반의 결합 분리 패턴들(Patterns), 높은 수준의 분산 구조에서 각 부분의 데이터를 가져오는 방법, 코드의 재사용 패턴들, Application을 부분적으로 분리시킬 때 동작 흐름(Workflow)와 통합 운영 (Ochestrations) 관리 방법, Transactional Sagas(번역 x), 대규모 단일 구조 프로그램(Applications)을 쪼개는 복잡도의 이해, 더 나은 의사결정(Dicisions)을 하는 방법과 그 내용을 효율적으로 문서화 하는 방법 등...

[The things I liked about the book]
> [이 책에서 내가 중요하게 생각하는 것들]

Here are some things that I found valuable in this book, and they are located primarily in chapters 1 to 7 in the first part of the book, which is focused on breaking things apart. The book’s second part brings different patterns for pulling things back together.

> 이 책에서 내가 찾은 가장 가치 있는 것들은, 책의 앞 부분인 1 ~ 7 챕터 사이에 우선적으로 작성되어 있다. 더 작은 단위로 나누는 기술에 대한 내용 이다.
> 7챕터 이후 (Second part)에는 작게 나눈 것들을 다시 합치는 패턴들을 설명하고 있습니다.

[Focus on tradeoffs]

The most essential architectural skill is making decisions and balancing tradeoffs. On this topic, the book gives some advice on how to do a modern tradeoff analysis by using the following steps:

1. Find what parts are entangled together.
2. Analyze how they are coupled to one another.
3. Assess tradeoffs by determining the impact of change on interdependent systems

> [가치 교환(tradeoffs)에 집중 하라]

> 가장 중요한 구조 기술(Achitectural Skill)은 가치 교환의 균형을 잡고 의사 결정을 하는 것 입니다. 이번 글의 주제(Topic)에서 이 책이 주는 몇 가지 조언은 아래의 단계 따라서 현대적인 가치교환 분석을 어떻게 하는지 그 방법에 관한 내용 입니다.

> 1. 서로 얽혀 있는 부분들을 찾아라. (해설 : 서로 의존성을 가지게 되서 문제가되는 코드를 찾고)
> 2. 그 부분들을 하나의 다른 부분으로 어떻게 합칠 수 있을 지 분석해라. (해설 : 그 부분들을 추출해 하나의 코드로 재구성할 수 있을지 분석하고)
> 3. 변화가 다른 독립적인 시스템들에 어떤 영향을 미치게 될지 결정하고 가치 교환을 평가해라. (해설 : 재구성 했을 때, 얽혀있지 않은 다른 부분들에는 어떤 영향을 미치는지 확인해라)

When analyzing how different parts are connected and communicating, they introduced the term quantum, which in architectural terms represents “ independently deployable artifacts with high functional cohesion, high static coupling, and synchronous dynamic coupling.” This can be one microsevice. In addition, the authors introduced static (how static dependencies resolve the architecture via contracts) and dynamic coupling (how quanta communicate at runtime).

> 어떻게 서로 다른 부분들을 연결하고 통신할 수 있는지 분석할 때, 양자라는 용어를 사용 합니다. 이 양자는 구조적 측면에서 "높은 기능적 응집력, 높은 정적 결합, 동기적 동적 결합들과 함께 독립적으로 배포될 수 있는 결과물"로 표현됩니다. 이 양자는 하나의 Microservice가 될 수도 있습니다. 게다가 저자들은 정적 결합과 동작 결합을 소개합니다.

> - 정적 결합 (Static Coupling) : 어떻게 정적 의존성이 Contracts를 통해 구조의 해법을 찾는지 
> - 동적 결합 (Dynamic Coupling) : 어떻게 양자들이 실행 시점에 통신을 하는지

[ The main modularity drivers ]

A clear business objective is central to modularizing a system into smaller parts. This objective could be:

* Speed-to-market is achieved by architectural agility, i.e., the ability to respond quickly to a change.
* Scalability, where the need for more scalability support increased user activity
* Fault tolerance is an application’s ability to fail and continue to operate.

> [ 핵심 모듈화 동인 ]

> 명확한 사업의 목적의 핵심은 작은 부분들로 모듈화 하는 것 이다. 그 목적은 아래와 같으 것일 수 있다.

> * 민첩한((i.e, 변화에 빠르게 반응하기 위한 능력)) 구조화로 빠른 시장 진입 달성. 
> * 확장성, 사용자 활동의 증가로 인해 더 많은 확장성을 고려해야할 때.
> * 실패 임계치는 동작이 실패로 멈출 지, 지속적으로 움직일 때 결졍하는 능력 입니다.

[ Breaking down the monolith ]
The authors proposed two methods:

1. Component-based decomposition (if monolith is modular): It applies different refactoring patterns for extracting components to form an incrementally distributed architecture. A component is a well-defined application block with a clear responsibility (e.g., in a namespace or directory). The process involves identifying and sizing components, over-gathering common domain components, and flattening them to create component domains and services. An essential element here is sizing components, and it’s done by calculating the total number of statements with a given component — the ideal size of 1 to 2 standard deviations from the average component size.

> [ 단일 구조 (Monolith) 쪼개기 ]

> 이 글의 저자들은 2가지 방법을 제시 합니다.

> 1. Component 기반의 분리 (만약 단일 구조 시스템이 모듈구조 라면) : 컴포넌트(Component)들을 추출하기 위한 다양한 Refactoring Pattern들을 적용해서 점진적으로 분산 구조를 만들어 갑니다. 
  
> 추출된 Compnent는 명확한 단일 책임을 가지는 잘 정의된 Application의 한 부분이 됩니다. (예. : Namespac 또는 Directory로 정의된). 이 절차는 Component들을 식별 및 규모 조절, 일반적인 도메인 컴포넌트 수집(Over-gathering), 그 컴포넌트들을 잘 다듬어서 컴포넌트의 도메인 또는 서비스 생성이 포함됩니다. 이 중 필수적인 요소는 Component의 규모 조절 입니다. 그리고 Component의 총 문장 수를 계산하는 것으로 가능 합니다. 
  (평균 컴포넌트 크기에서 표준 편차 1 ~ 2 사이의 규모가 최적)

Tactical forking (if the monolith is a big ball of mud): copy the whole monolith and remove the unnecessary parts. We build a proxy with old and new (forked) applications and two teams. Each team has the exact copy of the codebase and then starts to delete the code they don’t need. Ultimately, the goal is to have precise components in the forked application. This is much easier than extracting components with many dependencies.

> 2. 전술적 분기(Tactical Forking) (단일 구조가 모듈의 구조 없이 엄청 큰 경우) : 단일 구조 전체를 복사하고 불필요한 부분들을 삭제 하는 것 입니다. 예전 버전을 사용하는 Poxy와 분기해서 만든 새로운 프로그램과 2개의 팀을 만듭니다. 각 팀은 CodeBase에서 복사 후 그들이 불필요한 것들을 삭제합니다. 궁극적인 목표는 분기한 프로그램에서 정제된 Component들을 가지는 것 입니다. 이 과정은 많은 의존성을 가지고 있는 component들을 추출하는 것보다 훨씬 쉽습니다.

![image](https://github.com/RangK/mediums/assets/1219362/2b54c139-a0c3-484f-9dac-ffe8e8c42a18)\
*The decision tree for selecting a decomposition approach (Credits: Authors of the book “Software Architecture: The Hard Parts”)*

[ Service Granularity ]

While modularity concerns breaking up systems into different parts, granularity deals with the size of these parts. The authors focus on determining the right granularity level (component size). The metric for the granularity of components is the number of statements in a service and the number of public interfaces exposed by a service.

> [서비스 세분성]

> 모듈성은 시스템을 여러 부분을 나누는 것과 관련이 있다면, 세분성은 그 부분들의 크기를 결정합니다. 이 글의 저자들은 좋은 세분성 단계(컴포넌트 크기 : Component Size)를 결정하는 것에 초점을 맞추고 있습니다. 컴포넌트의 세분성 지표는 서비스에 사용된 문장의 수, 서비스에서 제공하는 공개용 인터페이스의 수가 있습니다.

Also, they provide some granularity desintegrators, which are justifications when to break service into smaller pieces:

> 또한, 저자들은 몇몇 세분성 분해 도구(desintegrators)를 제공 합니다. 그 도구는 언제 서비스를 더 작은 조각들로 나눌지를 판단 합니다.

* Service scope and function. Here, we need to consider cohesion and size directly related to the single responsibility principle (from SOLID), where each service should be aligned with its responsibility, i.e., to do one thing well.

> * 서비스 범위와 기능 : 응집성(cohesion)와 단일 책임 원칙(SRP from SOLID)와 연관된 크기, 각 서비스가 한 가지 일을 잘 할 수 있도록 어떤 책임을 가져야 하는지, 등을 고려하는 것이 필요합니다.

* Code volatility. Consider splitting a component that changes more frequently than the rest to reduce the scope of testing and deployment.

> * 코드 휘발성 (Code volatility) : 테스트와 배포 범위를 줄이기 위해서는 다른 부분들보다 더 자주 변경되는 컴포넌트를 분리하는 것을 고려해야 한다.

* Scalability and throughput. Consider this if some services need to scale more than others.

> * 확장성과 처리능력 : 몇몇 서비스들이 다른 서비스들보다 더 많은 확장을 필요로한다면, 이 영역을 고려해야한다.

* Fault tolerance. If one component crashes, this can impact other components.

> * 장애 허용 : 컴포넌트가 정상 동작하지 않는다면, 이 부분은 다른 컴포넌트에 영향을 줄 수 있습니다.

* Security. If we need to have different security concerns per component.

> * 보안 : 컴포넌트마다 서로 다른 보안 요소들을 가지고 있는가 ?

* Extensibility. A new service would be a better fit.

> * 확장성 : 새로운 서비스가 더 적합할 수 있음


Conversely, we have granularity integrators, which work oppositely; they justify when to put services back together. The main drivers for integration are:

> 반대로, 우리는 반대의 작업을 위한 세분성 도구도 가지고 있습니다. 통하 도구는 언제 서비스들을 다시 하나로 합쳐야할 지 판한합니다. 통합의 주요 인자들은 아래와 같습니다.

* Database transactions. Suppose we need an ACID transaction between two services.
> * Database 연속적 데이터 처리 : 우리가 ACID 데이터 처리를 두 서비스 간에 필요하다면 ?

* Workflow and Choreography. If services need to talk less to one another, they become more fault-tolerant and performant.
> * Workflow 와 Choreography : 서비스들이 다른 서비스와 통신을 줄일 필요가 있다면, 서비스들은 더 장애 허용과 성능 명에서 향상될 수 있다.

* Shared Code. If we have multiple services that use the same shared library, if a change occurs in the library, we would need to change all services.
> * 코드 공유 : 같은 공유 라이브러리를 사용하는 여러 서비스들이 있고, 만약 그 라이브러의 변화가 발생하게 되면 우리는 모든 서비스를 수정해야한다.

* Data Relationships. If we have data that belongs to a bounded context tightly coupled to the service.
> * 데이터의 관계 : 긴밀히(가깝게 ?) 연결된 서비스의 컨텍스트 범위에 속해있는 데이터를 가지고 있다면

[Different kinds of valuable patterns]

In the book’s second part, mainly focused on putting things back together, we can find some interesting patterns.

> [그외 여라가지 유용한 패턴의 종류]

> 이 책의 두 번째 부분에서는 주로 하나로 통합하는 것에 초점을 맞추고 있으며, 흥미로운 패턴들을 찾을 수 있습니다.

[Code reuse patterns]

> 코드 재사용 패턴

In this group, we have different kinds of code reuse patterns:

> 이 그룹에서 우리는 코드 재사용 패턴의 여러 종류를 가지고 있습니다.

* Code replication. Shared code is copied into each service, e.g., when we have a simple static code (annotations, attributes, etc.).
> * 코드 복재 : 공유되는 코드는 각 다른 서비스에 복사 됩니다. 예를 들어 우리가 간단한 정적인 코드(해설 : 변화이 일관성있게 유지될 코드) 를 가지고 있을 때 (annotations, attributes)...

* Shared library. It is a good approach for low- to moderate shared code change environments. We need to have fine-grained libraries which are versioned.
> * 공유 라이블리 : 공유 코드의 변경이 발생할 수 있는 환경에서 변경 사항을 중재량을 낮추기위한 좋은 방법이 됩니다. 다만, 우리는 이를 위해서 버전 관리를 포함하는 세분화된 라이브러리를 가지고 있어야 합니다.

* Shared Services. It is a common approach to addressing shared functionality, and it should be used in polyglot environments when shared functionality tends to change often. They are less performant and scalable than shared libraries.
> * 공유 서비스 : 공유 기능을 해결하는 가장 일반적인 접근 방식입니다. 공유 기능이 종종 변경되는 경향이 있는 다중 언어(polyglot) 환경에서 자주 사용됩니다. 공유 기능은 공유 라이브러리 보다 더 낮은 성능과 확장성을 가집니다.

Sidecars and service mesh. They are good choices when we have cross-cutting concerns.



