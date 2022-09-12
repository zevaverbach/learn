# 1.1-1
Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

Sorting: My son's Pokémon cards are scattered on the coffee table and he wants to be able to find the cards according to a) type and b) attack power.

Computing a convex hull: We are moving to a new city and want to have the smallest possible commute between home, school and work.

# 1.1-2
Other than speed, what other measures of efficiency might one use in a real-world setting?

Memory usage. Readability of the code.

# 1.1-3
Select a data structure that you have seen previously, and discuss its strengths and limitations.

I have seen an array in Python, I use them very often; they're called `list`s. Their strengths are that they are dynamically resized without any manual intervention, and their data can be accessed quickly via index. One limitation of any array is that inserting an item anywhere but at the end is slow, because all items after the insert have to be shifted over.

# 1.1-4
How are the shortest-path and traveling-salesman problems given above similar? How are they different?

They're almost identical; the only difference I see is that the traveling salesman doesn't necessarily have to return home at the end of a trip -- and therefore that leg of the itinerary doesn't have to be part of the calculation -- whereas the delivery company has to get the truck back to headquarters every day.

# 1.1-5
Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough.

