import heapq

def shortestPaths(edges, src):
  # create an adjaceny list, key = source, value = [destination, weight]
  adj = {}
  for source, dest, weight in edges:
    if not adj.get(dest):
      adj[dest] = []
    if adj.get(source):
      adj[source].append([dest, weight])
    else:
      adj[source] = [[dest, weight]]

  # create a shortest map that will be our answer
  shortest = {}

  # create a min heap, we know that the distance from our source to our source is 0
  minHeap = [[0, src]]
  
  # create a while loop for while the min heap is empty
  while minHeap:
    print(minHeap)
    # pop from heap and add to shortest map
    wPopped, nPopped = heapq.heappop(minHeap)
    if nPopped in shortest:
      continue
    shortest[nPopped] = wPopped

    # get the neighbors from node popped and add to heap
    for neighborNode, neightborWeight in adj[nPopped]:
      if not shortest.get(neighborNode):
        heapq.heappush(minHeap, [wPopped + neightborWeight, neighborNode])

  # return the shortest
  return shortest

ans = shortestPaths(
  [["a", "b", 10], ["a", "c", 3], ["b", "d", 2], ["c", "b", 4], ["c", "e", 2], ["c", "d", 8], ["d", "e", 5]],
  "a"
)

print(ans)