#! /usr/bin/python3

from course.models import Course, CourseInstance
from django.utils import timezone
from datetime import timedelta

today = timezone.now()
tomorrow = today + timedelta(days=1)
two_days_from_now = tomorrow + timedelta(days=1)
yesterday = today - timedelta(days=1)
spring_start = today - timedelta(days=180)
spring_end = today - timedelta(days=45)
summer_start = today
summer_end = today + timedelta(days=90)
fall_end = summer_end + timedelta(days=90)


course = Course.objects.create(
        name="Ohjelmoinnin perusteet",
        code="343553",
        url="ohpe"
)

a = Course.objects.create(name="Hands-on scientific computing exercises", code="CS-E4004", url="O1")
b = Course.objects.create(name="Aplus Manual", code="EDIT", url="O2")
c = Course.objects.create(name="Tietokannat", code="CS-A1150", url="O3")
d = Course.objects.create(name="Databases", code="CS-A1153", url="O4")
e = Course.objects.create(name="Programming 1 development and testing", code="o1-dev", url="64")
f = Course.objects.create(name="Ohjelmoinnin peruskurssi Y1", code="CS-A1111", url="74")
g = Course.objects.create(name="Data Structures and Algorithms", code="CS-A1140", url="54")
h = Course.objects.create(name="Artificial Intelligence", code="CS-E4800", url="O7")
i = Course(name="Ohjelmointistudio 2", code="CS-C2120", url="O44")
i.save()
j = Course(name="Tietorakenteet ja algoritmit Y", code="CS-A1141", url="O34")
j.save()




current_course_instance = CourseInstance.objects.create(
    instance_name="Summer 2020",
    starting_time=spring_start,
    ending_time=spring_end,
    course=a,
    url="Kevät-2020"
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="Example instance name",
    starting_time=summer_end,
    ending_time=fall_end,
    course=b,
    url="Syksy2020",
    visible_to_students=False
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="Kesä 2020",
    starting_time=summer_start,
    ending_time=summer_end,
    course=c,
    url="Kesä-2020",
    visible_to_students=False
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="Kesä 2020",
    starting_time=summer_start + timedelta(days=1),
    ending_time=summer_end,
    course=d,
    url="Kesäinen-2020",
    visible_to_students=False
)


hidden_course_instance = CourseInstance.objects.create(
    instance_name="Spring 2020",
    starting_time=summer_start + timedelta(days=10),
    ending_time=summer_end,
    course=e,
    url="60-merkkiä",
    visible_to_students=False
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="Kurssikerran nimi",
    enrollment_starting_time=summer_start - timedelta(days=10),
    enrollment_ending_time=summer_end,
    starting_time=summer_start,
    ending_time=summer_end,
    course=f,
    url="nimetön",
    visible_to_students=True
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="Mooc-version",
    starting_time=summer_start,
    ending_time=summer_end,
    course=g,
    url="20-merkkiä",
    visible_to_students=True
)

hidden_course_instance = CourseInstance.objects.create(
    instance_name="2020 Summer",
    starting_time=summer_start,
    ending_time=summer_end,
    course=h,
    url="2020",
    visible_to_students=True
)
