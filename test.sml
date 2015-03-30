fun lookup(k, table) =
  let
    fun find pred [] = 0 
      | find pred (x :: xs) = 
        if (pred x)
          then #2(x)
          else find pred xs;
  in
    find (fn (key, value) => (key = k)) table
  end

lookup(14, [(1,4), (14,5), (7,3), (22,6)])
