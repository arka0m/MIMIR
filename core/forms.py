from django.forms import ModelForm, TextInput, Select, Textarea, CharField, DateTimeField, DateTimeInput, ModelChoiceField, ModelMultipleChoiceField
from datetime import datetime

from .models import Artifact, Endpoint, Compromise, Actor, Area, User

class ArtifactForm(ModelForm):
    TTP = CharField(required=False)
    comment = CharField(required=False)
    actor = ModelChoiceField(queryset=Actor.objects.exclude(name=''), required=False)
    class Meta:
        model = Artifact
        fields = ['name', 'kind', 'status', 'TTP', 'comment', 'actor']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'kind': Select(choices=Artifact.ARTIFACT_KIND),
            'status': Select(choices=Artifact.ARTIFACT_STATUS),
            'TTP': TextInput(attrs={'class': 'form-control'}),
            'comment': Textarea(attrs={'class': 'form-control'})
        }

class EndpointForm(ModelForm):
    function = CharField(required=False)
    comment = CharField(required=False)
    area = ModelChoiceField(queryset=Area.objects.exclude(name=''), required=False)
    class Meta:
        model = Endpoint
        fields = ["name", "kind", 'status', 'function', 'criticality', 'comment', 'area']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'kind': Select(choices=Endpoint.ENDPOINT_KIND),
            'status': Select(choices=Endpoint.ENDPOINT_STATUS),
            'function': TextInput(attrs={'class': 'form-control'}),
            'criticality': Select(choices=Endpoint.ENDPOINT_CRITICALITY),
            'comment': Textarea(attrs={'class': 'form-control'})
        }

class CompromiseForm(ModelForm):
    dateBegin = DateTimeField(required=False)
    dateEnd = DateTimeField(required=False)
    artifact = ModelChoiceField(queryset=Artifact.objects.all())
    endpoint = ModelChoiceField(queryset=Endpoint.objects.all())
    class Meta:
        model = Compromise
        fields = ['artifact', 'endpoint', 'dateBegin', 'dateEnd']
        widgets = {
            'dateBegin': DateTimeInput(),
            'dateEnd': DateTimeField()
        }

class ActorForm(ModelForm):
    aim = CharField(required=False)
    TTPs = CharField(required=False)
    comment = CharField(required=False)
    class Meta:
        model = Actor
        fields = ["name", "kind", "aim", "TTPs", "comment"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'kind': Select(choices=Actor.ACTOR_KIND),
            'aim': TextInput(attrs={'class': 'form-control'}),
            'TTPs': TextInput(attrs={'class': 'form-control'}),
            'comment': Textarea(attrs={'class': 'form-control'}),
        }

class AreaForm(ModelForm):
    comment = CharField(required=False)
    class Meta:
        model = Area
        fields = ["name", "criticality", "comment"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'criticality': Select(choices=Area.AREA_CRITICALITY),
            'comment': Textarea(attrs={'class': 'form-control'}),
        }

class UserForm(ModelForm):
    lastName = CharField(required=False)
    firstName = CharField(required=False)
    function = CharField(required=False)
    comment = CharField(required=False)
    endpoint = ModelChoiceField(queryset=Endpoint.objects.exclude(name=''), required=False)
    class Meta:
        model = User
        fields = ["account", "lastName", "firstName", "status", "function", "criticality", "comment", "endpoint"]
        widgets = {
            'account': TextInput(attrs={'class': 'form-control'}),
            'lastName': TextInput(attrs={'class': 'form-control'}),
            'firstName': TextInput(attrs={'class': 'form-control'}),
            'status': Select(choices=User.USER_STATUS),
            'function': TextInput(attrs={'class': 'form-control'}),
            'criticality': Select(choices=User.USER_CRITICALITY),
            'comment': Textarea(attrs={'class': 'form-control'})
        }