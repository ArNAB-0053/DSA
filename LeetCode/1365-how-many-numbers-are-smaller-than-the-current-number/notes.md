- used an different approach as `counting sort + prefix array` to solve the problem

- although simply by `sorting + map` also can do so but that takes O(nlogn), but this approach takes O(n).

> If the value range were very large (e.g. nums[i] up to 10^9), using a frequency array would be impractical in terms of memory. In that case, the sorting + hashmap approach would be preferred:  `TC: O(n log n)`