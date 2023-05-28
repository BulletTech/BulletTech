---
template: overrides/blogs.html
tags:
  - analytics
  - database
---

# SnowFlake Permission Overview

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-06-06, Read time: about 6 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/fmtJR9O3jVVBav0A0X8yFw)

## 1 Introduction

Properly managing permissions for objects (such as databases and tables) in a database is very important but often overlooked. When it comes to permission issues and problems, people will regret not taking permission management seriously. Therefore, this article will take the very popular SnowFlake data warehouse as an example, succinctly explaining important concepts and commonly used commands for permission management. It is recommended to like and bookmark for later review and use!

## 2 SnowFlake Permission Control Framework

SnowFlake has two permission control models:

- Discretionary Access Control (DAC): Each object has an owner who can grant different permissions to others.
- Role-based Access Control (RBAC): Access permissions are controlled by roles, which can be assigned to different users.

In SnowFlake, there are some important concepts that help understand permission control:

- Securable object: An entity that can be granted specific permissions. If you do not have permission, access to the object will be denied.
- Role: An entity that can receive permissions, which can be assigned to users or other roles to form different role hierarchies.
- Privilege: The level of access control for objects. By setting different privileges, the granularity of access control can be controlled.
- User: An identity that can be recognized by SnowFlake and can be a person or a program.

In SnowFlake, the permission control of securable objects is shown in the figure below. Access to securable objects can be granted by assigning permissions to roles, which means that permissions are assigned to other roles or objects. In addition, each securable object has an owner who can grant permissions to other roles.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/access-control-relationships.png"  />
  <figcaption>SnowFlake Permission Control Diagram</figcaption>
</figure>

## 3 Common Commands

After a basic understanding of how SnowFlake manages permissions, using commands to operate and view permissions will be more convenient.

### 3.1 Granting Permissions

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

Where:

```sql
globalPrivileges ::=
  { { CREATE { ROLE | USER | WAREHOUSE | DATABASE | INTEGRATION } } | APPLY MASKING POLICY | APPLY ROW ACCESS POLICY | APPLY TAG | EXECUTE TASK | MANAGE GRANTS | MONITOR { EXECUTION | USAGE }  } [ , ... ]

accountObjectPrivileges ::=
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

schemaPrivileges ::=
    { MODIFY | MONITOR | USAGE | CREATE { TABLE | EXTERNAL TABLE | VIEW | MATERIALIZED VIEW | MASKING POLICY | ROW ACCESS POLICY | TAG | SEQUENCE | FUNCTION | PROCEDURE | FILE FORMAT | STAGE | PIPE | STREAM | TASK } } [ , ... ]

schemaObjectPrivileges ::=
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

The full list of all permissions can be found in SnowFlake's [API documentation](https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html 'Access Control Privileges').

The required parameters are `object_name`, `object_type`, `object_type_plural`, and `role_name`, which are self-explanatory. Optional parameters include:

- `ON FUTURE`: Specifies that the permission is granted to tables or views in a new database or schema, not existing objects.
- `WITH GRANT OPTION`: Specifies whether the recipient role is allowed to grant permissions to other roles.

Examples are as follows:

```sql
# Specify that the role can continue to grant permissions with grant option
grant operate on warehouse report_wh to role analyst with grant option;

# Grant select permission on all tables in schema mydb.myschema to role analyst
grant select on all tables in schema mydb.myschema to role analyst;
```

### 3.2 Viewing Permissions

You can view object permissions using the `SHOW GRANTS` command, as shown below:

```sql
SHOW GRANTS ON ACCOUNT

SHOW GRANTS ON <object_type> <object_name>

SHOW GRANTS TO { ROLE <role_name> | USER <user_name> | SHARE <share_name> }

SHOW GRANTS OF ROLE <role_name>

SHOW GRANTS OF SHARE <share_name>

SHOW FUTURE GRANTS IN SCHEMA { <schema_name> }

SHOW FUTURE GRANTS IN DATABASE { <database_name> }
```

### 3.3 Revoking Permissions

The command to revoke permissions uses the `REVOKE` keyword:

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
  FROM [