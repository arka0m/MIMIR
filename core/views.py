from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Artifact, Endpoint, Corrupted, Actor, Area, User
from .forms import ArtifactForm, EndpointForm, CorruptedForm, ActorForm, AreaForm, UserForm

def index(request):
    # Display index
    return render(request, 'core/index.html')

def artifacts(request):
    '''Manage display/creation/modification/deletion of artifact objects'''
    if request.method == 'POST':
    # IF method is POST, create/modify/delete an instance of Endpoint.
        if request.POST.get('delete'):
        # Manage deletion of an artifact
            artifactName = request.POST.get('delete')
            artifact = Artifact.objects.get(pk=artifactName)
            artifact.delete()
        else:
        # Managa creation or modification of an artifact
            name = request.POST.get('name')
            kind = request.POST.get('kind')
            status = request.POST.get('status')
            TTP = request.POST.get('TTP')
            comment = request.POST.get('comment')
            actor = request.POST.get('actor')
            actor = Actor.objects.get(pk=actor)
        
            artifact = Artifact.objects.filter(name=name)
            if not artifact.exists():
                #If artifact doesn't exist, create a new one.
                artifact = Artifact.objects.create(
                    name = name,
                    kind = kind,
                    status = status,
                    TTP = TTP,
                    comment = comment,
                    actor = actor
                )
                artifact.save()
            else:
                #If it exists, modify the attributs.
                artifact.update(
                    name = name,
                    kind = kind,
                    status = status,
                    TTP = TTP,
                    comment = comment,
                    actor = actor
                )
    # Make a list of all endpoints
    # TODO: Add filter features

    artifacts_list = Artifact.objects.all()
    # Get all the artifacts

    paginator = Paginator(artifacts_list, 20)
    # Manage pagination and display them per page.
    page = request.GET.get('page')
    try:
        artifacts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        artifacts = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        artifacts = paginator.page(paginator.num_pages)
    # Send to artifacts.html with the rights elements.
    context = {
        'artifacts' : artifacts
        }
    return render(request, 'core/artifacts/artifactsBase.html', context)

def artifactDetails(request, artifactName):
    '''Manage display of artifact details'''
    artifact = get_object_or_404(Artifact, pk=artifactName)
    # Get artifact object from its name
    endpoints = Corrupted.objects.filter(artifact_id=artifactName)
    # Get endpoints linked to an artifact
    context = {
        'artifact' : artifact,
        'endpoints' : endpoints
        }
    return render(request, 'core/artifacts/artifactDetails.html', context)

def artifactNew(request):
    '''Manage creation/modification of artifacts'''
    if request.method == 'POST':
        # Modification of an artifact
        form = ArtifactForm(request.POST)
    else:
        # Creation of an artifact
        form = ArtifactForm()
    context = {
        'form' : form
    }
    # Send to form
    return render(request, 'core/artifacts/artifactNew.html', context)

def endpoints(request):
    # IF method is POST, create/modify/delete an instance of Endpoint.
    if request.method == 'POST':
        if request.POST.get('delete'):
            endpointName = request.POST.get('delete')
            endpoint = Endpoint.objects.get(pk=endpointName)
            endpoint.delete()
        else:
            name = request.POST.get('name')
            kind = request.POST.get('kind')
            status = request.POST.get('status')
            function = request.POST.get('function')
            criticality = request.POST.get('criticality')
            comment = request.POST.get('comment')
            area = request.POST.get('area')
            area = Area.objects.get(pk=area)
        
            endpoint = Endpoint.objects.filter(pk=name)
            if not endpoint.exists():
                #If endpoint doesn't exist, create a new one.
                endpoint = Endpoint.objects.create(
                    name = name,
                    kind = kind,
                    status = status,
                    function = function,
                    criticality = criticality,
                    comment = comment,
                    area = area
                )
                endpoint.save()
            else:
                #If it exists, modify the attributs.
                endpoint.update(
                    name = name,
                    kind = kind,
                    status = status,
                    function = function,
                    criticality = criticality,
                    comment = comment,
                    area = area
                )
    # Make a list of all endpoints
    # TODO: Add filter features
    endpoints_list = Endpoint.objects.exclude(pk='')
    paginator = Paginator(endpoints_list, 10)
    page = request.GET.get('page')
    try:
        endpoints = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        endpoints = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        endpoints = paginator.page(paginator.num_pages)
    context = {
        'endpoints' : endpoints
        }
    return render(request, 'core/endpoints/endpointsBase.html', context)

def endpointDetails(request, endpointName):
    endpoint = Endpoint.objects.get(pk=endpointName)
    artifacts = Corrupted.objects.filter(endpoint_id=endpointName)
    users = User.objects.filter(endpoint_id=endpointName)
    context = {
        'endpoint' : endpoint,
        'artifacts' : artifacts,
        'users' : users
        }
    return render(request, 'core/endpoints/endpointDetails.html', context)

def endpointNew(request):
    if request.method == 'POST':
        form = EndpointForm(request.POST)
    else:
        form = EndpointForm()
    context = {
        'form' : form
    }
    return render(request, 'core/endpoints/endpointNew.html', context)

def compromise(request):
    # IF method is POST, This is a new instance of Corrupted.
    if request.method == 'POST':
        if request.POST.get('delete'):
            corruptedId = request.POST.get('delete')
            corrupted = Corrupted.objects.get(pk=corruptedId)
            corrupted.delete()
        else:
            artifact = request.POST.get('artifact')
            endpoint = request.POST.get('endpoint')
            id = request.POST.get('id')
            #dateDetection = request.POST.get('dateDetection')
            #dateBegin = request.POST.get('dateBegin')
            #dateEnd = request.POST.get('dateEnd')

            corrupted = Corrupted.objects.filter(pk=id)
            if not corrupted.exists():
                #If compromise link doesn't exist, create a new one.
                artifact = Artifact.objects.get(pk=artifact)
                endpoint = Endpoint.objects.get(pk=endpoint)
                corrupted = Corrupted.objects.create(
                    artifact = artifact,
                    endpoint = endpoint,
                )
                corrupted.save()
            # NOT YET IMPLEMENTED
            #else:
            #    corrupted.update(artifact=artifact, endpoint=endpoint, dateDetection=dateDetection, dateBegin=dateBegin, dateEnd=dateEnd)
    # Make a list of all corrupts
    # TODO: Add filter features
    corrupted_list = Corrupted.objects.all()
    paginator = Paginator(corrupted_list, 20)
    page = request.GET.get('page')
    try:
        corrupts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        corrupts = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        corrupts = paginator.page(paginator.num_pages)
    context = {
        'corrupts' : corrupts
        }
    return render(request, 'core/compromise/compromiseBase.html', context)

def compromiseDetails(request, compromiseId):
    corrupted = Corrupted.objects.get(pk=compromiseId)
    context = {
        'corrupted' : corrupted
        }
    return render(request, 'core/compromise/compromiseDetails.html', context)

def compromiseNew(request):
    if request.method == 'POST':
        form = CorruptedForm(request.POST)
    else:
        form = CorruptedForm()
    context = {
        'form' : form
    }
    return render(request, 'core/compromise/compromiseNew.html', context)

def actors(request):
    if request.method == 'POST':
        if request.POST.get('delete'):
            actorName = request.POST.get('delete')
            actor = Actor.objects.get(pk=actorName)
            actor.delete()
        else:
            name = request.POST.get('name')
            kind = request.POST.get('kind')
            aim = request.POST.get('aim')
            TTPs = request.POST.get('TTPs')
            comment = request.POST.get('comment')
        
            actor = Actor.objects.filter(pk=name)
            if not actor.exists():
                #If endpoint doesn't exist, create a new one.
                actor = Actor.objects.create(
                    name = name,
                    kind = kind,
                    aim= aim,
                    TTPs = TTPs,
                    comment = comment
                )
                actor.save()
            else:
                #If it exists, modify the attributs.
                actor.update(name=name, kind=kind, aim=aim, TTPs=TTPs, comment=comment)
    # Make a list of all actors
    # TODO: Add filter features
    actors_list = Actor.objects.exclude(pk='')
    paginator = Paginator(actors_list, 10)
    page = request.GET.get('page')
    try:
        actors = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        actors = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        actors = paginator.page(paginator.num_pages)
    context = {
        'actors' : actors
        }
    return render(request, 'core/actors/actorsBase.html', context)

def actorDetails(request, actorName):
    actor = Actor.objects.get(pk=actorName)
    artifacts = Artifact.objects.filter(actor=actorName)
    context = {
        'actor' : actor,
        'artifacts' : artifacts
        }
    return render(request, 'core/actors/actorDetails.html', context)

def actorNew(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
    else:
        form = ActorForm()
    context = {
        'form' : form
    }
    return render(request, 'core/actors/actorNew.html', context)

def areas(request):
    if request.method == 'POST':
        if request.POST.get('delete'):
            areaName = request.POST.get('delete')
            area = Area.objects.get(pk=areaName)
            area.delete()
        else:
            name = request.POST.get('name')
            criticality = request.POST.get('criticality')
            comment = request.POST.get('comment')
        
            area = Area.objects.filter(pk=name)
            if not area.exists():
                #If endpoint doesn't exist, create a new one.
                area = Area.objects.create(
                    name = name,
                    criticality = criticality,
                    comment = comment
                )
                area.save()
            else:
                #If it exists, modify the attributs.
                area.update(name=name, criticality=criticality, comment=comment)
    # Make a list of all actors
    # TODO: Add filter features
    areas_list = Area.objects.exclude(pk='')
    paginator = Paginator(areas_list, 10)
    page = request.GET.get('page')
    try:
        areas = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        areas = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        areas = paginator.page(paginator.num_pages)
    context = {
        'areas' : areas
        }
    return render(request, 'core/areas/areasBase.html', context)

def areaDetails(request, areaName):
    area = Area.objects.get(pk=areaName)
    endpoints = Endpoint.objects.filter(area=areaName)
    context = {
        'area' : area,
        'endpoints' : endpoints
        }
    return render(request, 'core/areas/areaDetails.html', context)

def areaNew(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
    else:
        form = AreaForm()
    context = {
        'form' : form
    }
    return render(request, 'core/areas/areaNew.html', context)

def users(request):
    '''Manage display/creation/modification/deletion of users objects'''
    if request.method == 'POST':
    # IF method is POST, create/modify/delete an instance of User.
        if request.POST.get('delete'):
        # Manage deletion of a user
            accountName = request.POST.get('delete')
            user = User.objects.get(pk=accountName)
            user.delete()
        else:
        # Manage creation or modification of a user
            account = request.POST.get('account')
            lastName = request.POST.get('lastName')
            firstName = request.POST.get('firstName')
            status = request.POST.get('status')
            function = request.POST.get('function')
            criticality = request.POST.get('criticality')
            comment = request.POST.get('comment')
            endpoint = request.POST.get('endpoint')
            endpoint = Endpoint.objects.get(pk=endpoint)
        
            user = User.objects.filter(pk=account)
            if not user.exists():
                #If user doesn't exist, create a new one.
                user = User.objects.create(
                    account = account,
                    lastName = lastName,
                    firstName = firstName,
                    status = status,
                    criticality = criticality,
                    comment = comment,
                    endpoint = endpoint
                )
                user.save()
            else:
                #If it exists, modify the attributs.
                user.update(
                    account = account,
                    lastName = lastName,
                    firstName = firstName,
                    status = status,
                    criticality = criticality,
                    comment = comment,
                    endpoint = endpoint
                )
    # Make a list of all users
    # TODO: Add filter features

    users_list = User.objects.all()
    # Get all the users

    paginator = Paginator(users_list, 20)
    # Manage pagination and display them per page.
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page.
        users = paginator.page(paginator.num_pages)
    # Send to users.html with the rights elements.
    context = {
        'users' : users
        }
    return render(request, 'core/users/usersBase.html', context)

def userDetails(request, accountName):
    '''Manage display of user details'''
    user = get_object_or_404(User, pk=accountName)
    # Get user object from its name
    context = {
        'user' : user,
        }
    return render(request, 'core/users/userDetails.html', context)

def userNew(request):
    '''Manage creation/modification of users'''
    if request.method == 'POST':
        # Modification of a user
        form = UserForm(request.POST)
    else:
        # Creation of a user
        form = UserForm()
    context = {
        'form' : form
    }
    # Send to form
    return render(request, 'core/users/userNew.html', context)

def search(request):
    query = request.GET['query']
    if not query:
        message = "Recherche vide !!"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]
        if len(albums) == 0:
            message = "Aucun album trouvé ..."
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Les albums correspondant sont :\n
                <ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

