#! /usr/bin/python3

from course.models import Course, CourseInstance
a = Course(name="Hands-on scientific computing exercises", code="CS-E4004", url="O1")
a.save()
b = Course(name="Aplus Manual", code="EDIT", url="O2")
b.save()
c = Course(name="Tietokannat", code="CS-A1150", url="O3")
c.save()
d = Course(name="Databases", code="CS-A1153", url="O4")
d.save()
e = Course(name="Programming 1 development and testing", code="o1-dev", url="O4")
e.save()
f = Course(name="Ohjelmoinnin peruskurssi Y1", code="CS-A1111", url="O4")
f.save()
g = Course(name="Data Structures and Algorithms", code="CS-A1140", url="O4")
g.save()
h = Course(name="Artificial Intelligence", code="CS-E4800", url="O4")
h.save()
i = Course(name="Ohjelmointistudio 2", code="CS-C2120", url="O4")
i.save()
j = Course(name="Tietorakenteet ja algoritmit Y", code="CS-A1141", url="O4")
j.save()



