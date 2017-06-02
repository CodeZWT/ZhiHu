# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
import json


class Answer(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    questionid = models.CharField(db_column = 'QuestionID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    answerid = models.CharField(db_column = 'AnswerID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    content = models.TextField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'answer'


class AnswerQuestion(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    questionid = models.CharField(db_column = 'QuestionID', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    answerid = models.CharField(db_column = 'AnswerId', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    questionname = models.TextField(db_column = 'QuestionName', blank = True, null = True)  # Field name made lowercase.
    fromtopicid = models.CharField(db_column = 'FromTopicId', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    fromtopicname = models.CharField(db_column = 'FromTopicName', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    content = models.TextField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'answer_question'


class AucComplex(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    sim = models.CharField(max_length = 10, blank = True, null = True)
    param = models.FloatField(blank = True, null = True)
    auc = models.FloatField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'auc_complex'


class AuthGroup(models.Model):
    name = models.CharField(unique = True, max_length = 80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length = 255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length = 100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length = 128)
    last_login = models.DateTimeField(blank = True, null = True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique = True, max_length = 150)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank = True, null = True)
    object_repr = models.CharField(max_length = 200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank = True, null = True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key = True, max_length = 40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Followees(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    person_id = models.IntegerField(blank = True, null = True)
    personid = models.CharField(max_length = 100, blank = True, null = True)
    id_f = models.IntegerField(blank = True, null = True)
    followeesid = models.CharField(max_length = 100, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'followees'


class Person(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 100)  # Field name made lowercase.
    password = models.CharField(max_length = 20, blank = True, null = True)
    personhashid = models.CharField(db_column = 'PersonHashID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personname = models.CharField(db_column = 'PersonName', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    persongender = models.CharField(db_column = 'PersonGender', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personbiography = models.CharField(db_column = 'PersonBiography', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personaddress = models.CharField(db_column = 'PersonAddress', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personbusiness = models.CharField(db_column = 'PersonBusiness', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personemployment = models.CharField(db_column = 'PersonEmployment', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personposition = models.CharField(db_column = 'PersonPosition', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personeducation = models.CharField(db_column = 'PersonEducation', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personeducation_extra = models.CharField(db_column = 'PersonEducation_extra', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    personfolloweesnum = models.IntegerField(db_column = 'PersonFolloweesNum', blank = True, null = True)  # Field name made lowercase.
    personfollowersnum = models.IntegerField(db_column = 'PersonFollowersNum', blank = True, null = True)  # Field name made lowercase.
    personagreenum = models.IntegerField(db_column = 'PersonAgreeNum', blank = True, null = True)  # Field name made lowercase.
    personthanksnum = models.IntegerField(db_column = 'PersonThanksNum', blank = True, null = True)  # Field name made lowercase.
    personasksnum = models.IntegerField(db_column = 'PersonAsksNum', blank = True, null = True)  # Field name made lowercase.
    personanswersnum = models.IntegerField(db_column = 'PersonAnswersNum', blank = True, null = True)  # Field name made lowercase.
    personpostsnum = models.IntegerField(db_column = 'PersonPostsNum', blank = True, null = True)  # Field name made lowercase.
    personcollectionsnum = models.IntegerField(db_column = 'PersonCollectionsNum', blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class PersonId(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 100, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_id'


class PersonTopic(models.Model):
    id = models.IntegerField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    topicid = models.CharField(db_column = 'TopicID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    topicname = models.CharField(db_column = 'TopicName', max_length = 100, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_topic'


class Question(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    questionid = models.CharField(db_column = 'QuestionID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    questionname = models.CharField(db_column = 'QuestionName', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    fromtopicid = models.CharField(db_column = 'FromTopicID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    fromtopicname = models.CharField(db_column = 'FromTopicName', max_length = 100, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'


class QuestionInfo(models.Model):
    questionid = models.CharField(db_column = 'QuestionID', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    questionname = models.TextField(db_column = 'QuestionName', blank = True, null = True)  # Field name made lowercase.
    fromtopicid = models.CharField(db_column = 'FromTopicId', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    fromtopicname = models.CharField(db_column = 'FromTopicName', max_length = 50, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question_info'


class RecommendFollow(models.Model):
    id = models.IntegerField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    personid = models.IntegerField(db_column = 'PersonID', blank = True, null = True)  # Field name made lowercase.
    refollow_id = models.IntegerField(db_column = 'reFollow_ID', blank = True, null = True)  # Field name made lowercase.
    personname = models.CharField(db_column = 'PersonName', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    count_cn = models.IntegerField(blank = True, null = True)
    cn_0 = models.IntegerField(blank = True, null = True)
    cn_0_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_1 = models.IntegerField(blank = True, null = True)
    cn_1_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_2 = models.IntegerField(blank = True, null = True)
    cn_2_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_3 = models.IntegerField(blank = True, null = True)
    cn_3_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_4 = models.IntegerField(blank = True, null = True)
    cn_4_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_5 = models.IntegerField(blank = True, null = True)
    cn_5_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_6 = models.IntegerField(blank = True, null = True)
    cn_6_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_7 = models.IntegerField(blank = True, null = True)
    cn_7_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_8 = models.IntegerField(blank = True, null = True)
    cn_8_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_9 = models.IntegerField(blank = True, null = True)
    cn_9_name = models.CharField(max_length = 50, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'recommend_follow'


class RecommendTopic(models.Model):
    id = models.IntegerField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    personid = models.IntegerField(db_column = 'PersonID', blank = True, null = True)  # Field name made lowercase.
    retopic_id = models.IntegerField(db_column = 'reTopic_ID', blank = True, null = True)  # Field name made lowercase.
    cn_0 = models.IntegerField(blank = True, null = True)
    cn_1 = models.IntegerField(blank = True, null = True)
    cn_2 = models.IntegerField(blank = True, null = True)
    cn_3 = models.IntegerField(blank = True, null = True)
    cn_4 = models.IntegerField(blank = True, null = True)
    cn_5 = models.IntegerField(blank = True, null = True)
    cn_6 = models.IntegerField(blank = True, null = True)
    cn_7 = models.IntegerField(blank = True, null = True)
    cn_8 = models.IntegerField(blank = True, null = True)
    cn_9 = models.IntegerField(blank = True, null = True)
    topicid = models.IntegerField(db_column = 'TopicID', blank = True, null = True)  # Field name made lowercase.
    topicname = models.CharField(db_column = 'TopicName', max_length = 50, blank = True, null = True)  # Field name made lowercase.
    cn_0_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_1_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_2_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_3_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_4_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_5_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_6_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_7_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_8_name = models.CharField(max_length = 50, blank = True, null = True)
    cn_9_name = models.CharField(max_length = 50, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'recommend_topic'


class Topic(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    father_topic = models.CharField(db_column = 'Father_Topic', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    father_topic_id = models.IntegerField(db_column = 'Father_Topic_ID', blank = True, null = True)  # Field name made lowercase.
    child_topic = models.CharField(db_column = 'Child_Topic', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    child_topic_id = models.IntegerField(db_column = 'Child_Topic_ID', blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic'


class TopicId(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    topicid = models.IntegerField(db_column = 'TopicID', blank = True, null = True)  # Field name made lowercase.
    topicname = models.CharField(db_column = 'TopicName', max_length = 100, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic_id'


class TopicIdIntroduction(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    topicid = models.IntegerField(db_column = 'TopicID', blank = True, null = True)  # Field name made lowercase.
    topicname = models.CharField(db_column = 'TopicName', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    topicintroduction = models.CharField(db_column = 'TopicIntroduction', max_length = 300, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic_id_introduction'


class Topicfollow(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    id_p = models.IntegerField(db_column = 'ID_p', blank = True, null = True)  # Field name made lowercase.
    personid = models.CharField(db_column = 'PersonID', max_length = 100, blank = True, null = True)  # Field name made lowercase.
    id_t = models.IntegerField(db_column = 'ID_t', blank = True, null = True)  # Field name made lowercase.
    topicid = models.CharField(db_column = 'TopicID', max_length = 100, blank = True, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topicfollow'

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            data = []
            data.append(obj.id)
            data.append(obj.personid)
            data.append(obj.password)
            data.append(obj.personhashid)
            data.append(obj.personname)
            data.append(obj.persongender)
            data.append(obj.personbiography)
            data.append(obj.personaddress)
            data.append(obj.personbusiness)
            data.append(obj.personemployment)
            data.append(obj.personposition)
            data.append(obj.personeducation)
            data.append(obj.personeducation_extra)
            data.append(obj.personfolloweesnum)
            data.append(obj.personfollowersnum)
            data.append(obj.personagreenum)
            data.append(obj.personthanksnum)
            data.append(obj.personasksnum)
            data.append(obj.personanswersnum)
            data.append(obj.personpostsnum)
            data.append(obj.personcollectionsnum)
            return data
        return json.JSONEncoder.default(self, obj)

class FollowEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            data = []
            data.append(obj.id_f)
            data.append(obj.followeesid)
            return data
        return json.JSONEncoder.default(self, obj)
