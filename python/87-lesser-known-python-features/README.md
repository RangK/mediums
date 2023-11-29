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