# CMPS 2200 Recitation 08

## Answers

**Name:** Daron Lebaredian

Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

The work and span of this algorithm would be, with E being the set of edges:

$W(n) \in O(|E|log(|E|))$

$S(n) \in O(|E|log(|E|))$

The work and span of heappush and heappop are both log(n). The number of times both of these functions are called is once per edge. Therefore the result above.

- **2b)**

The work and span of ths algorithm would be, with E being the set of edges and V being the set of verticles:

$W(n) \in O(|V|+|E|)$

$S(n) \in O(|V|+|E|)$

This is because all of the edges and verticles of an inputed graph is visted exactly once.

