# Binary Search

이진 검색이란 배열의 중간 지점을 기준으로 찾고자 하는 키값의 크기에 따라서 중간 값보다 작은지 아니면 더큰지를 구별하고 만약 크기 비교가 되었다면 탐색 범위를 줄이고 다시 중앙을 기준으로 판단을 하는 알고리즘이다.

*다만 이진 검색이 성공적으로 수행되려면 찾고자 하는 키값이 포함된 배열이 오름차순 또는 내림차순으로 정렬이 되어있어야한다. 

## example

a = [1,2,3,4,5,6,7] 해당 배열에서 5을 찾고자 할때, 처음 4를 기준으로 6은 더크기 때문에 탐색범위를 오른쪽으로 줄인다 (즉, 5,6,7). 이제 새로 정해진 탐색 배열에서 중간 값인 6을 기준으로 탐색을 한다. 이때 6보다 작으므로 새로 배열을 만든다. 그러나 1개의 원소만 구성되고 찾는 키값과 동일하므로 찾기가 완료되었다. 

종료 조건은 다음과 같다. 
- 탐색하는 값이 탐색 범위의 중앙값과 같은가?
- 검색 범위가 더 이상 없는가?

## Complexity

복잡도는 알고리즘의 성능을 객관적으로 평가하는 기준을 의미한다.

- 시간 복잡도 (time complexity): 실행하는 데 필요한 시간을 평가함
- 공간 복잡도 (space complexity): 메모리와 파일 공간이 얼마나 필요한지를 평가함.

선형 검색 방법에서는 O(n)
이진 검색에서는 O(log n)