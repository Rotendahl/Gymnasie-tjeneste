// Duration
open System

let duration f =
    let timer = new System.Diagnostics.Stopwatch()
    timer.Start()
    let returnValue = f()
    printfn "Elapsed Time: %i" timer.ElapsedMilliseconds
    returnValue

// Fibonacci recursive (hej hihihi)
let rec fibrec x =
  match x with
    | 1 -> 1
    | 2 -> 1
    | x -> fibrec(x-1) + fibrec(x-2)

// Fibonacci bottom-up dp
let fib x =
  let fibmap = new System.Collections.Generic.Dictionary<int,int64>()
  fibmap.[1] <- int64 1
  fibmap.[2] <- int64 1
  for i=3 to x do
    fibmap.[i] <- (fibmap.[i-1] + fibmap.[i-2])
  fibmap.[x]

// Le main (9gag)
let main() =
  printfn "Fibonacci recursive 30: %i" (duration ( fun() -> fibrec 30 ))
  printfn "Fibonacci dp 150: %i" (duration ( fun() -> fib 150 ))

main()
