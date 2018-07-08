from datetime import datetime
from django.test import TestCase
from PyIntern.users.models import Student, Company, Coordinator


class StudentModelTest(TestCase):
    """Test Student Model."""

    def setUp(self):
        self.obj = Student(
            registration=11160021,
            name='Lays Rodrigues',
            email='lays.rodrigues@kde.org',
            phone='21-11111-11111',
            address='Bourbon Street',
            username='lays147',
            course='SI',
            mini_bio='BlaBla',
            cpf='12345678901',
            birth_date='1992-09-17',
            competences='Skill1,Skill2',
        )
        self.obj.save()

    def test_create(self):
        """Test if the student was created."""
        self.assertTrue(Student.objects.exists())

    def test_created_at(self):
        """Student must have an auto created_at att."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Test if the object has the correct name."""
        self.assertEqual('Lays Rodrigues', str(self.obj))


class CoordinatorModelTest(TestCase):
    def setUp(self):
        self.obj = Coordinator(
            registration=11160021,
            name='Lays Rodrigues',
            email='lays.rodrigues@kde.org',
            phone='21-11111-11111',
            address='Bourbon Street',
            username='lays147',
            cpf='12345678901',
        )
        self.obj.save()

    def test_create(self):
        """Test if the coordinator was created."""
        self.assertTrue(Coordinator.objects.exists())

    def test_created_at(self):
        """Coordinator must have an auto created_at att."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Test if the object has the correct name."""
        self.assertEqual('Lays Rodrigues', str(self.obj))


class CompanyModelTest(TestCase):
    def setUp(self):
        self.obj = Company(
            registration=11160021,
            name='Lays Rodrigues',
            email='lays.rodrigues@kde.org',
            phone='21-11111-11111',
            address='Bourbon Street',
            username='lays147',
            company_name='Python>>Java',
            cnpj='12345678901478',
            description='BlaBla',
        )
        self.obj.save()

    def test_create(self):
        """Test if the user Company was created."""
        self.assertTrue(Company.objects.exists())

    def test_created_at(self):
        """Company must have an auto created_at att."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Test if the object has the correct name."""
        self.assertEqual('Lays Rodrigues', str(self.obj))
