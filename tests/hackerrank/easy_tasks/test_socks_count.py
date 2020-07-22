from hackerrank.easy_tasks.socks_count import sock_merchant


n = 9
arr = [1, 1, 1, 2, 2, 3, 3, 3, 3]


def test_count_socks(n=n, arr=arr):
    result = sock_merchant(n, arr)
    print(result)
    assert result
