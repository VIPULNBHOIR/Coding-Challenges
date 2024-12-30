def Count(pages : list[int], mid :int)-> int:
    students = 1
    no_of_pages = 0
    for book_pages in pages: 
        if (no_of_pages + book_pages <= mid):
            no_of_pages += book_pages
        else:
            students += 1
            no_of_pages = book_pages

    return students



if __name__ == '__main__':

    pages = []
    books = int(input())
    m = int(input())
    if m > books:
        print(-1)
    for i in range(books):
        pages.append(int(input()))

    low = max(pages)
    high = sum(pages)
    while (low <= high):
        mid = (low + high) // 2

        students = Count(pages, mid)

        if students > m:
            low = mid + 1
        else:
            high = mid - 1

    print(low) 
