The "Time Planner" Problem

Implement a meeting planner that can schedule meetings between two persons at a time.

Time is represented by Unix format (also called Epoch) - a positive integer holding the seconds since January 1st, 1970 at midnight. 

Planner input:

dur - Meeting duration in seconds (a positive integer).
timesA, timesB - Availability of each person, represented by an array of arrays.
Each sub-array is a time span holding the start (first element) and end (second element) times.
You may assume that time spans are disjointed.
Planner output:

Array of two items - start and end times of the planned meeting, representing the earliest opportunity for the two persons to meet for a dur length meeting.
If no possible meeting can be scheduled, return an empty array instead.
Design and implement an efficient solution and analyze its runtime and space complexity.

---

Solution

A naive solution would loop through both availability arrays and check every possible pair of availability time spans for a minimal overlap of dur seconds.
Such a solution is not efficient and involves O(n⋅m) runtime complexity (when n and m are lengths of timesA and timesB), and O(1) space complexity.

We can do better than that if the availability arrays are sorted (always consider asking your interviewer if the input is sorted).
Even if availability arrays are not sorted, we can still do better by sorting them first.
Since we know nothing else about the times, we can sort each availability array by start times at O(n∙log n) time complexity (when n is the number of time slots in the array).

After taking care of sorting, we can iterate over both arrays at once.
We use one index for each array, while forwarding one index at a time.
At each step we check if:

No overlap exists:
One time span ends before the other starts.
In this case, increase the index of the array with the earlier time.
Overlap exists for at least dur seconds:
The minimum of both end times is more than dur seconds after the maximum of both start times.
In this case, we've found a meeting time.
Overlap exists for less than dur seconds:
we've eliminated both previous cases.
In this case, we increase the index of the array with the earlier start time of its next time span.
ia = 0
ib = 0
while (ia < timesA.length and ib < timesB.length):
   start = max(timesA[ia][0], timesB[ib][0])
   end = min(timesA[ia][1], timesB[ib][1])
   if (start + dur <= end):
      return [start, start + dur]
   else:
      if (timesA[ia][1] < timesB[ib][1]):
         ia = ia + 1
      else:
         ib = ib + 1
return []
Runtime Complexity: linear O(n+m) for sorted time arrays or O(n∙log n+m∙log m) for non-sorted arrays, where n and m are lengths of timesA and timesB.

Space Complexity: constant O(1) for either case.