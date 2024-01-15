marks = {"DS":90,"algo":80,"oop":85}
marks["sp"] = 56
marks["DBMS"] = 78
print(marks)
del marks["sp"]
print(marks)

marks_keys = marks.keys()
marks_values = marks.values()

print(marks_keys)
print(marks_values)

marks_items = marks.items()
print(marks_items)
marks.clear()
m_i = marks.items()
print(m_i)
print(marks)

