def maxProfit(list)
  i = 0
  j = 0
  minimum_sales_price = list[i]
  max_revenue = 0
  while j < list.length
    # Check the revenue
    revenue = list[j] - list[i]
    max_revenue = revenue if revenue > max_revenue
    # Check if the number in j is smaller than the minimum_sales_price
    if list[j] < minimum_sales_price
      i = j
      minimum_sales_price = list[j]
    end

    # if so, update the minimum_sales_price, move the i to the point, and start them over
    # once the j reaches to the end of the list, return the max_revenue
    j += 1
  end

  max_revenue
end

p maxProfit([7, 1, 5, 3, 6, 4])
p maxProfit([7, 6, 4, 3, 1])
