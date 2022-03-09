0x0F-python-object_relational_mapping

**Background Context**

        The first part uses th module MySQLdb to connect  to
        MySQL database and execute SQL queries.

        The second part uses the model SQLAchemy an Object
        Relational Mapper

        The biggest difference is: no more SQL queries! Indeed,
        the purpose of an ORM is to abstract the storage to the
        usage. With an ORM, your biggest concern will be
        “What can I do with my objects” and not “How this object
        is stored? where? when?”. You won’t write any SQL queries
        only Python code. Last thing, your code won’t be “storage
        type” dependent. You will be able to change your storage
        easily without re-writing your entire project.


**Install MySQLdb module version 2.0.x**

        $ sudo apt-get install python3-dev
        $ sudo apt-get install libmysqlclient-dev
        $ sudo apt-get install zlib1g-dev
        $ sudo pip3 install mysqlclient
        ...
        $ python3
        >>> import MySQLdb
        >>> MySQLdb.version_info 
        (2, 0, 3, 'final', 0)

**Install SQLAlchemy module version 1.4.x**

        $ sudo pip3 install SQLAlchemy
        ...
        $ python3
        >>> import sqlalchemy
        >>> sqlalchemy.__version__ 
        '1.4.22'