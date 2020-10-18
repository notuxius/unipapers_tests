def test_calculate_default_price(home_page):
    home_page.load()
    home_page.calculate_default_price()

    assert home_page.current_price() == "$13.00"
    assert not home_page.discount_is_checked()
    assert not home_page.discount_info_is_displayed()


def test_calculate_custom_price(home_page):
    home_page.load()
    home_page.calculate_custom_price()

    assert home_page.current_price() == "$47.60"
    assert home_page.old_price() == "$56.00"
    assert home_page.discount_size() == "15% OFF"
