from django.db import models

class Actor(models.Model):
  ''' Class to define Threat Actor '''
  #ADD ARTIFACT_KIND (APT, Cybercrime, Hacktivism, ScriptKidies, ...)
  ACTOR_KIND = (
    ('APT', 'Advanced Persistent Threat'),
    ('CRI', 'CyberCrime'),
    ('HAK', 'Hacktivism'),
    ('KID', 'Opportunistic / ScriptKidies / Not directly targeted'),
    ('UNK', 'Unknown'),
  )
  name = models.CharField(max_length=64, primary_key=True)
  kind = models.CharField(max_length=3, choices=ACTOR_KIND, default='UNK')
  aim = models.TextField(null=True)
  TTPs = models.TextField(null=True)
  comment = models.TextField(null=True)

  def __str__(self):
    return self.name

class Artifact(models.Model):
  ''' Class for System and Network artifacts '''
  ARTIFACT_KIND = (
    ('IP', 'IP Address'),
    ('FQDN', 'Domain'),
    ('URL', 'URL path'),
    ('JA3', 'JA3/JA3S'),
    ('PROC', 'Process'),
    ('HIVE', 'Registry Key'),
    ('FILE', 'File or Folder'),
    ('HASH', 'HASH'),
    ('OTH', 'Other ...'),
  )
  ARTIFACT_STATUS = (
    ('IOC', 'Malicious'),
    ('SUS', 'Suspicious'),
    ('RAS', 'Whitelisted'),
  )
  name = models.CharField(max_length=255, primary_key=True)
  kind = models.CharField(max_length=4, choices=ARTIFACT_KIND, default='OTH')
  status = models.CharField(max_length=3, choices=ARTIFACT_STATUS, default='SUS')
  TTP = models.CharField(max_length=32, null=True)
  comment = models.TextField(null=True)
  actor = models.ForeignKey(Actor, on_delete=models.SET(''), blank=True, null=True)

  def __str__(self):
    return self.name

class Area(models.Model):
  ''' Class to define scope of compromised endpoint '''
  AREA_CRITICALITY = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
  )
  name = models.CharField(max_length=64, primary_key=True)
  criticality = models.CharField(max_length=1, choices=AREA_CRITICALITY, default='M')
  comment = models.TextField(null=True)

  def __str__(self):
    return self.name

class Endpoint(models.Model):
  ''' Class to define system endpoint '''
  ENDPOINT_STATUS = (
    ('COM', 'Compromised'),
    ('UNK', 'Unknown'),
    ('RAS', 'Healthy'),
  )
  ENDPOINT_CRITICALITY = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
  )
  ENDPOINT_KIND = (
    ('WKS', 'Workstation'),
    ('SVR', 'Server'),
    ('NET', 'Networking Device'),
    ('OTH', 'Other'),
    ('UNK', 'Unkown'),
  )
  name = models.CharField(max_length=64, primary_key=True)
  kind = models.CharField(max_length=3, choices=ENDPOINT_KIND, default='UNK')
  status = models.CharField(max_length=3, choices=ENDPOINT_STATUS, default='UNK')
  function = models.CharField(max_length=32, null=True)
  criticality = models.CharField(max_length=1, choices=ENDPOINT_CRITICALITY, default='M')
  comment = models.TextField(null=True)
  area = models.ForeignKey(Area, on_delete=models.SET(''), blank=True, null=True)

  def __str__(self):
    return self.name

class Corrupted(models.Model):
  ''' Class to follow relation between Artifact and Endpoint '''
  # WARNING: Primary is currently an ID auto-incremented.
  dateDetection = models.DateTimeField(auto_now_add=True)
  dateBegin = models.DateTimeField(null=True)
  dateEnd = models.DateTimeField(null=True)
  artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
  endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class User(models.Model):
  ''' Class to define user function and criticality '''
  USER_STATUS = (
    ('COM', 'Compromised'),
    ('UNK', 'Unknown'),
    ('RAS', 'Healthy'),
  )
  USER_CRITICALITY = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
  )
  account = models.CharField(max_length=64, primary_key=True)
  lastName = models.CharField(max_length=64, null=True)
  firstName = models.CharField(max_length=32, null=True)
  status = models.CharField(max_length=3, choices=USER_STATUS, default='UNK')
  function = models.CharField(max_length=32, null=True)
  criticality = models.CharField(max_length=1, choices=USER_CRITICALITY, default='M')
  comment = models.TextField(null=True)
  endpoint = models.ForeignKey(Endpoint, on_delete=models.SET(''), blank=True, null=True)

  def __str__(self):
    return self.name