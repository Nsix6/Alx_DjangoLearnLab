Welcome to the “Introduction to Django” project. This project is tailored for you to help you gain hands-on experience with Django, one of the most popular web frameworks for building robust web applications. Throughout this project, you will set up a Django development environment, learn about Django models and ORM, and explore the Django admin interface.

Objectives
Set Up Django Development Environment:

Install Django and create a new Django project.
Familiarize yourself with the project’s default structure and run the development server.
Implementing and Interacting with Django Models:

Create a Django app.
Define Django models with specified attributes.
Perform and document CRUD operations using Django’s ORM via the Django shell.
Utilizing the Django Admin Interface:

Register your models with the Django admin.
Customize the admin interface to enhance the management and visibility of your data.

Permissions and Groups Setup
This project uses custom permissions and groups to control access to different parts of the application. The goal is to ensure that only authorized users can perform actions such as viewing, creating, editing, or deleting content.

Custom Permissions
Custom permissions are defined in the Meta class of the chosen model. The following permissions are available:

can_view → allows viewing content

can_create → allows creating new content

can_edit → allows editing existing content

can_delete → allows deleting content

These permissions are created automatically when migrations are applied.

Groups
Three user groups are configured in the Django admin:

Viewers: Assigned only the can_view permission.

Editors: Assigned can_view, can_edit, and can_create permissions.

Admins: Assigned all permissions (can_view, can_create, can_edit, can_delete).

Users are added to groups through the Django admin interface. Group membership determines which actions a user can perform.

Enforcing Permissions
Permissions are enforced in views using Django’s built‑in tools:

Function‑based views use the @permission_required decorator.

Class‑based views use the PermissionRequiredMixin.

For example:

An edit view requires can_edit.

A create view requires can_create.

A delete view requires can_delete.

Testing
To verify permissions:

Create test users and assign them to different groups (Viewers, Editors, Admins).

Log in as each user and attempt to view, create, edit, or delete content.

Confirm that access is restricted according to the group’s assigned permissions.
