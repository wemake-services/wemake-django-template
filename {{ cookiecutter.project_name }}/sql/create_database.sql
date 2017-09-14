/*
This file is used to bootstrap development database.

Note: ONLY development database;
*/

CREATE USER {{ cookiecutter.project_name }} SUPERUSER;
CREATE DATABASE {{ cookiecutter.project_name }} OWNER {{ cookiecutter.project_name }} ENCODING 'utf-8';
