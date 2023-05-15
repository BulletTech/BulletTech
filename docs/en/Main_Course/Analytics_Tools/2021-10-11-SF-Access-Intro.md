---
template: overrides/blogs.html
tags:
  - analytics
  - database
---

# SnowFlake权限概览

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/fmtJR9O3jVVBav0A0X8yFw)

## 1 Introduction


The permissions that correctly manage objects (such as databases, tables, etc.) in the database are very important, but they are often ignored. They often involve permissions and troubles before they regret that they did not seriously treat authority management at that time.Therefore, this article will take the very popular Snowflake data warehouse as an example, to simply explain the important concepts and commonly used commands of authority management.It is recommended to like the collection and use it in the future!


## 2 Snowflake permissions control framework


Snowflake has two permissions control models:


-Discretionary Access Control (DAC), independent access control: each object (Object) has an owner (Owner), and the owner can grant different permissions of others.
-HLE-BASED Access Control (RBAC), character-based access control: access permissions are controlled by roles, and characters can be assigned to different users (USER).


In Snowflake, there are some important concepts to help the solution authority control:


-SECURABLE OBJECT, security object, a entity that can be granted specific permissions. If there is no permissions, the object of the object will be prohibited.
-ROLE, character, an entity that can accept permissions, the character can be assigned to the user, and the character can also be assigned to other characters, forming different roles.
-Livilege, permissions: the level of access control for objects.By setting different permissions, the particle size of the orientation level can be controlled.
-User, user, identity that can be recognized by Snowflake can be people or programs.


In Snowflake, the permissions control of the security object are shown below.Access security objects can give permissions through the character, that is, the authority is assigned to other characters or objects.In addition, each security object has one owner, which can grant other role permissions.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/access-control-relationships.png"  />

<figcaption> Snowflake permission control schematic diagram </figcaption>
</figure>


## 3 Commonly used commands


Basically understand how Snowflake manages the authority, and use the command to operate and view the command to be more handy.


### 3.1 Gift permissions


```sql
GRANT {  { globalPrivileges         | ALL [ PRIVILEGES ] } ON ACCOUNT
| { accountObjectPrivileges  | ALL [ PRIVILEGES ] } ON { USER | RESOURCE MONITOR | WAREHOUSE | DATABASE | INTEGRATION } <object_name>
| { schemaPrivileges         | ALL [ PRIVILEGES ] } ON { SCHEMA <schema_name> | ALL SCHEMAS IN DATABASE <db_name> }
| { schemaPrivileges         | ALL [ PRIVILEGES ] } ON { FUTURE SCHEMAS IN DATABASE <db_name> }
| { schemaObjectPrivileges   | ALL [ PRIVILEGES ] } ON { <object_type> <object_name> | ALL <object_type_plural> IN { DATABASE <db_name> | SCHEMA <schema_name> } }
| { schemaObjectPrivileges   | ALL [ PRIVILEGES ] } ON FUTURE <object_type_plural> IN { DATABASE <db_name> | SCHEMA <schema_name> }
}
TO [ ROLE ] <role_name> [ WITH GRANT OPTION ]
```


in:


```sql
global Privileges ::=
{ { CREATE { ROLE | USER | WAREHOUSE | DATABASE | INTEGRATION } } | APPLY MASKING POLICY | APPLY ROW ACCESS POLICY | APPLY TAG | EXECUTE TASK | MANAGE GRANTS | MONITOR { EXECUTION | USAGE }  } [ , ... ]


account Object Privileges ::=
-- For USER
{ MONITOR } [ , ... ]
-- For RESOURCE MONITOR
{ MODIFY | MONITOR } [ , ... ]
-- For WAREHOUSE
{ MODIFY | MONITOR | USAGE | OPERATE } [ , ... ]
-- For DATABASE
{ MODIFY | MONITOR | USAGE | CREATE SCHEMA | IMPORTED PRIVILEGES } [ , ... ]
-- For INTEGRATION
{ USAGE | USE_ANY_ROLE } [ , ... ]


schema Privileges ::=
{ MODIFY | MONITOR | USAGE | CREATE { TABLE | EXTERNAL TABLE | VIEW | MATERIALIZED VIEW | MASKING POLICY | ROW ACCESS POLICY | TAG | SEQUENCE | FUNCTION | PROCEDURE | FILE FORMAT | STAGE | PIPE | STREAM | TASK } } [ , ... ]


schema Object Privileges ::=
-- For TABLE
{ SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES } [ , ... ]
-- For VIEW
{ SELECT | REFERENCES } [ , ... ]
-- For MATERIALIZED VIEW
SELECT
-- For SEQUENCE, FUNCTION (UDF or external function), PROCEDURE, or FILE FORMAT
USAGE
-- For internal STAGE
READ [ , WRITE ]
-- For external STAGE
USAGE
-- For PIPE
{ MONITOR | OPERATE } [ , ... ]
-- For STREAM
SELECT
-- For TASK
{ MONITOR | OPERATE } [ , ... ]
-- For MASKING POLICY
APPLY
-- For ROW ACCESS POLICY
APPLY
-- For TAG
APPLY
```


The list of its ownership can view Snowflake’s
[API Document] (https://docs.snowflake.com/en/user-Security-Access-control-privileges.html 'Access Control Privileges')))))))
。


Must -fill parameters include `Object_name`, Object_type`, Object_type_plural` and` Role_name`.You can also add optional parameters:


-` On Future`: The specified permissions are granted tables or views in the new database or mode (SCHEMA) instead of present.
-` With Grant Option`: Specify the role of the role of the permission to be allowed to be granted to other characters.


The example is as follows:


```sql
# Through the designated character through With Grant Option, continue to give permissions
grant operate on warehouse report_wh to role analyst with grant option;


# 一 All tables in a mode (SCHEMA) are given to Role Analyst
grant select on all tables in schema mydb.myschema to role analyst;
```


### 3.2 View permissions


You can view the permissions of the object by using the `Show Grants` command. The example is as follows:


```sql
SHOW GRANTS ON ACCOUNT


SHOW GRANTS ON <object_type> <object_name>


SHOW GRANTS TO { ROLE <role_name> | USER <user_name> | SHARE <share_name> }


SHOW GRANTS OF ROLE <role_name>


SHOW GRANTS OF SHARE <share_name>


SHOW FUTURE GRANTS IN SCHEMA { <schema_name> }


SHOW FUTURE GRANTS IN DATABASE { <database_name> }
```


### 3.3 Removal permissions


The command of removal permissions uses the `Revoke` keyword:


```
REVOKE [ GRANT OPTION FOR ]
{
{ globalPrivileges         | ALL [ PRIVILEGES ] } ON ACCOUNT
| { accountObjectPrivileges  | ALL [ PRIVILEGES ] } ON { RESOURCE MONITOR | WAREHOUSE | DATABASE | INTEGRATION } <object_name>
| { schemaPrivileges         | ALL [ PRIVILEGES ] } ON { SCHEMA <schema_name> | ALL SCHEMAS IN DATABASE <db_name> }
| { schemaPrivileges         | ALL [ PRIVILEGES ] } ON { FUTURE SCHEMAS IN DATABASE <db_name> }
| { schemaObjectPrivileges   | ALL [ PRIVILEGES ] } ON { <object_type> <object_name> | ALL <object_type_plural> IN SCHEMA <schema_name> }
| { schemaObjectPrivileges   | ALL [ PRIVILEGES ] } ON FUTURE <object_type_plural> IN { DATABASE <db_name> | SCHEMA <schema_name> }
}
FROM [ ROLE ] <role_name> [ RESTRICT | CASCADE ]
```


The required parameters are the same as the Grant command, and the optional parameters are:


-` Grant Option for`: If specified, the receiver will not be allowed to give the receiver to other roles.
-` On Future`: If specified, the permissions of the new object will only be removed, and the permissions of granting the existing object are still valid.
-`RESTRICT | Cascade`: Depending on whether the authority is granted other characters, if you use Cascade, all dependent grants will be removed, but when using RESTRICT, if the authority is granted other characters, the Revoke order will notimplement.


## 4 Summary


The above content summarizes the important content of management authority in Snowflake. It is recommended to correctly create different roles in combination with actual work, and assigned to the correct permissions.If necessary, please check Snowflake further
[Official document] (https://docs.snowflake.com/en/user-Security-Access- Control-OverView.html 'Security-AControl-OverView')
。


I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>