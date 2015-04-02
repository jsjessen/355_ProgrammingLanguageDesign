fun lookup k [] = 0
  | lookup k ((key, value) :: xs) = 
      if key = k
        then value
        else lookup k xs

val james = lookup 14 [(1,4), (14,5), (7,3), (22,6)]
