from django.test import TestCase
from django.urls import reverse

from .models import Actor

# Create your tests here.
# Use of Given-When-Then testing method for unit test or input test

class IndexTestCase(TestCase):
    '''Index access test'''

    def tearDown(self):
        print("Index Test Case: OK")

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class DBAccessTestCase(TestCase):
    '''Class define to test database access'''

    def setUp(self):
        testActor = Actor.objects.create(
                        name = "test",
                        kind = "UNK",
                        aim= "testing",
                        TTPs = "T0000",
                        comment = "This is a test"
                        )
        testActor.save()

    def tearDown(self):
        testActor = Actor.objects.get(pk='test')
        testActor.delete()
        print("DB Access Test Case: OK")
    
    def test_GetActorObject(self):
        myTest = Actor.objects.get(pk='test')
        self.assertEqual(myTest.name, 'test')

    def test_ModifyActorObject(self):
        myTest = Actor.objects.get(pk='test')

class ArtifactTestCase(TestCase):
    '''Class define to test Artifact object'''

    def setUp(self):
        testActor = Actor.objects.create(
                        name = "test",
                        kind = "UNK",
                        aim= "testing",
                        TTPs = "T0000",
                        comment = "This is a test"
                        )
        testActor.save()

    def test_When_GetExistantActor_Then_200(self):
        response = self.client.get(reverse('actorDetails', kwargs={'actorName': 'test'}))
        self.assertEquals(response.status_code, 200)

    # DONT WORK
    def test_When_GetNonExistantActor_Then_404(self):
        response = self.client.get(reverse('actorDetails', args={'actorName': 'anyone'}))
        self.assertEquals(response.status_code, 404)

    def test_CreateActorObject(self):
        response = self.client.post(reverse('artifactNew'), data={
                        'name': "test",
                        'kind': "UNK",
                        'aim': "testing",
                        'TTPs': "T0000",
                        'comment': "This is a test"})
        self.assertEquals(response.status_code, 200)