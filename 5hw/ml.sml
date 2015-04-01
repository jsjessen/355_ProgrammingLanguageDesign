(*
* Poly/ML 5.2
* Linux/Unix
* 
* James Jessen
* 10918967
* CptS 355 HW5
*)

(*----------------------------------------------------------------------------*)

datatype TestResult = Pass | Fail

fun test(input, output) =
  if input = output
    then Pass
    else Fail

(*
================================================================================
IN_LIST
--------------------------------------------------------------------------------
* This function should return true if the first argument 
* is a member of the second argument.
*
* Type : ''a * ''a list -> bool.
*)

fun in_list(target, []) = false
  | in_list(target, cur :: rest) = 
      (cur = target) orelse in_list(target, rest)

val in_list_TEST = 
  (
    test(in_list(1,[]),               false),
    test(in_list(1,[1,2,3]),          true),
    test(in_list([1],[[1]]),          true),
    test(in_list([1],[[3],[5]]),      false),
    test(in_list("c",["b","c","z"]),  true)
  )

(*
================================================================================
INTERSECTION
--------------------------------------------------------------------------------
* This function should return the intersection of two lists.
*
* Each value should appear in the output list only once, 
* but the order does not matter.
*
* Type : ''a list * ''a list -> ''a list. 
*)

fun intersection(L1, L2) =
    let
      fun help(L1, [], result) = result 
        | help([], L2, result) = result 
        | help(cur :: rest, L2, result) =
            if in_list(cur, L2)
            andalso in_list(cur, result) = false
              then help(rest, L2, cur :: result)
              else help(rest, L2, result)
    in
      help(L1, L2, [])
    end

val intersection_TEST = 
  (
    test(intersection([],[]),                             []),
    test(intersection([1],[1]),                           [1]),
    test(intersection([1,2,3],[1,2]),                     [2,1]),
    test(intersection([[2,3],[1,2],[2,3]], [[1],[2,3]]),  [[2,3]])
  )

(*
================================================================================
UNION
--------------------------------------------------------------------------------
* This function should return the union of two lists. 
*
* Each value should appear in the output list only once
* but the order does not matter. 
*
* Type : ''a list -> ''a list -> ''a list
*)

fun union L1 L2 =
    let
      fun help([], [], result) = result 
        | help([], L2, result) = help(L2, [], result)
        | help(cur :: rest, L2, result) =
            if in_list(cur, result) 
              then help(rest, L2, result)
              else help(rest, L2, cur :: result)
    in
      help(L1, L2, [])
    end

val union_TEST = 
  (
    test(union [] [],                       []),
    test(union [1] [1],                     [1]),
    test(union [1,2,3] [1,2],               [3,2,1]),
    test(union [[2,3], [1,2]] [[1],[2,3]],  [[1],[1,2],[2,3]])
  )

(*
================================================================================
* FILTER AND REVERSE
--------------------------------------------------------------------------------
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
*
* It turns out that in using the accumulating parameter technique, 
* the result is produced in reverse order. 
* So you also need to define the function reverse that reverses a list. 
* reverse is also implemented as a tail-recursive function.
*)

fun reverse(L) = 
    let
      fun help [] result = result
        | help (cur :: rest) result = help rest (cur :: result)
    in
      help L []
    end

val reverse_TEST = 
  (
    test(reverse [],         []),
    test(reverse [1],        [1]),
    test(reverse [1,2,3],    [3,2,1]),
    test(reverse [1,2,3,4],  [4,3,2,1])
  )

(*----------------------------------------------------------------------------*)

fun filter pred L =
    let
      fun help pred [] result = result
        | help pred (cur :: rest) result = 
            if pred cur
              then help pred rest (cur :: result)
              else help pred rest result
    in
      reverse(help pred L [])
    end

val filter_TEST = 
  (
    test(filter(fn (x) => (x = 1))  [1,2,3],    [1]),
    test(filter(fn (x) => (x <= 3)) [1,2,3,4],  [1,2,3])
  )

(*
================================================================================
* GROUPNL AND GROUPNR
--------------------------------------------------------------------------------
* These functions take two arguments. 
* The first is an integer and the second is a list. 
* The idea is to produce a result in which the elements of the 
* original list have been collected into sublists each 
* containing N elements (where N is the integer argument). 
*
* The difference between the two functions is how they handle 
* the left-over elements of the list when the integer doesn't 
* divide the length of the list evenly. 
*
* groupNl treats the initial elements of the list as the extras, 
* thus the result starts with a list of between 1 and N elements 
* and all the remaining elements of the result list contain N elements. 
*
* groupNr does the opposite: the final group contains 
* between 1 and N elements and all the rest contain N elements.
*
* Type : int -> 'a list -> 'a list list
*)

fun groupNl N L =
    let
      fun transfer i [] [] = [[]] 
        | transfer i (dCur :: dRest) [] = [[]] 
        | transfer i [] (dCur :: dRest) = dCur :: dRest
        | transfer i (sCur :: sRest) (dCur :: dRest) = 
            if i > 0
              then transfer (i - 1) sRest ((sCur :: dCur) :: dRest)
              else transfer N (sCur :: sRest) ([] :: dCur :: dRest)
    in
      if N > 0
        then transfer N (reverse(L)) [[]]
        else [[]]
    end

val groupNl_TEST = 
  (
    test(groupNl 2 [1, 2, 3, 4, 5],     [[1], [2, 3], [4, 5]]),
    test(groupNl 3 [1, 2, 3, 4, 5],     [[1, 2], [3, 4, 5]]),
    test(groupNl 3 [1, 2, 3, 4, 5, 6],  [[1, 2, 3], [4, 5, 6]])
  )

(*----------------------------------------------------------------------------*)

fun groupNr N L =
    let
      fun transfer i [] [] = [[]] 
        | transfer i (dCur :: dRest) [] = [[]] 
        | transfer i [] (dCur :: dRest) = reverse(dCur) :: dRest
        | transfer i (sCur :: sRest) (dCur :: dRest) = 
            if i > 0
              then transfer (i - 1) sRest 
                            ((sCur :: dCur) :: dRest)
              else transfer N (sCur :: sRest) 
                            ([] :: reverse(dCur) :: dRest)
    in
      if N > 0
        then reverse(transfer N L [[]])
        else [[]]
    end

val groupNr_TEST = 
  (
    test(groupNr 2 [1, 2, 3, 4, 5],     [[1, 2], [3, 4], [5]]),
    test(groupNr 3 [1, 2, 3, 4, 5],     [[1, 2, 3], [4, 5]]),
    test(groupNr 3 [1, 2, 3, 4, 5, 6],  [[1, 2, 3], [4, 5, 6]])
  )

(*
================================================================================
MERGESORT
--------------------------------------------------------------------------------
* This function takes two arguments:
*   1) Comparator Function
*       Takes as its argument a pair (two-tuple) 
*       Returns a bool
*   2) List
*
* The function mergesort returns a list consisting of the members of its 
* second argument, ordered so that the comparator returns true on adjacent members.
*
* Recall the general structure of mergesort: split the list in 2 equal pieces.
* Recursively sort the pieces, then merge the two sorted sublists into a 
* sorted result (as in the Scheme assignment).
*
* Type : ('a * 'a -> bool) -> 'a list -> 'a list 
*)

fun mergesort comp [] = []
  | mergesort comp [single] = [single]
  | mergesort comp L = 
    let
      fun split []  = ([], [])
        | split [single] = ([single], [])
        | split (even :: odd :: rest) =
          let
            val (evenList, oddList) = split rest 
          in
            (even :: evenList, odd :: oddList)
          end

      val (L1, L2) = split L 

      fun merge [] [] = [] 
        | merge L1 [] = L1
        | merge [] L2 = L2
        | merge (cur1 :: rest1) (cur2 :: rest2) =
            if comp(cur1, cur2)
              then cur1 :: (merge rest1 (cur2 :: rest2))
              else cur2 :: (merge rest2 (cur1 :: rest1))
    in
      merge (mergesort comp L1) (mergesort comp L2) 
    end

val mergesort_TEST = 
  (
    test(mergesort (fn (x,y) => (x <= y)) [1],          [1]),
    test(mergesort (fn (x,y) => (x <= y)) [3,2,1,2],    [1,2,2,3]),
    test(mergesort (fn (x,y) => (x >= y)) [3,2,1,2],    [3,2,2,1]),
    test(mergesort (fn (x,y) => (x <= y)) [3,2,1,7,2],  [1,2,2,3,7]),
    test(mergesort (fn (x,y) => (x >= y)) [3,2,1,7,2],  [7,3,2,2,1])
  )

(*
================================================================================
PRACTICE WITH DATATYPES
--------------------------------------------------------------------------------
* Define an ML datatype: 
*   datatype either = ImAString of string | ImAnInt of int
* 
* Define an ML datatype named eitherTree 
* for binary trees containing values of type either,
* where the data is only at the leaves of the tree.
* 
* Define an ML function eitherSearch having 
* type eitherTree -> int -> bool that returns true
* if the int is in the tree and false otherwise. 
*   The trick to getting this to type check is to realize that 
*   ImAnInt of int values and int values do not have the same type. 
*   But you can transform either into the other.
* 
* Define an ML function of no arguments, eitherTest that:
*   • constructs an eitherTree with at least 5 int-containing leaves, 
*     at least 5 string-containing leaves, and at least 4 levels
*   • searches the tree using your eitherSearch function for an 
*     int that is present in the tree
*   • searches the tree using your eitherSearch function for 
*     a value that is not present in the tree
*)

datatype either = ImAString of string | ImAnInt of int
datatype eitherTree = LEAF of either | BRANCH of eitherTree * eitherTree

fun eitherSearch (LEAF(ImAString data)) n = false
  | eitherSearch (LEAF(ImAnInt data)) n = (data = n)
  | eitherSearch (BRANCH(left, right)) n =
      (eitherSearch left n) orelse (eitherSearch right n)

(*
  It doesn't seem to like it as a function:
  fun eitherTest() =
*)
val eitherTest =
  let
    (* Data *)
    val Ls1 = LEAF (ImAString "one") 
    val Ls2 = LEAF (ImAString "two")
    val Ls3 = LEAF (ImAString "three")
    val Ls4 = LEAF (ImAString "four")
    val Ls5 = LEAF (ImAString "five")
    val Ln1 = LEAF (ImAnInt 1)
    val Ln2 = LEAF (ImAnInt 2)
    val Ln3 = LEAF (ImAnInt 3)
    val Ln4 = LEAF (ImAnInt 4)
    val Ln5 = LEAF (ImAnInt 5)

    (* Level 4 *)
    val F = BRANCH (Ls1, Ls2)
    val G = BRANCH (Ls3, Ls4)
    val H = BRANCH (Ls5, Ln1)
    val I = BRANCH (Ln2, Ln3)

    (* Level 3 *)
    val D = BRANCH (F, G)
    val E = BRANCH (H, I)

    (* Level 2 *)
    val B = BRANCH (D, E)
    val C = BRANCH (Ln4, Ln5)

    (* Level 1 *)
    val A = BRANCH (B, C)
  in
    (
      (eitherSearch A 1),
      (eitherSearch A 8)
    )
  end

(*
================================================================================
TREETOSTRING
--------------------------------------------------------------------------------
A polymorphic tree type, with data only at the leaves, 
in SML might be represented using:

  datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) list

Write a function treeToString:  

  ('a -> string) -> 'a Tree -> string 

that returns a parenthesized string representing an arbitrary Tree. 
treeToString is invoked as treeToString f t,
where f is a function that converts data of type 'a to a string 
and t is an 'a Tree. 

The parenthesization rules implemented by treeToString are as follows:
  • For a LEAF node, the returned value is just f the-data-in-the-leaf.
  • For a LIST node, concatenate the strings produced 
    by treeToString on the elements of the list and surround the 
    resulting string with parentheses. 

For this function, you may use built-in functions map and String.concat

the ^ infix operator concatenates two strings, thus:
    "abc" ^ "def"
    "abcdef"

String.concat concatenates all of the strings in a list of strings:
    String.concat ["abc", "def", "ghi"]
    "abcdefghi"
*)

datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) list

fun treeToString f (LEAF data) = f data 
  | treeToString f (NODE treeList) =
      "(" ^ (String.concat (map (treeToString f) treeList)) ^ ")"
      
val treeToString_TEST = 
  let 
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
  in
    (
      test(treeToString String.toString L5,  "((cb((abc)(bca)ab)))"),
      test(treeToString Int.toString iL5,    "((32((123)(231)12)))")
    )
  end
    
(*
================================================================================
PERMS
--------------------------------------------------------------------------------
* Function perms is given a list, l, and returns a list of lists, 
* each of the sublists being one of the length(l)!
* permutations of l. 
*
* The permutations may be in any order.
*)

(*
fun insertEverywhere [] = [[0]]
  | insertEverywhere (y::ys) = 
    let
      fun consY list = y::list
    in
      (0::y::ys) :: (map consY (insertEverywhere ys))
    end
*)

fun perms [] = [[]]
  | perms (x :: xs) = 
    let
      fun myMap f [] = []
        | myMap f (cur :: rest) = (f cur) :: (myMap f rest)

      (* fun myConcat *)

      fun insertEverywhere [] = [[x]]
        | insertEverywhere (y :: ys) = 
          let
            fun consY L = y :: L 
          in
            (x :: y :: ys) :: (myMap consY (insertEverywhere ys))
          end
    in
      (* remove 'List.concat' and see output, 
      *  then design myConcat accordingly *)
      List.concat (myMap insertEverywhere (perms xs))
    end

val perms_TEST = 
  (
    test(perms [],       [[]]),
    test(perms [1],      [[1]]),
    test(perms [1,2],    [[1,2], [2,1]]),
    test(perms [1,2,3],  [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]])
                      (* [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]) *)
  )
