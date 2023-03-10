# Introduction

문자열에서 부분 문자열을 검색하는 알고리즘으로 브루트 포스법, KMP 법, 보이어 무어법등이 존재함.

문자열 검색은 어떤 문자열 안에 다른 문자열이 포함되어 있는지를 검사하고 만약 포함되어 있다면 어디에 위치하는지 찾아내는 알고리즘임.

ex -> 문자열 STRING에서 IN을 검색하면 성공하되 ABC를 검색하면 안되는 것

여기서 검색되는 STRING 문자열을 `텍스트`라고 하며 찾아내는 문자열 `IN`을 패턴이라고 함.

## Brute Force

문자열 검색 알고리즘 중에서 가장 기초적이면서 단순한 알고리즘인 브루트 포스법은 선형 검색을 단순하게 확장한 알고리즘이기에 `단순법`이라고도 함.

ex) `ABABCDEFGHA`에서 패턴 `ABC`를 브루트 포스법으로 검색하는 순서는 다음과 같다. 

- 1 step) 텍스트의 첫 문자 `A`가 동일하고 나머지 BC가 동일한지 검색했을때 C가 안맞으로 x
- 2 step) 패턴을 오른쪽으로 1칸 밀고, 텍스트의 2번째 문자와 그 이후 부분이 일치하는지 검사를 함 (그 다음 텍스트 문자인 B가 A와 다르므로 x)
- 3 step) 텍스트의 세번째 단어인 A가 나왔을때 비교를 시작하면 모두 일치하므로 검색에 성공하고 종료됨.



