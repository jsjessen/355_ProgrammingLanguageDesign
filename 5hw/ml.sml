(*
* Poly/ML 5.2
* Linux/Unix
* 
* James Jessen
* 10918967
* CptS 355 HW5
*)

(*================================================================*)

(*
* in_list
* -------
* This function should return true if the first argument 
* is a member of the second argument.
*
* type (''a * ''a list) -> bool.
*)

fun in_list (target, []) = false
  | in_list (target, cur :: rest) = 
  if cur = target then true 
  else in_list(target, rest)

val test_in_list = 
  if      in_list (1,[]) = false 
  andalso in_list (1,[1,2,3]) = true
  andalso in_list ([1],[[1]]) = true
  andalso in_list ([1],[[3],[5]]) = false
  andalso in_list ("c",["b","c","z"]) = true
  then "in_list: PASS"
  else "in_list: FAIL"

(*----------------------------------------------------------------*)

(*
* intersection
* ------------
* This function should return the intersection of two lists.
*
* type ''a list * ''a list -> ''a list. 
*
* Maybe you can make use of in_list?
*
* Each value should appear in the output list only once, 
* but the order does not matter.
*)

fun intersection ([], []) = []
  | fun intersection (current1 :: rest1, current2 :: rest2) = []

val test_intersection = 
  if      intersection ([1],[1]) = [1]
  andalso intersection ([1,2,3],[1,2]) = [1,2]
  andalso intersection ([[2,3],[1,2],[2,3]], [[1],[2,3]]) = [[2,3]]
  then "intersection: PASS"
  else "intersection: FAIL"

(*----------------------------------------------------------------*)

(*
* union
* -----
* This function should return the union of two lists. 
* Each value should appear in the output list only once
* but the order does not matter. 
*
* In the intersection function above the two lists were supplied as a tuple.
* That is, it had type (''a list * ''a list) -> ''a list. 
*
* Make union a function of two arguments: 
* type ''a list -> ''a list -> ''a list.
*)

val test_union = 
  if      union [1] [1] = [1] 
  andalso union [1,2,3] [1,2] = [1,2,3]
  andalso union [[2,3],[1,2]] [[1],[2,3]] = [[1],[2,3],[1,2]]
  then "union: PASS"
  else "union: FAIL"

(*----------------------------------------------------------------*)

(*
* filter and reverse
* ------------------
* filter takes as its first argument a one-argument function, 
* called a predicate, which returns true or false, 
* and as its second argument a list. 
* It returns a list of all elements in the second argument 
* that satisfy that predicate. 
* The elements must appear in the result in the same order 
* that they appear in the original list.
*
* For this problem (only) your implementation is required to be 
* tail recursive, so you will need to define an auxiliary function 
* that takes a parameter in which the result is accumulated. 
* The function filter will simply call the 
* auxiliary function with [] as the initial result. 
* It is the auxiliary function that will be tail recursive. 
* It turns out that in using the accumulating parameter technique, 
* the result is produced in reverse order. 
* So you also need to define the function reverse that reverses a list. 
* reverse is also implemented as a tail-recursive function.
*)

val test_filter = 
  if      filter (fn (x) => (x = 1)) [1,2,3] = [1]
  andalso filter (fn (x) => (x <= 3))[1,2,3,4] = [1,2,3]
  then "filter: PASS"
  else "filter: FAIL"

(*----------------------------------------------------------------*)

(*
* groupNl and groupNr
* -------------------
* These functions take two arguments. 
* The first is an integer and the second is a list. 
* The idea is to produce a result in which the elements of the 
* original list have been collected into sublists each 
* containing N elements (where N is the integer argument). 
* Thus the type of each of these is int -> 'a list -> 'a list list. 
* The difference between the two functions is how they handle 
* the left-over elements of the list when the integer doesn't 
* divide the length of the list evenly. 
* groupNl treats the initial elements of the list as the extras, 
* thus the result starts with a list of between 1 and N elements 
* and all the remaining elements of the result list contain N elements. 
* groupNr does the opposite: the final group contains 
* between 1 and N elements and all the rest contain N elements.
*)

val test_groupNl = 
  if groupNl 2 [1, 2, 3, 4, 5] = [[1], [2, 3], [4, 5]]
  then "groupNl: PASS"
  else "groupNl: FAIL"

val test_groupNr = 
  if groupNr 2 [1, 2, 3, 4, 5] = [[1, 2], [3, 4], [5]]
  then "groupNr: PASS"
  else "groupNr: FAIL"

(*----------------------------------------------------------------*)

(*
* mergesort - 15%
* ------------------------------------------
* This function takes two arguments. 
* The first argument is a function called a comparator 
* and takes as its argument a pair (two-tuple) and returns a boolean. 
* The second argument is a list. 
* The type of the sorting function is ('a * 'a -> bool) -> 'a list -> 'a list. 
* The function mergesort returns a list consisting of the members of its 
* second argument, ordered so that the comparator returns true on adjacent members.
*
* Recall the general structure of mergesort: split the list in 2 equal pieces.
* Recursively sort the pieces, then merge the two sorted sublists into a 
* sorted result (as in the Scheme assignment).
*)

val test_mergesort = 
  if      mergesort (fn (x,y) => (x <= y)) [1] = [1]       
  andalso mergesort (fn (x,y) => (x <= y)) [3,2,1,2] = [1,2,2,3]
  andalso mergesort (fn (x,y) => (x >= y)) [3,2,1,2] = [3,2,2,1]
  then "mergesort: PASS"
  else "mergesort: FAIL"

(*----------------------------------------------------------------*)

  (*
------------------------------------------
Practice with datatypes - 15%
------------------------------------------
Define an ML datatype datatype either = ImAString of string | ImAnInt of int.

Define an ML datatype named eitherTree for binary trees containing values of
type either where the data is only at the leaves of the tree.

Define an ML function eitherSearch having type eitherTree -> int -> bool that returns true
if the int is in the tree and false otherwise. The trick to getting this to type check is to realize that ImAnInt of int values and int values do not have the same type. But you can transform either into the
other.

Define an ML function of no arguments, eitherTest that:

    • constructs an eitherTree with at least 5 int-containing leaves, at least 5 string-containing
    leaves, and at least 4 levels;
    • searches the tree using your eitherSearch function for an int that is present in the tree;
    • and, searches the tree using your eitherSearch function for a value that is not present in the
    tree.

(*----------------------------------------------------------------*)
------------------------------------------
treeToString - 15%
------------------------------------------
A polymorphic tree type, with data only at the leaves, in SML might be represented using

    datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) list

Write a function treeToString: ('a -> string) -> 'a Tree -> string that returns a
parenthesized string representing an arbitrary Tree. treeToString is invoked as treeToString f t
where f is a function that converts data of type 'a to a string and t is an 'a Tree. The
parenthesization rules implemented by treeToString are as follows:

    • For a LEAF node, the returned value is just f the-data-in-the-leaf.
    • For a LIST node, concatenate the strings produced by treeToString on the elements of the list
    and surround the resulting string with parentheses. For this function, you may use built-in functions map and String.concat in addition to the generally allowable functions listed above.

We suggest that you start by solving a simpler non-polymorphic problem using

    datatype Tree = LEAF of string | NODE of Tree list

Since the leaves in this simpler problem are already strings you don't need the function argument but
you can see the overall structure of the solution. Then make the datatype polymorphic and add the
function parameter.

Hint: The whole function is neatly expressed as two lines of code.

Here is some test data:

val L1a = LEAF "a"
val L1b = LEAF "b"
val L1c = LEAF "c"
val L2a = NODE [L1a, L1b, L1c]
val L2b = NODE [L1b, L1c, L1a]
val L3 = NODE [L2a, L2b, L1a, L1b]
val L4 = NODE [L1c, L1b, L3]
val L5 = NODE [L4]
val iL1a = LEAF 1
val iL1b = LEAF 2
val iL1c = LEAF 3
val iL2a = NODE [iL1a, iL1b, iL1c]
val iL2b = NODE [iL1b, iL1c, iL1a]
val iL3 = NODE [iL2a, iL2b, iL1a, iL1b]
val iL4 = NODE [iL1c, iL1b, iL3]
val iL5 = NODE [iL4]

treeToString String.toString L5 should produce "((cb((abc)(bca)ab)))" and
treeToString Int.toString iL5 should produce "((32((123)(231)12)))".

Note that interactive SML systems typically do not print all of the contents of deeply nested data
structures. So after evaluating the declaration for il5 the response may be something like

    val iL5 = NODE [NODE [LEAF #,LEAF #,NODE #]] : int Tree

depending on what SML system you are using (in this case SMLofNJ).
Additional information about string manipulation: the ^ infix operator concatenates two strings, thus:

- "abc" ^ "def";
"abcdef"

and String.concat concatenates all of the strings in a list of strings. Thus:

- String.concat ["abc", "def", "ghi"];
"abcdefghi"

(*----------------------------------------------------------------*)
------------------------------------------
Perms - 5%
------------------------------------------
Function perms is given a list, l, and returns a list of lists, each of the sublists being one of the length(l)!
permutations of l. The permutations may be in any order.

- perms [1, 2, 3]
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
*)
