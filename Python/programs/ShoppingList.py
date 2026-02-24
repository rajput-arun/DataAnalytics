def compare_shopping_lists(your_list: set, friend_list: set) -> bool:
    return (set(your_list) == set(friend_list))

compare_shopping_lists({"apples", "bread"}, {"bread", "apples"}) # True
compare_shopping_lists({"apples", "bread"}, {"bananas", "bread"}) # False
