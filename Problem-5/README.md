# CSCE 423 - Final Problem 5

Jet is building a new feature designed to significantly reduce order delivery times. However, faster delivery sometimes means higher shipping fees, and for cost-conscious customers this might be a problem. Your task is to implement a function that finds the fastest delivery time for a given order, taking into account that the customer doesn't want to pay more than maxPrice.

Consider a customer's basket of items. You are given a list of available vendors from which you can order these items. For each vendor you know the products they provide with their price (vendorProducts) and the time it will take to deliver them (vendorsDelivery). Find the vendors that should be chosen so that the total price of items in the basket is not greater than the maxPrice, while keeping delivery time to a minimum. The delivery time is the maximum delivery time of all chosen vendors.

You should only choose vendors you're going to buy something from. It is guaranteed that there is always exactly one solution.

# Example

For maxPrice = 7, vendorsDelivery = [5, 4, 2, 3], and

vendorsProducts = [[1, 1, 1],
                   [3, -1, 3],
                   [-1, 2, 2],
                   [5, -1, -1]]
the output should be
minimalBasketPrice(maxPrice, vendorsDelivery, vendorsProducts) = [1, 2].

There are three items in the basket, so here is the list of options:

although vendor 0 can provide all items for the lowest price, it will take 5 days to deliver them;
vendors 1 and 2 can deliver all items in 4 and 2 days respectively, so in 4 days all of the items will have been delivered. It would cost 3 + 2 + 2 = 7 (note that the 2nd 0-based item is provided by both vendors, but since the price at vendor number 2 is lower, that's where we would purchase it);
vendors 2 and 3 will deliver everything in just 3 days, but it would cost 2 + 2 + 5 = 9, which is too much.
Thus, vendors 1 and 2 should be chosen to fulfill the order.