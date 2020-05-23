class Pagination:

    def __init__(self, items=[], pagesize=10):
        self.items = items
        self.pagesize = pagesize
        self.totalpages = 1 if not self.items else len(self.items) // self.pagesize + 1
        self.current_page = 1

    def get_items(self):
        return self.items

    def get_page_size(self):
        return self.pagesize

    def get_current_page(self):
        return self.current_page

    def get_visible_items(self):
        start = (self.current_page - 1) * self.pagesize
        return (self.items[start:start + self.pagesize])

    def next_page(self):
        if self.current_page == self.totalpages:
            return self
        self.current_page += 1
        return self

    def prev_page(self):
        if self.current_page == 1:
            return self
        self.current_page -= 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.totalpages
        return self

    def go_to_page(self, page):
        if page < 1:
            page = 1
        elif page > self.totalpages:
            page = self.totalpages
        self.current_page = page
        return self


lst = list('VQ4v9qvqv345343242')

p = Pagination(lst)
print(list(p.get_visible_items()))
print(p.current_page)
p.go_to_page(2)
print(p.current_page)
print(list(p.get_visible_items()))
# p.next_page()
# print(list(p.get_visible_items()))
# p.last_page()
# print(list(p.get_visible_items()))
# p.first_page()
# print(list(p.get_visible_items()))
