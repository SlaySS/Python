class Pagination():
    current_page = 0

    def __init__(self, item=[], pagesize=5):
        self.item = item
        self.pagesize = pagesize

    def get_visible_items(self):
        yield self.item[self.current_page:self.current_page + self.pagesize]

    def next_page(self):
        self.current_page += self.pagesize

    def prev_page(self):
        self.current_page -= self.pagesize

    def first_page(self):
        self.current_page = 0

    def last_page(self):
        self.current_page = len(self.item) - len(self.item) % self.pagesize

    def go_to_page(self, page):
        self.page=page
        if page < 1:
            self.first_page()
        if page > len(self.item) % self.pagesize:
            self.last_page()
        else:
            self.current_page = self.pagesize*page-1



lst = list('VQ4v9qvqv345343242')

p = Pagination(lst)
print(list(p.get_visible_items()))
print(p.current_page)
p.go_to_page(-2)
print(p.current_page)
print(list(p.get_visible_items()))
# p.next_page()
# print(list(p.get_visible_items()))
# p.last_page()
# print(list(p.get_visible_items()))
# p.first_page()
# print(list(p.get_visible_items()))
