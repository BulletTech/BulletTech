---
template: overrides/blogs.html
---

# SnowFlake表权限介绍

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

在数据库中正确管理表的权限非常重要，但却又常被人忽视，往往到涉及到权限问题、碰到麻烦时，才会后悔当时没有认真对待权限管理。因此这篇文章将以火爆的SnowFlake数据仓库为例，简明扼要地讲解权限管理的问题和最佳实践。建议点赞收藏，日后回顾使用！

## 2 SnowFlake权限控制框架

SnowFlake有两种权限控制模型：

- Discretionary Access Control (DAC)，自主访问控制：每一个对象（Object）有一个所有者（Owner），所有者能授予他人不同的权限。
- Role-based Access Control (RBAC)，基于角色的访问控制：访问权限由角色（Role）控制，角色可以分配给不同的用户（User）。

在SnowFlake里，有一些重要的概念帮助理解权限控制：

- Securable object，安全对象，一个可以被授予特定权限的实体，如果没有权限，则对象的访问会被禁止。
- Role，角色，一个可以接受权限的实体，角色又可以被分配给用户，同时角色也可以分配给其他角色，构成不同的角色阶层。
- Privilege，权限：针对对象的访问控制水平。通过设置不同的权限，可以控制方位水平的粒度。
- User，用户，能够被SnowFlake识别的身份，可以是人或者程序。

在SnowFlake里，关于安全对象的权限控制如下图所示。访问安全对象可以通过向角色赋予权限，即是把权限分配给了其他的角色或者对象。另外，每个安全对象有一个所有者，其可以授予其他角色权限。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/access-control-relationships.png"  />
  <figcaption>SnowFlake权限控制示意图</figcaption>
</figure>

## 3 常用的命令

基本了解SnowFlake如何管理权限后，使用命令去操作和查看命令就更加得心应手了。

### 3.1 授予权限

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

其中：

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

其所有权限的列表可以查看SnowFlake的[API文档](https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html 'Access Control Privileges')。

必填参数有`object_name`，`object_type`，`object_type_plural`和`role_name`，这些都很好理解，不再赘述。还可加上可选参数:

- `ON FUTURE`：指定权限被授予在新的数据库或模式（schema)中的表或者视图，而非现有的对象。
- `WITH GRANT OPTION`：指定是否允许接受权限的角色授予权限给其他角色。

示例如下：

```sql
# 通过with grant option指定角色继续赋予权限
grant operate on warehouse report_wh to role analyst with grant option;

# 权限授予一个模式（schema)中所有的表给role analyst
grant select on all tables in schema mydb.myschema to role analyst;
```

### 3.2 查看权限

通过使用`SHOW GRANTS`命令可以查看对象的权限，示例如下：

```sql
SHOW GRANTS ON ACCOUNT

SHOW GRANTS ON <object_type> <object_name>

SHOW GRANTS TO { ROLE <role_name> | USER <user_name> | SHARE <share_name> }

SHOW GRANTS OF ROLE <role_name>

SHOW GRANTS OF SHARE <share_name>

SHOW FUTURE GRANTS IN SCHEMA { <schema_name> }

SHOW FUTURE GRANTS IN DATABASE { <database_name> }
```

### 3.3 移除权限

移除权限的命令使用`REVOKE`关键字：

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

必选参数和GRANT命令的相同，而可选参数有：

- `GRANT OPTION FOR`：如指定，将不允许接收者再授予权限给其他角色。
- `ON FUTURE`：如指定，将只会移除新对象的权限，授予在现有对象的权限仍然有效。
- `RESTRICT | CASCADE`：取决于权限是否被授予了其他的角色，若使用CASCADE，则所有依赖的grant都会被移除，但使用RESTRICT时，如果权限被授予了其他的角色，则REVOKE命令不执行。

## 4 总结

上述内容概括了在SnowFlake里管理权限的重要内容，必要时，请进一步查阅SnowFlake的[官方文档](https://docs.snowflake.com/en/user-guide/security-access-control-overview.html 'security-access-control-overview')。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
