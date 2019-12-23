from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    # 상속받은 자식 클래스에서, 부모 클래스의 meta속성을 가지면서 자신만의 속성을 추가하고 싶다면
    # 부모클래스.meta를 상속받고 나머지 필요한 속성들을 정의하도록 한다.
    # 아래 경우 부모로부터 ordering 상속
    class Meta(CommonInfo.Meta):
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'
        # db_table = 'Abstract_Student_Table'

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원 {self.academy})'


# Be careful with related_name and related_query_name
class Base(models.Model):
    m2m = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
