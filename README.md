# django with uwsgi and nginx

## test configuration of nginx

```
 sudo service nginx configtest
```

## class Meta
In Django, the Meta class is used to provide metadata or configuration options for a model or a form. The Meta class can have several attributes that allow you to customize the behavior of the model or form. Here are some commonly used attributes within the Meta class for Django models:

1. ordering: Specifies the default ordering for the model's database records.

2. verbose_name and verbose_name_plural: Provide human-readable names for the model in singular and plural forms, respectively.

3. db_table: Specifies the database table name for the model.

4. unique_together: A list of tuples specifying which fields, taken together, must be unique.

5. indexes: A list of database indexes to create for the model.

6. constraints: A list of database constraints to create for the model.

7. default_permissions: Controls the default set of permissions to be created when the model is created.

8. permissions: A list of permission strings associated with the model.

9. abstract: Boolean flag indicating if the model is an abstract base class.

10. app_label: The name of the application to which the model belongs.

11. managed: Boolean flag indicating if Django should manage the database table for the model or if it's a read-only or external table.

12. proxy: Boolean flag indicating if the model is a proxy model.

13. indexes: A list of Index objects to be created on the model's database table.

## aws elasticbeanstalk
### steps:
1. 